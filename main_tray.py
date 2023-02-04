# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 16:03:13 2022

@author: mrkure
"""
import os, sys, __init__
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QSystemTrayIcon, QAction, QMenu, QApplication
from lib_tools import Tools
import _main_exe as me

class TrayAppTradeWhisper(QSystemTrayIcon, QWidget):
    def __init__(self):
        super(QSystemTrayIcon, self).__init__()
        super(QWidget, self).__init__()        
        self.dic_params = Tools.load_params()
        
#%% TRAY SETTINGS

        self.icon_running   = QIcon( Tools.get_dir_path([__file__, 'resources', 'running.png'],['resources', 'running.png'] ))            
        self.icon_stopped   = QIcon( Tools.get_dir_path([__file__, 'resources', 'stopped.png'],['resources', 'stopped.png'] ))   

        self.menu           = QMenu() 
        self.setContextMenu(self.menu)
        self.setIcon(self.icon_running)
        self.option_close = QAction("Close")
        self.menu.addAction(self.option_close)
        self.running = True       
        self.setVisible(True)  
        
#%% TRAY SIGNALS
        self.option_close.triggered.connect(self.on_close)   
        self.activated.connect(self.on_icon_click_right)
  
#%% MAIN WINDOW   
        self.create_main_window()
        
    def create_main_window(self):      
        self.window = me.MainWindow(self.dic_params)
        self.window.show()
    
#%% CALLBACKS      

    def on_icon_click_right(self, button):
   
        if button == 2 or button == 3:  # left click
            print('icon right click')
            if self.running:
                self.window.show()
                self.window.time_to_lower_window_opacity_counter = 0 

        elif button == 4:   # middle click
            print('icon right click')
            if self.running:
                self.setIcon(self.icon_stopped) 
                self.running    = False
                self.dic_params =  {**self.dic_params, **self.window.get_window_params()} 
                self.window.window_close()
                
            elif not self.running:
                self.setIcon(self.icon_running) 
                self.running = True   
                self.create_main_window()
                        
    def on_close(self): 
        Tools.save_params( {**self.dic_params, **self.window.get_window_params()} )
        self.window.window_close()
        self.hide()
        QtCore.QCoreApplication.quit()  

#%% MAIN  
if __name__ == "__main__":
    app = QApplication([])
    tray_app_trade_whisper = TrayAppTradeWhisper()
    app.exec()