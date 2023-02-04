# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 07:56:17 2023

@author: mrkure
"""
use_notif_reader = True
import os, sys, keyboard
import win32gui
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QPoint, pyqtSignal
from PyQt5.QtWidgets import QWidget, QScrollArea,QVBoxLayout
from lib_tools import Tools
from lib_parser import StringParser


class MainWindow(QWidget):
    main_window_closed = pyqtSignal(object)
    
    def __init__(self, dic_params):   
        super().__init__()        
        self.setWindowFlags ( QtCore.Qt.FramelessWindowHint  | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.Tool )  
        
        self.dic_params = dic_params
        if self.dic_params['use_notif_reader']:
            from lib_notif_reader import MyNotification, MyNotificatons, NotificationReader, current_win_epoch_stamp

        self.parser                  = StringParser() 
        self.w, self.h               = self.dic_params['w'], self.dic_params['h']
        self.max_items_before_scroll = self.dic_params['mibs']

        # properties
        self.file                                 = self.dic_params['log_file']
        self.initial_file_size                    = os.path.getsize(self.file)
        self.time                                 = 0
        self.time_whisper_max                     = self.dic_params['time_to_rem_whisper']
        self.time_to_lower_window_opacity         = self.dic_params['time_to_hide']
        self.time_to_lower_window_opacity_counter = 0 
        self.window_opacity_low                   = 1  
        self.window_opacity_high                  = 1
        self.mouse_over_app                       = False  
       
        # main vbox layout
        self.vbox = QVBoxLayout()  
        self.vbox.setContentsMargins(0,0,0,0)
        self.vbox.setSpacing(0)
        self.setLayout(self.vbox)
        self.hwndMain = win32gui.FindWindow(None, "Path of Exile")  
       
        # menu
        self.add_menu() 

        # scroll area layout
        self.vboxsc = QVBoxLayout()  
        self.vboxsc.setContentsMargins(0,0,0,0)
        self.vboxsc.setSpacing(0)
        self.canvas = QWidget()
        self.canvas.setLayout(self.vboxsc)
        self.scrollarea = QScrollArea()         
        self.scrollarea.setWidget(self.canvas) 
        self.scrollarea.setWidgetResizable(True) 
        self.scrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.vbox.addWidget(self.scrollarea, 1000)         
        self.scrollarea.setStyleSheet("background-color: rgb(98, 98, 98);")
        self.scrollarea.setMinimumHeight(1)
        self.scrollarea.verticalScrollBar().setValue(0)

        # sizegrip
        sizegrip = QtWidgets.QSizeGrip(self)
        sizegrip.setMaximumHeight(5)
        sizegrip.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.vbox.addWidget(sizegrip, 1, QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)   

        # main window
        self.setStyleSheet("background-color: rgb(98, 98, 98);")
        self.setGeometry(self.dic_params['wposx'], self.dic_params['wposy'], 300, 300)
        self.setWindowTitle('Trade Helper')
        ww, hh = self.recalculate_window_size()
        self.resize_window(ww, hh)        
 
        # notif reading
        if self.dic_params['use_notif_reader']:
            self.my_notifications                 = MyNotificatons()
            self.my_notifications.last_time_notif = current_win_epoch_stamp()
            self.notif_reader                     = NotificationReader()   
        
        # timer 100 msec
        self.timer_100_msec    = QtCore.QTimer()
        self.timer_100_msec.timeout.connect(self.on_100_ms_timer) 
        self.timer_100_msec.start(self.dic_params['check_period'])
        
        # timer 1000 msec        
        self.timer_1000_msec=QtCore.QTimer()
        self.timer_1000_msec.timeout.connect(self.on_1000_ms_timer) 
        self.timer_1000_msec.start(1000)

#%% TIMERS
    
    # check and evaluate last line of log on size change
    def on_100_ms_timer(self):
        current_file_size = os.path.getsize(self.file)
        
        if current_file_size != self.initial_file_size:
            with open(self.file, 'rb') as f:
                try:  # catch OSError in case of a one line file 
                    f.seek(-2, os.SEEK_END)
                    while f.read(1) != b'\n':
                        f.seek(-2, os.SEEK_CUR)
                except OSError:
                    f.seek(0)
                last_line = f.readline().decode()
                result = self.parser.evaluate_string(last_line)
                if result:                   
                    self.add_whisper( self.parser.buyer, self.parser.item, self.parser.price)
        self.initial_file_size = current_file_size  

        if self.dic_params['use_notif_reader']:
            self.notif_reader.read_notifications([], self.my_notifications.last_time_notif, self.my_notifications)
            self.my_notifications.evaluate_notifications()
            self.my_notifications.printt()
            for notification in self.my_notifications.notifications:
                self.add_whisper( notification.sender, notification.title + ' :' +  notification.message, notification.time)
            self.my_notifications.clear_notifications()
        
    # remove whisper after set time and change opacity if empty
    def on_1000_ms_timer(self):
        self.time += 1
        # remove widget after set time
        for num, widget in enumerate(self.canvas.children()):
            if isinstance(widget, QtWidgets.QFrame) and widget.objectName() != 'frame_menu':
                if self.time - widget.time > self.time_whisper_max and widget.used == False: 
                    widget.setParent(None) 
        w, h = self.recalculate_window_size()
        self.resize_window(w, h)
        
        # change opacity of window after set time while empty     
        if num == 0 :
            self.time_to_lower_window_opacity_counter += 1
            if self.time_to_lower_window_opacity_counter == self.time_to_lower_window_opacity:
                self.setWindowOpacity(self.window_opacity_low)
                self.hide()
        if num > 0 or self.mouse_over_app:
            self.setWindowOpacity(self.window_opacity_high)
            self.show()
            self.time_to_lower_window_opacity_counter = 0

#%% METHODS
  
    def add_menu(self):
        self.menu_o = Tools.create_menu_frame(self, self.w, self.h)
        self.menu_callback_hook(self.menu_o)
        self.vbox.addWidget(self.menu_o,1)    
        self.menu_o.setMinimumWidth(self.w+15)
        self.menu_o.setMaximumWidth(self.w+15) 
        for widget in self.menu_o.children():
            if isinstance(widget, QtWidgets.QLabel) :
                widget.setText(str(self.max_items_before_scroll))
                
    def add_whisper(self, buyer, item, price):
        whisper_o = Tools.create_whisper_frame(self, self.w, self.h, self.time, buyer, item, price)  
        self.whisper_callback_hook(whisper_o)
        self.vboxsc.insertWidget(0, whisper_o, 1)        
        w, h = self.recalculate_window_size()
        self.resize_window(w, h)

    def recalculate_window_size(self):
        wc, hc     = 0,0
        wc = self.w
        for num, w in enumerate(self.canvas.children()): 
            if isinstance(w, QtWidgets.QFrame):
                if num <= self.max_items_before_scroll:
                    hc += self.h
        return wc+15, hc +35

    def resize_window(self, w, h):
        self.setMaximumSize(QtCore.QSize(w+1, h+1))
        self.setMinimumSize(QtCore.QSize(w-1, h-1)) 
        self.resize(w, h)

    def resize_frame_x(self, value):
        self.w += value
        self.menu_o.setMinimumWidth(self.w+15)
        self.menu_o.setMaximumWidth(self.w+15)        
        for widget in self.canvas.children():
            if isinstance(widget, QtWidgets.QFrame) and widget.objectName() != 'frame_menu':
                widget.setMinimumWidth(self.w)
                widget.setMaximumWidth(self.w)   
        w, h = self.recalculate_window_size()
        self.resize_window(w, h)

    def resize_frame_y(self, value):
        self.h += value
        for widget in self.canvas.children():           
            if isinstance(widget, QtWidgets.QFrame) and widget.objectName() != 'frame_menu':
                widget.setMinimumHeight(self.h)
                widget.setMaximumHeight(self.h) 
        w, h = self.recalculate_window_size()
        self.resize_window(w, h)
        
    def set_poe_as_foreground_window(self):
        try:
            keyboard.press('alt')
            if self.hwndMain == 0:
                self.hwndMain = win32gui.FindWindow(None, "Path of Exile") 
            win32gui.SetForegroundWindow(self.hwndMain)
            keyboard.release('alt')
        except:
            keyboard.release('alt') 
        
    def get_window_params(self):
        dic_params = {'w':self.w, 'h':self.h, 'mibs':self.max_items_before_scroll,'wposx':self.pos().x(), 'wposy':self.pos().y()}
        return dic_params
    
    def window_close(self):
        self.timer_100_msec.stop()
        self.timer_1000_msec.stop()
        self.close() 
        
#%% MENU CALLBACKS

    def menu_callback_hook(self, menu):
        for widget in self.menu_o.children():
            if isinstance(widget, QtWidgets.QPushButton) :
                if widget.objectName() == 'pushButton_add_whisper':
                    widget.clicked.connect(self.on_menu_button_add_whisper_press)
                if widget.objectName() == 'pushButton_enlarge_x':
                    widget.clicked.connect(self.on_menu_button_enlarge_x)
                if widget.objectName() == 'pushButton_reduce_x':
                    widget.clicked.connect(self.on_menu_button_reduce_x)
                if widget.objectName() == 'pushButton_enlarge_y':
                    widget.clicked.connect(self.on_menu_button_enlarge_y)
                if widget.objectName() == 'pushButton_reduce_y':
                    widget.clicked.connect(self.on_menu_button_reduce_y)
                if widget.objectName() == 'pushButton_increment_scroll_items':
                    widget.clicked.connect(self.on_menu_button_increment_scroll_items)
                if widget.objectName() == 'pushButton_decrement_scroll_items':
                    widget.clicked.connect(self.on_menu_button_decrement_scroll_items)   
                if widget.objectName() == 'pushButton_remove_all_wisphers':
                    widget.clicked.connect(self.on_menu_button_remove_all_whispers)                               
                if widget.objectName() == 'pushButton_close_app':
                    widget.clicked.connect(self.on_menu_button_close_app)

    def on_menu_button_add_whisper_press(self):
        self.set_poe_as_foreground_window() 
        whisper_o = Tools.create_whisper_frame(self, self.w, self.h, self.time)  
        self.whisper_callback_hook(whisper_o)
        self.vboxsc.addWidget(whisper_o,1)
        w, h = self.recalculate_window_size()
        self.resize_window(w, h)
                
    def on_menu_button_enlarge_x(self):
        self.resize_frame_x(10)
        
    def on_menu_button_reduce_x(self):
        self.resize_frame_x(-10)  
        
    def on_menu_button_enlarge_y(self):
        self.resize_frame_y(5)
        
    def on_menu_button_reduce_y(self):
        self.resize_frame_y(-5)
 
    def on_menu_button_increment_scroll_items(self):
        self.set_poe_as_foreground_window()
        self.max_items_before_scroll += 1
        for widget in self.menu_o.children():
            if isinstance(widget, QtWidgets.QLabel) :
                widget.setText(str(self.max_items_before_scroll))
        w, h = self.recalculate_window_size()
        self.resize_window(w, h)
        
    def on_menu_button_decrement_scroll_items(self):
        self.set_poe_as_foreground_window()
        self.max_items_before_scroll += -1
        if self.max_items_before_scroll <= 0: self.max_items_before_scroll = 0
        for widget in self.menu_o.children():
            if isinstance(widget, QtWidgets.QLabel) :
                widget.setText(str(self.max_items_before_scroll))

        w, h = self.recalculate_window_size()
        self.resize_window(w, h)
 
    def on_menu_button_remove_all_whispers(self):
        self.set_poe_as_foreground_window()
        for widget in self.canvas.children():
            if isinstance(widget, QtWidgets.QFrame) and widget.objectName() != 'frame_menu':   
                widget.setMinimumHeight(self.h)
                widget.setMaximumHeight(self.h)
                widget.setParent(None) 
        w, h = self.recalculate_window_size()
        self.resize_window(w, h)
        
    def on_menu_button_close_app(self):
        self.on_menu_button_remove_all_whispers()
        self.set_poe_as_foreground_window()
        self.hide()   
                   
#%% WHISPER CALLBACKS

    def whisper_callback_hook(self, whisper):
        for widget in whisper.children():
            if isinstance(widget, QtWidgets.QPushButton) :
                widget.clicked.connect(self.on_any_button_press)
                
                if widget.objectName() == 'pushButton_invite':
                    widget.clicked.connect(self.on_whisper_button_invite_press) 
                if widget.objectName() == 'pushButton_leave':
                    widget.clicked.connect(self.on_whisper_button_leave_press) 
                if widget.objectName() == 'pushButton_close':
                    widget.clicked.connect(self.on_whisper_button_close_press) 
                if widget.objectName() == 'pushButton_trade':
                    widget.clicked.connect(self.on_whisper_button_trade_press) 
                if widget.objectName() == 'pushButton_wait':
                    widget.clicked.connect(self.on_whisper_button_wait_press) 
                if widget.objectName() == 'pushButton_time':
                    widget.clicked.connect(self.on_whisper_button_time_press)                    

    def on_any_button_press(self):
        self.sender().parent().used = True
        
    def on_whisper_button_invite_press(self):
        self.set_poe_as_foreground_window()
        keyboard.send('enter')
        keyboard.write('/invite ' + self.sender().parent().buyer)
        keyboard.send('enter')
    
    def on_whisper_button_leave_press(self):
        self.set_poe_as_foreground_window()
        buyer = self.sender().parent().buyer
        keyboard.send('enter')
        keyboard.write('@' + buyer + ' ty')  
        keyboard.send('enter')
        keyboard.send('enter')
        keyboard.write('/kick ' + buyer)  
        keyboard.send('enter')
        self.sender().parent().setParent(None)
        w, h = self.recalculate_window_size()
        self.resize_window(w, h)
        
    def on_whisper_button_close_press(self):
        self.set_poe_as_foreground_window()
        self.sender().parent().setParent(None)
        w, h = self.recalculate_window_size()
        self.resize_window(w, h)      
        
    def on_whisper_button_trade_press(self):
        self.set_poe_as_foreground_window()
        keyboard.send('enter')
        keyboard.write('/tradewith ' + self.sender().parent().buyer) 
        keyboard.send('enter')

    def on_whisper_button_wait_press(self):
        self.set_poe_as_foreground_window()
        keyboard.send('enter')
        keyboard.write('@' + self.sender().parent().buyer + ' one minute')  
        keyboard.send('enter')
        
    def on_whisper_button_time_press(self):
        self.set_poe_as_foreground_window()

#%% EVENTS

    def resizeEvent(self, event):
        pass
    
    # APP MOVING ON MOUSE PRESS AND MOVE    
    def mousePressEvent(self, evt):
        """Select the toolbar."""
        self.oldPos = evt.globalPos()
    
    # APP MOVING ON MOUSE PRESS AND MOVE  
    def mouseMoveEvent(self, evt):
        """Move the toolbar with mouse iteration."""

        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()    

    def wheelEvent(self,event):
        if event.y() < 24 and event.angleDelta().y() < 0:
            self.resize_frame_x(-10) 
            self.resize_frame_y(-5) 
        elif event.y() < 24 and event.angleDelta().y() > 0:
            self.resize_frame_x(10) 
            self.resize_frame_y(5)

    def enterEvent(self, event):
        print('enter event')
        self.setWindowOpacity(self.window_opacity_high)
        self.mouse_over_app = True
        
    def leaveEvent(self, event):
        print('leave event')
        self.mouse_over_app = False      
        
#%% MAIN        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dic_params = Tools.load_params()
    main = MainWindow(dic_params)
    main.show()
    sys.exit(app.exec_())
