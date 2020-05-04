# -*- coding:utf-8 -*-
'''
@Description: 
@Author: lamborghini1993
@Date: 2020-05-04 14:34:07
@UpdateDate: 2020-05-04 14:44:48
'''

from PyQt5.QtWidgets import QMainWindow

class CMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("样例")
        