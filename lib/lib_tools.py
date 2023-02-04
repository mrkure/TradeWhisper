# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 08:32:27 2023

@author: CAZ2BJ
"""
import json, os, sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.ui_whisper_element import Ui_whisper_frame
from ui.ui_menu_element import Ui_Frame
        
class Tools:
    
    dic_params = { "use_notif_reader": True, 
                   'time_to_rem_whisper': 36000, 
                   'time_to_hide': 40, 
                   'check_period': 10, 
                   'log_file':'C:/binary_build/team3/resources/dummy.txt', 
                   'w':550, 
                   'h':60, 
                   'mibs':5, 
                   'wposx':600, 
                   'wposy':100
                   }
    
    def get_dir_path(script = [], exe = []):
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            path = os.path.realpath(os.path.join(os.path.dirname(sys.executable),*exe))
            return path
        else:
            path = os.path.realpath(os.path.join(os.path.dirname(script[0]),*script[1:]))
            return path

    def load_path_file():
        file = Tools.get_dir_path([__file__, '..', 'resources', 'config.txt'], [ 'resources', 'config.txt'])
        with open(file) as f:
            lines = f.readlines()  
        return lines[0]
            
    def save_params(dic_params):
        file = Tools.get_dir_path([__file__, '..', 'resources', 'config.txt'], [ 'resources', 'config.txt'])
        with open(file, 'w') as file_object:  
            json.dump(dic_params, file_object, indent = 4) 
            
    def load_params():
        try:
            file = Tools.get_dir_path([__file__, '..', 'resources', 'config.txt'], [ 'resources', 'config.txt'])
            with open(file, 'r') as file_object:  
                dic_params = json.load(file_object)     
        except:
            return Tools.dic_params
        return {**Tools.dic_params, **dic_params} 
    
    def create_whisper_frame(parent, width, height, time, buyer='buyer', item='item', price = 'price'):
        frame   = QtWidgets.QFrame()
        builder = Ui_whisper_frame()
        builder.setupUi(frame)
        frame.parent = parent
        frame.setGeometry(QtCore.QRect(120, 140, 600, 141))
        frame.setMinimumSize(QtCore.QSize(width, height))
        frame.setMaximumSize(QtCore.QSize(width, height))
        frame.used = False
        frame.buyer = buyer
        frame.item  = item
        frame.price = price
        frame.time  = time
        builder.label_string_value.setText( f'<font color="#000000">{item}</font>')
        builder.label_seller_name.setText(f'<font color="#000000">{buyer}</font><font color="#000000"> -> </font><font color="#FFD700">{price}</font>')
        return frame

    def create_menu_frame(parent, width, height):
        frame   = QtWidgets.QFrame()
        builder = Ui_Frame()
        builder.setupUi(frame)
        frame.parent = parent
        frame.setMinimumSize(QtCore.QSize(width, 30))
        frame.setMaximumSize(QtCore.QSize(width, 30))
        return frame
        
#%% TEST
if __name__ == "__main__":
    
    # Tools.save_params(dic_params)
    dic = Tools.load_params()

    # print(dic_params)
    # input('Press enter to exit :')



