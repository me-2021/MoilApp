from .user_interface.ui_mainwindow import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from CoordinateSystem import CoordinateSystem
from moilutils.camera_parameters import CameraParameters
from moilutils.moilutils import MoilUtils
from MoilAlgorithm import MoilAlgorithm
from Exif.exif_lib import MetaImage
import cv2


class ControllerMain(Ui_MainWindow):
    def __init__(self, parent):
        super(ControllerMain, self).__init__()
        self.parent = parent
        self.setupUi(self.parent)
        self.img_l = None
        self.img_r = None
        self.img_result_l = None
        self.img_result_r = None
        self.coordinate_sys = None
        self.clicked_time_l = 0
        self.clicked_time_r = 0
        self.width_image = 720
        self.disable_widget()
        self.checkBox.setChecked(False)
        self.delta_x.setValue(2.0)
        self.camParams = QtWidgets.QDialog()
        self.winCamParams = CameraParameters(self, self.camParams)

        self.build_coordinate()
        self.connect_to_widget()

    def connect_to_widget(self):
        self.actionOpen_image.triggered.connect(self.open_image)
        self.actionMaximize.triggered.connect(self.onclick_maximize)
        self.actionMinimize.triggered.connect(self.onclick_minimize)
        self.Label_image_L.mousePressEvent = self.mouse_label_image_left
        self.Label_Image_R.mousePressEvent = self.mouse_label_image_right
        self.checkBox_5.clicked.connect(self.show_corner_detection)
        self.clear_button.clicked.connect(self.onclick_clear)
        self.pushButton.clicked.connect(self.calculate)
        self.OpenImage.clicked.connect(self.open_image)
        self.OpenParams.clicked.connect(self.cam_params_window)
        self.parent.closeEvent = self.close_event

    def cam_params_window(self):
        """
        Open the window of camera parameter form, this window you can update, add, and
        delete the camera parameter from database.

        """
        self.camParams.show()

    def disable_widget(self):
        self.clear_button.setEnabled(False)
        self.checkBox_5.setEnabled(False)
        self.checkBox_6.setEnabled(False)

    def enable_widget(self):
        self.clear_button.setEnabled(True)
        self.checkBox_5.setEnabled(True)
        self.checkBox_6.setEnabled(True)

    def onclick_maximize(self):
        self.frame_3.hide()
        self.line_3.hide()
        self.label.hide()
        if self.img_l is not None and self.img_r is not None:
            self.show_to_ui_window()
            self.ratioLabel()

    def onclick_minimize(self):
        self.frame_3.show()
        self.line_3.show()
        self.label.show()
        if self.img_l is not None and self.img_r is not None:
            self.ratioLabel()
            self.show_to_ui_window()

    def ratioLabel(self):
        self.Label_image_L.update()
        label_w = self.Label_image_L.width()
        label_h = self.Label_image_L.height()
        w = self.moildev.get_imageWidth()
        h = self.moildev.get_imageHeight()
        self.ratio_x = w / label_w
        self.ratio_y = h / label_h
        self.ratio_image_3.setText(str(self.ratio_x))

    def open_image(self):
        QtWidgets.QMessageBox.information(self.parent, "Information", "Select Source Image\nL -> R")
        # self.ui.status_label.setText("select the image !!")
        img_file_path_l = MoilUtils.select_file(self.parent, "Select Image", "", "Image Files (*.jpeg *.jpg "
                                                                                 "*.png *.gif *.bmg)")

        # self.ui.status_label.setText("Find the corner on the object !!")
        if img_file_path_l:
            self.label_status.setText("Corner Detection Process !!")
            img_file_path_r = MoilUtils.select_file(self.parent, "Select Image", "",
                                                    "Image Files (*.jpeg *.jpg *.png *.gif *.bmg)")

            if img_file_path_r:
                img_l = MoilUtils.read_image(img_file_path_l)
                img_r = MoilUtils.read_image(img_file_path_r)
                img = MetaImage(img_file_path_r)
                self.type_camera = img.read_comment()
                self.moildev = MoilUtils.connect_to_moildev(self.type_camera)
                if self.moildev is not None:
                    self.img_l, self.img_r = self.ratio3D_Measurement(img_l, img_r, self.width_image)
                    self.img_result_l = self.img_l.copy()
                    self.img_result_r = self.img_r.copy()
                    self.corner_list_1 = MoilUtils.corner_detect(self.img_l, sigma=3, threshold=0.01)
                    self.corner_list_2 = MoilUtils.corner_detect(self.img_r, sigma=3, threshold=0.01)
                    self.show_to_ui_window()
                    self.ratioLabel()
                    self.enable_widget()

    def ratio3D_Measurement(self, image_1, image_2, width=600):
        h, w = image_1.shape[:2]
        size = w, h
        self.Image_size_3.setText(str(size))
        r = width / float(w)
        hi = round(h * r)
        self.Label_image_L.setMaximumSize(QtCore.QSize(width, hi))
        self.Label_Image_R.setMaximumSize(QtCore.QSize(width, hi))
        img_result_1 = cv2.resize(image_1, (width, hi), interpolation=cv2.INTER_AREA)
        img_result_2 = cv2.resize(image_2, (width, hi), interpolation=cv2.INTER_AREA)
        return img_result_1, img_result_2

    def show_corner_detection(self):
        if self.checkBox_5.isChecked():
            self.img_result_l = MoilUtils.draw_corners(self.corner_list_1, self.img_l.copy())
            self.img_result_r = MoilUtils.draw_corners(self.corner_list_2, self.img_r.copy())
        else:
            self.img_result_l = self.img_l.copy()
            self.img_result_r = self.img_r.copy()
        self.show_to_ui_window()

    def onclick_clear(self):
        self.checkBox_5.setChecked(False)
        self.show_corner_detection()

    def build_coordinate(self):
        cam1_3d_coordinate = []
        cam2_3d_coordinate = []
        self.coordinate_sys = CoordinateSystem(cam1_3d_coordinate, cam2_3d_coordinate)

    def calculate(self):
        cam1_3d_coordinate = []
        cam2_3d_coordinate = []

        cam1_3d_coordinate.append(0)
        cam1_3d_coordinate.append(0)
        cam1_3d_coordinate.append(0)

        cam2_3d_coordinate.append(self.delta_x.value())
        cam2_3d_coordinate.append(0)
        cam2_3d_coordinate.append(0)

        self.coordinate_sys.set_cam1_3d_coordinate(cam1_3d_coordinate)
        self.coordinate_sys.set_cam2_3d_coordinate(cam2_3d_coordinate)

        dis = self.coordinate_sys.calculate_dis()
        self.label_distance.setText(str(round(dis, 2)))
        self.label_distanc_config.setText(str(round(dis, 2)))

    def mouse_label_image_left(self, e):
        if self.img_l is not None:
            if e.button() == QtCore.Qt.LeftButton:
                pos_x = round(e.x())
                pos_y = round(e.y())
                pos = '{},{}'.format(pos_y, pos_x)
                pos = tuple(map(int, pos.split(',')))
                if self.clicked_time_l == 0:
                    if self.checkBox.isChecked():
                        nearest = min(self.corner_list_1, key=lambda x: MoilUtils.distance(x, pos))
                        self.point_l_1 = (list(nearest)[1], list(nearest)[0])
                        coor_y = list(nearest)[0] * self.ratio_y
                        coor_x = list(nearest)[1] * self.ratio_x

                    else:
                        self.point_l_1 = pos_x, pos_y
                        coor_y = pos_y * self.ratio_y
                        coor_x = pos_x * self.ratio_x

                    point = (round(coor_y), round(coor_x))
                    self.point_1_image_1.setText(str(point))
                    label_clicked_x = round(coor_x)
                    label_clicked_y = round(coor_y)
                    delta_x = self.moildev.get_Icx() - label_clicked_x
                    delta_y = self.moildev.get_Icy() - label_clicked_y
                    alpha = MoilAlgorithm.get_alpha_griffey(delta_x, delta_y, self.ratio_x)
                    beta = MoilAlgorithm.get_beta(delta_x, delta_y)
                    print("alpha: {},Beta: {}".format(alpha, beta))
                    self.coordinate_sys.point1_alpha_l = alpha
                    self.coordinate_sys.point1_beta_l = beta
                    self.img_result_l = MoilUtils.drawPoint(self.img_result_l, self.Label_image_L, self.point_l_1)
                    self.show_to_ui_window()

                    self.clicked_time_l = 1

                elif self.clicked_time_l == 1:
                    if self.checkBox.isChecked():
                        nearest = min(self.corner_list_1, key=lambda x: MoilUtils.distance(x, pos))
                        self.point_l_2 = (list(nearest)[1], list(nearest)[0])
                        coor_y = list(nearest)[0] * self.ratio_y
                        coor_x = list(nearest)[1] * self.ratio_x

                    else:
                        self.point_l_2 = pos_x, pos_y
                        coor_y = pos_y * self.ratio_y
                        coor_x = pos_x * self.ratio_x

                    point = (round(coor_y), round(coor_x))
                    self.point_2_image_1.setText(str(point))
                    label_clicked_x = round(coor_x)
                    label_clicked_y = round(coor_y)
                    delta_x = self.moildev.get_Icx() - label_clicked_x
                    delta_y = self.moildev.get_Icy() - label_clicked_y
                    alpha = MoilAlgorithm.get_alpha_griffey(delta_x, delta_y, self.ratio_x)
                    beta = MoilAlgorithm.get_beta(delta_x, delta_y)
                    print("alpha: {},Beta: {}".format(alpha, beta))
                    self.coordinate_sys.point2_alpha_l = alpha
                    self.coordinate_sys.point2_beta_l = beta
                    self.img_result_l = MoilUtils.drawPoint(self.img_result_l, self.Label_image_L, self.point_l_2)
                    self.img_result_l = MoilUtils.draw_line(self.img_result_l, self.point_l_1, self.point_l_2)
                    self.show_to_ui_window()

                    self.clicked_time_l = 0

                else:
                    print("No Left Image !!!")

    def mouse_label_image_right(self, e):
        """ Get the position coordinate from mouse event"""
        if self.img_r is not None:
            if e.button() == QtCore.Qt.LeftButton:
                pos_x = round(e.x())
                pos_y = round(e.y())
                pos = '{},{}'.format(pos_y, pos_x)
                pos = tuple(map(int, pos.split(',')))
                if self.clicked_time_r == 0:
                    if self.checkBox.isChecked():
                        nearest = min(self.corner_list_2, key=lambda x: MoilUtils.distance(x, pos))
                        self.point_r_1 = (list(nearest)[1], list(nearest)[0])
                        coor_y = list(nearest)[0] * self.ratio_y
                        coor_x = list(nearest)[1] * self.ratio_x
                    else:
                        self.point_r_1 = pos_x, pos_y
                        coor_y = pos_y * self.ratio_y
                        coor_x = pos_x * self.ratio_x

                    point = (round(coor_y), round(coor_x))
                    self.point_1_image_2.setText(str(point))
                    label_clicked_x = round(coor_x)
                    label_clicked_y = round(coor_y)
                    delta_x = self.moildev.get_Icx() - label_clicked_x
                    delta_y = self.moildev.get_Icy() - label_clicked_y

                    alpha = MoilAlgorithm.get_alpha_griffey(delta_x, delta_y, self.ratio_x)
                    beta = MoilAlgorithm.get_beta(delta_x, delta_y)
                    print("alpha: {},Beta: {}".format(alpha, beta))
                    self.coordinate_sys.point1_alpha_r = alpha
                    self.coordinate_sys.point1_beta_r = beta
                    self.img_result_r = MoilUtils.drawPoint(self.img_result_r, self.Label_Image_R, self.point_r_1)
                    self.show_to_ui_window()
                    self.clicked_time_r = 1

                elif self.clicked_time_r == 1:
                    if self.checkBox.isChecked():
                        nearest = min(self.corner_list_2, key=lambda x: MoilUtils.distance(x, pos))
                        self.point_r_2 = (list(nearest)[1], list(nearest)[0])
                        coor_y = list(nearest)[0] * self.ratio_y
                        coor_x = list(nearest)[1] * self.ratio_x
                    else:
                        self.point_r_2 = pos_x, pos_y
                        coor_y = pos_y * self.ratio_y
                        coor_x = pos_x * self.ratio_x

                    point = (round(coor_y), round(coor_x))
                    self.point_2_image_2.setText(str(point))
                    label_clicked_x = round(coor_x)
                    label_clicked_y = round(coor_y)
                    delta_x = self.moildev.get_Icx() - label_clicked_x
                    delta_y = self.moildev.get_Icy() - label_clicked_y
                    alpha = MoilAlgorithm.get_alpha_griffey(delta_x, delta_y, self.ratio_x)
                    beta = MoilAlgorithm.get_beta(delta_x, delta_y)
                    print("alpha: {},Beta: {}".format(alpha, beta))
                    self.coordinate_sys.point2_alpha_r = alpha
                    self.coordinate_sys.point2_beta_r = beta
                    self.img_result_r = MoilUtils.drawPoint(self.img_result_r, self.Label_Image_R, self.point_r_2)
                    self.img_result_r = MoilUtils.draw_line(self.img_result_r, self.point_r_1, self.point_r_2)
                    self.show_to_ui_window()

                    self.clicked_time_r = 0

                else:
                    print("No Left Image !!!")

    def show_to_ui_window(self):
        MoilUtils.showing_image_object_measurement(self.Label_image_L,
                                                   self.img_result_l,
                                                   self.width_image)
        MoilUtils.showing_image_object_measurement(self.Label_Image_R,
                                                   self.img_result_r,
                                                   self.width_image)

    def close_event(self, e):
        self.camParams.close()
