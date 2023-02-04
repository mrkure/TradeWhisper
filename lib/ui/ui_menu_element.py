# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\_python\project\poe_trade_helper_new\lib\ui\ui_menu_element.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(587, 32)
        Frame.setStyleSheet("background-color: rgb(170, 85, 255);\n"
"background-color: rgb(0, 170, 0);\n"
"background-color: rgb(98, 98, 98);")
        Frame.setFrameShape(QtWidgets.QFrame.Box)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        Frame.setLineWidth(2)
        self.gridLayout = QtWidgets.QGridLayout(Frame)
        self.gridLayout.setContentsMargins(1, 1, 0, 0)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_add_whisper = QtWidgets.QPushButton(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add_whisper.sizePolicy().hasHeightForWidth())
        self.pushButton_add_whisper.setSizePolicy(sizePolicy)
        self.pushButton_add_whisper.setStyleSheet("background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.pushButton_add_whisper.setObjectName("pushButton_add_whisper")
        self.gridLayout.addWidget(self.pushButton_add_whisper, 0, 0, 1, 1)
        self.pushButton_enlarge_x = QtWidgets.QPushButton(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_enlarge_x.sizePolicy().hasHeightForWidth())
        self.pushButton_enlarge_x.setSizePolicy(sizePolicy)
        self.pushButton_enlarge_x.setStyleSheet("background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.pushButton_enlarge_x.setAutoRepeat(True)
        self.pushButton_enlarge_x.setAutoRepeatDelay(100)
        self.pushButton_enlarge_x.setAutoRepeatInterval(45)
        self.pushButton_enlarge_x.setObjectName("pushButton_enlarge_x")
        self.gridLayout.addWidget(self.pushButton_enlarge_x, 0, 1, 1, 1)
        self.pushButton_reduce_x = QtWidgets.QPushButton(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_reduce_x.sizePolicy().hasHeightForWidth())
        self.pushButton_reduce_x.setSizePolicy(sizePolicy)
        self.pushButton_reduce_x.setStyleSheet("background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.pushButton_reduce_x.setAutoRepeat(True)
        self.pushButton_reduce_x.setAutoRepeatDelay(100)
        self.pushButton_reduce_x.setAutoRepeatInterval(45)
        self.pushButton_reduce_x.setObjectName("pushButton_reduce_x")
        self.gridLayout.addWidget(self.pushButton_reduce_x, 0, 2, 1, 1)
        self.pushButton_enlarge_y = QtWidgets.QPushButton(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_enlarge_y.sizePolicy().hasHeightForWidth())
        self.pushButton_enlarge_y.setSizePolicy(sizePolicy)
        self.pushButton_enlarge_y.setStyleSheet("background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.pushButton_enlarge_y.setAutoRepeat(True)
        self.pushButton_enlarge_y.setAutoRepeatDelay(100)
        self.pushButton_enlarge_y.setAutoRepeatInterval(45)
        self.pushButton_enlarge_y.setObjectName("pushButton_enlarge_y")
        self.gridLayout.addWidget(self.pushButton_enlarge_y, 0, 3, 1, 1)
        self.pushButton_reduce_y = QtWidgets.QPushButton(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_reduce_y.sizePolicy().hasHeightForWidth())
        self.pushButton_reduce_y.setSizePolicy(sizePolicy)
        self.pushButton_reduce_y.setStyleSheet("background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.pushButton_reduce_y.setAutoRepeat(True)
        self.pushButton_reduce_y.setAutoRepeatDelay(100)
        self.pushButton_reduce_y.setAutoRepeatInterval(45)
        self.pushButton_reduce_y.setObjectName("pushButton_reduce_y")
        self.gridLayout.addWidget(self.pushButton_reduce_y, 0, 4, 1, 1)
        self.pushButton_increment_scroll_items = QtWidgets.QPushButton(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_increment_scroll_items.sizePolicy().hasHeightForWidth())
        self.pushButton_increment_scroll_items.setSizePolicy(sizePolicy)
        self.pushButton_increment_scroll_items.setStyleSheet("background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.pushButton_increment_scroll_items.setAutoRepeat(True)
        self.pushButton_increment_scroll_items.setObjectName("pushButton_increment_scroll_items")
        self.gridLayout.addWidget(self.pushButton_increment_scroll_items, 0, 5, 1, 1)
        self.pushButton_decrement_scroll_items = QtWidgets.QPushButton(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_decrement_scroll_items.sizePolicy().hasHeightForWidth())
        self.pushButton_decrement_scroll_items.setSizePolicy(sizePolicy)
        self.pushButton_decrement_scroll_items.setStyleSheet("background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.pushButton_decrement_scroll_items.setAutoRepeat(True)
        self.pushButton_decrement_scroll_items.setObjectName("pushButton_decrement_scroll_items")
        self.gridLayout.addWidget(self.pushButton_decrement_scroll_items, 0, 6, 1, 1)
        self.label_scroll_items_value = QtWidgets.QLabel(Frame)
        self.label_scroll_items_value.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_scroll_items_value.sizePolicy().hasHeightForWidth())
        self.label_scroll_items_value.setSizePolicy(sizePolicy)
        self.label_scroll_items_value.setMinimumSize(QtCore.QSize(10, 0))
        self.label_scroll_items_value.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"border-top-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(0, 0, 0);")
        self.label_scroll_items_value.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_scroll_items_value.setTextFormat(QtCore.Qt.PlainText)
        self.label_scroll_items_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_scroll_items_value.setIndent(-1)
        self.label_scroll_items_value.setObjectName("label_scroll_items_value")
        self.gridLayout.addWidget(self.label_scroll_items_value, 0, 7, 1, 1)
        self.pushButton_remove_all_wisphers = QtWidgets.QPushButton(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_remove_all_wisphers.sizePolicy().hasHeightForWidth())
        self.pushButton_remove_all_wisphers.setSizePolicy(sizePolicy)
        self.pushButton_remove_all_wisphers.setStyleSheet("background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.pushButton_remove_all_wisphers.setObjectName("pushButton_remove_all_wisphers")
        self.gridLayout.addWidget(self.pushButton_remove_all_wisphers, 0, 8, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(159, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 9, 1, 1)
        self.pushButton_close_app = QtWidgets.QPushButton(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_close_app.sizePolicy().hasHeightForWidth())
        self.pushButton_close_app.setSizePolicy(sizePolicy)
        self.pushButton_close_app.setStyleSheet("background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.pushButton_close_app.setObjectName("pushButton_close_app")
        self.gridLayout.addWidget(self.pushButton_close_app, 0, 10, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 1)
        self.gridLayout.setColumnStretch(5, 1)
        self.gridLayout.setColumnStretch(6, 1)
        self.gridLayout.setColumnStretch(7, 1)
        self.gridLayout.setColumnStretch(8, 1)
        self.gridLayout.setColumnStretch(9, 4)
        self.gridLayout.setColumnStretch(10, 1)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton_add_whisper.setText(_translate("Frame", "T"))
        self.pushButton_enlarge_x.setText(_translate("Frame", "X+"))
        self.pushButton_reduce_x.setText(_translate("Frame", "X-"))
        self.pushButton_enlarge_y.setText(_translate("Frame", "Y+"))
        self.pushButton_reduce_y.setText(_translate("Frame", "Y-"))
        self.pushButton_increment_scroll_items.setText(_translate("Frame", "S+"))
        self.pushButton_decrement_scroll_items.setText(_translate("Frame", "S-"))
        self.label_scroll_items_value.setText(_translate("Frame", "0"))
        self.pushButton_remove_all_wisphers.setText(_translate("Frame", "X"))
        self.pushButton_close_app.setText(_translate("Frame", "XX"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

