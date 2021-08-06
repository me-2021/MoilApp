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
        self.angle = 0
        self.width_result_image = 1360
        self.width_result_multi = 540
        self.width_ori_image = 340
        self.video_controller = VideoController(self)
        self.manipulate = ManipulateView(self)
        self.video_controller.set_button_disable()
        self.openCam = QtWidgets.QDialog()
        self.winOpenCam = CameraSource(self, self.openCam)
        self.camParams = QtWidgets.QDialog()
        self.winCamParams = CameraParameters(self, self.camParams)
        self.hide_widget_for_original()
        self.connect_event()

    def connect_event(self):
        self.actionOpen_Image.triggered.connect(self.open_image)
        self.actionLoad_Video.triggered.connect(self.load_video)
        self.actionOpen_Camera.triggered.connect(self.onclick_open_camera)
        self.actionSave_image.triggered.connect(self.save_image)
        self.actionCam_parameter.triggered.connect(self.cam_params_window)
        self.btn_open_image.clicked.connect(self.open_image)
        self.btn_open_video.clicked.connect(self.load_video)
        self.btn_open_camera.clicked.connect(self.onclick_open_camera)
        self.btn_6view.clicked.connect(self.onclick_multiple_view)
        self.btn_ori_view.clicked.connect(self.onclick_original)
        self.btn_view_1.clicked.connect(self.onclick_window_left)
        self.btn_view_2.clicked.connect(self.onclick_window_middle)
        self.btn_view_3.clicked.connect(self.onclick_window_right)
        self.btn_view_4.clicked.connect(self.onclick_window_left_down)
        self.btn_view_5.clicked.connect(self.onclick_window_down)
        self.btn_view_6.clicked.connect(self.onclick_window_right_down)
        self.label_image1.mousePressEvent = self.mouse_window_l
        self.label_image2.mousePressEvent = self.mouse_window_m
        self.label_image3.mousePressEvent = self.mouse_window_r
        self.label_image4.mousePressEvent = self.mouse_window_ld
        self.label_image5.mousePressEvent = self.mouse_window_d
        self.label_image6.mousePressEvent = self.mouse_window_rd
        self.label_Original_image.wheelEvent = self.mouse_wheelEvent
        self.label_Original_image.mouseReleaseEvent = self.mouse_release_event
        self.parent.closeEvent = self.close_event
        self.actionAccesibility.triggered.connect(self.onclick_accessibility)
        self.coombo_zoom.activated.connect(self.combo_percentage_zoom)

        self.btn_play_pouse.clicked.connect(self.video_controller.onclick_play_pause_button)
        self.btn_stop_video.clicked.connect(self.video_controller.stop_video)
        self.btn_prev_video.clicked.connect(self.video_controller.prev_video)
        self.btn_skip_video.clicked.connect(self.video_controller.skip_video)
        # self.actionRecord_video.triggered.connect(self.video_controller.action_record_video)
        # self.btn_Record_video.clicked.connect(self.video_controller.recordVideo)
        self.slider_Video.valueChanged.connect(self.video_controller.changeValueSlider)

        self.btn_rotate_left.clicked.connect(self.manipulate.rotate_left)
        self.btn_rotate_right.clicked.connect(self.manipulate.rotate_right)
        self.btn_zoom_out.clicked.connect(self.manipulate.zoom_in)
        self.btn_zoom_in.clicked.connect(self.manipulate.zoom_out)
        self.btn_save_image.clicked.connect(self.save_image)
        self.actionExit.triggered.connect(self.parent.close)

    def hide_widget_for_original(self):
        self.scrollArea_3.hide()
        self.frame_2.hide()

    def cam_params_window(self):
        """
        Open the window of camera parameter form, this window you can update, add, and
        delete the camera parameter from database.

        """
        self.camParams.show()

    def open_image(self):
        filename = MoilUtils.selectFile(self.parent, "Select Image", "../SourceImage",
                                        "Image Files (*.jpeg *.jpg *.png *.gif *.bmg)")
        if filename:
            self.image = MoilUtils.readImage(filename)
            self.h, self.w = self.image.shape[:2]
            self.parent.setWindowTitle("Multi View - " + filename)
            self.type_camera = MoilUtils.readCameraType(filename)
            if self.type_camera:
                self.cam = False
                self.onclick_original()
                self.label_camera.setText("Camera type: " + self.type_camera)
                self.video_controller.set_button_disable()
                self.show_percentage()

    def load_video(self):
        """
        Open Dialog to search video file from Directory. after you select the video file, it will show the prompt
        to select the type of camera.

        """
        video_source = MoilUtils.selectFile(self.parent,
                                            "Select Video Files",
                                            "../",
                                            "Video Files (*.mp4 *.avi *.mpg *.gif *.mov)")
        if video_source:
            self.type_camera = MoilUtils.selectCameraType()
            self.parent.setWindowTitle("Multi View - " + video_source)
            if self.type_camera is not None:
                self.running_video(video_source)
                self.label_camera.setText("Camera type: " + self.type_camera)
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
        self.type_camera = MoilUtils.selectCameraType()
        if self.type_camera is not None:
            self.running_video(camera_source)
            self.label_camera.setText("Camera type: " + self.type_camera)
            self.onclick_original()

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
            self.window_left()
            self.window_middle()
            self.window_right()
            self.window_left_down()
            self.window_down()
            self.window_right_down()
            self.normal_view = False
            self.single_view = False
            self.multiple_view = True
            self.show_to_window()

    def window_left(self):
        self.normal_view = False
        self.single_view = True
        self.multiple_view = False
        self.window = 1
        moildev = MoilUtils.connectToMoildev(self.type_camera)
        self.mapX_1, self.mapY_1, = moildev.getAnypointMaps(0, -50,
                                                            self.zoom_any,
                                                            self.anypoint_mode)

    def onclick_window_left(self):
        self.btn_ori_view.setChecked(False)
        self.btn_6view.setChecked(False)
        self.btn_view_1.setChecked(True)
        self.btn_view_2.setChecked(False)
        self.btn_view_3.setChecked(False)
        self.btn_view_4.setChecked(False)
        self.btn_view_5.setChecked(False)
        self.btn_view_6.setChecked(False)
        if self.image is not None:
            self.window_left()
            self.show_to_window()

    def window_middle(self):
        self.normal_view = False
        self.single_view = True
        self.multiple_view = False
        self.window = 2
        moildev = MoilUtils.connectToMoildev(self.type_camera)
        self.mapX_2, self.mapY_2, = moildev.getAnypointMaps(0, 0,
                                                            self.zoom_any,
                                                            self.anypoint_mode)

    def onclick_window_middle(self):
        self.btn_ori_view.setChecked(False)
        self.btn_6view.setChecked(False)
        self.btn_view_1.setChecked(False)
        self.btn_view_2.setChecked(True)
        self.btn_view_3.setChecked(False)
        self.btn_view_4.setChecked(False)
        self.btn_view_5.setChecked(False)
        self.btn_view_6.setChecked(False)
        if self.image is not None:
            self.window_middle()
            self.show_to_window()

    def window_right(self):
        self.normal_view = False
        self.single_view = True
        self.multiple_view = False
        self.window = 3
        moildev = MoilUtils.connectToMoildev(self.type_camera)
        self.mapX_3, self.mapY_3, = moildev.getAnypointMaps(0, 50,
                                                            self.zoom_any,
                                                            self.anypoint_mode)

    def onclick_window_right(self):
        self.btn_ori_view.setChecked(False)
        self.btn_6view.setChecked(False)
        self.btn_view_1.setChecked(False)
        self.btn_view_2.setChecked(False)
        self.btn_view_3.setChecked(True)
        self.btn_view_4.setChecked(False)
        self.btn_view_5.setChecked(False)
        self.btn_view_6.setChecked(False)
        if self.image is not None:
            self.window_right()
            self.show_to_window()

    def window_left_down(self):
        self.normal_view = False
        self.single_view = True
        self.multiple_view = False
        self.window = 4
        moildev = MoilUtils.connectToMoildev(self.type_camera)
        self.mapX_4, self.mapY_4, = moildev.getAnypointMaps(-45, -50,
                                                            self.zoom_any,
                                                            self.anypoint_mode)

    def onclick_window_left_down(self):
        self.btn_ori_view.setChecked(False)
        self.btn_6view.setChecked(False)
        self.btn_view_1.setChecked(False)
        self.btn_view_2.setChecked(False)
        self.btn_view_3.setChecked(False)
        self.btn_view_4.setChecked(True)
        self.btn_view_5.setChecked(False)
        self.btn_view_6.setChecked(False)
        if self.image is not None:
            self.window_left_down()
            self.show_to_window()

    def window_down(self):
        self.normal_view = False
        self.single_view = True
        self.multiple_view = False
        self.window = 5
        moildev = MoilUtils.connectToMoildev(self.type_camera)
        self.mapX_5, self.mapY_5, = moildev.getAnypointMaps(-70, 0,
                                                            self.zoom_any,
                                                            self.anypoint_mode)

    def onclick_window_down(self):
        self.btn_ori_view.setChecked(False)
        self.btn_6view.setChecked(False)
        self.btn_view_1.setChecked(False)
        self.btn_view_2.setChecked(False)
        self.btn_view_3.setChecked(False)
        self.btn_view_4.setChecked(False)
        self.btn_view_5.setChecked(True)
        self.btn_view_6.setChecked(False)
        if self.image is not None:
            self.window_down()
            self.show_to_window()

    def window_right_down(self):
        self.normal_view = False
        self.single_view = True
        self.multiple_view = False
        self.window = 6
        moildev = MoilUtils.connectToMoildev(self.type_camera)
        self.mapX_6, self.mapY_6, = moildev.getAnypointMaps(-45, 50,
                                                            self.zoom_any,
                                                            self.anypoint_mode)

    def onclick_window_right_down(self):
        self.btn_ori_view.setChecked(False)
        self.btn_6view.setChecked(False)
        self.btn_view_1.setChecked(False)
        self.btn_view_2.setChecked(False)
        self.btn_view_3.setChecked(False)
        self.btn_view_4.setChecked(False)
        self.btn_view_5.setChecked(False)
        self.btn_view_6.setChecked(True)
        if self.image is not None:
            self.window_right_down()
            self.show_to_window()

    def mouse_window_l(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.onclick_window_left()

    def mouse_window_m(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.onclick_window_middle()

    def mouse_window_r(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.onclick_window_right()

    def mouse_window_ld(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.onclick_window_left_down()

    def mouse_window_d(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.onclick_window_down()

    def mouse_window_rd(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.onclick_window_right_down()

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
        height = MoilUtils.calculateHeight(self.image, 200)
        self.listWidget.setIconSize(QtCore.QSize(200, height))
        new_widget = QtWidgets.QListWidgetItem()

        image_ = MoilUtils.resizeImage(image_save, 200)
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

    @classmethod
    def onclick_help(cls):
        """
        Showing the message box to show help information obout this application.

        """
        Help.about_us()

    def show_to_window(self):
        """
        Showing the processing result image into the frame UI.

        """
        global image, image_ori
        if self.normal_view:
            MoilUtils.showImageToLabel(self.label_Original_image,
                                       self.image,
                                       self.width_result_image, self.angle)

        elif self.multiple_view:
            self.frame_2.hide()
            self.scrollArea.hide()
            self.listWidget.hide()
            self.label_3.hide()
            self.scrollArea_3.show()
            image_1 = cv2.remap(self.image.copy(), self.mapX_1, self.mapY_1, cv2.INTER_CUBIC)
            MoilUtils.showImageToLabel(self.label_image1, image_1, self.width_result_multi)
            image_2 = cv2.remap(self.image.copy(), self.mapX_2, self.mapY_2, cv2.INTER_CUBIC)
            MoilUtils.showImageToLabel(self.label_image2, image_2, self.width_result_multi)
            image_3 = cv2.remap(self.image.copy(), self.mapX_3, self.mapY_3, cv2.INTER_CUBIC)
            MoilUtils.showImageToLabel(self.label_image3, image_3, self.width_result_multi)
            image_4 = cv2.remap(self.image.copy(), self.mapX_4, self.mapY_4, cv2.INTER_CUBIC)
            MoilUtils.showImageToLabel(self.label_image4, image_4, self.width_result_multi)
            image_5 = cv2.remap(self.image.copy(), self.mapX_5, self.mapY_5, cv2.INTER_CUBIC)
            MoilUtils.showImageToLabel(self.label_image5, image_5, self.width_result_multi)
            image_6 = cv2.remap(self.image.copy(), self.mapX_6, self.mapY_6, cv2.INTER_CUBIC)
            MoilUtils.showImageToLabel(self.label_image6, image_6, self.width_result_multi)

        elif self.single_view:
            self.frame_2.show()
            self.scrollArea.show()
            self.listWidget.show()
            self.label_3.show()
            self.scrollArea_3.hide()
            if self.window == 1:
                self.image_result = cv2.remap(self.image.copy(), self.mapX_1, self.mapY_1, cv2.INTER_CUBIC)
                image_ori = MoilUtils.drawPolygon(self.image.copy(), self.mapX_1, self.mapY_1)
            elif self.window == 2:
                self.image_result = cv2.remap(self.image.copy(), self.mapX_2, self.mapY_2, cv2.INTER_CUBIC)
                image_ori = MoilUtils.drawPolygon(self.image.copy(), self.mapX_2, self.mapY_2)
            elif self.window == 3:
                self.image_result = cv2.remap(self.image.copy(), self.mapX_3, self.mapY_3, cv2.INTER_CUBIC)
                image_ori = MoilUtils.drawPolygon(self.image.copy(), self.mapX_3, self.mapY_3)
            elif self.window == 4:
                self.image_result = cv2.remap(self.image.copy(), self.mapX_4, self.mapY_4, cv2.INTER_CUBIC)
                image_ori = MoilUtils.drawPolygon(self.image.copy(), self.mapX_4, self.mapY_4)
            elif self.window == 5:
                self.image_result = cv2.remap(self.image.copy(), self.mapX_5, self.mapY_5, cv2.INTER_CUBIC)
                image_ori = MoilUtils.drawPolygon(self.image.copy(), self.mapX_5, self.mapY_5)
            elif self.window == 6:
                self.image_result = cv2.remap(self.image.copy(), self.mapX_6, self.mapY_6, cv2.INTER_CUBIC)
                image_ori = MoilUtils.drawPolygon(self.image.copy(), self.mapX_6, self.mapY_6)

            result = MoilUtils.drawLine(self.image_result)
            MoilUtils.showImageToLabel(self.label_Original_image,
                                       result,
                                       self.width_result_image, self.angle)
            MoilUtils.showImageToLabel(self.label,
                                       image_ori,
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
            if self.multiple_view:
                pass
            else:
                self.coombo_zoom.removeItem(8)
                percent = self.coombo_zoom.currentText()
                percent = int(percent.replace("%", ""))
                print(percent)
                self.width_result_image = round((self.w * percent) / 100)
                print(self.width_result_image)
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
                                          "m\t: Multiple View\n"
                                          "1\t: Open View 1\n"
                                          "2\t: Open View 2\n"
                                          "3\t: Open View 3\n"
                                          "4\t: Open View 4\n"
                                          "5\t: Open View 5\n"
                                          "6\t: Open View 6\n"

                                          "Ctrl+Shift+/\t:show help\n\n")
