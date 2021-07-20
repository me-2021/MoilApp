from .user_interface.ui_mainwindow import Ui_MainWindow
from moilutils import MoilUtils
from help import Help
import datetime
import cv2
from PyQt5 import QtWidgets, QtCore, QtGui
from video_controller import VideoController
from camera_source import CameraSource
from camera_parameter import CameraParameters
from control_view import ManipulateView


class UiController(Ui_MainWindow):
    def __init__(self, mainWindow):
        super(UiController, self).__init__()
        self.parent = mainWindow
        self.setupUi(self.parent)
        self.title = "Template"
        self.type_camera = None
        self.normal_view = True
        self.panorama_view = False
        self.anypoint_view = False
        self.cam = False
        self.point = None
        self.moildev = None
        self.window = None
        self.image = None
        self.dir_save = None
        self.result_image = None
        self.angle = 0
        self.alpha = 0
        self.beta = 0
        self.zoom_any = 4
        self.anypoint_mode = 1
        self.__pano_alpha_min = 10
        self.__pano_alpha_max = 110
        self.width_result_image = 1360
        self.width_ori_image = 360
        self.h = None
        self.w = None
        self.mapX = None
        self.mapY = None
        self.radio_btn_mode_1.setChecked(True)
        self.video_controller = VideoController(self)
        self.manipulate = ManipulateView(self)
        self.video_controller.set_button_disable()
        self.openCam = QtWidgets.QDialog()
        self.winOpenCam = CameraSource(self, self.openCam)
        self.camParams = QtWidgets.QDialog()
        self.winCamParams = CameraParameters(self, self.camParams)
        self.frame_panorama.hide()
        self.frame_navigator.hide()
        self.connect_event()

    def connect_event(self):
        """
        Connect button to the function....

        Returns:

        """
        self.actionOpen_Image.triggered.connect(self.open_image)
        self.actionLoad_Video.triggered.connect(self.load_video)
        self.actionOpen_Camera.triggered.connect(self.onclick_open_camera)
        self.actionSave_image.triggered.connect(self.save_image)
        self.actionCam_parameter.triggered.connect(self.cam_params_window)
        self.actionMaximized.triggered.connect(self.maximized)
        self.actionMinimized.triggered.connect(self.minimized)
        self.actionRotate_left.triggered.connect(self.manipulate.rotate_left)
        self.actionRotatevright.triggered.connect(self.manipulate.rotate_right)
        self.actionZoom_in.triggered.connect(self.manipulate.zoom_in)
        self.actionZoom_out.triggered.connect(self.manipulate.zoom_out)
        self.actionAbout_Us.triggered.connect(self.onclick_aboutUs)
        self.actionHelp.triggered.connect(self.onclick_help)
        self.btn_open_image.clicked.connect(self.open_image)
        self.btn_open_video.clicked.connect(self.load_video)
        self.btn_open_camera.clicked.connect(self.onclick_open_camera)
        self.btn_normal.clicked.connect(self.onclick_normal)
        self.btn_anypoint.clicked.connect(self.onclick_anypoint)
        self.btn_panorama.clicked.connect(self.onclick_panorama)
        self.label_result.wheelEvent = self.mouse_wheelEvent
        self.label_result.mouseReleaseEvent = self.mouse_release_event
        self.label_ori.mousePressEvent = self.mouse_event
        self.label_ori.mouseMoveEvent = self.mouseMovedOriImage
        self.label_ori.mouseDoubleClickEvent = self.mouseDoubleclick_event
        self.label_result.mouseDoubleClickEvent = self.mouseDoubleclick_event
        self.parent.closeEvent = self.close_event
        self.actionAccesibility.triggered.connect(self.onclick_accessibility)
        self.coombo_zoom.activated.connect(self.combo_percentage_zoom)

        self.btn_play_pouse.clicked.connect(self.video_controller.onclick_play_pause_button)
        self.btn_stop_video.clicked.connect(self.video_controller.stop_video)
        self.btn_prev_video.clicked.connect(self.video_controller.prev_video)
        self.btn_skip_video.clicked.connect(self.video_controller.skip_video)
        self.actionRecord_video.triggered.connect(self.video_controller.action_record_video)
        self.btn_Record_video.clicked.connect(self.video_controller.recordVideo)
        self.slider_Video.valueChanged.connect(self.video_controller.changeValueSlider)

        self.btn_rotate_left.clicked.connect(self.manipulate.rotate_left)
        self.btn_rotate_right.clicked.connect(self.manipulate.rotate_right)
        self.btn_zoom_out.clicked.connect(self.manipulate.zoom_out)
        self.btn_zoom_in.clicked.connect(self.manipulate.zoom_in)
        self.btn_save_image.clicked.connect(self.save_image)
        self.actionExit.triggered.connect(self.parent.close)
        self.button_menu.clicked.connect(self.control_extra_button)

        self.btn_Up_View.clicked.connect(self.__up)
        self.btn_Right_view.clicked.connect(self.__right)
        self.btn_left_view.clicked.connect(self.__left)
        self.btn_center_view.clicked.connect(self.__center)
        self.btn_Down_view.clicked.connect(self.__down)
        self.radio_btn_mode_1.clicked.connect(self.__anypoint_mode_1)
        self.radio_btn_mode_2.clicked.connect(self.__anypoint_mode_2)
        self.max_pano.valueChanged.connect(self.change_panorama_fov)
        self.min_pano.valueChanged.connect(self.change_panorama_fov)

    def control_extra_button(self):
        """
        Control extra button in anypoint and panorama mode.

        """
        if self.button_menu.isChecked():
            if self.anypoint_view:
                self.frame_navigator.hide()
            elif self.panorama_view:
                self.frame_panorama.hide()
            else:
                print("coming soon")
        else:
            if self.anypoint_view:
                self.frame_navigator.show()
            elif self.panorama_view:
                self.frame_panorama.show()
            else:
                print("coming soon")

    def cam_params_window(self):
        """
        Open the window of camera parameter form, this window you can update, add, and
        delete the camera parameter from database.

        """
        self.camParams.show()

    def open_image(self):
        """
        Function for open image. Open Dialog to search image file from Directory...

        Returns:
            showing to the window in user interface..
        """
        filename = MoilUtils.selectFile(self.parent, "Select Image", "../SourceImage",
                                        "Image Files (*.jpeg *.jpg *.png *.gif *.bmg)")
        if filename:
            self.image = MoilUtils.readImage(filename)
            self.h, self.w = self.image.shape[:2]
            self.parent.setWindowTitle(self.title + " - " + filename)
            self.type_camera = MoilUtils.readCameraType(filename)
            if self.type_camera:
                self.cam = False
                self.onclick_normal()
                self.label_camera.setText("Camera type: " + self.type_camera)
                self.video_controller.set_button_disable()
                self.show_percentage()

    def load_video(self):
        """
        Open Dialog to search video file from Directory. after you select the video file, it will show the prompt
        to select the type of camera.

        Returns:

        """
        video_source = MoilUtils.selectFile(self.parent,
                                            "Select Video Files",
                                            "../",
                                            "Video Files (*.mp4 *.avi *.mpg *.gif *.mov)")
        if video_source:
            self.type_camera = MoilUtils.selectCameraType()
            self.parent.setWindowTitle(self.title + " - " + video_source)
            if self.type_camera is not None:
                self.running_video(video_source)
                self.label_camera.setText("Camera type: " + self.type_camera)
                self.onclick_normal()

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
            self.h, self.w = image.shape[:2]
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
        self.type_camera = MoilUtils.selectCameraType()
        if self.type_camera is not None:
            self.running_video(camera_source)
            self.label_camera.setText("Camera type: " + self.type_camera)
            self.onclick_normal()

    # normal view here ++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def onclick_normal(self):
        """
        Change to normal view..

        Returns:

        """
        if self.image is not None:
            self.normal_view = True
            self.anypoint_view = False
            self.panorama_view = False
            self.scrollArea.show()
            self.show_to_window()
            self.reset_mode_view()

    # anypoint view start here+++++++++++++++++++++++++++++++++++++++++++++++
    def onclick_anypoint(self):
        """
        Change to anypoint mode..

        Returns:

        """
        if self.image is not None:
            if self.type_camera:
                self.moildev = MoilUtils.connectToMoildev(self.type_camera)
                self.anypoint()
                self.show_percentage()
                self.frame_navigator.show()

    def anypoint(self):
        """
        Anypoint algorithm.

        """
        self.normal_view = False
        self.panorama_view = False
        self.anypoint_view = True
        self.btn_anypoint.setChecked(True)
        self.btn_panorama.setChecked(False)
        self.btn_normal.setChecked(False)
        self.angle = 0
        self.frame_navigator.show()
        self.frame_panorama.hide()
        self.mapX, self.mapY, = self.moildev.getAnypointMaps(
            self.alpha, self.beta, self.zoom_any, self.anypoint_mode)

        self.show_to_window()

    def __anypoint_mode_1(self):
        """
        Execute the anypoint process mode 1.

        Returns:
            None.
        """
        self.anypoint_mode = 1
        self.resetAlphaBeta()
        self.onclick_anypoint()

    def __anypoint_mode_2(self):
        """
        Execute the anypoint process mode 2.

        Returns:
            None.
        """
        self.anypoint_mode = 2
        self.resetAlphaBeta()
        self.onclick_anypoint()

    def resetAlphaBeta(self):
        """
        The method for reset alpha, beta, zoom, and angle.

        Returns:
            None.
        """
        self.alpha = 0
        self.beta = 0
        self.zoom_any = 4
        self.point = (round(self.w / 2), round(self.h / 2))

    def __up(self):
        """
        The method showing anypoint widget_controller in specific area.
        """
        self.point = None
        if self.radio_btn_mode_1.isChecked():
            self.alpha = 75
            self.beta = 0
        elif self.radio_btn_mode_2.isChecked():
            self.alpha = 50
            self.beta = 0
        self.anypoint()

    def __left(self):
        """
        The method showing anypoint widget_controller in specific area.
        """
        self.point = None
        if self.radio_btn_mode_1.isChecked():
            self.alpha = 65
            self.beta = -90
        elif self.radio_btn_mode_2.isChecked():
            self.alpha = 0
            self.beta = -75
        self.anypoint()

    def __center(self):
        """
        The method showing anypoint widget_controller in specific area.
        """
        self.point = (round(self.w / 2), round(self.h / 2))
        if self.radio_btn_mode_1.isChecked():
            self.alpha = 0
            self.beta = 0
        elif self.radio_btn_mode_2.isChecked():
            self.alpha = 0
            self.beta = 0
        self.anypoint()

    def __right(self):
        """
        The method showing anypoint widget_controller in specific area.
        """
        self.point = None
        if self.radio_btn_mode_1.isChecked():
            self.alpha = 65
            self.beta = 90
        elif self.radio_btn_mode_2.isChecked():
            self.alpha = 0
            self.beta = 65
        self.anypoint()

    def __down(self):
        """
        The method showing anypoint widget_controller in specific area.
        """
        self.point = None
        if self.radio_btn_mode_1.isChecked():
            self.alpha = 65
            self.beta = 180
        elif self.radio_btn_mode_2.isChecked():
            self.alpha = -65
            self.beta = 0
        self.anypoint()

    # panorama start here++++++++++++++++++++++++++++++++++++++++++++++++++
    def onclick_panorama(self):
        if self.image is not None:
            if self.type_camera:
                self.moildev = MoilUtils.connectToMoildev(self.type_camera)
                self.panorama()
                self.show_percentage()
                self.frame_panorama.show()

    def panorama(self):
        """
        Panorama function.

        """
        self.normal_view = False
        self.anypoint_view = False
        self.panorama_view = True
        self.btn_anypoint.setChecked(False)
        self.btn_panorama.setChecked(True)
        self.btn_normal.setChecked(False)
        self.angle = 0
        self.rho = self.moildev.getRhoFromAlpha(self.__pano_alpha_min)
        self.frame_navigator.hide()
        self.frame_panorama.show()
        self.mapX, self.mapY, = self.moildev.getPanoramaMaps(
            10, self.__pano_alpha_max)
        self.max_pano.setValue(self.__pano_alpha_max)
        self.min_pano.setValue(self.__pano_alpha_min)
        self.show_to_window()

    def change_panorama_fov(self):
        """
        Change the panorama widget_controller with change the field of widget_controller.

        """
        self.__pano_alpha_min = self.min_pano.value()
        self.__pano_alpha_max = self.max_pano.value()
        self.onclick_panorama()

    def init_ori_ratio(self, image):
        """
        Calculate the initial ratio of the image.

        Returns:
            ratio_x : ratio width between image and ui window.
            ratio_y : ratio height between image and ui window.
            center : find the center image on window user interface.
        """
        h = self.label_ori.height()
        w = self.label_ori.width()
        height, width = image.shape[:2]
        ratio_x = width / w
        ratio_y = height / h
        return ratio_x, ratio_y

    def mouseMovedOriImage(self, e):
        """
        Mouse move event to look in surrounding widget_controller in result label image.

        Args:
            e ():

        Returns:

        """
        pos_x = round(e.x())
        pos_y = round(e.y())
        ratio_x, ratio_y = self.init_ori_ratio(self.image)
        coordinate_X = round(pos_x * ratio_x)
        coordinate_Y = round(pos_y * ratio_y)
        self.point = (coordinate_X, coordinate_Y)
        if self.normal_view:
            pass
        if self.anypoint_view:
            self.alpha, self.beta = self.moildev.getAlphaBeta(
                coordinate_X, coordinate_Y, self.anypoint_mode)
            self.anypoint()

        elif self.panorama_view:
            print("coming soon")
        else:
            pass

    def mouse_event(self, e):
        """
        Specify coordinate from mouse left event to generate anypoint widget_controller and recenter image.

        Args:
            e (): Coordinate point return by pyqt core

        Returns:

        """
        if self.image is not None:
            if e.button() == QtCore.Qt.LeftButton:
                pos_x = round(e.x())
                pos_y = round(e.y())
                ratio_x, ratio_y = self.init_ori_ratio(self.image)
                coordinate_X = round(pos_x * ratio_x)
                coordinate_Y = round(pos_y * ratio_y)
                self.point = (coordinate_X, coordinate_Y)
                if self.normal_view:
                    pass

                if self.anypoint_view:
                    self.alpha, self.beta = self.moildev.getAlphaBeta(
                        coordinate_X, coordinate_Y, self.anypoint_mode)
                    self.anypoint()

                elif self.panorama_view:
                    print("coming soon")
                else:
                    pass

    def mouseDoubleclick_event(self, e):
        """
        Reset to default by mouse event.

        Args:
            e ():

        Returns:

        """
        if self.image is not None:
            if self.normal_view:
                pass
            elif self.anypoint_view:
                self.resetAlphaBeta()
                self.anypoint()
                self.show_percentage()
            else:
                pass

    def mouse_wheelEvent(self, e):
        """
        Resize image using mouse wheel event.
        """
        if self.image is not None:
            modifiers = QtWidgets.QApplication.keyboardModifiers()
            if modifiers == QtCore.Qt.ControlModifier:
                wheel_counter = e.angleDelta()
                if wheel_counter.y() / 120 == -1:
                    if self.width_result_image < 800:
                        pass
                    else:
                        self.width_result_image -= 100

                if wheel_counter.y() / 120 == 1:
                    if self.width_result_image > 6000:
                        pass
                    else:
                        self.width_result_image += 100
                self.show_to_window()
                self.show_percentage()

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
        mini = menu.addAction("Minimized")
        maxi = menu.addAction("Maximized")
        save = menu.addAction("Save Image")
        info = menu.addAction("Show Info")
        mini.triggered.connect(self.minimized)
        maxi.triggered.connect(self.maximized)
        save.triggered.connect(self.save_image)
        info.triggered.connect(self.onclick_aboutUs)
        menu.exec_(e.globalPos())

    def save_image(self):
        """
        Save image into local directory, it can save original image or
        result image from panorama or anypoint processing.

        """
        if self.image is not None:
            image_save = self.image if self.normal_view else self.result_image
            if self.dir_save is None or self.dir_save == "":
                self.dir_save = MoilUtils.selectDirectory()
            if self.dir_save:
                MoilUtils.saveImage(image_save, self.dir_save, self.type_camera)
                self.addWidget(image_save)
                QtWidgets.QMessageBox.information(
                    self.parent, "Information", "Image saved !!\n\nLoc @: " + self.dir_save)

    def addWidget(self, image_save):
        """
        Add the image widget in the list widget_controller of saved image. it can be reopen when you select.
        Args:
            image_save (): the image saved.

        """
        height = MoilUtils.calculateHeight(self.image, 160)
        self.listWidget.setIconSize(QtCore.QSize(160, height))
        new_widget = QtWidgets.QListWidgetItem()

        image_ = MoilUtils.resizeImage(image_save, 160)
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
        self.type_camera = MoilUtils.readCameraType(filename)
        if self.cam:
            self.video_controller.pause_video()
        self.image = MoilUtils.readImage(filename)
        self.show_to_window()

    def reset_mode_view(self):
        """
        Update the properties widget_controller when you reset.

        """
        self.result_image = None
        self.width_result_image = 1360
        self.normal_view = True
        self.resetAlphaBeta()
        self.btn_Record_video.setChecked(False)
        self.btn_normal.setChecked(True)
        self.btn_anypoint.setChecked(False)
        self.btn_panorama.setChecked(False)
        self.point = (round(self.w / 2), round(self.h / 2))
        self.label_ori.clear()
        self.frame_navigator.hide()
        self.frame_panorama.hide()

    def maximized(self):
        self.frame_3.hide()
        self.frame_4.hide()

    def minimized(self):
        self.frame_3.show()
        self.frame_4.show()

    @classmethod
    def onclick_aboutUs(cls):
        """
        Showing the message box to show help information obout this application.

        """
        Help.about_us()

    @classmethod
    def onclick_help(cls):
        """
        Showing the message box to show help information obout this application.

        """
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("Help")
        msgbox.setText(
            "Coming soon!!!")
        msgbox.setIconPixmap(QtGui.QPixmap('icon/moildev2.png'))
        msgbox.exec()

    def show_to_window(self):
        """
        Showing the processing result image into the frame UI.

        """
        radius = 6 if self.h < 800 else 10
        if self.normal_view:
            MoilUtils.showImageToLabel(self.label_result,
                                       self.image,
                                       self.width_result_image, self.angle, plusIcon=False)

        else:
            self.result_image = cv2.remap(self.image, self.mapX, self.mapY, cv2.INTER_CUBIC)
            if self.anypoint_view:
                image = MoilUtils.drawPolygon(self.image.copy(), self.mapX, self.mapY)
                image = MoilUtils.drawPoint(image, self.point, radius)
                result = MoilUtils.drawLine(self.result_image.copy())
                plusIcon = True
            else:
                image = self.image
                result = self.result_image
                plusIcon = False
            MoilUtils.showImageToLabel(self.label_result,
                                       result,
                                       self.width_result_image, self.angle, plusIcon)
            MoilUtils.showImageToLabel(self.label_ori,
                                       image,
                                       self.width_ori_image)

    def show_percentage(self):
        count = self.coombo_zoom.count()
        if count == 8:
            self.coombo_zoom.addItem("")
        self.coombo_zoom.setCurrentIndex(8)
        size = round((self.width_result_image / self.w) * 100)
        self.coombo_zoom.setItemText(8, (str(size) + "%"))

    def combo_percentage_zoom(self):
        if self.image is not None:
            self.coombo_zoom.removeItem(8)
            percent = self.coombo_zoom.currentText()
            percent = int(percent.replace("%", ""))
            self.width_result_image = round((self.w * percent) / 100)
            self.show_to_window()

    def close_event(self, e):
        self.openCam.close()
        self.camParams.close()

    def onclick_accessibility(self):
        """
        Open prompt for accessibility MoilApp
        Returns:

        """
        QtWidgets.QMessageBox.information(
            self.parent, "Accessibility", "MoilApp  Multiple View Accessibility\n\n"
                                          "Information !!\n"
                                          "Crtl + I\t: Open Image\n"
                                          "Ctrl + V\t: Open Video\n"
                                          "Ctrl + C\t: Open cam\n"
                                          "Left\t: Prev video\n"
                                          "Space\t: play/pause video\n"
                                          "s \t: Stop video\n"
                                          "Right\t: skip video\n"
                                          "n\t: Normal View\n"

                                          "Ctrl+Shift+/\t:show help\n\n")
