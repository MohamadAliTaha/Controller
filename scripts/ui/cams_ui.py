# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/controller/resource/PluginUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from utils.helpers import Stream
from PyQt5 import QtWidgets


class Cams_Ui(QtWidgets.QWidget):
    def __init__(self, width: float, height: float, parent=None):
        super().__init__()
        self.width = width
        self.height = height
        self.parent = parent

        self.setObjectName("cams")
        self.setupUi()

    def setupUi(self):
        self.cam1_stream = Stream(
            0, self.width, self.height, self.parent, 0.05 * self.width, 0.01 * self.height
        )
        self.cam1_stream.setup()
        self.cam2_stream = Stream(1, self.width, self.height, self.parent, self.width / 2, 0.01 * self.height)
        self.cam2_stream.setup()
        self.cam3_stream = Stream(
            2, self.width, self.height, self.parent, 0.05 * self.width, self.height / 2.2
        )
        self.cam3_stream.setup()
        self.cam4_stream = Stream(3, self.width, self.height, self.parent, self.width / 2, self.height / 2.2)
        self.cam4_stream.setup()

        self.cam1_stream.change_geometry(self.width / 3, self.height / 2.5)
        self.cam2_stream.change_geometry(self.width / 3, self.height / 2.5)
        self.cam3_stream.change_geometry(self.width / 3, self.height / 2.5)
        self.cam4_stream.change_geometry(self.width / 3, self.height / 2.5)
