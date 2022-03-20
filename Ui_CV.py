
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

import sys
import cv2 as cv

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ChooseImgFile = QtWidgets.QPushButton(self.centralwidget)
        self.ChooseImgFile.setGeometry(QtCore.QRect(610, 10, 100, 30))
        self.ChooseImgFile.setObjectName("ChooseImgFile")
        self.FloderName = QtWidgets.QLineEdit(self.centralwidget)
        self.FloderName.setGeometry(QtCore.QRect(20, 10, 550, 30))
        self.FloderName.setObjectName("FloderName")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 80, 30))
        self.label.setObjectName("ImgShow")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(510, 110, 121, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.GrayImg = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GrayImg.sizePolicy().hasHeightForWidth())
        self.GrayImg.setSizePolicy(sizePolicy)
        self.GrayImg.setObjectName("GrayImg")
        self.verticalLayout.addWidget(self.GrayImg)
        spacerItem = QtWidgets.QSpacerItem(18, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        spacerItem2 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.ImgShow = QtWidgets.QLabel(self.centralwidget)
        self.ImgShow.setGeometry(QtCore.QRect(20, 120, 400, 250))   #选择图片的文件一定要与label的尺寸匹配
        self.ImgShow.setObjectName("ImgShow")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.ChooseImgFile.clicked.connect(self.msg)
        self.ChooseImgFile.clicked.connect(self.image_show)
    



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ChooseImgFile.setText(_translate("MainWindow", "选择文件"))
        self.label.setText(_translate("MainWindow", "原始图片展示"))
        self.GrayImg.setText(_translate("MainWindow", "灰度图"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.ImgShow.setText(_translate("MainWindow", "TextLabel"))

    def msg(self,filepath):
        m = QtWidgets.QFileDialog.getOpenFileName(None,"选取图片文件",'C:/','Image files (*.jpg *.gif *.png *.jpeg)')
        self.FloderName.setText(m[0])
    def image_show(self):
        print(self.FloderName.text()) #获取图片的路径
        self.ImgShow.setPixmap(QPixmap(self.FloderName.text()))
        self.ImgShow.setScaledContents(True)
        # self.QtWidgets.Qwidget.show()
        # pix = QtWidgets.QGraphicsPixmapItem  

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())