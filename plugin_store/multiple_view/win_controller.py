from .user_interface.ui_mainwindoww import Ui_MainWindow
from moilutils import MoilUtils
from Exif.exif_lib import MetaImage
from help.help import Help
import datetime
import cv2
import json
from PyQt5 import QtWidgets, QtCore, QtGui
from video_controller import VideoController
from moilutils.select_source_camera import OpenCameraSource


class UiController(Ui_MainWindow):
    camera_parameter = 'cam_params/camera_parameters.json'

    def __init__(self, mainWindow):
        super(UiController, self).__init__()
        self.Dialog = QtWidgets.QDialog()
        self.parent = mainWindow
        self.setupUi(self.parent)
        self.type_camera = None
        self.normal_view = False
        self.single_view = False
        self.multiple_view = False
        self.cam = False
        self.moildev = None
        self.zoom_any = 4
        self.anypoint_mode = 2
        self.window = None
        self.image = None
        self.dir_save = None
        self.width_result_image = 1360
        self.width_result_multi = 540
        self.width_ori_image = 340
        self.video_controller = VideoController(self)
        self.video_controller.set_button_disable()
        self.openCam = QtWidgets.QDialog()
        self.winOpenCam = OpenCameraSource(self, self.openCam)
        self.hide_widget_for_original()
        self.connect_event()

    def connect_event(self):
        self.actionOpen_Image.triggered.connect(self.open_image)
        self.actionLoad_Video.triggered.connect(self.load_video)
        self.actionOpen_Camera.triggered.connect(self.onclick_open_camera)
        self.actionSave_image.triggered.connect(self.save_image)
        self.pushButton_2.clicked.connect(self.open_image)
        self.pushButton.clicked.connect(self.load_video)
        self.pushButton_3.clicked.connect(self.onclick_open_camera)
        self.btn_6view.clicked.connect(self.onclick_multiple_view)
        self.btn_ori_view.clicked.connect(self.onclick_original)
        self.btn_view_1.clicked.connect(self.onclick_window_left_top)
        self.btn_view_2.clicked.connect(self.onclick_window_top)
        self.btn_view_3.clicked.connect(self.onclick_window_right_top)
        self.btn_view_4.clicked.connect(self.onclick_window_left)
        self.btn_view_5.clicked.connect(self.onclick_window_middle)
        self.btn_view_6.clicked.connect(self.onclick_window_right)
        self.label_image1.mousePressEvent = self.mouse_window_lt
        self.label_image2.mousePressEvent = self.mouse_window_t
        self.label_image3.mousePressEvent = self.mouse_window_rt
        self.label_image4.mousePressEvent = self.mouse_window_l
        self.label_image5.mousePressEvent = self.mouse_window_m
        self.label_image6.mousePressEvent = self.mouse_window_r
        self.label_Original_image.wheelEvent = self.mouse_wheelEvent
        self.label_Original_image.mouseReleaseEvent = self.mouse_release_event
        self.parent.closeEvent = self.closeEvent

    def hide_widget_for_original(self):
        self.scrollArea_3.hide()
        self.frame_2.hide()

    def open_image(self):
        filename = MoilUtils.select_file(self.parent, "Select Image", "",
                                         "Image Files (*.jpeg *.jpg *.png *.gif *.bmg)")
        if filename:
            self.image = MoilUtils.read_image(filename)
            img = MetaImage(filename)
            self.type_camera = img.read_comment()
            if self.type_camera:
                self.cam = False
                self.onclick_original()
                self.video_controller.set_button_disable()

    def load_video(self):
        """
        Open Dialog to search video file from Directory. after you select the video file, it will show the prompt
        to select the type of camera.

        """
        video_source = MoilUtils.select_file(self.parent,
                                             "Select Video Files",
                                             "",
                                             "Video Files (*.mp4 *.avi *.mpg *.gif *.mov)")
        if video_source:
            self.select_camera_type()
            if self.type_camera is not None:
                self.running_video(video_source)
                self.onclick_original()

    def running_video(self, video_source):
        """
        Open Video following the source given.

        Args:
            video_source (): the source of media, can be camera and video file.

        """
        self.video_controller.set_button_enable()
        self.cap = cv2.VideoCapture(video_source)
        _, image = self.cap.read()
        if image is None:
            QtWidgets.QMessageBox.information(self.parent, "Information", "No source camera founded")
        else:
            self.cam = True
            self.video_controller.next_frame_slot()
            self.video_controller.set_button_enable()

    def onclick_open_camera(self):
        """
        Show the window of selection camera source.

        """
        self.openCam.show()

    def open_camera(self):
        """
        open the camera from the available source in the system,
        this function provide 2 source namely USB cam and Streaming Cam from Raspberry pi.
        """
        camera_source = self.winOpenCam.camera_source_used()
        self.select_camera_type()
        if self.type_camera is not None:
            self.running_video(camera_source)
            self.onclick_original()

    def select_camera_type(self):
        """
        Select the camera type prompt.

        """
        with open(self.camera_parameter) as f:
            data = json.load(f)
        new_list = []
        for key in data.keys():
            new_list.append(key)
        self.Dialog.setObjectName("Dialog")
        self.Dialog.setWindowTitle("Select Camera !!!")
        self.Dialog.resize(240, 120)
        buttonBox = QtWidgets.QDialogButtonBox(self.Dialog)
        buttonBox.setGeometry(QtCore.QRect(20, 80, 200, 32))
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        buttonBox.setObjectName("buttonBox")
        self.comboBox_cam_type = QtWidgets.QComboBox(self.Dialog)
        self.comboBox_cam_type.setGeometry(QtCore.QRect(20, 40, 200, 30))
        self.comboBox_cam_type.setObjectName("comboBox")
        self.comboBox_cam_type.addItems(new_list)
        label = QtWidgets.QLabel(self.Dialog)
        label.setGeometry(QtCore.QRect(10, 10, 220, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(13)
        label.setFont(font)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setObjectName("label")
        label.setText("Select the camera type !!!")

        buttonBox.accepted.connect(self.dialog_camera_oke)
        buttonBox.rejected.connect(self.Dialog.reject)

        self.Dialog.exec_()

    def dialog_camera_oke(self):
        """
        The function will execute when you press accept or ok in dialog camera type selection.

        """
        self.type_camera = self.comboBox_cam_type.currentText()
        self.Dialog.close()

    def onclick_original(self):
        self.btn_ori_view.setChecked(True)
        self.btn_6view.setChecked(False)
        self.btn_view_1.setChecked(False)
        self.btn_view_2.setChecked(False)
        self.btn_view_3.setChecked(False)
        self.btn_view_4.setChecked(False)
        self.btn_view_5.setChecked(False)
        self.btn_view_6.setChecked(False)
        if self.image is not None:
            self.normal_view = True
            self.single_view = False
            self.multiple_view = False
            self.hide_widget_for_original()
            self.label_3.show()
            self.scrollArea.show()
            self.listWidget.show()
            self.show_to_window()

    def onclick_multiple_view(self):
        self.btn_ori_view.setChecked(False)
        self.btn_6view.setChecked(True)
        self.btn_view_1.setChecked(False)
        self.btn_view_2.setChecked(False)
        self.btn_view_3.setChecked(False)
        self.btn_view_4.setChecked(False)
        self.btn_view_5.setChecked(False)
        self.btn_view_6.setChecked(False)
        if self.image is not None:
            self.window_left_top()
            self.window_top()
            self.window_right_top()
            self.window_left()
            self.window_middle()
            self.window_right()
            self.normal_view = False
            self.single_view = False
            self.multiple_view = True
            self.show_to_window()

    def window_left_top(self):
        self.normal_view = False
        self.single_view = True
        self.multiple_view = False
        self.window = 1
        moildev = MoilUtils.connect_to_moildev(self.type_camera)
        self.mapX_1, self.mapY_1, = moildev.getAnypointMaps(30,-50,
                                                            self.zoom_any,
                                                            self.anypoint_mode)

    def onclick_window_left_top(self):
        self.btn_ori_view.setChecked(False)
        self.btn_6view.setChecked(False)
        self.btn_view_1.setChecked(True)
        self.btn_view_2.setChecked(False)
        self.btn_view_3.setChecked(False)
        self.btn_view_4.setChecked(False)
        self.btn_view_5.setChecked(False)
        self.btn_view_6.setChecked(False)
        if self.image is not None:
            self.window_left_top()
            self.show_to_window()

    def window_top(self):
        self.normal_view = False
        self.single_view = True
        self.multiple_view = False
        self.window = 2
        moildev = MoilUtils.connect_to_moildev(self.type_camera)
        self.mapX_2, self.mapY_2, = moildev.getAnypointMaps(50, 0,
                                                            self.zoom_any,
                                                            self.anypoint_mode)

    def onclick_window_top(self):
        self.btn_ori_view.setChecked(False)
        self.btn_6view.setChecked(False)
        self.btn_view_1.setChecked(False)
        self.btn_view_2.setChecked(True)
        self.btn_view_3.setChecked(False)
        self.btn_view_4.setChecked(False)
        self.btn_view_5.setChecked(False)
        self.btn_view_6.setChecked(False)
        if self.image is not None:
            self.window_top()
            self.show_to_window()

    def window_right_top(self):
        self.normal_view = False
        self.single_view = True
        self.multiple_view = False
        self.window = 3
        moildev = MoilUtils.connect_to_moildev(self.type_camera)
        self.mapX_3, self.mapY_3, = moildev.getAnypointMaps(30, 50,
                                                            self.zoom_any,
                                                            self.anypoint_mode)

    def onclick_window_right_top(self):
        self.btn_ori_view.setChecked(False)
        self.btn_6view.setChecked(False)
        self.btn_view_1.setChecked(False)
        self.btn_view_2.setChecked(False)
        self.btn_view_3.setChecked(True)
        self.btn_view_4.setChecked(False)
        self.btn_view_5.setChecked(False)
        self.btn_view_6.setChecked(False)
        if self.image is not None:
            self.window_right_top()
            self.show_to_window()

    def window_left(self):
        self.normal_view = False
        self.single_view = True
        self.multiple_view = False
        self.window = 4
        moildev = MoilUtils.connect_to_moildev(self.type_camera)
        self.mapX_4, self.mapY_4, = moildev.getAnypointMaps(0, -50,
                                                            self.zoom_any,
                                                            self.anypoint_mode)

    def onclick_window_left(self):
        self.btn_ori_view.setChecked(False)
        self.btn_6view.setChecked(False)
        self.btn_view_1.setChecked(False)
        self.btn_view_2.setChecked(False)
        self.btn_view_3.setChecked(False)
        self.btn_view_4.setChecked(True)
        self.btn_view_5.setChecked(False)
        self.btn_view_6.setChecked(False)
        if self.image is not None:
            self.window_left()
            self.show_to_window()

    def window_middle(self):
        self.normal_view = False
        self.single_view = True
        self.multiple_view = False
        self.window = 5
        moildev = MoilUtils.connect_to_moildev(self.type_camera)
        self.mapX_5, self.mapY_5, = moildev.getAnypointMaps(0, 0,
                                                            self.zoom_any,
                                                            self.anypoint_mode)

    def onclick_window_middle(self):
        self.btn_ori_view.setChecked(False)
        self.btn_6view.setChecked(False)
        self.btn_view_1.setChecked(False)
        self.btn_view_2.setChecked(False)
        self.btn_view_3.setChecked(False)
        self.btn_view_4.setChecked(False)
        self.btn_view_5.setChecked(True)
        self.btn_view_6.setChecked(False)
        if self.image is not None:
            self.window_middle()
            self.show_to_window()

    def window_right(self):
        self.normal_view = False
        self.single_view = True
        self.multiple_view = False
        self.window = 6
        moildev = MoilUtils.connect_to_moildev(self.type_camera)
        self.mapX_6, self.mapY_6, = moildev.getAnypointMaps(0, 50,
                                                            self.zoom_any,
                                                            self.anypoint_mode)

    def onclick_window_right(self):
        self.btn_ori_view.setChecked(False)
        self.btn_6view.setChecked(False)
        self.btn_view_1.setChecked(False)
        self.btn_view_2.setChecked(False)
        self.btn_view_3.setChecked(False)
        self.btn_view_4.setChecked(False)
        self.btn_view_5.setChecked(False)
        self.btn_view_6.setChecked(True)
        if self.image is not None:
            self.window_right()
            self.show_to_window()

    def mouse_window_lt(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.onclick_window_left_top()

    def mouse_window_t(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.onclick_window_top()

    def mouse_window_rt(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.onclick_window_right_top()

    def mouse_window_l(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.onclick_window_left()

    def mouse_window_m(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.onclick_window_middle()

    def mouse_window_r(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.onclick_window_right()

    def mouse_wheelEvent(self, e):
        """
        Resize image using mouse wheel event.
        """
        if self.image is not None:
            modifiers = QtWidgets.QApplication.keyboardModifiers()
            if modifiers == QtCore.Qt.ControlModifier:
                wheel_counter = e.angleDelta()
                if wheel_counter.y() / 120 == -1:
                    if self.width_result_image == 1000:
                        pass
                    else:
                        self.width_result_image -= 100

                if wheel_counter.y() / 120 == 1:
                    if self.width_result_image == 4000:
                        pass
                    else:
                        self.width_result_image += 100
                self.show_to_window()

    def mouse_release_event(self, e):
        """
        Mouse release event right click to show menu. the menu can select is show maximum, show minimum,
        save image, and show info.

        Args:
            e ():

        Returns:
            None.
        """
        if e.button() == QtCore.Qt.LeftButton:
            pass
        else:
            if self.image is None:
                pass
            else:
                self.menuMouseEvent(e)

    def menuMouseEvent(self, e):
        """
        showing the menu image when release right click.

        Args:
            e ():

        Returns:
            None.
        """
        menu = QtWidgets.QMenu()
        save = menu.addAction("Save Image")
        info = menu.addAction("Show Info")
        save.triggered.connect(self.save_image)
        info.triggered.connect(self.onclick_help)
        menu.exec_(e.globalPos())

    def save_image(self):
        """
        Save image into local directory, it can save original image or
        result image from panorama or anypoint processing.

        """
        if self.image is not None:
            image_save = self.image if self.normal_view else self.image_result
            if self.dir_save is None or self.dir_save == "":
                self.dir_save = MoilUtils.selectDir()
            if self.dir_save:
                MoilUtils.save_image(image_save, self.dir_save, self.type_camera)
                self.addWidget(image_save)
                QtWidgets.QMessageBox.information(
                    self.parent, "Information", "Image saved !!\n\nLoc @: " + self.dir_save)

    def addWidget(self, image_save):
        """
        Add the image widget in the list widget_controller of saved image. it can be reopen when you select.
        Args:
            image_save (): the image saved.

        """
        height = MoilUtils.calculate_height(self.image, 200)
        self.listWidget.setIconSize(QtCore.QSize(200, height))
        new_widget = QtWidgets.QListWidgetItem()

        image_ = MoilUtils.resize_image(image_save, 200)
        imagePixmap = QtGui.QImage(
            image_.data,
            image_.shape[1],
            image_.shape[0],
            QtGui.QImage.Format_RGB888).rgbSwapped()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(imagePixmap))
        new_widget.setIcon(icon)
        new_widget.setText(str(datetime.datetime.now().strftime("%m%d%H_%M%S")) + ".png")
        self.listWidget.addItem(new_widget)

    def saved_image_activated(self):
        """
        Function that for connect with the event in list widget to reopen the image.

        """
        filename = self.dir_save + "/" + self.listWidget.currentItem().text()
        img = MetaImage(filename)
        self.type_camera = img.read_comment()
        if self.cam:
            self.video_controller.pause_video()
        self.image = MoilUtils.read_image(filename)
        self.show_to_window()

    @classmethod
    def onclick_help(cls):
        """
        Showing the message box to show help information obout this application.

        """
        Help.help_moildev_apps()

    def show_to_window(self):
        """
        Showing the processing result image into the frame UI.

        """
        global image, image_ori
        if self.normal_view:
            MoilUtils.showing_image(self.label_Original_image,
                                    self.image,
                                    self.width_result_image)

        elif self.multiple_view:
            self.frame_2.hide()
            self.scrollArea.hide()
            self.listWidget.hide()
            self.label_3.hide()
            self.scrollArea_3.show()
            image_1 = cv2.remap(self.image.copy(), self.mapX_1, self.mapY_1, cv2.INTER_CUBIC)
            MoilUtils.showing_image(self.label_image1, image_1, self.width_result_multi)
            image_2 = cv2.remap(self.image.copy(), self.mapX_2, self.mapY_2, cv2.INTER_CUBIC)
            MoilUtils.showing_image(self.label_image2, image_2, self.width_result_multi)
            image_3 = cv2.remap(self.image.copy(), self.mapX_3, self.mapY_3, cv2.INTER_CUBIC)
            MoilUtils.showing_image(self.label_image3, image_3, self.width_result_multi)
            image_4 = cv2.remap(self.image.copy(), self.mapX_4, self.mapY_4, cv2.INTER_CUBIC)
            MoilUtils.showing_image(self.label_image4, image_4, self.width_result_multi)
            image_5 = cv2.remap(self.image.copy(), self.mapX_5, self.mapY_5, cv2.INTER_CUBIC)
            MoilUtils.showing_image(self.label_image5, image_5, self.width_result_multi)
            image_6 = cv2.remap(self.image.copy(), self.mapX_6, self.mapY_6, cv2.INTER_CUBIC)
            MoilUtils.showing_image(self.label_image6, image_6, self.width_result_multi)

        elif self.single_view:
            self.frame_2.show()
            self.scrollArea.show()
            self.listWidget.show()
            self.label_3.show()
            self.scrollArea_3.hide()
            if self.window == 1:
                self.image_result = cv2.remap(self.image.copy(), self.mapX_1, self.mapY_1, cv2.INTER_CUBIC)
                image_ori = MoilUtils.draw_polygon(self.image.copy(), self.mapX_1, self.mapY_1)
            elif self.window == 2:
                self.image_result = cv2.remap(self.image.copy(), self.mapX_2, self.mapY_2, cv2.INTER_CUBIC)
                image_ori = MoilUtils.draw_polygon(self.image.copy(), self.mapX_2, self.mapY_2)
            elif self.window == 3:
                self.image_result = cv2.remap(self.image.copy(), self.mapX_3, self.mapY_3, cv2.INTER_CUBIC)
                image_ori = MoilUtils.draw_polygon(self.image.copy(), self.mapX_3, self.mapY_3)
            elif self.window == 4:
                self.image_result = cv2.remap(self.image.copy(), self.mapX_4, self.mapY_4, cv2.INTER_CUBIC)
                image_ori = MoilUtils.draw_polygon(self.image.copy(), self.mapX_4, self.mapY_4)
            elif self.window == 5:
                self.image_result = cv2.remap(self.image.copy(), self.mapX_5, self.mapY_5, cv2.INTER_CUBIC)
                image_ori = MoilUtils.draw_polygon(self.image.copy(), self.mapX_5, self.mapY_5)
            elif self.window == 6:
                self.image_result = cv2.remap(self.image.copy(), self.mapX_6, self.mapY_6, cv2.INTER_CUBIC)
                image_ori = MoilUtils.draw_polygon(self.image.copy(), self.mapX_6, self.mapY_6)

            MoilUtils.showing_image(self.label_Original_image,
                                    self.image_result,
                                    self.width_result_image)
            MoilUtils.showing_image(self.label,
                                    image_ori,
                                    self.width_ori_image)

    def closeEvent(self, e):
        self.parent.close()
