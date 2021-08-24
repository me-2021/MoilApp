from PyQt5 import QtWidgets

from plugin_store.tutorial_sample.ui.mainwindow_first_window import Ui_MainWinodwFirstWindow
from plugin_store.tutorial_sample.controller_second_window import UiControllerSecondWindow


class UiControllerFirstWindow(Ui_MainWinodwFirstWindow):

    def __init__(self, current_window):
        super(UiControllerFirstWindow, self).__init__()
        self.current_window = current_window
        self.setupUi(self.current_window)

        self.connect_event()

    def connect_event(self):
        self.pushbtn_go.clicked.connect(self.btn_clicked_go)

    def btn_clicked_go(self):

        second_window = QtWidgets.QDialog()
        ui_second_window = UiControllerSecondWindow(second_window, self.current_window)

        data = self.lineedit_date.text()
        print(data)
        if data != "":

            data = '"' + data + '"'
            data += " from first window"
            ui_second_window.label_data.setText(data)

        else:
            ui_second_window.label_data.setText("Didn't send any data")

        print('second UI:', ui_second_window.label_data.text())

        second_window.exec_()
        second_window.show()
