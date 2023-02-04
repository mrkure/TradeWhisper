# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\_python\project\poe_trade_helper_new\lib\ui\ui_whisper_element.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_whisper_frame(object):
    def setupUi(self, whisper_frame):
        whisper_frame.setObjectName("whisper_frame")
        whisper_frame.resize(569, 143)
        whisper_frame.setStyleSheet("background-color: rgb(85, 255, 0);")
        whisper_frame.setFrameShape(QtWidgets.QFrame.Box)
        whisper_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        whisper_frame.setMidLineWidth(1)
        self.gridLayout = QtWidgets.QGridLayout(whisper_frame)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.label_seller_name = QtWidgets.QLabel(whisper_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_seller_name.sizePolicy().hasHeightForWidth())
        self.label_seller_name.setSizePolicy(sizePolicy)
        self.label_seller_name.setToolTipDuration(-3)
        self.label_seller_name.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_seller_name.setFrameShape(QtWidgets.QFrame.Box)
        self.label_seller_name.setLineWidth(0)
        self.label_seller_name.setMidLineWidth(0)
        self.label_seller_name.setIndent(10)
        self.label_seller_name.setObjectName("label_seller_name")
        self.gridLayout.addWidget(self.label_seller_name, 0, 0, 1, 1)
        self.pushButton_invite = QtWidgets.QPushButton(whisper_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_invite.sizePolicy().hasHeightForWidth())
        self.pushButton_invite.setSizePolicy(sizePolicy)
        self.pushButton_invite.setStyleSheet("background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.pushButton_invite.setObjectName("pushButton_invite")
        self.gridLayout.addWidget(self.pushButton_invite, 0, 1, 1, 1)
        self.pushButton_leave = QtWidgets.QPushButton(whisper_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_leave.sizePolicy().hasHeightForWidth())
        self.pushButton_leave.setSizePolicy(sizePolicy)
        self.pushButton_leave.setStyleSheet("background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.pushButton_leave.setObjectName("pushButton_leave")
        self.gridLayout.addWidget(self.pushButton_leave, 0, 2, 1, 1)
        self.pushButton_close = QtWidgets.QPushButton(whisper_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy)
        self.pushButton_close.setStyleSheet("background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout.addWidget(self.pushButton_close, 0, 3, 1, 1)
        self.label_string_value = QtWidgets.QLabel(whisper_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_string_value.sizePolicy().hasHeightForWidth())
        self.label_string_value.setSizePolicy(sizePolicy)
        self.label_string_value.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_string_value.setFrameShape(QtWidgets.QFrame.Box)
        self.label_string_value.setLineWidth(0)
        self.label_string_value.setMidLineWidth(0)
        self.label_string_value.setIndent(10)
        self.label_string_value.setObjectName("label_string_value")
        self.gridLayout.addWidget(self.label_string_value, 1, 0, 1, 1)
        self.pushButton_trade = QtWidgets.QPushButton(whisper_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_trade.sizePolicy().hasHeightForWidth())
        self.pushButton_trade.setSizePolicy(sizePolicy)
        self.pushButton_trade.setStyleSheet("background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.pushButton_trade.setObjectName("pushButton_trade")
        self.gridLayout.addWidget(self.pushButton_trade, 1, 1, 1, 1)
        self.pushButton_wait = QtWidgets.QPushButton(whisper_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_wait.sizePolicy().hasHeightForWidth())
        self.pushButton_wait.setSizePolicy(sizePolicy)
        self.pushButton_wait.setStyleSheet("background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.pushButton_wait.setObjectName("pushButton_wait")
        self.gridLayout.addWidget(self.pushButton_wait, 1, 2, 1, 1)
        self.pushButton_time = QtWidgets.QPushButton(whisper_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_time.sizePolicy().hasHeightForWidth())
        self.pushButton_time.setSizePolicy(sizePolicy)
        self.pushButton_time.setStyleSheet("background-color: rgb(98, 98, 98);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(0, 255, 0);")
        self.pushButton_time.setObjectName("pushButton_time")
        self.gridLayout.addWidget(self.pushButton_time, 1, 3, 1, 1)
        self.gridLayout.setColumnStretch(0, 10)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)

        self.retranslateUi(whisper_frame)
        QtCore.QMetaObject.connectSlotsByName(whisper_frame)

    def retranslateUi(self, whisper_frame):
        _translate = QtCore.QCoreApplication.translate
        whisper_frame.setWindowTitle(_translate("whisper_frame", "Frame"))
        self.label_seller_name.setText(_translate("whisper_frame", "name_text"))
        self.pushButton_invite.setText(_translate("whisper_frame", "+"))
        self.pushButton_leave.setText(_translate("whisper_frame", "-"))
        self.pushButton_close.setText(_translate("whisper_frame", "X"))
        self.label_string_value.setText(_translate("whisper_frame", "test_string_value"))
        self.pushButton_trade.setText(_translate("whisper_frame", "T"))
        self.pushButton_wait.setText(_translate("whisper_frame", "1m"))
        self.pushButton_time.setText(_translate("whisper_frame", "ti"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    whisper_frame = QtWidgets.QFrame()
    ui = Ui_whisper_frame()
    ui.setupUi(whisper_frame)
    whisper_frame.show()
    sys.exit(app.exec_())

