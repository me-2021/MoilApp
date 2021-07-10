# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'from_figma.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 917)
        MainWindow.showMaximized()
        font = QtGui.QFont()
        font.setUnderline(False)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(60, 60))
        self.frame_2.setStyleSheet("background-color: #71D1BA;   \n"
                                   "border-radius: 10px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.btn_Home = QtWidgets.QPushButton(self.frame_2)
        self.btn_Home.setGeometry(QtCore.QRect(5, 5, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_Home.sizePolicy().hasHeightForWidth())
        self.btn_Home.setSizePolicy(sizePolicy)
        self.btn_Home.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_Home.setToolTipDuration(-1)
        self.btn_Home.setStyleSheet(
            "QPushButton{ background-color :  rgb(211, 215, 207);}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_Home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("icon/MoilApp 128px.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_Home.setIcon(icon)
        self.btn_Home.setIconSize(QtCore.QSize(40, 40))
        self.btn_Home.setEnabled(False)
        self.btn_Home.setObjectName("btn_Home")
        self.verticalLayout_4.addWidget(self.frame_2)
        spacerItem = QtWidgets.QSpacerItem(
            20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem)

        self.frame_feature = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_feature.sizePolicy().hasHeightForWidth())
        self.frame_feature.setSizePolicy(sizePolicy)
        self.frame_feature.setMinimumSize(QtCore.QSize(60, 190))
        self.frame_feature.setStyleSheet("border-color: rgb(66, 69, 183);\n"
                                         "border-radius: 10px;\n"
                                         "background-color: #71D1BA; ")
        self.frame_feature.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_feature.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_feature.setObjectName("frame_feature")
        self.btn_normal = QtWidgets.QPushButton(self.frame_feature)
        self.btn_normal.setGeometry(QtCore.QRect(5, 40, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_normal.sizePolicy().hasHeightForWidth())
        self.btn_normal.setSizePolicy(sizePolicy)
        self.btn_normal.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        self.btn_normal.setFont(font)
        self.btn_normal.setStyleSheet("QPushButton{ background-color :  rgb(211, 215, 207);}\n"
                                      "QPushButton::pressed{ background-color : #71AED1; }\n"
                                      "border-radius: 10px;")
        self.btn_normal.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/Default.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_normal.setIcon(icon1)
        self.btn_normal.setIconSize(QtCore.QSize(40, 40))
        self.btn_normal.setCheckable(True)
        self.btn_normal.setChecked(False)
        self.btn_normal.setObjectName("btn_normal")
        self.btn_anypoint = QtWidgets.QPushButton(self.frame_feature)
        self.btn_anypoint.setGeometry(QtCore.QRect(5, 90, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_anypoint.sizePolicy().hasHeightForWidth())
        self.btn_anypoint.setSizePolicy(sizePolicy)
        self.btn_anypoint.setMinimumSize(QtCore.QSize(30, 40))
        self.btn_anypoint.setStyleSheet("QPushButton{ background-color :  rgb(211, 215, 207);}\n"
                                        "QPushButton::pressed{ background-color : #71AED1; }\n"
                                        "border-radius: 10px;")
        self.btn_anypoint.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/Anypoint_color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_anypoint.setIcon(icon2)
        self.btn_anypoint.setIconSize(QtCore.QSize(40, 40))
        self.btn_anypoint.setCheckable(False)
        self.btn_anypoint.setObjectName("btn_anypoint")
        self.btn_panorama = QtWidgets.QPushButton(self.frame_feature)
        self.btn_panorama.setGeometry(QtCore.QRect(5, 140, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_panorama.sizePolicy().hasHeightForWidth())
        self.btn_panorama.setSizePolicy(sizePolicy)
        self.btn_panorama.setMinimumSize(QtCore.QSize(30, 40))
        self.btn_panorama.setStyleSheet("QPushButton{ background-color :  rgb(211, 215, 207);}\n"
                                        "QPushButton::pressed{ background-color : #71AED1; }\n"
                                        "border-radius: 10px;")
        self.btn_panorama.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/Panorama_color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_panorama.setIcon(icon3)
        self.btn_panorama.setIconSize(QtCore.QSize(40, 40))
        self.btn_panorama.setCheckable(False)
        self.btn_panorama.setObjectName("btn_panorama")
        self.label = QtWidgets.QLabel(self.frame_feature)
        self.label.setGeometry(QtCore.QRect(5, 10, 50, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("border-color: rgb(66, 69, 183);\n"
                                 "border-radius: 5px;\n"
                                 "background-color: #71D1BA; ")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.frame_feature)

        self.frame_help = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_help.sizePolicy().hasHeightForWidth())
        self.frame_help.setSizePolicy(sizePolicy)
        self.frame_help.setMinimumSize(QtCore.QSize(60, 190))
        self.frame_help.setStyleSheet("background-color: #71D1BA;   \n"
                                      "border-radius: 10px;")
        self.frame_help.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_help.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_help.setObjectName("frame_help")
        self.btn_about_moilapp = QtWidgets.QPushButton(self.frame_help)
        self.btn_about_moilapp.setGeometry(QtCore.QRect(5, 140, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_about_moilapp.sizePolicy().hasHeightForWidth())
        self.btn_about_moilapp.setSizePolicy(sizePolicy)
        self.btn_about_moilapp.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_about_moilapp.setStyleSheet("QPushButton{ background-color :  rgb(211, 215, 207);}\n"
                                         "QPushButton::pressed{ background-color : #71AED1; }\n"
                                         "border-radius: 10px;")
        self.btn_about_moilapp.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/Help question mark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_about_moilapp.setIcon(icon4)
        self.btn_about_moilapp.setIconSize(QtCore.QSize(40, 40))
        self.btn_about_moilapp.setObjectName("btn_about_moilapp")
        self.btn_MoilApp_help = QtWidgets.QPushButton(self.frame_help)
        self.btn_MoilApp_help.setGeometry(QtCore.QRect(5, 40, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_MoilApp_help.sizePolicy().hasHeightForWidth())
        self.btn_MoilApp_help.setSizePolicy(sizePolicy)
        self.btn_MoilApp_help.setMinimumSize(QtCore.QSize(30, 40))
        self.btn_MoilApp_help.setStyleSheet("QPushButton{ background-color :  rgb(211, 215, 207);}\n"
                                         "QPushButton::pressed{ background-color : #71AED1; }\n"
                                         "border-radius: 10px;")
        self.btn_MoilApp_help.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/Help MoilApp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_MoilApp_help.setIcon(icon5)
        self.btn_MoilApp_help.setIconSize(QtCore.QSize(35, 35))
        self.btn_MoilApp_help.setObjectName("btn_MoilApp_help")
        self.btn_about_us = QtWidgets.QPushButton(self.frame_help)
        self.btn_about_us.setGeometry(QtCore.QRect(5, 90, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_about_us.sizePolicy().hasHeightForWidth())
        self.btn_about_us.setSizePolicy(sizePolicy)
        self.btn_about_us.setMinimumSize(QtCore.QSize(30, 40))
        self.btn_about_us.setStyleSheet("QPushButton{ background-color :  rgb(211, 215, 207);}\n"
                                         "QPushButton::pressed{ background-color : #71AED1; }\n"
                                         "border-radius: 10px;")
        self.btn_about_us.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icon/Information mark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_about_us.setIcon(icon6)
        self.btn_about_us.setIconSize(QtCore.QSize(30, 40))
        self.btn_about_us.setObjectName("btn_about_us")
        self.label_2 = QtWidgets.QLabel(self.frame_help)
        self.label_2.setGeometry(QtCore.QRect(5, 10, 50, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-color: rgb(66, 69, 183);\n"
                                   "border-radius: 5px;\n"
                                   "background-color: #71D1BA; ")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.frame_help)

        #################################
        self.frame_clear = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_clear.sizePolicy().hasHeightForWidth())
        self.frame_clear.setSizePolicy(sizePolicy)
        self.frame_clear.setMinimumSize(QtCore.QSize(60, 95))
        self.frame_clear.setStyleSheet("background-color: #71D1BA;   \n"
                                       "border-radius: 10px;")
        self.frame_clear.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_clear.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_clear.setObjectName("frame_clear")

        self.label_clear = QtWidgets.QLabel(self.frame_clear)
        self.label_clear.setGeometry(QtCore.QRect(5, 10, 50, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_clear.sizePolicy().hasHeightForWidth())
        self.label_clear.setSizePolicy(sizePolicy)
        self.label_clear.setMinimumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.label_clear.setFont(font)
        self.label_clear.setStyleSheet("border-color: rgb(66, 69, 183);\n"
                                       "border-radius: 5px;\n"
                                       "background-color: #71D1BA; ")
        self.label_clear.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clear.setObjectName("label_clear")

        self.btn_clear = QtWidgets.QPushButton(self.frame_clear)
        self.btn_clear.setGeometry(QtCore.QRect(5, 40, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setMinimumSize(QtCore.QSize(40, 45))
        self.btn_clear.setStyleSheet("QPushButton{ background-color :  rgb(211, 215, 207);}\n"
                                     "QPushButton::pressed{ background-color : #71AED1; }\n"
                                     "border-radius: 10px;")
        self.btn_clear.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/Clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_clear.setIcon(icon4)
        self.btn_clear.setIconSize(QtCore.QSize(40, 40))
        self.btn_clear.setObjectName("btn_clear")
        self.verticalLayout_4.addWidget(self.frame_clear)

        # ++++++++++++++++++++++++++++++++++++++++

        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(
            10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_Open_Source = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_Open_Source.sizePolicy().hasHeightForWidth())
        self.frame_Open_Source.setSizePolicy(sizePolicy)
        self.frame_Open_Source.setMinimumSize(QtCore.QSize(170, 50))
        self.frame_Open_Source.setStyleSheet("background-color: #71D1BA;   \n"
                                             "border-radius: 10px;")
        self.frame_Open_Source.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Open_Source.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Open_Source.setObjectName("frame_Open_Source")
        self.btn_Open_Image = QtWidgets.QPushButton(self.frame_Open_Source)
        self.btn_Open_Image.setGeometry(QtCore.QRect(10, 5, 38, 40))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_Open_Image.sizePolicy().hasHeightForWidth())
        self.btn_Open_Image.setSizePolicy(sizePolicy)
        self.btn_Open_Image.setMinimumSize(QtCore.QSize(35, 30))
        self.btn_Open_Image.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_Open_Image.setStyleSheet(
            "QPushButton{ background-color :  rgb(211, 215, 207);}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_Open_Image.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(
            QtGui.QPixmap("icon/Load_image.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_Open_Image.setIcon(icon7)
        self.btn_Open_Image.setIconSize(QtCore.QSize(40, 40))
        self.btn_Open_Image.setCheckable(False)
        self.btn_Open_Image.setObjectName("btn_Open_Image")
        self.btn_Open_Video = QtWidgets.QPushButton(self.frame_Open_Source)
        self.btn_Open_Video.setGeometry(QtCore.QRect(60, 5, 38, 40))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_Open_Video.sizePolicy().hasHeightForWidth())
        self.btn_Open_Video.setSizePolicy(sizePolicy)
        self.btn_Open_Video.setMinimumSize(QtCore.QSize(38, 30))
        self.btn_Open_Video.setStyleSheet(
            "QPushButton{ background-color :  rgb(211, 215, 207);}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_Open_Video.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(
            QtGui.QPixmap("icon/Load_video.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_Open_Video.setIcon(icon8)
        self.btn_Open_Video.setIconSize(QtCore.QSize(40, 40))
        self.btn_Open_Video.setObjectName("btn_Open_Video")
        self.btn_Open_Cam = QtWidgets.QPushButton(self.frame_Open_Source)
        self.btn_Open_Cam.setGeometry(QtCore.QRect(110, 5, 50, 40))
        self.btn_Open_Cam.setStyleSheet(
            "QPushButton{ background-color :  rgb(211, 215, 207);}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_Open_Cam.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(
            QtGui.QPixmap("icon/Load_camera.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_Open_Cam.setIcon(icon9)
        self.btn_Open_Cam.setIconSize(QtCore.QSize(40, 40))
        self.btn_Open_Cam.setObjectName("btn_Open_Cam")
        self.horizontalLayout_3.addWidget(self.frame_Open_Source)
        self.frame_rotate = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_rotate.sizePolicy().hasHeightForWidth())
        self.frame_rotate.setSizePolicy(sizePolicy)
        self.frame_rotate.setMinimumSize(QtCore.QSize(110, 50))
        self.frame_rotate.setStyleSheet("background-color: #71D1BA;   \n"
                                        "border-radius: 10px;")
        self.frame_rotate.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_rotate.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_rotate.setObjectName("frame_rotate")
        self.btn_Rotate_Left = QtWidgets.QPushButton(self.frame_rotate)
        self.btn_Rotate_Left.setGeometry(QtCore.QRect(10, 5, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_Rotate_Left.sizePolicy().hasHeightForWidth())
        self.btn_Rotate_Left.setSizePolicy(sizePolicy)
        self.btn_Rotate_Left.setMinimumSize(QtCore.QSize(40, 30))
        self.btn_Rotate_Left.setStyleSheet(
            "QPushButton{ background-color :  rgb(211, 215, 207);}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_Rotate_Left.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(
            QtGui.QPixmap("icon/Rotate_left.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_Rotate_Left.setIcon(icon10)
        self.btn_Rotate_Left.setIconSize(QtCore.QSize(35, 35))
        self.btn_Rotate_Left.setObjectName("btn_Rotate_Left")
        self.btn_Rotate_Right = QtWidgets.QPushButton(self.frame_rotate)
        self.btn_Rotate_Right.setGeometry(QtCore.QRect(60, 5, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_Rotate_Right.sizePolicy().hasHeightForWidth())
        self.btn_Rotate_Right.setSizePolicy(sizePolicy)
        self.btn_Rotate_Right.setMinimumSize(QtCore.QSize(40, 30))
        self.btn_Rotate_Right.setStyleSheet(
            "QPushButton{ background-color :  rgb(211, 215, 207);}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_Rotate_Right.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(
            QtGui.QPixmap("icon/Rotate_right.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_Rotate_Right.setIcon(icon11)
        self.btn_Rotate_Right.setIconSize(QtCore.QSize(35, 35))
        self.btn_Rotate_Right.setObjectName("btn_Rotate_Right")
        self.horizontalLayout_3.addWidget(self.frame_rotate)

        self.frame_zoom = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_zoom.sizePolicy().hasHeightForWidth())
        self.frame_zoom.setSizePolicy(sizePolicy)
        self.frame_zoom.setMinimumSize(QtCore.QSize(200, 50))
        self.frame_zoom.setStyleSheet("background-color: #71D1BA;   \n"
                                      "border-radius: 10px;")
        self.frame_zoom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_zoom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_zoom.setObjectName("frame_zoom")
        self.btn_Zoom_in = QtWidgets.QPushButton(self.frame_zoom)
        self.btn_Zoom_in.setGeometry(QtCore.QRect(55, 5, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Zoom_in.sizePolicy().hasHeightForWidth())
        self.btn_Zoom_in.setSizePolicy(sizePolicy)
        self.btn_Zoom_in.setMinimumSize(QtCore.QSize(40, 30))
        self.btn_Zoom_in.setStyleSheet("QPushButton{ background-color :  #71D1BA;}\n"
                                       "QPushButton::pressed{ background-color : #71AED1; }\n"
                                       "border-radius: 10px;")
        self.btn_Zoom_in.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icon/Zoom-in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Zoom_in.setIcon(icon9)
        self.btn_Zoom_in.setIconSize(QtCore.QSize(40, 40))
        self.btn_Zoom_in.setObjectName("btn_Zoom_in")
        self.btn_Zoom_out = QtWidgets.QPushButton(self.frame_zoom)
        self.btn_Zoom_out.setGeometry(QtCore.QRect(5, 5, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Zoom_out.sizePolicy().hasHeightForWidth())
        self.btn_Zoom_out.setSizePolicy(sizePolicy)
        self.btn_Zoom_out.setMinimumSize(QtCore.QSize(40, 30))
        self.btn_Zoom_out.setStyleSheet("QPushButton{ background-color :  #71D1BA;}\n"
                                        "QPushButton::pressed{ background-color : #71AED1; }\n"
                                        "border-radius: 10px;")
        self.btn_Zoom_out.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icon/Zoom-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Zoom_out.setIcon(icon10)
        self.btn_Zoom_out.setIconSize(QtCore.QSize(40, 40))
        self.btn_Zoom_out.setObjectName("btn_Zoom_out")
        self.comboBox_zoom = QtWidgets.QComboBox(self.frame_zoom)
        self.comboBox_zoom.setGeometry(QtCore.QRect(105, 7, 85, 36))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.comboBox_zoom.setFont(font)
        self.comboBox_zoom.setStyleSheet("border-radius: 5px;\n"
                                         "border : 2px solid black;\n"
                                         "QComboBox::editable:pressed\n"
                                         "border : 2px solid;\n"
                                         "border-color : yellow\n"
                                         "")
        self.comboBox_zoom.setObjectName("comboBox_zoom")
        self.comboBox_zoom.addItem("")
        self.comboBox_zoom.addItem("")
        self.comboBox_zoom.addItem("")
        self.comboBox_zoom.addItem("")
        self.comboBox_zoom.addItem("")
        self.comboBox_zoom.addItem("")
        self.comboBox_zoom.addItem("")
        self.comboBox_zoom.addItem("")
        self.horizontalLayout_3.addWidget(self.frame_zoom)

        self.frame_save = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_save.sizePolicy().hasHeightForWidth())
        self.frame_save.setSizePolicy(sizePolicy)
        self.frame_save.setMinimumSize(QtCore.QSize(125, 50))
        self.frame_save.setStyleSheet("background-color: #71D1BA;   \n"
                                      "border-radius: 10px;")
        self.frame_save.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_save.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_save.setObjectName("frame_save")
        self.btn_Save_Image = QtWidgets.QPushButton(self.frame_save)
        self.btn_Save_Image.setGeometry(QtCore.QRect(10, 5, 45, 40))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_Save_Image.sizePolicy().hasHeightForWidth())
        self.btn_Save_Image.setSizePolicy(sizePolicy)
        self.btn_Save_Image.setMinimumSize(QtCore.QSize(45, 30))
        self.btn_Save_Image.setStyleSheet(
            "QPushButton{ background-color :  rgb(211, 215, 207);}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_Save_Image.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(
            QtGui.QPixmap("icon/Save_image.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_Save_Image.setIcon(icon14)
        self.btn_Save_Image.setIconSize(QtCore.QSize(40, 40))
        self.btn_Save_Image.setObjectName("btn_Save_Image")
        self.btn_Record_video = QtWidgets.QPushButton(self.frame_save)
        self.btn_Record_video.setGeometry(QtCore.QRect(65, 5, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_Record_video.sizePolicy().hasHeightForWidth())
        self.btn_Record_video.setSizePolicy(sizePolicy)
        self.btn_Record_video.setMinimumSize(QtCore.QSize(50, 40))
        self.btn_Record_video.setStyleSheet(
            "QPushButton{ background-color :  rgb(211, 215, 207);}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_Record_video.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(
            QtGui.QPixmap("icon/Save_video-record.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_Record_video.setIcon(icon15)
        self.btn_Record_video.setIconSize(QtCore.QSize(50, 40))
        self.btn_Record_video.setCheckable(True)
        self.btn_Record_video.setObjectName("btn_Record_video")
        self.horizontalLayout_3.addWidget(self.frame_save)

        # self.frame_ctrl_axis = QtWidgets.QFrame(self.centralwidget)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.frame_ctrl_axis.sizePolicy().hasHeightForWidth())
        # self.frame_ctrl_axis.setSizePolicy(sizePolicy)
        # self.frame_ctrl_axis.setMinimumSize(QtCore.QSize(495, 50))
        # self.frame_ctrl_axis.setStyleSheet("background-color: #71D1BA;   \n"
        #                                    "border-radius: 10px;")
        # self.frame_ctrl_axis.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_ctrl_axis.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_ctrl_axis.setObjectName("frame_ctrl_axis")
        # self.btn_ctrl_axis = QtWidgets.QPushButton(self.frame_ctrl_axis)
        # self.btn_ctrl_axis.setGeometry(QtCore.QRect(10, 5, 45, 40))
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.btn_ctrl_axis.sizePolicy().hasHeightForWidth())
        # self.btn_ctrl_axis.setSizePolicy(sizePolicy)
        # self.btn_ctrl_axis.setMinimumSize(QtCore.QSize(45, 30))
        # self.btn_ctrl_axis.setStyleSheet("QPushButton{ background-color :  rgb(211, 215, 207);}\n"
        #                                  "QPushButton::pressed{ background-color : #71AED1; }\n"
        #                                  "border-radius: 10px;")
        # self.btn_ctrl_axis.setText("")
        # icon16 = QtGui.QIcon()
        # icon16.addPixmap(QtGui.QPixmap("icon/axis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.btn_ctrl_axis.setIcon(icon16)
        # self.btn_ctrl_axis.setIconSize(QtCore.QSize(40, 35))
        # self.btn_ctrl_axis.setObjectName("btn_ctrl_axis")
        # self.horizontalLayout_3.addWidget(self.frame_ctrl_axis)

        self.frame_apps = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_apps.sizePolicy().hasHeightForWidth())
        self.frame_apps.setSizePolicy(sizePolicy)
        self.frame_apps.setMinimumSize(QtCore.QSize(420, 50))
        self.frame_apps.setStyleSheet("background-color: #71D1BA;   \n"
                                      "border-radius: 10px;")
        self.frame_apps.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_apps.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_apps.setObjectName("frame_apps")
        self.btn_add_apps = QtWidgets.QPushButton(self.frame_apps)
        self.btn_add_apps.setGeometry(QtCore.QRect(5, 5, 40, 40))
        self.btn_add_apps.setMinimumSize(QtCore.QSize(40, 30))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        self.btn_add_apps.setFont(font)
        self.btn_add_apps.setStyleSheet("QPushButton{ background-color :  #71D1BA;}\n"
                                        "QPushButton::pressed{ background-color : #71AED1; }\n"
                                        "border-radius: 10px;")
        self.btn_add_apps.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icon/Add_apps.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_apps.setIcon(icon13)
        self.btn_add_apps.setIconSize(QtCore.QSize(40, 40))
        self.btn_add_apps.setObjectName("btn_add_apps")
        self.btn_open_app = QtWidgets.QPushButton(self.frame_apps)
        self.btn_open_app.setGeometry(QtCore.QRect(330, 5, 40, 40))
        self.btn_open_app.setStyleSheet("QPushButton{ background-color :  #71D1BA;}\n"
                                        "QPushButton::pressed{ background-color : #71AED1; }\n"
                                        "border-radius: 10px;")
        self.btn_open_app.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icon/Open_apps.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_open_app.setIcon(icon14)
        self.btn_open_app.setIconSize(QtCore.QSize(50, 50))
        self.btn_open_app.setObjectName("btn_open_app")
        self.btn_delete_app = QtWidgets.QPushButton(self.frame_apps)
        self.btn_delete_app.setGeometry(QtCore.QRect(375, 5, 40, 40))
        self.btn_delete_app.setStyleSheet("QPushButton{ background-color :  #71D1BA;}\n"
                                          "QPushButton::pressed{ background-color : #71AED1; }\n"
                                          "border-radius: 10px;")
        self.btn_delete_app.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("icon/Delete_apps.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_delete_app.setIcon(icon15)
        self.btn_delete_app.setIconSize(QtCore.QSize(36, 36))
        self.btn_delete_app.setObjectName("btn_delete_app")
        self.comboBox = QtWidgets.QComboBox(self.frame_apps)
        self.comboBox.setGeometry(QtCore.QRect(55, 7, 270, 36))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("border-radius: 5px;\n"
                                    "border : 2px solid black;\n"
                                    "QComboBox::editable:pressed\n"
                                    "border : 2px solid;\n"
                                    "border-color : yellow\n"
                                    "")
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_3.addWidget(self.frame_apps)

        self.label_Application = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_Application.setFont(font)
        self.label_Application.setStyleSheet("border-radius: 10px;\n"
                                             "background-color: #71AED1;   ")
        self.label_Application.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Application.setObjectName("label_Application")
        self.horizontalLayout_3.addWidget(self.label_Application)
        # self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        # sizePolicy = QtWidgets.QSizePolicy(
        #     QtWidgets.QSizePolicy.Fixed,
        #     QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(
        #     self.frame_5.sizePolicy().hasHeightForWidth())
        # self.frame_5.setSizePolicy(sizePolicy)
        # self.frame_5.setMinimumSize(QtCore.QSize(50, 50))
        # self.frame_5.setStyleSheet("background-color: #71D1BA;   \n"
        #                            "border-radius: 10px;")
        # self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_5.setObjectName("frame_5")
        # self.btn_Quit = QtWidgets.QPushButton(self.frame_5)
        # self.btn_Quit.setGeometry(QtCore.QRect(5, 5, 40, 40))
        # sizePolicy = QtWidgets.QSizePolicy(
        #     QtWidgets.QSizePolicy.Fixed,
        #     QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(
        #     self.btn_Quit.sizePolicy().hasHeightForWidth())
        # self.btn_Quit.setSizePolicy(sizePolicy)
        # self.btn_Quit.setMinimumSize(QtCore.QSize(40, 40))
        # self.btn_Quit.setStyleSheet(
        #     "QPushButton{ background-color :  #71D1BA;}\n"
        #     "QPushButton::pressed{ background-color : #71AED1; }\n"
        #     "border-radius: 10px;\n"
        #     "border-radius: 10px;")
        # self.btn_Quit.setText("")
        # icon16 = QtGui.QIcon()
        # icon16.addPixmap(
        #     QtGui.QPixmap("icon/shutdown.png"),
        #     QtGui.QIcon.Normal,
        #     QtGui.QIcon.Off)
        # self.btn_Quit.setIcon(icon16)
        # self.btn_Quit.setIconSize(QtCore.QSize(40, 40))
        # self.btn_Quit.setObjectName("btn_Quit")
        # self.horizontalLayout_3.addWidget(self.frame_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Panel)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(
            QtCore.QRect(0, 0, 1450, 711))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(
            self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_Result_Image = QtWidgets.QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_Result_Image.sizePolicy().hasHeightForWidth())
        self.label_Result_Image.setSizePolicy(sizePolicy)
        # self.label_Result_Image.setMinimumSize(QtCore.QSize(600, 400))
        # self.label_Result_Image.setMaximumSize(QtCore.QSize(600, 400))
        # self.label_Result_Image.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Result_Image.setText("")
        self.label_Result_Image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Result_Image.setObjectName("label_Result_Image")

        self.rubberband = QtWidgets.QRubberBand(QtWidgets.QRubberBand.Rectangle, self.label_Result_Image)
        self.setMouseTracking(True)

        self.button_menu = QtWidgets.QPushButton(self.scrollArea)
        self.button_menu.setGeometry(QtCore.QRect(10, 10, 40, 30))
        self.button_menu.setStyleSheet(
            "QPushButton{\n"
            "  border-color: #71D1BA;\n"
            "  border-width: 2px;        \n"
            "  border-style: solid;\n"
            "  border-radius: 5px;\n"
            "}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "")
        self.button_menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("icon/Menu.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.button_menu.setIcon(icon)
        self.button_menu.setCheckable(True)
        self.button_menu.setChecked(False)
        self.button_menu.setIconSize(QtCore.QSize(40, 30))
        self.button_menu.setObjectName("button_menu")

        # self.label_34 = QtWidgets.QLabel(self.scrollArea)
        # self.label_34.setGeometry(QtCore.QRect(180, 60, 80, 80))
        # self.label_34.setText("")
        # self.label_34.setPixmap(QtGui.QPixmap("icon/north.png"))
        # self.label_34.setScaledContents(True)
        # self.label_34.setObjectName("label")

        self.frame_navigator = QtWidgets.QFrame(self.scrollArea)
        self.frame_navigator.setGeometry(QtCore.QRect(10, 40, 160, 290))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_navigator.sizePolicy().hasHeightForWidth())
        self.frame_navigator.setSizePolicy(sizePolicy)
        self.frame_navigator.setMinimumSize(QtCore.QSize(160, 160))
        self.frame_navigator.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_navigator.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_navigator.setLineWidth(0)
        self.frame_navigator.setObjectName("frame_navigator")
        self.frame_20 = QtWidgets.QFrame(self.frame_navigator)
        self.frame_20.setGeometry(QtCore.QRect(60, 10, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_20.setStyleSheet("background-color: #71D1BA;   \n"
                                    "border-radius: 10px;")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.btn_Up_View = QtWidgets.QPushButton(self.frame_20)
        self.btn_Up_View.setGeometry(QtCore.QRect(0, 0, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Up_View.sizePolicy().hasHeightForWidth())
        self.btn_Up_View.setSizePolicy(sizePolicy)
        self.btn_Up_View.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_Up_View.setStyleSheet("QPushButton{ background-color :  #71D1BA;}\n"
                                       "QPushButton::pressed{ background-color : #71AED1; }\n"
                                       "border-radius: 10px;")
        self.btn_Up_View.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/Up anypoint.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Up_View.setIcon(icon)
        self.btn_Up_View.setIconSize(QtCore.QSize(40, 40))
        self.btn_Up_View.setObjectName("btn_Up_View")
        self.frame_21 = QtWidgets.QFrame(self.frame_navigator)
        self.frame_21.setGeometry(QtCore.QRect(110, 60, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_21.setStyleSheet("background-color: #71D1BA;   \n"
                                    "border-radius: 10px;")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.btn_Right_view = QtWidgets.QPushButton(self.frame_21)
        self.btn_Right_view.setGeometry(QtCore.QRect(0, 0, 40, 40))
        self.btn_Right_view.setStyleSheet("QPushButton{ background-color :  #71D1BA;}\n"
                                          "QPushButton::pressed{ background-color : #71AED1; }\n"
                                          "border-radius: 10px;")
        self.btn_Right_view.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/Right anypoint.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Right_view.setIcon(icon1)
        self.btn_Right_view.setIconSize(QtCore.QSize(40, 40))
        self.btn_Right_view.setObjectName("btn_Right_view")
        self.frame_22 = QtWidgets.QFrame(self.frame_navigator)
        self.frame_22.setGeometry(QtCore.QRect(10, 60, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_22.setStyleSheet("background-color: #71D1BA;   \n"
                                    "border-radius: 10px;")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.btn_left_view = QtWidgets.QPushButton(self.frame_22)
        self.btn_left_view.setGeometry(QtCore.QRect(0, 0, 40, 40))
        self.btn_left_view.setStyleSheet("QPushButton{ background-color :  #71D1BA;}\n"
                                         "QPushButton::pressed{ background-color : #71AED1; }\n"
                                         "border-radius: 10px;")
        self.btn_left_view.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/Left anypoint.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_left_view.setIcon(icon2)
        self.btn_left_view.setIconSize(QtCore.QSize(40, 40))
        self.btn_left_view.setObjectName("btn_left_view")
        self.frame_23 = QtWidgets.QFrame(self.frame_navigator)
        self.frame_23.setGeometry(QtCore.QRect(60, 110, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_23.setStyleSheet("background-color: #71D1BA;   \n"
                                    "border-radius: 10px;")
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.btn_Down_view = QtWidgets.QPushButton(self.frame_23)
        self.btn_Down_view.setGeometry(QtCore.QRect(0, 0, 40, 40))
        self.btn_Down_view.setStyleSheet("QPushButton{ background-color :  #71D1BA;}\n"
                                         "QPushButton::pressed{ background-color : #71AED1; }\n"
                                         "border-radius: 10px;")
        self.btn_Down_view.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/Below anypoint.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Down_view.setIcon(icon3)
        self.btn_Down_view.setIconSize(QtCore.QSize(40, 40))
        self.btn_Down_view.setObjectName("btn_Down_view")
        self.frame_24 = QtWidgets.QFrame(self.frame_navigator)
        self.frame_24.setGeometry(QtCore.QRect(60, 60, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy)
        self.frame_24.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_24.setStyleSheet("background-color: #71D1BA;   \n"
                                    "border-radius: 10px;")
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.btn_center_view = QtWidgets.QPushButton(self.frame_24)
        self.btn_center_view.setGeometry(QtCore.QRect(0, 0, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_center_view.sizePolicy().hasHeightForWidth())
        self.btn_center_view.setSizePolicy(sizePolicy)
        self.btn_center_view.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_center_view.setStyleSheet("QPushButton{ background-color :  #71D1BA;}\n"
                                           "QPushButton::pressed{ background-color : #71AED1; }\n"
                                           "border-radius: 10px;")
        self.btn_center_view.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/Center anypoint.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_center_view.setIcon(icon4)
        self.btn_center_view.setIconSize(QtCore.QSize(30, 40))
        self.btn_center_view.setObjectName("btn_center_view")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.frame_navigator)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 160, 161, 27))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_mode = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.label_mode.setFont(font)
        self.label_mode.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_mode.setObjectName("label_mode")
        self.horizontalLayout_4.addWidget(self.label_mode)
        self.radio_btn_mode_1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.radio_btn_mode_1.setMinimumSize(QtCore.QSize(35, 0))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.radio_btn_mode_1.setFont(font)
        self.radio_btn_mode_1.setObjectName("radio_btn_mode_1")
        self.horizontalLayout_4.addWidget(self.radio_btn_mode_1)
        self.radio_btn_mode_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.radio_btn_mode_2.setMinimumSize(QtCore.QSize(35, 0))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.radio_btn_mode_2.setFont(font)
        self.radio_btn_mode_2.setObjectName("radio_btn_mode_2")
        self.horizontalLayout_4.addWidget(self.radio_btn_mode_2)

        self.alpha_2 = QtWidgets.QLabel(self.frame_navigator)
        self.alpha_2.setGeometry(QtCore.QRect(0, 189, 50, 27))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.alpha_2.setFont(font)
        self.alpha_2.setObjectName("alpha_2")

        self.beta_2 = QtWidgets.QLabel(self.frame_navigator)
        self.beta_2.setGeometry(QtCore.QRect(0, 219, 50, 27))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.beta_2.setFont(font)
        self.beta_2.setObjectName("beta_2")
        self.lineedit_alpha_2 = QtWidgets.QDoubleSpinBox(self.frame_navigator)
        self.lineedit_alpha_2.setGeometry(QtCore.QRect(60, 190, 80, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineedit_alpha_2.sizePolicy().hasHeightForWidth())
        self.lineedit_alpha_2.setSizePolicy(sizePolicy)
        self.lineedit_alpha_2.setDecimals(1)
        self.lineedit_alpha_2.setRange(-360.0, 360)
        # self.lineedit_alpha_2.setMinimum(-360.0)
        self.lineedit_alpha_2.setSingleStep(1.0)
        self.lineedit_alpha_2.setObjectName("lineedit_alpha_2")

        self.lineedit_beta_2 = QtWidgets.QDoubleSpinBox(self.frame_navigator)
        self.lineedit_beta_2.setGeometry(QtCore.QRect(60, 220, 80, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineedit_beta_2.sizePolicy().hasHeightForWidth())
        self.lineedit_beta_2.setSizePolicy(sizePolicy)
        self.lineedit_beta_2.setDecimals(1)
        self.lineedit_beta_2.setRange(-360.0, 360)
        # self.lineedit_beta_2.setMinimum(-360.0)
        self.lineedit_beta_2.setSingleStep(1.0)
        self.lineedit_beta_2.setObjectName("lineedit_beta_2")

        self.anypoint_zoom_2 = QtWidgets.QDoubleSpinBox(self.frame_navigator)
        self.anypoint_zoom_2.setGeometry(QtCore.QRect(60, 250, 80, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.anypoint_zoom_2.sizePolicy().hasHeightForWidth())
        self.anypoint_zoom_2.setSizePolicy(sizePolicy)
        self.anypoint_zoom_2.setDecimals(1)
        self.anypoint_zoom_2.setMaximum(14.0)
        self.anypoint_zoom_2.setMinimum(3.0)
        self.anypoint_zoom_2.setSingleStep(0.1)
        self.anypoint_zoom_2.setObjectName("anypoint_zoom_2")

        self.zoom_2 = QtWidgets.QLabel(self.frame_navigator)
        self.zoom_2.setGeometry(QtCore.QRect(0, 250, 50, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoom_2.sizePolicy().hasHeightForWidth())
        self.zoom_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.zoom_2.setFont(font)
        self.zoom_2.setObjectName("zoom_2")

        self.frame_panorama = QtWidgets.QFrame(self.scrollArea)
        self.frame_panorama.setGeometry(QtCore.QRect(10, 40, 200, 80))
        self.frame_panorama.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_panorama.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_panorama.setObjectName("frame_panorama")
        self.max_pano = QtWidgets.QSpinBox(self.frame_panorama)
        self.max_pano.setGeometry(QtCore.QRect(80, 10, 65, 30))
        self.max_pano.setMinimum(50)
        self.max_pano.setMaximum(110)
        self.max_pano.setSingleStep(1)
        self.max_pano.setObjectName("max_pano")
        self.max = QtWidgets.QLabel(self.frame_panorama)
        self.max.setGeometry(QtCore.QRect(10, 10, 70, 30))
        self.max.setObjectName("max")
        self.min_pano = QtWidgets.QSpinBox(self.frame_panorama)
        self.min_pano.setGeometry(QtCore.QRect(80, 45, 65, 30))
        self.min_pano.setMinimum(10)
        self.min_pano.setMaximum(100)
        self.min_pano.setSingleStep(1)
        self.min_pano.setObjectName("min_pano")
        self.min = QtWidgets.QLabel(self.frame_panorama)
        self.min.setGeometry(QtCore.QRect(10, 45, 70, 30))
        self.min.setObjectName("min")
        # self.pushButton = QtWidgets.QPushButton(self.frame_panorama)
        # self.pushButton.setGeometry(QtCore.QRect(150, 15, 50, 54))
        # self.pushButton.setText("")
        # self.pushButton.setIcon(icon6)
        # self.pushButton.setIconSize(QtCore.QSize(40, 40))
        # self.pushButton.setObjectName("pushButton")

        self.horizontalLayout_2.addWidget(self.label_Result_Image)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(
            50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.frame_16 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setMinimumSize(QtCore.QSize(50, 40))
        self.frame_16.setStyleSheet("background-color: #71D1BA;   \n"
                                    "border-radius: 10px;")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.btn_prev_video = QtWidgets.QPushButton(self.frame_16)
        self.btn_prev_video.setGeometry(QtCore.QRect(5, 5, 40, 30))
        self.btn_prev_video.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_prev_video.setStyleSheet(
            "QPushButton{ background-color :  #71D1BA;}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_prev_video.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(
            QtGui.QPixmap("icon/Rewind.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_prev_video.setIcon(icon17)
        self.btn_prev_video.setIconSize(QtCore.QSize(40, 40))
        self.btn_prev_video.setObjectName("btn_prev_video")
        self.horizontalLayout_4.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setMinimumSize(QtCore.QSize(50, 40))
        self.frame_17.setStyleSheet("background-color: #71D1BA;   \n"
                                    "border-radius: 10px;")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.btn_play_pouse = QtWidgets.QPushButton(self.frame_17)
        self.btn_play_pouse.setGeometry(QtCore.QRect(5, 5, 40, 30))
        self.btn_play_pouse.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_play_pouse.setStyleSheet(
            "QPushButton{ background-color :  #71D1BA;}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_play_pouse.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(
            QtGui.QPixmap("icon/Play.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_play_pouse.setIcon(icon18)
        self.btn_play_pouse.setIconSize(QtCore.QSize(40, 40))
        self.btn_play_pouse.setObjectName("btn_play_pouse")
        self.horizontalLayout_4.addWidget(self.frame_17)
        self.frame_18 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setMinimumSize(QtCore.QSize(50, 40))
        self.frame_18.setStyleSheet("background-color: #71D1BA;   \n"
                                    "border-radius: 10px;")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.btn_stop_video = QtWidgets.QPushButton(self.frame_18)
        self.btn_stop_video.setGeometry(QtCore.QRect(5, 5, 40, 30))
        self.btn_stop_video.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_stop_video.setStyleSheet(
            "QPushButton{ background-color :  #71D1BA;}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_stop_video.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(
            QtGui.QPixmap("icon/Stop.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_stop_video.setIcon(icon19)
        self.btn_stop_video.setIconSize(QtCore.QSize(40, 40))
        self.btn_stop_video.setObjectName("btn_stop_video")
        self.horizontalLayout_4.addWidget(self.frame_18)
        self.frame_13 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setMinimumSize(QtCore.QSize(50, 40))
        self.frame_13.setStyleSheet("background-color: #71D1BA;   \n"
                                    "border-radius: 10px;")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.btn_skip_video = QtWidgets.QPushButton(self.frame_13)
        self.btn_skip_video.setGeometry(QtCore.QRect(5, 5, 40, 30))
        self.btn_skip_video.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_skip_video.setStyleSheet(
            "QPushButton{ background-color :  #71D1BA;}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_skip_video.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(
            QtGui.QPixmap("icon/Forward.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_skip_video.setIcon(icon20)
        self.btn_skip_video.setIconSize(QtCore.QSize(40, 40))
        self.btn_skip_video.setObjectName("btn_skip_video")
        self.horizontalLayout_4.addWidget(self.frame_13)
        self.label_time_recent = QtWidgets.QLabel(self.centralwidget)
        self.label_time_recent.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(18)
        self.label_time_recent.setFont(font)
        self.label_time_recent.setStyleSheet("border-color: #71D1BA;\n"
                                             "border-width: 2px;        \n"
                                             "border-style: solid;\n"
                                             "border-radius: 10px;")
        self.label_time_recent.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_recent.setObjectName("label_time_recent")
        self.horizontalLayout_4.addWidget(self.label_time_recent)
        self.slider_Video = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.slider_Video.sizePolicy().hasHeightForWidth())
        self.slider_Video.setSizePolicy(sizePolicy)
        self.slider_Video.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.slider_Video.setFont(font)
        self.slider_Video.setStyleSheet("")
        self.slider_Video.setOrientation(QtCore.Qt.Horizontal)
        self.slider_Video.setObjectName("slider_Video")
        self.horizontalLayout_4.addWidget(self.slider_Video)
        self.label_time_end = QtWidgets.QLabel(self.centralwidget)
        self.label_time_end.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(18)
        self.label_time_end.setFont(font)
        self.label_time_end.setStyleSheet("border-color: #71D1BA;\n"
                                          "border-width: 2px;        \n"
                                          "border-style: solid;\n"
                                          "border-radius: 10px;")
        self.label_time_end.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_end.setObjectName("label_time_end")
        self.horizontalLayout_4.addWidget(self.label_time_end)
        spacerItem6 = QtWidgets.QSpacerItem(
            50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(
            10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_saved_image = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_saved_image.sizePolicy().hasHeightForWidth())
        self.label_saved_image.setSizePolicy(sizePolicy)
        self.label_saved_image.setMinimumSize(QtCore.QSize(320, 50))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_saved_image.setFont(font)
        self.label_saved_image.setStyleSheet(
            "border-color: rgb(66, 69, 183);\n"
            "background-color: #71D1BA;\n"
            "border-radius: 10px;")
        self.label_saved_image.setFrameShape(QtWidgets.QFrame.Box)
        self.label_saved_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_saved_image.setObjectName("label_saved_image")
        self.verticalLayout.addWidget(self.label_saved_image)
        spacerItem8 = QtWidgets.QSpacerItem(
            20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem8)

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(320, 0))
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listWidget.setViewMode(QtWidgets.QListView.IconMode)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)

        self.frame_original_image = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_original_image.sizePolicy().hasHeightForWidth())
        self.frame_original_image.setSizePolicy(sizePolicy)
        self.frame_original_image.setMinimumSize(QtCore.QSize(0, 220))
        self.frame_original_image.setStyleSheet(
            "background-color: rgb(0, 0, 0);\n"
            "border-radius: 10px;")
        self.frame_original_image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_original_image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_original_image.setObjectName("frame_original_image")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(
            self.frame_original_image)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_Original_Image = QtWidgets.QLabel(self.frame_original_image)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_Original_Image.sizePolicy().hasHeightForWidth())
        self.label_Original_Image.setSizePolicy(sizePolicy)
        self.label_Original_Image.setMinimumSize(QtCore.QSize(266, 200))
        self.label_Original_Image.setStyleSheet("border-radius: 10px;")
        self.label_Original_Image.setText("")
        self.label_Original_Image.setScaledContents(False)
        self.label_Original_Image.setMouseTracking(True)
        self.label_Original_Image.setObjectName("label_Original_Image")
        self.horizontalLayout_11.addWidget(self.label_Original_Image)
        self.verticalLayout.addWidget(self.frame_original_image)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1723, 28))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(14)
        font.setUnderline(False)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        self.menuHelp.setFont(font)
        self.menuHelp.setObjectName("menuHelp")

        self.menuWindow = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        self.menuWindow.setFont(font)
        self.menuWindow.setObjectName("menuWindow")

        self.menuApps = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        self.menuApps.setFont(font)
        self.menuApps.setObjectName("menuApps")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # creating a label widget
        self.mouseIcon = QtWidgets.QLabel()
        self.mouseIcon.setMaximumSize(QtCore.QSize(20, 20))
        self.mouseIcon.setPixmap(QtGui.QPixmap("icon/Mouse cursor.png"))
        self.mouseIcon.setScaledContents(True)
        self.status_alpha = QtWidgets.QLabel("Alpha: 0")
        self.status_alpha.setMinimumSize(QtCore.QSize(100, 20))
        self.status_alpha.setAlignment(QtCore.Qt.AlignCenter)

        self.status_beta = QtWidgets.QLabel("Beta: 0")
        self.status_beta.setMinimumSize(QtCore.QSize(100, 20))
        self.status_beta.setAlignment(QtCore.Qt.AlignCenter)

        self.spacer = QtWidgets.QLabel()
        self.spacer.setMinimumSize(QtCore.QSize(40, 20))

        self.statusbar.addPermanentWidget(self.mouseIcon)
        self.statusbar.addPermanentWidget(self.status_alpha)
        self.statusbar.addPermanentWidget(self.status_beta)
        self.statusbar.addPermanentWidget(self.spacer)

        MainWindow.setStatusBar(self.statusbar)

        self.actionLoad_Image = QtWidgets.QAction(MainWindow)
        self.actionLoad_Image.setIcon(icon7)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.actionLoad_Image.setFont(font)
        self.actionLoad_Image.setObjectName("actionLoad_Image")
        self.actionLoad_Video = QtWidgets.QAction(MainWindow)
        self.actionLoad_Video.setIcon(icon8)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.actionLoad_Video.setFont(font)
        self.actionLoad_Video.setObjectName("actionLoad_Video")
        self.actionOpen_Cam = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.actionOpen_Cam.setFont(font)
        self.actionOpen_Cam.setObjectName("actionOpen_Cam")
        self.actionRecord_video = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.actionRecord_video.setFont(font)
        self.actionRecord_video.setCheckable(True)
        self.actionRecord_video.setObjectName("actionRecord_video")
        self.actionSave_Image = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.actionSave_Image.setFont(font)
        self.actionSave_Image.setObjectName("actionSave_Image")

        self.actionExit = QtWidgets.QAction(MainWindow)
        icon_exit = QtGui.QIcon()
        icon_exit.addPixmap(
            QtGui.QPixmap("icon/Shutdown.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.actionExit.setIcon(icon_exit)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.actionExit.setFont(font)
        self.actionExit.setObjectName("actionExit")

        self.actionMaximize = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.actionMaximize.setFont(font)
        self.actionMaximize.setObjectName("actionMaximize")

        self.actionMinimize = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.actionMinimize.setFont(font)
        self.actionMinimize.setObjectName("actionMinimize")

        self.actionAdd_Apps = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.actionAdd_Apps.setFont(font)
        # self.actionMinimize.setCheckable(True)
        self.actionAdd_Apps.setObjectName("actionAdd_Apps")

        self.actionDelete_Apps = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.actionDelete_Apps.setFont(font)
        # self.actionMinimize.setCheckable(True)
        self.actionDelete_Apps.setObjectName("actionDelete_Apps")

        self.actionOpen_Apps = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.actionOpen_Apps.setFont(font)
        # self.actionMinimize.setCheckable(True)
        self.actionOpen_Apps.setObjectName("actionOpen_Apps")

        self.actionAbout_Apps = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.actionAbout_Apps.setFont(font)
        self.actionAbout_Apps.setObjectName("actionAbout_Apps")

        # self.actiontest = QtWidgets.QAction(MainWindow)
        # self.actiontest.setObjectName("actiontest")
        # self.actiontest1 = QtWidgets.QAction(MainWindow)
        # self.actiontest1.setObjectName("actiontest1")

        self.actionAbout_Us = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.actionAbout_Us.setFont(font)
        self.actionAbout_Us.setObjectName("actionAbout_Us")

        self.actionCreatePlugins = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.actionCreatePlugins.setFont(font)
        self.actionCreatePlugins.setObjectName("actionCreatePlugins")

        self.actionHelpPlugins = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.actionHelpPlugins.setFont(font)
        self.actionHelpPlugins.setObjectName("actionHelpPlugins")

        self.action_accessibility = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.action_accessibility.setFont(font)
        self.action_accessibility.setObjectName("action_accessibility")

        self.actionCamera_Parameters = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.actionCamera_Parameters.setFont(font)
        self.actionCamera_Parameters.setObjectName("actionCamera_Parameters")
        self.menuFile.addAction(self.actionLoad_Image)
        self.menuFile.addAction(self.actionLoad_Video)
        self.menuFile.addAction(self.actionOpen_Cam)
        self.menuFile.addAction(self.actionCamera_Parameters)
        self.menuFile.addAction(self.actionRecord_video)
        self.menuFile.addAction(self.actionSave_Image)
        self.menuFile.addAction(self.actionExit)
        self.menuWindow.addAction(self.actionMaximize)
        self.menuWindow.addAction(self.actionMinimize)

        self.menuApps.addAction(self.actionAdd_Apps)

        # self.actionOpen_Apps.addAction(self.actiontest)
        # self.actionOpen_Apps.addAction(self.actiontest1)

        self.menuApps.addAction(self.actionOpen_Apps)
        self.menuApps.addAction(self.actionDelete_Apps)
        self.menuApps.addAction(self.actionCreatePlugins)
        self.menuApps.addAction(self.actionHelpPlugins)

        self.menuHelp.addAction(self.actionAbout_Apps)
        self.menuHelp.addAction(self.actionAbout_Us)
        self.menuHelp.addAction(self.action_accessibility)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuApps.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MoilApp"))
        self.btn_Home.setShortcut(_translate("MainWindow", "H"))
        self.btn_Home.setToolTip(_translate("MainWindow", "MoilApp"))
        self.btn_Home.setStatusTip(_translate("MainWindow", "MoilApp icon"))

        self.label_Original_Image.setStatusTip(_translate("MainWindow", "Original image"))
        self.label_Result_Image.setStatusTip(_translate("MainWindow", "Processes image"))
        self.label_Application.setStatusTip(_translate("MainWindow", "MoilApp or type of Camera name"))
        self.slider_Video.setStatusTip(_translate("MainWindow", "Time of Video"))
        self.button_menu.setToolTip(_translate("MainWindow", "Support button"))
        self.button_menu.setStatusTip(_translate("MainWindow", "Support button for anypoint and panorama"))

        # view
        self.label.setText(_translate("MainWindow", "View"))
        self.btn_normal.setToolTip(_translate("MainWindow", "Normal View"))
        self.btn_normal.setStatusTip(_translate("MainWindow", "Show original image"))
        self.btn_anypoint.setToolTip(_translate("MainWindow", "Anypoint View"))
        self.btn_anypoint.setStatusTip(_translate("MainWindow", "Show anypoint View"))
        self.btn_panorama.setToolTip(_translate("MainWindow", "Panorama View"))
        self.btn_panorama.setStatusTip(_translate("MainWindow", "Show panorama image"))

        # source
        self.btn_Open_Image.setToolTip(_translate("MainWindow", "Load Image"))
        self.btn_Open_Image.setStatusTip(_translate("MainWindow", "Open image from local directory (Ctrl+i)"))
        self.btn_Open_Image.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.btn_Open_Video.setToolTip(_translate("MainWindow", "Load Video"))
        self.btn_Open_Video.setStatusTip(_translate("MainWindow", "Open Video file from local directory (Ctrl+v)"))
        self.btn_Open_Video.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.btn_Open_Cam.setToolTip(_translate("MainWindow", "Open Camera"))
        self.btn_Open_Cam.setStatusTip(_translate("MainWindow", "Open camera source, its can be streaming URL camera "
                                                                "or usb camera (Ctrl+C)"))
        self.btn_Open_Cam.setShortcut(_translate("MainWindow", "Ctrl+C"))
        # zoom
        self.btn_Zoom_in.setToolTip(_translate("MainWindow", "Zoom in"))
        self.btn_Zoom_in.setStatusTip(
            _translate("MainWindow", "Resize window size image on user interface view larger"))
        self.btn_Zoom_in.setShortcut(_translate("MainWindow", "="))
        self.btn_Zoom_out.setToolTip(_translate("MainWindow", "Zoom out"))
        self.btn_Zoom_out.setStatusTip(_translate("MainWindow", "Resize window size image on user interface view "
                                                                "smaller"))
        self.comboBox_zoom.setToolTip(_translate("MainWindow", "Zoom ratio"))
        self.comboBox_zoom.setStatusTip(_translate("MainWindow", "Zooming ratio between result frame with original view"
                                                                 ""))
        self.btn_Zoom_out.setShortcut(_translate("MainWindow", "-"))
        self.comboBox_zoom.setItemText(0, _translate("MainWindow", "25%"))
        self.comboBox_zoom.setItemText(1, _translate("MainWindow", "50%"))
        self.comboBox_zoom.setItemText(2, _translate("MainWindow", "75%"))
        self.comboBox_zoom.setItemText(3, _translate("MainWindow", "100%"))
        self.comboBox_zoom.setItemText(4, _translate("MainWindow", "125%"))
        self.comboBox_zoom.setItemText(5, _translate("MainWindow", "150%"))
        self.comboBox_zoom.setItemText(6, _translate("MainWindow", "175%"))
        self.comboBox_zoom.setItemText(7, _translate("MainWindow", "200%"))

        # rotate
        self.btn_Rotate_Left.setToolTip(_translate("MainWindow", "Rotate Left"))
        self.btn_Rotate_Left.setStatusTip(_translate("MainWindow", "Rotate the image counterclockwise by 10 degrees"))
        self.btn_Rotate_Right.setToolTip(_translate("MainWindow", "Rotate Right"))
        self.btn_Rotate_Right.setStatusTip(_translate("MainWindow", "Rotate the image clockwise by 10 degrees"))

        # player
        self.label_Application.setText(_translate("MainWindow", "MoilApp"))
        self.btn_prev_video.setShortcut(_translate("MainWindow", "Ctrl+Left"))
        self.btn_prev_video.setToolTip(_translate("MainWindow", "Rewind"))
        self.btn_prev_video.setStatusTip(_translate("MainWindow", "Rewind video for 5 seconds"))
        self.btn_play_pouse.setShortcut(_translate("MainWindow", "Space"))
        self.btn_play_pouse.setToolTip(_translate("MainWindow", "Play/Pause"))
        self.btn_play_pouse.setStatusTip(_translate("MainWindow", "Play or Pause video"))
        self.btn_stop_video.setShortcut(_translate("MainWindow", "0"))
        self.btn_stop_video.setToolTip(_translate("MainWindow", "Stop"))
        self.btn_stop_video.setStatusTip(_translate("MainWindow", "Stop video"))
        self.btn_skip_video.setShortcut(_translate("MainWindow", "Ctrl+Right"))
        self.btn_skip_video.setToolTip(_translate("MainWindow", "Forward"))
        self.btn_skip_video.setStatusTip(_translate("MainWindow", "Forward video for 5 seconds"))
        self.label_time_recent.setText(_translate("MainWindow", "00.00"))
        self.label_time_recent.setToolTip(_translate("MainWindow", "Current time"))
        self.label_time_recent.setStatusTip(_translate("MainWindow", "Starting video / Show current time"))

        self.label_time_end.setText(_translate("MainWindow", "00.00"))
        self.label_time_end.setToolTip(_translate("MainWindow", "End video"))
        self.label_time_end.setStatusTip(_translate("MainWindow", "Display the end time of the video"))

        # help
        self.label_2.setText(_translate("MainWindow", "Help"))
        self.label_clear.setText(_translate("MainWindow", "Clear"))
        self.btn_clear.setToolTip(_translate("MainWindow", "Clear"))
        self.btn_clear.setStatusTip(_translate("MainWindow", "Remove all content on user interface"))
        self.btn_about_us.setShortcut(_translate("MainWindow", "Ctrl+Shift+/"))

        self.btn_about_us.setToolTip(_translate("MainWindow", "About Us"))
        self.btn_about_us.setStatusTip(_translate("MainWindow", "Show information about developer grub"))
        self.btn_MoilApp_help.setToolTip(_translate("MainWindow", "MoilApp Helps"))
        self.btn_MoilApp_help.setStatusTip(_translate("MainWindow", "Information of All application"))
        self.btn_about_moilapp.setToolTip(_translate("MainWindow", "About MoilApp"))
        self.btn_about_moilapp.setStatusTip(_translate("MainWindow", "Show information about MoilApp"))

        # save
        self.btn_Save_Image.setToolTip(_translate("MainWindow", "Save Image"))
        self.btn_Save_Image.setStatusTip(_translate("MainWindow", "For save your image"))
        self.btn_Record_video.setToolTip(_translate("MainWindow", "Record Video"))
        self.btn_Record_video.setStatusTip(_translate("MainWindow", "For record your video"))
        self.label_saved_image.setText(_translate("MainWindow", "Image Saved"))
        self.label_saved_image.setStatusTip(_translate("MainWindow", "Every image save will show in below this frame"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.menuApps.setTitle(_translate("MainWindow", "Apps"))
        # self.actionOpen_Apps

        # self.actiontest.setText(_translate("MainWindow", "test"))
        # self.actiontest1.setText(_translate("MainWindow", "test1"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionLoad_Image.setText(_translate("MainWindow", "Load Image"))
        self.actionLoad_Video.setText(_translate("MainWindow", "Load Video"))
        self.actionOpen_Cam.setText(_translate("MainWindow", "Open Cam"))
        self.actionRecord_video.setText(
            _translate("MainWindow", "Record video"))
        self.actionSave_Image.setText(_translate("MainWindow", "Save Image"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionMaximize.setText(_translate("MainWindow", "Maximize"))
        self.actionMinimize.setText(_translate("MainWindow", "Minimize"))
        self.actionAdd_Apps.setText(_translate("MainWindow", "Add Plugins"))
        self.actionOpen_Apps.setText(_translate("MainWindow", "Open Plugins"))
        self.actionDelete_Apps.setText(_translate("MainWindow", "Delete Plugins"))
        self.actionCreatePlugins.setText(_translate("MainWindow", "Create Plugins"))
        self.actionHelpPlugins.setText(_translate("MainWindow", "Help Plugins"))

        self.actionAbout_Apps.setText(_translate("MainWindow", "About Apps"))
        self.actionAbout_Us.setText(_translate("MainWindow", "About Us"))
        self.action_accessibility.setText(_translate("MainWindow", "Accessibility"))

        self.btn_Up_View.setShortcut(_translate("MainWindow", "Up"))
        self.btn_Up_View.setToolTip(_translate("MainWindow", "Up view"))
        self.btn_Up_View.setStatusTip(_translate("MainWindow", "Showing anypoint on up direction"))
        self.btn_Right_view.setShortcut(_translate("MainWindow", "Right"))
        self.btn_Right_view.setToolTip(_translate("MainWindow", "Right view"))
        self.btn_Right_view.setStatusTip(_translate("MainWindow", "Showing anypoint on right direction"))
        self.btn_left_view.setShortcut(_translate("MainWindow", "Left"))
        self.btn_left_view.setToolTip(_translate("MainWindow", "Left view"))
        self.btn_left_view.setStatusTip(_translate("MainWindow", "Showing anypoint on left direction"))
        self.btn_Down_view.setShortcut(_translate("MainWindow", "Down"))
        self.btn_Down_view.setToolTip(_translate("MainWindow", "Below view"))
        self.btn_Down_view.setStatusTip(_translate("MainWindow", "Showing anypoint on below direction"))
        self.btn_center_view.setToolTip(_translate("MainWindow", "Center view"))
        self.btn_center_view.setStatusTip(_translate("MainWindow", "Showing center view of anypoint"))
        self.label_mode.setText(_translate("MainWindow", "Mode:"))
        self.radio_btn_mode_1.setText(_translate("MainWindow", "1"))
        self.radio_btn_mode_1.setToolTip(_translate("MainWindow", "Mode 1"))
        self.radio_btn_mode_1.setStatusTip(_translate("MainWindow", "Anypoint Mode 1"))
        self.radio_btn_mode_2.setText(_translate("MainWindow", "2"))
        self.radio_btn_mode_2.setToolTip(_translate("MainWindow", "Mode 2"))
        self.radio_btn_mode_2.setStatusTip(_translate("MainWindow", "Anypoint Mode 2"))
        self.alpha_2.setText(_translate("MainWindow", "Alpha:"))
        self.lineedit_alpha_2.setToolTip(_translate("MainWindow", "Alpha degree"))
        self.lineedit_alpha_2.setStatusTip(_translate("MainWindow", "The value of alpha degree"))
        self.beta_2.setText(_translate("MainWindow", "Beta  :"))
        self.lineedit_beta_2.setToolTip(_translate("MainWindow", "Beta degree"))
        self.lineedit_beta_2.setStatusTip(_translate("MainWindow", "The value of beta degree"))
        self.zoom_2.setText(_translate("MainWindow", "Zoom:"))
        self.anypoint_zoom_2.setToolTip(_translate("MainWindow", "Zoom factor"))
        self.anypoint_zoom_2.setStatusTip(_translate("MainWindow", "Zoom factor of anypoint"))

        # Plugins
        self.btn_add_apps.setToolTip(_translate("MainWindow", "Add apps"))
        self.btn_add_apps.setStatusTip(_translate("MainWindow", "Add new plugin applications"))
        self.comboBox.setToolTip(_translate("MainWindow", "Application list"))
        self.comboBox.setStatusTip(_translate("MainWindow", "Select application here to open or delete"))
        self.btn_open_app.setToolTip(_translate("MainWindow", "Open apps"))
        self.btn_open_app.setStatusTip(_translate("MainWindow", "Open plugin application"))
        self.btn_delete_app.setToolTip(_translate("MainWindow", "Delete apps"))
        self.btn_delete_app.setStatusTip(_translate("MainWindow", "Delete plugin application"))
        self.actionCamera_Parameters.setText(_translate("MainWindow", "Cam Parameters"))

        self.max.setText(_translate("MainWindow", "Max Fov :"))
        self.max_pano.setToolTip(_translate("MainWindow", "Maximal FoV"))
        self.max_pano.setStatusTip(_translate("MainWindow", "Maximal degree of Field of view"))
        self.min_pano.setToolTip(_translate("MainWindow", "Minimal FoV"))
        self.min_pano.setStatusTip(_translate("MainWindow", "Minimal degree of Field of view"))
        self.min.setText(_translate("MainWindow", "Min Fov :"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
