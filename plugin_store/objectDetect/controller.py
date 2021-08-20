from . import ui_mainwindow
from PyQt5 import QtWidgets, QtCore, QtGui
import cv2
import imutils
import datetime
import numpy as np
from imutils import grab_contours, contours
from moilutils import MoilUtils
from reCenter import RecenterImage
from souceIcon import ResourceIcon


class UiController(ui_mainwindow.Ui_MainWindow):
    def __init__(self, mainWindow):
        super(UiController, self).__init__()
        self.maxThresh = None
        self.minThresh = None
        self.parent = mainWindow
        self.setupUi(self.parent)
        self.title = "Image Evaluation"
        self.result_image = None
        self.recImage = None
        self.zoom_area = False
        self.morphImage = None
        self.kernel_opening = None
        self.gaussian_filter = None
        self.ratioThresh = None
        self.maxWidth = None
        self.maxHeight = None
        self.valGammaContrast = None
        self.valBetaContrast = None
        self.valAlphaContrast = None
        self.fps = None
        self.pos_frame = None
        self.frame_count = None
        self.minute = None
        self.minutes = None
        self.seconds = None
        self.sec = None
        self.play = False
        self.video_writer = None
        self.videoDir = None
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.next_frame_slot)
        self.rs = ResourceIcon()
        self.moildev = None
        self.image = None
        self.cam = False
        self.cap = None
        self.w = None
        self.h = None
        self.alpha = 0
        self.beta = 0
        self.zoom_any = 4
        self.anypoint_mode = 1
        # self.radio_btn_mode_1.setChecked(True)
        self.point = None
        self.type_camera = None
        self.normal_view = True
        self.anypoint_view = False
        self.panorama_view = False
        self.widthImageResult = None
        self.__pano_alpha_min = 10
        self.__pano_alpha_max = None
        self.angle = 0
        self.frame.hide()
        self.frameVideoController.hide()
        self.titleRecenter.hide()
        self.labelRecenter.hide()
        self.frameEvaluate.hide()
        self.frame_panorama.hide()
        self.frame_navigator.hide()
        self.buttonBack.hide()
        self.buttonRecenter.hide()
        self.recenter = RecenterImage(self)
        self.initConfigurationObjectDetection()
        self.connectEvent()

    def connectEvent(self):
        self.openImage.clicked.connect(self.onclickOpenImage)
        self.openVideo.clicked.connect(self.load_video)
        self.checkBox.clicked.connect(self.activeEvaluate)
        self.zoomIn.clicked.connect(self.zoom_in)
        self.zoomOut.clicked.connect(self.zoom_out)
        self.rotateLeft.clicked.connect(self.rotate_left)
        self.rotateRight.clicked.connect(self.rotate_right)
        self.comboBox.activated.connect(self.combo_percentage_zoom)
        self.label_result.wheelEvent = self.mouse_wheelEvent
        self.button_menu.clicked.connect(self.control_extra_button)

        self.btn_normal.clicked.connect(self.onclick_normal)
        self.btn_anypoint.clicked.connect(self.onclick_anypoint)
        self.btn_panorama.clicked.connect(self.onclick_panorama)

        self.buttonRecenter.clicked.connect(self.onclickRecenter)
        self.setIcx.valueChanged.connect(self.recenter.positionCoorX)
        self.setIcy.valueChanged.connect(self.recenter.positionCoorY)

        # video controller
        self.btn_play_pouse.clicked.connect(self.onclick_play_pause_button)

        # evaluation Image
        self.btn_objectDetect.clicked.connect(self.show_to_window)
        self.pushButton.clicked.connect(self.onclickShowProcess)
        self.gausianSpinBox.valueChanged.connect(self.setGausianFilter)
        self.openingSpinbox.valueChanged.connect(self.setKernelOpening)
        self.alphaContrast.valueChanged.connect(self.setAlphaContrast)
        self.betaContrast.valueChanged.connect(self.setBetaContrast)
        self.gamaContrast.valueChanged.connect(self.setGammaContrast)
        self.heightThreshold.valueChanged.connect(self.setMaxHeightThreshold)
        self.widthThreshold.valueChanged.connect(self.setMaxWidthThreshold)
        self.ratioThreshold.valueChanged.connect(self.setRatioThreshold)
        self.minThreshold.valueChanged.connect(self.setMinThresh)
        self.maxThreshold.valueChanged.connect(self.setMaxThresh)

    def onclickRecenter(self):
        if self.buttonRecenter.isChecked():
            self.buttonRecenter.setStyleSheet(
                "QPushButton{\n"
                "  border-color: #71D1BA;\n"
                "  border-width: 2px;        \n"
                "  border-style: solid;\n"
                "  border-radius: 5px;\n"
                "  background-color : #81AED1; }\n")
            self.recenter.onclickRecenter()
            self.frame_panorama.show()

        else:
            self.buttonRecenter.setStyleSheet(
                "QPushButton{\n"
                "  border-color: #71D1BA;\n"
                "  border-width: 2px;        \n"
                "  border-style: solid;\n"
                "  border-radius: 5px;\n"
                "  background-color : rgb(238, 238, 236); }\n")
            self.show_to_window()
            self.recImage = None

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
                pass
        else:
            if self.anypoint_view:
                self.frame_navigator.show()
            elif self.panorama_view:
                self.frame_panorama.show()
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
                    if self.widthImageResult < 800:
                        pass
                    else:
                        self.widthImageResult -= 100

                if wheel_counter.y() / 120 == 1:
                    if self.widthImageResult > 6000:
                        pass
                    else:
                        self.widthImageResult += 100
                self.show_to_window()

    def showInformationCamera(self):
        self.labelTypeCamera.setText(self.type_camera)
        self.labelFoV.setText(str(self.moildev.getCameraFov()))
        self.labelWidth.setText(str(self.moildev.getImageWidth()))
        self.labelHeight.setText(str(self.moildev.getImageHeight()))
        self.imgIcx.setText(str(self.moildev.getIcx()))
        self.imgIcy.setText(str(self.moildev.getIcy()))
        self.frame.show()

    def onclickOpenImage(self):
        filename = MoilUtils.selectFile(self.parent, "Select Image", "../SourceImage",
                                        "Image Files (*.jpeg *.jpg *.png *.gif *.bmg)")
        if filename:
            self.image = MoilUtils.readImage(filename)
            self.h, self.w = self.image.shape[:2]
            self.widthImageResult = 1160 if (self.h / self.w) == 0.75 else 900
            self.type_camera = MoilUtils.readCameraType(filename)
            self.moildev = MoilUtils.connectToMoildev(self.type_camera)
            self.showInformationCamera()
            self.cam = False
            self.onclick_normal()

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
            self.moildev = MoilUtils.connectToMoildev(self.type_camera)
            self.parent.setWindowTitle(self.title + " - " + video_source)
            if self.type_camera is not None:
                self.running_video(video_source)

    def running_video(self, video_source):
        """
        Open Video following the source given.

        Args:
            video_source (): the source of media, can be camera and video file.
        """
        self.cap = cv2.VideoCapture(video_source)
        success, image = self.cap.read()
        if success:
            self.h, self.w = image.shape[:2]
            self.widthImageResult = 1160 if (self.h / self.w) == 0.75 else 900
            self.cam = True
            self.next_frame_slot()
        else:
            QtWidgets.QMessageBox.information(self.parent, "Information", "No source camera founded")

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
            self.onclick_normal()

    # normal view start here +++++++++++++++++++++++++++++++
    def onclick_normal(self):
        """
        Change to normal view..

        Returns:

        """
        self.btn_anypoint.setChecked(False)
        self.btn_panorama.setChecked(False)
        self.btn_normal.setChecked(True)
        if self.image is not None:
            self.normal_view = True
            self.anypoint_view = False
            self.panorama_view = False
            self.result_image = None
            self.show_to_window()

    # anypoint view start here+++++++++++++++++++++++++++++
    def onclick_anypoint(self):
        """
        Change to anypoint mode..

        Returns:

        """
        self.btn_anypoint.setChecked(True)
        self.btn_panorama.setChecked(False)
        self.btn_normal.setChecked(False)
        if self.image is not None:
            if self.type_camera:
                self.normal_view = False
                self.panorama_view = False
                self.anypoint_view = True
                self.moildev = MoilUtils.connectToMoildev(self.type_camera)
                self.anypoint()

    def anypoint(self):
        """
        Anypoint algorithm.

        """
        if self.image is not None:
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
        self.btn_anypoint.setChecked(False)
        self.btn_panorama.setChecked(True)
        self.btn_normal.setChecked(False)
        if self.image is not None:
            if self.type_camera:
                self.normal_view = False
                self.anypoint_view = False
                self.panorama_view = True
                self.moildev = MoilUtils.connectToMoildev(self.type_camera)
                self.__pano_alpha_max = self.moildev.getCameraFov() / 2
                self.panorama()

    def panorama(self):
        """
        Panorama function.

        """
        self.angle = 0
        self.rho = self.moildev.getRhoFromAlpha(self.__pano_alpha_min)
        self.frame_navigator.hide()
        self.frame_panorama.show()
        mapX, mapY, = self.moildev.getPanoramaMaps(
            10, self.__pano_alpha_max)
        np.save("./maps_pano/mapX.npy", mapX)
        np.save("./maps_pano/mapY.npy", mapY)
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

    def show_to_window(self):
        """
        Showing the processing result image into the frame UI.

        """
        if self.cam:
            self.frameVideoController.show()
        else:
            self.frameVideoController.hide()
        self.zoom_area = False
        self.buttonBack.hide()
        radius = 6 if self.h < 800 else 10
        if self.normal_view:
            self.labelRecenter.hide()
            self.titleRecenter.hide()
            self.buttonRecenter.show()
            if self.buttonRecenter.isChecked():
                self.labelMin.hide()
                self.labelMax.hide()
                self.min_pano.hide()
                self.max_pano.hide()
                self.labelIcx.show()
                self.labelIcy.show()
                self.setIcx.show()
                self.setIcy.show()
                self.recImage = self.recenter.returnImage()
                resImage = self.recImage
                self.frame_panorama.setGeometry(QtCore.QRect(5, 50, 180, 80))
            else:
                if self.btn_objectDetect.isChecked():
                    resImage = self.detector(self.image.copy(),
                                             self.kernel_opening,
                                             self.gaussian_filter,
                                             self.valAlphaContrast,
                                             self.valBetaContrast,
                                             self.valGammaContrast,
                                             self.minThresh,
                                             self.maxThresh,
                                             self.maxWidth,
                                             self.maxHeight,
                                             self.ratioThresh)
                else:
                    resImage = self.image
                    self.point = (round(self.moildev.getIcx()), round(self.moildev.getIcy()))
                    self.frame_panorama.hide()
            image = MoilUtils.drawPoint(self.image.copy(), self.point, radius)
            MoilUtils.showImageToLabel(self.label_ori,
                                       image, 400)
            MoilUtils.showImageToLabel(self.label_result,
                                       resImage,
                                       self.widthImageResult, self.angle, plusIcon=True)

        elif self.panorama_view:
            self.buttonRecenter.show()
            mapX = np.load(
                './maps_pano/mapX.npy')
            mapY = np.load(
                './maps_pano/mapY.npy')
            # rho = self.panorama.rho
            if self.buttonRecenter.isChecked():
                self.labelRecenter.show()
                self.titleRecenter.show()
                self.labelIcx.show()
                self.labelIcy.show()
                self.setIcx.show()
                self.setIcy.show()
                self.labelMin.show()
                self.labelMax.show()
                self.min_pano.show()
                self.max_pano.show()
                self.frame_panorama.setGeometry(QtCore.QRect(5, 50, 180, 145))
                self.recImage = self.recenter.returnImage()
                resImage = self.recImage
                res = MoilUtils.drawPolygon(resImage.copy(), mapX, mapY)
                MoilUtils.showImageToLabel(self.labelRecenter,
                                           res, 400, plusIcon=True)
                image = MoilUtils.drawPoint(self.image.copy(), self.point, radius)
                MoilUtils.showImageToLabel(self.label_ori,
                                           image, 400)
            else:
                self.labelRecenter.hide()
                self.titleRecenter.hide()
                self.labelIcx.hide()
                self.labelIcy.hide()
                self.setIcx.hide()
                self.setIcy.hide()
                self.labelMin.show()
                self.labelMax.show()
                self.min_pano.show()
                self.max_pano.show()
                self.frame_panorama.setGeometry(QtCore.QRect(5, 50, 180, 80))
                resImage = self.image.copy()
                self.point = (round(self.moildev.getIcx()), round(self.moildev.getIcy()))

                # self.result_image = self.result_image[round(rho):self.h, 0:self.w]
                # print(self.result_image)
                image = MoilUtils.drawPolygon(self.image.copy(), mapX, mapY)
                image = MoilUtils.drawPoint(image, self.point, radius)
                MoilUtils.showImageToLabel(self.label_ori,
                                           image, 400)
            self.result_image = cv2.remap(resImage, mapX, mapY, cv2.INTER_CUBIC)
            if self.btn_objectDetect.isChecked():
                self.result_image = self.detector(self.result_image.copy(),
                                                  self.kernel_opening,
                                                  self.gaussian_filter,
                                                  self.valAlphaContrast,
                                                  self.valBetaContrast,
                                                  self.valGammaContrast,
                                                  self.minThresh,
                                                  self.maxThresh,
                                                  self.maxWidth,
                                                  self.maxHeight,
                                                  self.ratioThresh)
            else:
                self.result_image = self.result_image

            MoilUtils.showImageToLabel(self.label_result,
                                       self.result_image,
                                       self.widthImageResult, self.angle)

        else:
            self.buttonRecenter.hide()
            self.labelRecenter.hide()
            self.titleRecenter.hide()
            image = MoilUtils.drawPolygon(self.image.copy(), self.mapX, self.mapY)
            image = MoilUtils.drawPoint(image, self.point, radius)
            self.result_image = cv2.remap(self.image, self.mapX, self.mapY, cv2.INTER_CUBIC)
            if self.btn_objectDetect.isChecked():
                self.result_image = self.detector(self.result_image.copy(),
                                                  self.kernel_opening,
                                                  self.gaussian_filter,
                                                  self.valAlphaContrast,
                                                  self.valBetaContrast,
                                                  self.valGammaContrast,
                                                  self.minThresh,
                                                  self.maxThresh,
                                                  self.maxWidth,
                                                  self.maxHeight,
                                                  self.ratioThresh)
            else:
                self.result_image = self.result_image

            result = MoilUtils.drawLine(self.result_image)
            MoilUtils.showImageToLabel(self.label_result,
                                       result,
                                       self.widthImageResult, self.angle, plusIcon=True)
            MoilUtils.showImageToLabel(self.label_ori,
                                       image, 400)
        self.show_percentage()

    def activeEvaluate(self):
        if self.image is not None:
            if self.checkBox.isChecked():
                self.frameEvaluate.show()
            else:
                self.frameEvaluate.hide()

    def initConfigurationObjectDetection(self):
        self.gausianSpinBox.setValue(15)
        self.openingSpinbox.setValue(26)
        self.alphaContrast.setValue(3.85)
        self.betaContrast.setValue(-95.2)
        self.gamaContrast.setValue(1.5)
        self.heightThreshold.setValue(300)
        self.widthThreshold.setValue(300)
        self.ratioThreshold.setValue(2.0)
        self.valAlphaContrast = self.alphaContrast.value()
        self.valBetaContrast = self.betaContrast.value()
        self.valGammaContrast = self.gamaContrast.value()
        self.maxHeight = self.heightThreshold.value()
        self.maxWidth = self.widthThreshold.value()
        self.ratioThresh = self.ratioThreshold.value()
        self.gaussian_filter = self.gausianSpinBox.value()
        self.kernel_opening = self.openingSpinbox.value()
        self.minThresh = self.minThreshold.value()
        self.maxThresh = self.maxThreshold.value()

    def setAlphaContrast(self):
        if self.pushButton.isChecked():
            self.onclickShowProcess()
        self.valAlphaContrast = self.alphaContrast.value()
        self.show_to_window()

    def setBetaContrast(self):
        if self.pushButton.isChecked():
            self.onclickShowProcess()
        self.valBetaContrast = self.betaContrast.value()
        self.show_to_window()

    def setGammaContrast(self):
        if self.pushButton.isChecked():
            self.onclickShowProcess()
        self.valGammaContrast = self.gamaContrast.value()
        self.show_to_window()

    def setMaxHeightThreshold(self):
        if self.pushButton.isChecked():
            self.onclickShowProcess()
        self.maxHeight = self.heightThreshold.value()
        self.show_to_window()

    def setMaxWidthThreshold(self):
        if self.pushButton.isChecked():
            self.onclickShowProcess()
        self.maxWidth = self.widthThreshold.value()
        self.show_to_window()

    def setRatioThreshold(self):
        if self.pushButton.isChecked():
            self.onclickShowProcess()
        self.ratioThresh = self.ratioThreshold.value()
        self.show_to_window()

    def setGausianFilter(self):
        if self.pushButton.isChecked():
            self.onclickShowProcess()
        self.gaussian_filter = self.gausianSpinBox.value()
        self.show_to_window()

    def setKernelOpening(self):
        if self.pushButton.isChecked():
            self.onclickShowProcess()
        self.kernel_opening = self.openingSpinbox.value()
        self.show_to_window()

    def setMaxThresh(self):
        if self.pushButton.isChecked():
            self.onclickShowProcess()
        self.maxThresh = self.maxThreshold.value()
        self.show_to_window()

    def setMinThresh(self):
        if self.pushButton.isChecked():
            self.onclickShowProcess()
        self.minThresh = self.minThreshold.value()
        self.show_to_window()

    def zoom_in(self):
        """
        Zoom in image on result label

        """
        if self.image is not None:
            if self.widthImageResult > 6000:
                pass
            else:
                self.widthImageResult += 100
            self.show_to_window()

    def zoom_out(self):
        """
        Zoom out image on result label

        """
        if self.image is not None:
            if self.widthImageResult < 800:
                pass
            else:
                self.widthImageResult -= 100
            self.show_to_window()

    def rotate_left(self):
        """
        Rotate image in anti clockwise.

        """
        if self.image is not None:
            if self.angle == 180:
                pass
            else:
                self.angle += 10
            self.show_to_window()

    def rotate_right(self):
        """
        Rotate image in clockwise.

        """
        if self.image is not None:
            if self.angle == 180:
                pass
            else:
                self.angle -= 10
            self.show_to_window()

    def show_percentage(self):
        count = self.comboBox.count()
        if count == 8:
            self.comboBox.addItem("")
        self.comboBox.setCurrentIndex(8)
        size = round((self.widthImageResult / self.w) * 100)
        self.comboBox.setItemText(8, (str(size) + "%"))

    def combo_percentage_zoom(self):
        if self.image is not None:
            self.comboBox.removeItem(8)
            percent = self.comboBox.currentText()
            percent = int(percent.replace("%", ""))
            self.widthImageResult = round((self.w * percent) / 100)
            self.show_to_window()

    def onclickShowProcess(self):
        if self.pushButton.isChecked():
            image = self.image if self.result_image is None else self.result_image
            img = self.showImageProcessing(image, self.kernel_opening, self.gaussian_filter,
                                           self.valAlphaContrast, self.valBetaContrast, self.minThresh,
                                           self.maxThresh)
            img = MoilUtils.resizeImage(img, 800)
            cv2.imshow("Processing", img)
        else:
            cv2.destroyAllWindows()
        # cv2.waitKey()

    def showImageProcessing(self, image, kernel_opening, gaussian_filter, alpha_contrast, beta_contrast,
                            minThresh, maxThresh):
        """
            object detection function
        """
        kernel = np.ones((kernel_opening, kernel_opening), np.uint8)
        new_image = cv2.convertScaleAbs(image, alpha=alpha_contrast, beta=beta_contrast)
        gray = cv2.cvtColor(new_image, cv2.IMREAD_GRAYSCALE)
        opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
        gray = cv2.GaussianBlur(opening, (gaussian_filter, gaussian_filter), 0)
        # perform edge detection, then perform a dilation + erosion to
        # close gaps in between object edges
        edged = cv2.Canny(gray, minThresh, maxThresh)
        edged = cv2.dilate(edged, None, iterations=1)
        edged = cv2.erode(edged, None, iterations=1)
        return edged

    def detector(self, image, kernel_opening, gaussian_filter, alpha_contrast, beta_contrast, gama_contrast, minThresh,
                 maxThresh, maxWidth, maxHeight, ratio):
        """
        object detection function
        """
        kernel = np.ones((kernel_opening, kernel_opening), np.uint8)
        new_image = cv2.convertScaleAbs(image, alpha=alpha_contrast, beta=beta_contrast)
        gray = cv2.cvtColor(new_image, cv2.IMREAD_GRAYSCALE)
        opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
        gray = cv2.GaussianBlur(opening, (gaussian_filter, gaussian_filter), 0)
        # perform edge detection, then perform a dilation + erosion to
        # close gaps in between object edges
        edged = cv2.Canny(gray, minThresh, maxThresh)
        edged = cv2.dilate(edged, None, iterations=1)
        edged = cv2.erode(edged, None, iterations=1)
        cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = grab_contours(cnts)
        # sort the contours from left-to-right and initialize the bounding box
        # point colors
        if cnts:
            (cnts, _) = contours.sort_contours(cnts)
            colors = ((0, 0, 255), (240, 0, 159), (255, 0, 0), (255, 255, 0))
            # loop over the contours individually
            for (i, c) in enumerate(cnts):
                # if the contour is not sufficiently large, ignore it
                if cv2.contourArea(c) < 100:
                    continue
                # compute the rotated bounding box of the contour, then
                # draw the contours
                box = cv2.minAreaRect(c)
                (x, y), (w, h), angle = box
                if w > maxWidth or w < 100:
                    continue
                if h > maxHeight or h < 100:
                    continue
                if w / h > ratio or h / w > ratio:
                    continue
                box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
                box = np.array(box, dtype="int")
                cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
                cv2.putText(image, "H=" + str(round(h)) + "px", (int(x - 40), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 255, 0),
                            2)
                cv2.putText(image, "W=" + str(round(w)) + "px", (int(x - 40), int(y + 40)), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 255, 0), 2)

        return image

    # migrate to video controller
    def next_frame_slot(self):
        """
        looping the frame showing in label user interface.

        """
        success, self.image = self.cap.read()
        if success:
            self.fps = self.cap.get(cv2.CAP_PROP_FPS)
            self.pos_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
            self.frame_count = float(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
            duration_sec = int(self.frame_count / self.fps)
            self.minutes = duration_sec // 60
            duration_sec %= 60
            self.seconds = duration_sec
            sec_pos = int(self.pos_frame / self.fps)
            self.minute = int(sec_pos // 60)
            sec_pos %= 60
            self.sec = sec_pos
            self.controller()
            self.show_to_window()
            # if self.parent.btn_Record_video.isChecked():
            #     image = self.parent.image if self.parent.normal_view else self.parent.result_image
            #     self.parent.video_writer.write(image)

    def reset_time(self):
        """
        Reset the time when open the new video.

        """
        current = self.label_time_recent
        current.setAlignment(QtCore.Qt.AlignCenter)
        current.setText("00:00")

        end_time = self.label_time_end
        end_time.setAlignment(QtCore.Qt.AlignCenter)
        end_time.setText("00:00")

    def onclick_play_pause_button(self):
        """
        Control the play and pause video controller button
        for example, if play is true: it will change the icon button

        """
        if self.play:
            self.pause_video()

        else:
            self.play_video()

    def pause_video(self):
        """
        Pause the frame in video or camera mode.

        """
        if self.video_writer is not None:
            answer = QtWidgets.QMessageBox.information(
                self.parent,
                "Information",
                "System in record mode, pause will stop recorded. \n\nContinue process ??",
                QtWidgets.QMessageBox.Yes,
                QtWidgets.QMessageBox.No)

            if answer == QtWidgets.QMessageBox.Yes:
                self.timer.stop()
                self.btn_play_pouse.setIcon(
                    QtGui.QIcon(QtGui.QPixmap.fromImage(self.rs.iconPlay())))
                QtWidgets.QMessageBox.information(
                    self.parent,
                    "Information",
                    "Video saved !!\n\nLoc: " +
                    self.videoDir)
                self.btn_Record_video.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(self.rs.iconRecording())))
                self.btn_Record_video.setChecked(False)
                self.video_writer = None
                self.play = False
        else:
            self.timer.stop()
            self.btn_play_pouse.setIcon(
                QtGui.QIcon(QtGui.QPixmap.fromImage(self.rs.iconPlay())))
            self.play = False

    def play_video(self):
        """
        Play video by connect to timer function.

        """
        if self.cap.isOpened():
            self.btn_play_pouse.setIcon(
                QtGui.QIcon(QtGui.QPixmap.fromImage(self.rs.iconPause())))
            self.timer.start(1000 / self.fps)
        self.play = True

    def controller(self):
        """
        Manage the video to setup the current timer.

        """
        dst_value = self.pos_frame * (self.slider_Video.maximum() + 1) / self.frame_count
        self.slider_Video.blockSignals(True)
        self.slider_Video.setValue(dst_value)
        self.slider_Video.blockSignals(False)

        current = self.label_time_recent
        current.setAlignment(QtCore.Qt.AlignCenter)
        current.setText("%02d : %02d" % (self.minute, self.sec))

        if self.minutes < 0:
            "this is for live camera, when the times more than 1000 minutes, it will set to 00:00"
            my_label3 = self.label_time_end
            my_label3.setAlignment(QtCore.Qt.AlignCenter)
            my_label3.setText("00:00")

        else:
            my_label3 = self.label_time_end
            my_label3.setAlignment(QtCore.Qt.AlignCenter)
            my_label3.setText("%02d : %02d" %
                              (self.minutes, self.seconds))

    def stop_video(self):
        """
        Stop video and set the time as a beginning, including the slider time

        """
        self.play = False
        self.btn_play_pouse.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(self.rs.iconPlay())))
        if self.cap.isOpened():
            self.timer.stop()
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            self.next_frame_slot()
            self.reset_label_time()
        else:
            pass

    def reset_label_time(self):
        """
        Reset the time when open the new video.

        """
        current = self.label_time_recent
        current.setAlignment(QtCore.Qt.AlignCenter)
        current.setText("00:00")

        current_1 = self.label_time_end
        current_1.setAlignment(QtCore.Qt.AlignCenter)
        current_1.setText("00:00")

    def prev_video(self):
        """
        Previous video is 5 seconds.

        """
        if self.cap.isOpened():
            position = self.pos_frame - 5 * self.fps
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, position)
            self.next_frame_slot()
        else:
            pass

    def skip_video(self):
        """
        skip video in 5 seconds.

        """
        if self.cap.isOpened():
            position = self.pos_frame + 5 * self.fps
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, position)
            self.next_frame_slot()
        else:
            pass

    def changeValueSlider(self, value):
        """
        Set and control the slider to control the video.

        Args:
            value (): Value from slider

        """
        if self.cap.isOpened():
            dst_frame = self.frame_count * value / self.slider_Video.maximum()
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, dst_frame)
            self.next_frame_slot()
            self.pause_video()
            self.play = False

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
                        self.video_controller.pause_video()
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
                            self.video_controller.play_video()
                            self.video_writer = cv2.VideoWriter(
                                name, cv2.VideoWriter_fourcc(
                                    *'XVID'), self.video_controller.fps, (frame_width, frame_height))
                            os.makedirs(os.path.dirname(name), exist_ok=True)
                            self.btn_Record_video.setChecked(True)
                            self.btn_Record_video.setIcon(
                                QtGui.QIcon(QtGui.QPixmap.fromImage(self.rs.iconRecording())))
                            self.actionRecord_video.setIcon(
                                QtGui.QIcon(QtGui.QPixmap.fromImage(self.rs.iconRecording())))
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
                        self.btn_play_pouse.setIcon(
                            QtGui.QIcon(QtGui.QPixmap.fromImage(self.rs.iconPlay())))
                        QtWidgets.QMessageBox.information(
                            self.parent,
                            "Information",
                            "Video saved !!\n\nLoc: " +
                            self.videoDir)
                        self.video_writer = None
                        self.video_controller.play = False
                        self.record = False
                        self.actionRecord_video.setChecked(False)
                        self.btn_Record_video.setChecked(False)
                        self.btn_Record_video.setIcon(
                            QtGui.QIcon(QtGui.QPixmap.fromImage(self.rs.iconRecord())))
                        self.actionRecord_video.setIcon(
                            QtGui.QIcon(QtGui.QPixmap.fromImage(self.rs.iconRecord())))

    def buttonRecordVideo(self):
        """
        Create video writer to save video.

        """
        if self.image is None:
            self.btn_Record_video.setChecked(False)
        else:
            if self.cam:
                if self.btn_Record_video.isChecked():
                    if self.video_controller.play:
                        self.video_controller.pause_video()
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
                            self.video_controller.play_video()
                            self.video_writer = cv2.VideoWriter(
                                name, cv2.VideoWriter_fourcc(
                                    *'XVID'), self.video_controller.fps, (frame_width, frame_height))
                            os.makedirs(os.path.dirname(name), exist_ok=True)
                            self.actionRecord_video.setChecked(True)
                            self.btn_Record_video.setIcon(
                                QtGui.QIcon(QtGui.QPixmap.fromImage(self.rs.iconRecording())))
                            self.actionRecord_video.setIcon(
                                QtGui.QIcon(QtGui.QPixmap.fromImage(self.rs.iconRecording())))
                            self.record = True
                        if answer == QtWidgets.QMessageBox.No:
                            self.btn_Record_video.setChecked(False)
                            self.record = False
                    else:
                        self.videoDir = None
                        self.btn_Record_video.setChecked(False)

                else:
                    if self.videoDir:
                        self.video_controller.timer.stop()
                        self.btn_play_pouse.setIcon(
                            QtGui.QIcon(QtGui.QPixmap.fromImage(self.rs.iconPlay())))
                        QtWidgets.QMessageBox.information(
                            self.parent,
                            "Information",
                            "Video saved !!\n\nLoc: " +
                            self.videoDir)
                        self.video_writer = None
                        self.video_controller.play = False
                        self.record = False
                        self.actionRecord_video.setChecked(False)
                        self.btn_Record_video.setChecked(False)
                        self.btn_Record_video.setIcon(
                            QtGui.QIcon(QtGui.QPixmap.fromImage(self.rs.iconRecord())))
                        self.actionRecord_video.setIcon(
                            QtGui.QIcon(QtGui.QPixmap.fromImage(self.rs.iconRecord())))
