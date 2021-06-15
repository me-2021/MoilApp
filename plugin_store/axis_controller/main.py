import os
from PyQt5 import QtWidgets
from base_plugin import Plugin
from .serial_axis_api import ThreadAxisAPI
from .ui_mainwindow import Ui_MainWindow


class Controller(Ui_MainWindow):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setupUi(self.parent)
        self.__threadAxisAPI = None
        self.__speed = 500
        self.set_speed.setValue(self.__speed)
        self.set_speed.setEnabled(False)
        self.btn_ok.setEnabled(False)
        self.input_abs.setEnabled(False)
        self.connect_event()
        self.position = None
        self.input_abs.setText("0")

    def connect_event(self):
        self.btn_connect.clicked.connect(self.go_connect_serial)
        self.btn_disconnect.clicked.connect(self.go_disconnect_serial)
        self.help_axis.clicked.connect(self.help_axis_controller)
        self.btn_reset.clicked.connect(self.go_reset)
        self.prev_speed.clicked.connect(self.go_related_moving_backward)
        self.next_speed.clicked.connect(self.go_related_moving_forward)
        self.btn_ok.clicked.connect(self.go_absolute_moving)
        self.set_speed.valueChanged.connect(self.set_speed_axis)

    def getPassword(self):
        """
        Get password from input dialog.

        """
        passwd, ok = QtWidgets.QInputDialog.getText(
            self.parent, "Authentication", "Sudo Password?", QtWidgets.QLineEdit.Password)
        if ok and passwd != '':
            return passwd

    def set_speed_axis(self):
        """
        Set the speed axis from the value given by user.

        """
        if self.__threadAxisAPI is not None:
            self.__speed = self.set_speed.value()
            self.__threadAxisAPI.set_speed(self.__speed)

    def go_connect_serial(self):
        """
        Connect the serial port into the system.

        """
        passwd = self.getPassword()
        if passwd:
            os.system("echo " + passwd + "| sudo -S chmod a+rw /dev/ttyUSB*")
            try:
                self.__threadAxisAPI = ThreadAxisAPI()
                self.__threadAxisAPI.connect_serial(serial_port="/dev/ttyUSB0")
                QtWidgets.QMessageBox.information(
                    self.parent, "Info !!", "Serial port connected!!\nAll system will be reset")
                self.set_speed.setEnabled(True)
                self.btn_ok.setEnabled(True)
                self.input_abs.setEnabled(True)
                self.go_reset()
                self.position = 0
            except OSError as err:
                self.__threadAxisAPI.logger.error(err)
                QtWidgets.QMessageBox.warning(
                    self.parent,
                    "Error",
                    "Make sure you have connect the serial port to the computer\nOr typing the correct "
                    "password!!\n\nError: " +
                    str(err))

    def go_disconnect_serial(self):
        """
        Disconnect the serial port with the system.

        """
        if self.__threadAxisAPI is not None:
            self.__threadAxisAPI.disconnect_serial()
            QtWidgets.QMessageBox.information(
                self.parent, "Info !!", "Serial port Disconnected!!")
            self.set_speed.setEnabled(False)
            self.btn_ok.setEnabled(False)
            self.input_abs.setEnabled(False)

        self.__threadAxisAPI = None

    def go_reset(self):
        """
        Reset the axis controller, speed and position.

        """
        if self.__threadAxisAPI is not None:
            self.position = 0
            self.__speed = 500

            self.__threadAxisAPI.axis_init()
            self.label_6.setText("0 mm")
            self.set_speed.setValue(self.__speed)
            QtWidgets.QMessageBox.information(
                self.parent, "Info !!", "Serial configuration has been reset!!")

    def go_absolute_moving(self):
        """
        axis will move with absolute moving.

        """
        if self.__threadAxisAPI is not None:
            try:
                self.position = float(self.input_abs.text())
                position = self.position
                self.__threadAxisAPI.absolute_moving(int(position))
                self.label_6.setText(str(round(self.position, 2)) + " mm")
            except ValueError as e:
                print("error: ", type(e))
                QtWidgets.QMessageBox.warning(
                    self.parent,
                    "Error",
                    "Make sure you input was number\n use ' . ' not ' , ' for decimal input"
                    "\n\nError: " +
                    str(e))

    def go_related_moving_forward(self):
        """
        axis will move with related moving forward which the value is plus.

        """
        if self.__threadAxisAPI is not None:
            self.forward = + 20
            self.__threadAxisAPI.related_moving(self.forward)
            self.position = self.position + 20
            if self.position >= 238.333:
                self.position = 238.33
                QtWidgets.QMessageBox.information(
                    self.parent, "information", "Maximum Distance\n"
                                                "By default these devices are only have maximum distance is 238.33"
                                                "mm\n\n "
                                                "Please contact Moil Lab if any setting change")
            self.label_6.setText(str(round(self.position, 2)) + " mm")

    def go_related_moving_backward(self):
        """
        axis will move with related moving backward which the value is minus.

        """
        if self.__threadAxisAPI is not None:
            self.backward = - 20

            self.__threadAxisAPI.related_moving(self.backward)
            self.position = self.position - 20
            if self.position <= -26.21:
                self.position = -26.21
                QtWidgets.QMessageBox.information(
                    self.parent, "information", "Minimum Distance\n"
                                                "By default these devices are only have minimum distance is -26.21"
                                                " \n\n"
                                                "Please contact Moil Lab if any setting change")
            self.label_6.setText(str(round(self.position, 2)) + " mm")

    @classmethod
    def help_axis_controller(cls):
        """
        Open prompt for axis controller help.

        """
        QtWidgets.QMessageBox.information(
            None, "Help", "This Plugin was using for control Moil Lab Devices\n"
                          "Please connect to your devices and input your password\n\n"
                          "Information !!\n"
                          "Speed\t: speed in RPM (1 RPM = 0.1 m/s)\n"
                          "Abs Move\t: move devices according to input\n"
                          "Forward\t: move forward 20 mm\n"
                          "backward\t: move Backward -20 mm\n\n"
                          "For more information Please Contact MOIL LAB\n")


class AxisController(Plugin):
    def __init__(self):
        """
        The class that represent the plugins application, class name will be read as
        the name of application.
        """
        super().__init__()
        self.apps = None
        self.description = "This is Axis Controller"

    def perform_operation(self, argument):
        """
        The main application will execute this function when click button open.

        Args:
            argument (): is the object widget from main application class.

        Returns:
            Will show the window of application.

        """
        self.apps = Controller(argument)
        argument.show()
