#################################################
# Colonoscopy project was build by Haryanto.    #
# Email = Haryanto@o365.mcut.edu.tw             #
#################################################

from .ui_mainWindow import Ui_MainWindow
from functools import partial
from moilutils import MoilUtils
from moilutils import ResourceIcon
from help import Help
import datetime
import cv2
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from moilutils import VideoController
from reCenter import RecenterImage
from .libs.detect_center import FindCenter


class UiController(Ui_MainWindow):
    def __init__(self, mainWindow):
        super(UiController, self).__init__()
        self.parent = mainWindow
        self.setupUi(self.parent)
        self.parent.setFixedSize(1695, 981)
        self.title = "Colonoscopy Apps"
        self.parent.setWindowTitle(self.title)
        self.cam = False
        self.type_camera = None
        self.mode_view = "Normal"
        self.recImage = None
        self.point = None
        self.moildev = None
        self.window = None
        self.image = None
        self.zoom_area = None
        self.dir_save = None
        self.record = False
        self.result_image = None
        self.angle = 0
        self.alpha = 0
        self.beta = 0
        self.zoom_any = 4
        self.anypoint_mode = 1
        self.__pano_alpha_min = 10
        self.__pano_alpha_max = 100
        self.width_result_image = 1060
        self.width_ori_image = 400
        self.h = None
        self.w = None
        self.mapX = None
        self.mapY = None
        self.posVid = []
        self.resource = ResourceIcon()

        self.video_writer = None
        self.videoDir = None
        self.detector = None

        try:
            model = "./plugins/colonoscopy/center_colon.h5"
            self.detector = FindCenter(os.path.abspath(model))
        except:
            QtWidgets.QMessageBox.warning(None, "Warning!",
                                          "you not install the requirement to run this program well,"
                                          "This program still can run, but some feature may not available "
                                          "and cant use such as auto center. please install it first  by"
                                          "reading the Readme file in colonoscopy plugin then re run to running"
                                          "this program successfully ~ Developer")

        self.dialogHelp = QtWidgets.QDialog()
        self.winHelp = Help(self, self.dialogHelp)
        self.frame_panorama.hide()
        self.frame_navigator.hide()
        self.buttonBack.hide()
        self.radio_btn_mode_1.setChecked(True)
        self.btn_Auto.hide()
        self.button_menu.hide()
        self.labelRecenter.hide()
        self.frameVideoController.hide()
        self.video_controller = VideoController(self)
        self.recenter = RecenterImage(self)
        self.connect_event()

    def connect_event(self):
        """
        Connect button to the function....

        Returns:

        """
        # from menu file
        self.actionOpen_Image.triggered.connect(self.open_image)
        self.actionLoad_Video.triggered.connect(self.load_video)
        self.actionOpen_Camera.triggered.connect(self.onclick_open_camera)
        self.actionSave_image.triggered.connect(self.save_image)
        self.actionRecord_video.triggered.connect(self.actionRecordVideo)
        self.actionCam_parameter.triggered.connect(MoilUtils.parametersForm)
        self.actionExit.triggered.connect(self.parent.close)

        # from menu view
        self.actionRotate_left.triggered.connect(self.rotate_left)
        self.actionRotateright.triggered.connect(self.rotate_right)
        self.actionZoom_in.triggered.connect(self.zoom_in)
        self.actionZoom_out.triggered.connect(self.zoom_out)

        # from menu window
        self.actionMaximized.triggered.connect(self.maximized)
        self.actionMinimized.triggered.connect(self.minimized)

        # from menu help
        self.actionAbout_Us.triggered.connect(self.onclick_aboutUs)
        self.actionHelp.triggered.connect(self.onclick_help)
        self.actionAccesibility.triggered.connect(self.onclick_accessibility)

        # btn normal view
        self.btn_normal.clicked.connect(self.onclick_normal)

        # # anypoint processing
        self.btn_anypoint.clicked.connect(self.onclick_anypoint)
        self.btn_Up_View.clicked.connect(self.__up)
        self.btn_Right_view.clicked.connect(self.__right)
        self.btn_left_view.clicked.connect(self.__left)
        self.btn_center_view.clicked.connect(self.__center)
        self.btn_Down_view.clicked.connect(self.__down)
        self.radio_btn_mode_1.clicked.connect(self.__anypoint_mode_1)
        self.radio_btn_mode_2.clicked.connect(self.__anypoint_mode_2)
        self.lineedit_alpha_2.editingFinished.connect(self.set_param_any)
        self.lineedit_beta_2.editingFinished.connect(self.set_param_any)
        self.anypoint_zoom_2.editingFinished.connect(self.set_param_any)

        # # button panorama view
        self.btn_panorama.clicked.connect(self.onclick_panorama)
        # self.max_pano.valueChanged.connect(self.change_panorama_fov)
        self.max_pano.editingFinished.connect(self.change_panorama_fov)
        self.min_pano.editingFinished.connect(self.change_panorama_fov)

        # recenter
        self.buttonRecenter.clicked.connect(self.onclickRecenter)
        self.setIcx.editingFinished.connect(self.recenter.positionCoorX)
        self.setIcy.editingFinished.connect(self.recenter.positionCoorY)

        # auto
        self.btn_Auto.clicked.connect(self.onclickAuto)

        # mouse event controller
        self.label_result.wheelEvent = self.mouse_wheelEvent
        self.label_result.mouseReleaseEvent = self.mouse_release_event
        self.label_ori.mousePressEvent = self.mouse_event
        self.label_ori.mouseMoveEvent = self.mouseMovedOriImage
        self.label_ori.mouseDoubleClickEvent = self.mouseDoubleclick_event
        self.label_result.mouseDoubleClickEvent = self.mouseDoubleclick_event

        # Media players controller
        self.btnPlayPause.clicked.connect(partial(self.video_controller.playPauseVideo, self.btnPlayPause))
        self.btn_stop_video.clicked.connect(self.video_controller.stopVideo)
        self.btn_prev_video.clicked.connect(self.video_controller.rewindVideo)
        self.btn_skip_video.clicked.connect(self.video_controller.forwardVideo)
        self.slider_Video.valueChanged.connect(self.video_controller.sliderController)

        # others
        self.parent.closeEvent = self.close_event
        self.comboBox_zoom.activated.connect(self.combo_percentage_zoom)
        self.button_menu.clicked.connect(self.control_additional_frame)
        self.listWidget.currentItemChanged.connect(self.saved_image_activated)

    def control_btn_recenter(self):
        if self.image:
            self.buttonRecenter.show()
        else:
            self.buttonRecenter.hide()

    def control_button_back(self):
        if self.zoom_area:
            self.buttonBack.show()
        else:
            self.buttonBack.hide()

    def control_additional_frame(self):
        """
        Control extra button in anypoint and panorama mode.

        """
        if self.image is not None:
            if self.button_menu.isChecked():
                self.button_menu.setStyleSheet("QPushButton{ background-color :  rgb(211, 215, 207);}\n"
                                               "QPushButton::checked{ background-color : rgb(252, 233, 79); }\n"
                                               "border-radius: 10px;")

                if self.mode_view == "Anypoint":
                    self.frame_navigator.show()
                else:
                    self.frame_panorama.show()
                    if self.buttonRecenter.isChecked():
                        pass

            else:
                self.frame_navigator.hide()
                self.frame_panorama.hide()

    def open_image(self):
        """
        Function for open image. Open Dialog to search image file from Directory...

        Returns:
            showing to the window in user interface..
        """
        filename = MoilUtils.selectFile(self.parent, "Select Image", "",
                                        "Image Files (*.jpeg *.jpg *.png *.gif *.bmg)")
        if filename:
            self.image = MoilUtils.readImage(filename)
            self.parent.setWindowTitle(self.title + " - " + filename)

            if self.cam:
                self.video_controller.stopVideo()
                self.cap.release()
                self.frameVideoController.hide()
            typeCam = MoilUtils.readCameraType(filename)
            if typeCam == "":
                self.type_camera = MoilUtils.selectCameraType()
                MoilUtils.writeCameraType(filename, self.type_camera)
            else:
                self.type_camera = typeCam

            self.cam = False
            self.title_image_ori.setText("  Camera type: " + self.type_camera)
            self.moildev = MoilUtils.connectToMoildev(self.type_camera)
            self.w = self.moildev.getImageWidth()
            self.h = self.moildev.getImageHeight()
            self.onclick_normal()
            self.frameVideoController.hide()

    def load_video(self):
        """
        Open Dialog to search video file from Directory. after you select the video file, it will show the prompt
        to select the type of camera.

        Returns:

        """
        video_source = MoilUtils.selectFile(self.parent,
                                            "Select Video Files",
                                            "",
                                            "Video Files (*.mp4 *.avi *.mpg *.gif *.mov)")
        if video_source:
            self.type_camera = MoilUtils.selectCameraType()
            self.parent.setWindowTitle(self.title + " - " + video_source)
            if self.type_camera is not None:
                self.running_video(video_source)
                self.title_image_ori.setText("   Camera type: " + self.type_camera)
                self.onclick_normal()

    def running_video(self, video_source):
        """
        Open Video following the source given.

        Args:
            video_source (): the source of media, can be camera and video file.
        """
        self.cap = cv2.VideoCapture(video_source)
        _, image = self.cap.read()
        if image is None:
            QtWidgets.QMessageBox.information(self.parent, "Information", "No source camera founded")
        else:
            self.cam = True
            self.moildev = MoilUtils.connectToMoildev(self.type_camera)
            self.w = self.moildev.getImageWidth()
            self.h = self.moildev.getImageHeight()
            self.video_controller.nextFrame()
            self.frameVideoController.show()

    def onclick_open_camera(self):
        """
        open the camera from the available source in the system,
        this function provide 2 source namely USB cam and Streaming Cam from Raspberry pi.

        """
        # self.reset_mode_view()
        camera_source = MoilUtils.selectCameraSource()
        if camera_source is not None:
            self.type_camera = MoilUtils.selectCameraType()
            if self.type_camera is not None:
                # self.updateLabel()
                self.running_video(camera_source)
                self.title_image_ori.setText("   Camera type: " + self.type_camera)
                self.onclick_normal()

    # normal view here ++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def onclick_normal(self):
        """
        Change to normal view..

        Returns:

        """
        if self.image is not None:
            self.mode_view = "Normal"
            self.button_menu.setChecked(False)
            self.control_additional_frame()
            self.btn_anypoint.setChecked(False)
            self.btn_panorama.setChecked(False)
            self.buttonRecenter.setChecked(False)
            self.buttonRecenter.setStyleSheet(
                "QPushButton{\n"
                "  border-color: #71D1BA;\n"
                "  border-width: 2px;        \n"
                "  border-style: solid;\n"
                "  border-radius: 5px;\n"
                "  background-color : rgb(238, 238, 236); }\n")
            self.recImage = None
            self.showToWindow()
            self.button_menu.hide()
            self.reset_mode_view()

    # anypoint view start here+++++++++++++++++++++++++++++++++++++++++++++++
    def onclick_anypoint(self):
        """
        Change to anypoint mode..

        Returns:

        """
        if self.btn_anypoint.isChecked():
            if self.image is not None:
                self.mode_view = "Anypoint"
                self.frame_panorama.hide()
                self.frame_navigator.show()
                self.button_menu.setChecked(True)
                self.control_additional_frame()
                self.button_menu.show()
                self.btn_anypoint.setStyleSheet("QPushButton{ background-color :  rgb(211, 215, 207);}\n"
                                                "QPushButton::checked{ background-color : rgb(252, 233, 79); }\n"
                                                "border-radius: 10px;"
                                                )
                self.moildev = MoilUtils.connectToMoildev(self.type_camera)
                self.anypoint()
        else:
            self.onclick_normal()

    def anypoint(self):
        """
        Anypoint algorithm.

        """
        self.btn_panorama.setChecked(False)
        self.btn_normal.setChecked(False)
        self.angle = 0
        self.mapX, self.mapY, = self.moildev.getAnypointMaps(
            self.alpha, self.beta, self.zoom_any, self.anypoint_mode)
        self.showToWindow()

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
        if self.type_camera == "endoscope":
            self.point = (self.moildev.getIcx() + 160, self.moildev.getIcy())
        else:
            self.point = (self.moildev.getIcx(), self.moildev.getIcy())

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
        if self.btn_panorama.isChecked():
            if self.image is not None:
                self.mode_view = "Panorama"
                self.button_menu.show()
                self.frame_navigator.hide()
                self.frame_panorama.show()
                self.button_menu.setChecked(True)
                self.control_additional_frame()
                self.btn_panorama.setStyleSheet("QPushButton{ background-color :  rgb(211, 215, 207);}\n"
                                                "QPushButton::checked{ background-color :rgb(252, 233, 79); }\n"
                                                "border-radius: 10px;")
                self.moildev = MoilUtils.connectToMoildev(self.type_camera)
                self.btn_anypoint.setChecked(False)
                self.btn_normal.setChecked(False)
                self.buttonRecenter.setChecked(False)
                self.buttonRecenter.setStyleSheet(
                    "QPushButton{\n"
                    "  border-color: #71D1BA;\n"
                    "  border-width: 2px;        \n"
                    "  border-style: solid;\n"
                    "  border-radius: 5px;\n"
                    "  background-color : rgb(238, 238, 236); }\n")
                self.recImage = None
                self.panorama()
        else:
            self.onclick_normal()

    def panorama(self):
        """
        Panorama function.

        """
        self.angle = 0
        self.rho = self.moildev.getRhoFromAlpha(self.__pano_alpha_min)
        self.mapX_pano, self.mapY_pano = self.moildev.getPanoramaMaps(self.__pano_alpha_min, self.__pano_alpha_max)
        self.max_pano.setValue(self.__pano_alpha_max)
        self.min_pano.setValue(self.__pano_alpha_min)
        self.showToWindow()

    def change_panorama_fov(self):
        """
        Change the panorama widget_controller with change the field of widget_controller.

        """
        self.__pano_alpha_min = self.min_pano.value()
        self.__pano_alpha_max = self.max_pano.value()
        self.onclick_panorama()

    def onclickAuto(self):
        if self.image is not None:
            if self.btn_Auto.isChecked():
                self.labelMin.show()
                self.labelMax.show()
                self.min_pano.show()
                self.max_pano.show()
                self.labelIcx.hide()
                self.labelIcy.hide()
                self.setIcx.hide()
                self.setIcy.hide()
                self.frame_panorama.setGeometry(QtCore.QRect(5, 45, 180, 80))
                self.buttonRecenter.hide()
                self.btn_Auto.setStyleSheet(
                    "QPushButton{\n"
                    "  border-color: #71D1BA;\n"
                    "  border-width: 2px;        \n"
                    "  border-style: solid;\n"
                    "  border-radius: 5px;\n"
                    "  background-color : rgb(252, 233, 79);}\n")

            else:
                self.labelIcx.show()
                self.labelIcy.show()
                self.setIcx.show()
                self.setIcy.show()
                self.labelMin.show()
                self.labelMax.show()
                self.min_pano.show()
                self.max_pano.show()
                self.frame_panorama.setGeometry(QtCore.QRect(5, 45, 180, 145))
                self.buttonRecenter.show()
                self.btn_Auto.setStyleSheet(
                    "QPushButton{\n"
                    "  border-color: #71D1BA;\n"
                    "  border-width: 2px;        \n"
                    "  border-style: solid;\n"
                    "  border-radius: 5px;\n"
                    "  background-color : rgb(211, 215, 207);}\n")
            self.showToWindow()

            # if self.type_camera == "endoscope":
            #     self.point = (self.moildev.getIcx() + 160, self.moildev.getIcy())
            # else:
            #     self.point = (self.moildev.getIcx(), self.moildev.getIcy())
            # self.showToWindow()

    def init_ori_ratio(self):
        """
        Calculate the initial ratio of the image.

        Returns:
            ratio_x : ratio width between image and ui window.
            ratio_y : ratio height between image and ui window.
            center : find the center image on window user interface.
        """
        h = self.label_ori.height()
        w = self.label_ori.width()
        # height, width = image.shape[:2]
        ratio_x = self.moildev.getImageWidth() / w
        ratio_y = self.moildev.getImageHeight() / h
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
        if self.image is not None:
            ratio_x = self.moildev.getImageWidth() / self.label_ori.width()
            ratio_y = self.moildev.getImageHeight() / self.label_ori.height()
            # ratio_x, ratio_y = self.init_ori_ratio()
            X = round(pos_x * ratio_x)
            Y = round(pos_y * ratio_y)
            if X <= 0 or X >= self.w and Y <= 0 or Y >= self.h:
                if self.type_camera == "endoscope":
                    coordinate_X = int(self.moildev.getIcx() + 160)
                    coordinate_Y = int(self.moildev.getIcy())
                else:
                    coordinate_X = int(self.moildev.getIcx())
                    coordinate_Y = int(self.moildev.getIcy())
            else:
                coordinate_X = X
                coordinate_Y = Y
            if e.buttons() == QtCore.Qt.NoButton:
                if self.mode_view == "Anypoint" or self.buttonRecenter.isChecked():
                    self.alpha, self.beta = self.moildev.getAlphaBeta(
                        coordinate_X, coordinate_Y, self.anypoint_mode)
                    self.status_alpha.setText("Alpha: %.1f" % self.alpha)
                    self.status_beta.setText("Beta: %.1f" % self.beta)

            if e.buttons() == QtCore.Qt.LeftButton:
                self.point = (coordinate_X, coordinate_Y)
                if self.mode_view == "Anypoint":
                    self.alpha, self.beta = self.moildev.getAlphaBeta(
                        coordinate_X, coordinate_Y, self.anypoint_mode)
                    self.status_alpha.setText("Alpha: %.1f" % self.alpha)
                    self.status_beta.setText("Beta: %.1f" % self.beta)
                    self.anypoint()
                elif self.buttonRecenter.isChecked():
                    self.alpha, self.beta = self.moildev.getAlphaBeta(
                        coordinate_X, coordinate_Y, self.anypoint_mode)
                    self.showToWindow()

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
                ratio_x, ratio_y = self.init_ori_ratio()
                X = round(pos_x * ratio_x)
                Y = round(pos_y * ratio_y)
                if X <= 0 or X >= self.w and Y <= 0 or Y >= self.h:
                    if self.type_camera == "endoscope":
                        coordinate_X = int(self.moildev.getIcx() + 160)
                        coordinate_Y = int(self.moildev.getIcy())
                    else:
                        coordinate_X = int(self.moildev.getIcx())
                        coordinate_Y = int(self.moildev.getIcy())
                else:
                    coordinate_X = X
                    coordinate_Y = Y
                self.point = (coordinate_X, coordinate_Y)
                if self.mode_view == "Anypoint":
                    self.alpha, self.beta = self.moildev.getAlphaBeta(
                        coordinate_X, coordinate_Y, self.anypoint_mode)
                    self.status_alpha.setText("Alpha: %.1f" % self.alpha)
                    self.status_beta.setText("Beta: %.1f" % self.beta)
                    self.anypoint()
                elif self.buttonRecenter.isChecked():
                    self.alpha, self.beta = self.moildev.getAlphaBeta(
                        coordinate_X, coordinate_Y, self.anypoint_mode)
                    self.setIcx.setValue(coordinate_X)
                    self.setIcy.setValue(coordinate_Y)
                    self.showToWindow()

    def mouseDoubleclick_event(self, e):
        """
        Reset to default by mouse event.

        Args:
            e ():

        Returns:

        """
        if self.image is not None:
            if e.button() == QtCore.Qt.LeftButton:
                if self.mode_view == "Anypoint":
                    self.resetAlphaBeta()
                    self.anypoint()

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
                self.showToWindow()

    def mouse_release_event(self, e):
        """
        Mouse release event right click to show menu. the menu can select is show maximum, show minimum,
        save image, and show info.

        Args:
            e ():

        Returns:
            None.
        """
        if e.button() == QtCore.Qt.RightButton:
            if self.image is not None:
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
            if self.normal_view:
                if self.buttonRecenter.isChecked():
                    image_save = self.recImage
                else:
                    image_save = self.image
            else:
                image_save = self.result_image
            if self.dir_save is None or self.dir_save == "":
                self.dir_save = MoilUtils.selectDirectory()
            if self.dir_save:
                self.name_saved = MoilUtils.saveImage(image_save, self.dir_save, self.type_camera)
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
        new_widget.setText(str(self.name_saved) + ".png")
        self.listWidget.addItem(new_widget)
        self.posVid.append(self.video_controller.pos_frame)

    def saved_image_activated(self):
        """
        Function that for connect with the event in list widget to reopen the image.

        """
        filename = self.dir_save + "/" + self.listWidget.currentItem().text()
        posFrame = self.posVid[self.listWidget.currentRow()]
        self.type_camera = MoilUtils.readCameraType(filename)
        if self.cam:
            self.video_controller.pauseVideo()
            self.reset_mode_view()
            self.image = MoilUtils.readImage(filename)
            self.h, self.w = self.image.shape[:2]
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, posFrame)
            self.video_controller.nextFrame()
            if self.listWidget.count() == 1:
                self.listWidget.selectionModel().reset()

    def reset_mode_view(self):
        """
        Update the properties widget_controller when you reset.

        """
        self.result_image = None
        self.width_result_image = 1060
        self.normal_view = True
        self.resetAlphaBeta()
        self.btn_normal.setChecked(True)
        self.btn_anypoint.setChecked(False)
        self.btn_panorama.setChecked(False)
        if self.type_camera == "endoscope":
            self.point = (self.moildev.getIcx() + 160, self.moildev.getIcy())
        else:
            self.point = (self.moildev.getIcx(), self.moildev.getIcy())
        # self.frame_navigator.hide()
        self.frame_panorama.hide()

    def maximized(self):
        self.toolBar.hide()
        self.line_5.hide()
        self.title_image_ori.hide()
        self.label_ori.hide()
        self.listWidget.hide()
        self.label_3.hide()
        self.statusBar.hide()

    def minimized(self):
        self.toolBar.show()
        self.line_5.show()
        self.title_image_ori.show()
        self.label_ori.show()
        self.listWidget.show()
        self.label_3.show()
        self.statusBar.show()

    def onclick_aboutUs(self):
        """
        Showing the message box to show help information obout this application.

        """
        self.winHelp.about_us()

    def onclick_help(self):
        """
        Showing the message box to show help information obout this application.

        """
        if self.cam:
            self.video_controller.pauseVideo()
        self.dialogHelp.show()

    def framePanoramaNormal(self):
        self.labelMin.hide()
        self.labelMax.hide()
        self.min_pano.hide()
        self.max_pano.hide()
        self.labelIcx.show()
        self.labelIcy.show()
        self.setIcx.show()
        self.setIcy.show()
        self.frame_panorama.setGeometry(QtCore.QRect(5, 45, 180, 80))

    def framePanoramaRecenter(self):
        self.labelRecenter.show()
        self.labelIcx.show()
        self.labelIcy.show()
        self.setIcx.show()
        self.setIcy.show()
        self.labelMin.show()
        self.labelMax.show()
        self.min_pano.show()
        self.max_pano.show()
        self.frame_panorama.setGeometry(QtCore.QRect(5, 45, 180, 145))

    def framePanoramaAuto(self):
        self.labelIcx.hide()
        self.labelIcy.hide()
        self.setIcx.hide()
        self.setIcy.hide()
        self.labelMin.show()
        self.labelMax.show()
        self.min_pano.show()
        self.max_pano.show()
        self.frame_panorama.setGeometry(QtCore.QRect(5, 45, 180, 80))

    def showRecenter(self):
        if self.btn_Auto.isChecked():
            if self.detector is None:
                QtWidgets.QMessageBox.warning(None, "Warning!", "You have environment not match with the requirement,\n"
                                                                "please read the README on plugin apps folder!!. ")
                self.btn_Auto.setChecked(False)
                self.btn_Auto.setStyleSheet(
                    "QPushButton{\n"
                    "  border-color: #71D1BA;\n"
                    "  border-width: 2px;        \n"
                    "  border-style: solid;\n"
                    "  border-radius: 5px;\n"
                    "  background-color : rgb(211, 215, 207);}\n")
            else:
                self.point = self.detector.center_coordinate(self.image)
                self.setIcx.setValue(self.point[0])
                self.setIcy.setValue(self.point[1])
                alpha, beta = self.moildev.getAlphaBeta(self.point[0], self.point[1])
                self.recImage = self.recenter.returnImage(alpha, beta)
                self.setIcx.setDisabled(True)
                self.setIcy.setDisabled(True)
        else:
            self.recImage = self.recenter.returnImage(self.alpha, self.beta)
            self.setIcx.setDisabled(False)
            self.setIcy.setDisabled(False)

    def showToWindow(self):
        """
        Showing the processing result image into the frame UI.

        """
        global plusIcon, resImage
        image = self.image.copy()
        radius = 6 if self.h < 800 else 10
        if self.mode_view == "Normal":
            self.buttonRecenter.show()
            if self.buttonRecenter.isChecked():
                self.framePanoramaNormal()
                self.showRecenter()
                resImage = self.recImage
            else:
                resImage = self.image
                if self.type_camera == "endoscope":
                    self.point = (self.moildev.getIcx() + 160, self.moildev.getIcy())
                else:
                    self.point = (self.moildev.getIcx(), self.moildev.getIcy())
                self.frame_panorama.hide()

            image = MoilUtils.drawPoint(image, self.point, radius)
            plusIcon = True

        elif self.mode_view == "Anypoint":
            self.result_image = MoilUtils.remap(self.image, self.mapX, self.mapY)
            image = MoilUtils.drawPolygon(self.image.copy(), self.mapX, self.mapY)
            image = MoilUtils.drawPoint(image, self.point, radius)
            resImage = MoilUtils.drawLine(self.result_image.copy())
            plusIcon = True

        elif self.mode_view == "Panorama":
            self.buttonRecenter.show()
            if self.buttonRecenter.isChecked():
                self.labelRecenter.show()
                self.framePanoramaRecenter()
                self.showRecenter()
                image_rec = self.recImage
                image = MoilUtils.drawPoint(image, self.point, radius)

            else:
                self.labelRecenter.hide()
                self.framePanoramaAuto()
                image_rec = self.image.copy()
                if self.type_camera == "endoscope":
                    self.point = (self.moildev.getIcx() + 160, self.moildev.getIcy())
                else:
                    self.point = (self.moildev.getIcx(), self.moildev.getIcy())

            resImage = MoilUtils.remap(image_rec, self.mapX_pano, self.mapY_pano)
            plusIcon = False

        MoilUtils.showImageToLabel(self.label_result,
                                   resImage,
                                   self.width_result_image, self.angle, plusIcon)

        MoilUtils.showImageToLabel(self.label_ori,
                                   image,
                                   self.width_ori_image)
        self.show_percentage()

    def show_percentage(self):
        count = self.comboBox_zoom.count()
        if count == 8:
            self.comboBox_zoom.addItem("")
        self.comboBox_zoom.setCurrentIndex(8)
        size = round((self.width_result_image / self.w) * 100)
        self.comboBox_zoom.setItemText(8, (str(size) + "%"))

    def zoom_in(self):
        """
        Zoom in image on result label

        """
        if self.image is not None:
            if self.width_result_image > 6000:
                pass
            else:
                self.width_result_image += 100
            self.showToWindow()

    def zoom_out(self):
        """
        Zoom out image on result label

        """
        if self.image is not None:
            if self.width_result_image < 800:
                pass
            else:
                self.width_result_image -= 100
            self.showToWindow()

    def rotate_left(self):
        """
        Rotate image in anti clockwise.

        """
        if self.image is not None:
            if self.angle == 180:
                pass
            else:
                self.angle += 10
            self.showToWindow()

    def rotate_right(self):
        """
        Rotate image in clockwise.

        """
        if self.image is not None:
            if self.angle == 180:
                pass
            else:
                self.angle -= 10
            self.showToWindow()

    def combo_percentage_zoom(self):
        if self.image is not None:
            self.comboBox_zoom.removeItem(8)
            percent = self.comboBox_zoom.currentText()
            percent = int(percent.replace("%", ""))
            self.width_result_image = round((self.w * percent) / 100)
            self.showToWindow()

    def set_param_any(self):
        self.point = None
        self.alpha = float(self.lineedit_alpha_2.text())
        self.beta = float(self.lineedit_beta_2.text())
        self.zoom_any = float(self.anypoint_zoom_2.text())
        self.anypoint()

    def onclickRecenter(self):
        if self.image is not None:
            if self.buttonRecenter.isChecked():
                self.buttonRecenter.setStyleSheet(
                    "QPushButton{\n"
                    "  border-color: #71D1BA;\n"
                    "  border-width: 2px;        \n"
                    "  border-style: solid;\n"
                    "  border-radius: 5px;\n"
                    "  background-color : rgb(252, 233, 79); }\n")
                self.recenter.onclickRecenter()

                self.btn_Auto.show()
                self.button_menu.show()
                self.button_menu.setChecked(True)
                self.control_additional_frame()

            else:
                self.buttonRecenter.setStyleSheet(
                    "QPushButton{\n"
                    "  border-color: #71D1BA;\n"
                    "  border-width: 2px;        \n"
                    "  border-style: solid;\n"
                    "  border-radius: 5px;\n"
                    "  background-color : rgb(211, 215, 207); }\n")
                self.recImage = None
                self.btn_Auto.hide()
                self.btn_Auto.setChecked(False)
                self.onclickAuto()
                self.button_menu.hide()
        else:
            self.buttonRecenter.setStyleSheet(
                "QPushButton{\n"
                "  border-color: #71D1BA;\n"
                "  border-width: 2px;        \n"
                "  border-style: solid;\n"
                "  border-radius: 5px;\n"
                "  background-color : rgb(211, 215, 207); }\n")

    def actionRecordVideo(self):
        """
        Create video writer to save video.

        """
        if self.image is None:
            self.actionRecord_video.setChecked(False)
        else:
            if self.cam:
                if self.actionRecord_video.isChecked():
                    if self.video_controller.play:
                        self.video_controller.pauseVideo()
                    if self.videoDir is None or self.videoDir == "":
                        self.videoDir = MoilUtils.selectDirectory()
                    if self.videoDir:
                        ss = datetime.datetime.now().strftime("%m%d%H_%M%S")
                        frame_width = int(self.cap.get(3))
                        frame_height = int(self.cap.get(4))
                        filename = "Recorded"  # if self.parent.normal_view else "result"

                        name = self.videoDir + "/" + filename + "_" + str(ss) + ".avi"
                        answer = QtWidgets.QMessageBox.information(
                            self.parent,
                            "Information",
                            " Start Record Video !!",
                            QtWidgets.QMessageBox.Yes,
                            QtWidgets.QMessageBox.No)

                        if answer == QtWidgets.QMessageBox.Yes:
                            self.video_controller.playVideo()
                            self.video_writer = cv2.VideoWriter(
                                name, cv2.VideoWriter_fourcc(
                                    *'XVID'), self.video_controller.fps, (frame_width, frame_height))
                            os.makedirs(os.path.dirname(name), exist_ok=True)
                            self.actionRecord_video.setIcon(
                                QtGui.QIcon(QtGui.QPixmap.fromImage(self.resource.iconRecording())))
                            self.record = True
                        if answer == QtWidgets.QMessageBox.No:
                            self.actionRecord_video.setChecked(False)
                            self.record = False
                    else:
                        self.videoDir = None
                        self.actionRecord_video.setChecked(False)

                else:
                    if self.videoDir:
                        self.video_controller.timer.stop()
                        self.btnPlayPause.setIcon(
                            QtGui.QIcon(QtGui.QPixmap.fromImage(self.resource.iconPlay())))
                        QtWidgets.QMessageBox.information(
                            self.parent,
                            "Information",
                            "Video saved !!\n\nLoc: " +
                            self.videoDir)
                        self.video_writer = None
                        self.video_controller.play = False
                        self.record = False
                        self.actionRecord_video.setChecked(False)
                        self.actionRecord_video.setIcon(
                            QtGui.QIcon(QtGui.QPixmap.fromImage(self.resource.iconRecord())))

    def close_event(self, e):
        self.parent.close()

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
