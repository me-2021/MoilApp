import json
from PyQt5 import QtWidgets
import sys

sys.path.append("..")
from user_interface.Ui_Camera_params import Ui_Dialog


class CameraParameters(Ui_Dialog):
    camera_parameter = 'cam_params/camera_parameters.json'

    def __init__(self, Parent, RecentWindow):
        """
        Create class controller open camera with inheritance from Ui Dialog Class.

        Args:
            Parent (): the main class of this application
            RecentWindow (): The windows displayed now
        """
        super(CameraParameters, self).__init__()
        self.parent = Parent
        self.recent = RecentWindow
        self.setupUi(self.recent)
        self.data = None
        self.a_dict = None
        self.list_cam_available()
        self.connect_event()

    def connect_event(self):
        """
        Connect a push button to each function
        """
        self.List_Parameter.activated.connect(self.handle_combo_box)
        self.btn_exit.clicked.connect(self.close_dialog)
        self.btn_delete.clicked.connect(self.delete_camera_param)
        self.btn_clean_all.clicked.connect(self.clear_all)
        self.btn_new.clicked.connect(self.add_new_params)
        self.btn_update.clicked.connect(self.update_params)

    def list_cam_available(self):
        """
        Provides information about parameters that have been save in the application

        """
        with open(self.camera_parameter) as f:
            self.data = json.load(f)
        new_list = []
        for key in self.data.keys():
            new_list.append(key)
        self.List_Parameter.addItems(new_list)

    def handle_combo_box(self):
        """
        Displays the selected parameter

        """
        camera = self.List_Parameter.currentText()
        if camera in self.data.keys():
            self.camera_name.setText(self.data[camera]["cameraName"])
            self.cam_sensor_width.setText(str(self.data[camera]['cameraSensorWidth']))
            self.cam_sensor_height.setText(str(self.data[camera]['cameraSensorHeight']))
            self.image_center_X.setText(str(self.data[camera]['iCx']))
            self.image_center_Y.setText(str(self.data[camera]['iCy']))
            self.ratio.setText(str(self.data[camera]['ratio']))
            self.image_width.setText(str(self.data[camera]['imageWidth']))
            self.image_height.setText(str(self.data[camera]['imageHeight']))
            self.calib_ratio.setText(str(self.data[camera]['calibrationRatio']))
            self.parameter0.setText(str(self.data[camera]['parameter0']))
            self.parameter1.setText(str(self.data[camera]['parameter1']))
            self.parameter2.setText(str(self.data[camera]['parameter2']))
            self.parameter3.setText(str(self.data[camera]['parameter3']))
            self.parameter4.setText(str(self.data[camera]['parameter4']))
            self.parameter5.setText(str(self.data[camera]['parameter5']))

    def delete_camera_param(self):
        """
        Delete parameters that have been save in the application

        """
        camera = self.List_Parameter.currentText()
        if camera in self.data.keys():
            reply = QtWidgets.QMessageBox.question(
                self.recent,
                'Message',
                "Are you want to delete?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                self.data.pop(camera)
                with open(self.camera_parameter, 'w') as f:
                    json.dump(self.data, f)
                self.clear_all()
                self.List_Parameter.clear()
                self.list_cam_available()
                QtWidgets.QMessageBox.information(
                    self.recent,
                    "Information!!",
                    "The parameter has been Deleted!!")
            else:
                pass

    def update_params(self):
        """
        Update parameters that have been save in the application
        (Update existing parameter)

        """
        self.get_params_from_form()
        if self.camera_name.text() in self.data.keys():
            reply = QtWidgets.QMessageBox.question(
                self.recent,
                'Message',
                "Are you want to Update?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                self.data.update(self.a_dict)
                with open(self.camera_parameter, 'w') as f:
                    json.dump(self.data, f)
                self.handle_combo_box()
                QtWidgets.QMessageBox.information(
                    self.recent,
                    "Information!!",
                    "The parameter has been updated!!")

            else:
                pass

    def add_new_params(self):
        """
        add new parameters to the application
        """
        self.get_params_from_form()
        if self.camera_name.text() in self.data.keys():
            QtWidgets.QMessageBox.information(
                self.recent,
                "Information!!",
                "The parameter already exist!!")
        else:
            reply = QtWidgets.QMessageBox.question(
                self.recent,
                'Message',
                "Are you want to Add Parameter?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                self.data.update(self.a_dict)
                with open(self.camera_parameter, 'w') as f:
                    json.dump(self.data, f)

                self.List_Parameter.clear()
                self.list_cam_available()
                QtWidgets.QMessageBox.information(
                    self.recent,
                    "Information!!",
                    "The new parameter added!!")

    def clear_all(self):
        """
        Clear all input parameter box (LineEdit)
        """
        self.camera_name.setText("")
        self.cam_sensor_width.setText("")
        self.cam_sensor_height.setText("")
        self.image_center_X.setText("")
        self.image_center_Y.setText("")
        self.ratio.setText("")
        self.image_width.setText("")
        self.image_height.setText("")
        self.calib_ratio.setText("")
        self.parameter0.setText("")
        self.parameter1.setText("")
        self.parameter2.setText("")
        self.parameter3.setText("")
        self.parameter4.setText("")
        self.parameter5.setText("")

    def get_params_from_form(self):
        """
        Get data from input parameter box (LineEdit)
        """
        self.a_dict = {self.camera_name.text(): {
            "cameraName": self.camera_name.text(),
            "cameraSensorWidth": float(self.cam_sensor_width.text()),
            "cameraSensorHeight": float(self.cam_sensor_height.text()),
            "iCx": float(self.image_center_X.text()),
            "iCy": float(self.image_center_Y.text()),
            "ratio": float(self.ratio.text()),
            "imageWidth": float(self.image_width.text()),
            "imageHeight": float(self.image_height.text()),
            "calibrationRatio": float(self.calib_ratio.text()),
            "parameter0": float(self.parameter0.text()),
            "parameter1": float(self.parameter1.text()),
            "parameter2": float(self.parameter2.text()),
            "parameter3": float(self.parameter3.text()),
            "parameter4": float(self.parameter4.text()),
            "parameter5": float(self.parameter5.text())
        }}

    def close_dialog(self):
        """
        Closes the parameter dialog frame and returns to the application
        """
        self.recent.reject()
