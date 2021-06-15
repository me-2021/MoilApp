import webbrowser
from PyQt5 import QtWidgets, QtGui
import os


class Help():
    def __init__(self):
        super(Help, self).__init__()

    @classmethod
    def open_information_moildev(self):
        # file = os.path.realpath('./plugins/Thread_inspection/help/index.html')
        # print(file)
        # webbrowser.open('file://' + file)
        webbrowser.open('https://github.com/MoilOrg/MoilApps-Plugins/wiki')

    @classmethod
    def about_us(self):
        """
        Showing prompt About us information (MOIL LAB).

        Returns:
            None.
        """
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("About Us")
        msgbox.setText(
            "MOIL \n\nOmnidirectional Imaging & Surveillance Lab\nMing Chi University of Technology\n")
        msgbox.setIconPixmap(QtGui.QPixmap('./images/moildev2.png'))
        msgbox.exec()

    @classmethod
    def help_moildev_apps(self):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("Help !!")
        msgbox.setText(
            "Moildev-Apps\n\n"
            "Moildev-Apps is software to process fisheye "
            "image with the result panorama widget_controller and Anypoint"
            " widget_controller. \n\nThe panoramic widget_controller may present a horizontal"
            "widget_controller in a specific immersed environment to meet the"
            "common human visual perception, while the Anypoint"
            "widget_controller is an image that has been undistorted in a certain"
            "area according to the input coordinates."
            "\n\nMore reference about Moildev, contact us\n\n")
        msgbox.setIconPixmap(QtGui.QPixmap('images/moildev.png'))
        msgbox.exec()
