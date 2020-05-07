# -*- coding:utf-8 -*-
'''
@Description: 测试窗口
@Author: lamborghini1993
@Date: 2020-05-04 14:34:07
@UpdateDate: 2020-05-07 20:00:32
'''

from PyQt5 import QtWidgets, QtCore


class CMainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("样例")
        self.resize(500, 300)
        vbox = QtWidgets.QVBoxLayout(self)
        label = QtWidgets.QLabel("有本事来解密", self)
        label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        vbox.addWidget(label)
