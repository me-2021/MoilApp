#########################################################################
#   MoilApp (Applications for sophisticated fisheye image processing)   #
#   Written by Haryanto (haryanto@o3635.mcut.edu.tw)                    #
#   Based on Moil-Lab (Ming Chi University of Technology)               #
#########################################################################
import cv2
import datetime
import numpy as np
from help import Help
from PyQt5 import QtWidgets, QtGui, QtCore
from moilutils.moilutils import MoilUtils
from plugin_controller import PluginController
from camera_source import CameraSource
from Ui_Moilapp import Ui_MainWindow
from panorama import Panorama
from anypoint import Anypoint
from control_view import ManipulateView
from event_controller import MouseEvent
from camera_parameter import CameraParameters
from video_controller import VideoController


class Controller(Ui_MainWindow):
    resized = QtCore.pyqtSignal()

    def __init__(self, parent):
        """

        Args:
            parent ():
        """
        super().__init__(parent)
        self.comboBox_cam_type = None
        self.parent = parent
        self.setupUi(self.parent)
        self.open_plugin = False
        self.image = None
        self.cap = None
        self.cam = False
        self.normal_view = True
        self.panorama_view = False
        self.anypoint_view = False
        self.axis_controller = False
        self.dir_save = None
        self.mapX = None
        self.mapY = None
        self.mapX_pano = None
        self.mapY_pano = None
        self.zoom_area = False
        self.type_camera = "Raspi"
        self.num = 0
        self.pos_x = 0
        self.w = 0
        self.h = 0
        self.point = None
        self.result_image = None
        self.width_original_image = 300
        self.width_result_image = 1080
        self.angle = 0

        self.openCam = QtWidgets.QDialog()
        self.winOpenCam = CameraSource(self, self.openCam)

        self.dialogHelp = QtWidgets.QDialog()
        self.winHelp = Help(self, self.dialogHelp)

        self.camParams = QtWidgets.QDialog()
        self.winCamParams = CameraParameters(self, self.camParams)
        self.video_controller = VideoController(self)
        self.panorama = Panorama(self)
        self.anypoint = Anypoint(self)
        self.control_mouse = MouseEvent(self)
        self.manipulate = ManipulateView(self)
        self.control_plugin = PluginController(self)

        self.video_controller.set_button_disable()
        self.frame_panorama.hide()
        self.frame_navigator.hide()
        # self.label_34.hide()
        self.connect_event()

    def connect_event(self):
        """
        Connect every event on user interface like button event, mouse event
        and etc to the function processing.

        """
        # action from menubar
        self.parent.closeEvent = self.closeEvent
        self.parent.resizeEvent = self.resizeEvent
        self.actionExit.triggered.connect(self.onclick_exit)
        self.actionLoad_Image.triggered.connect(self.open_image)
        self.actionLoad_Video.triggered.connect(self.onclick_load_video)
        self.actionOpen_Cam.triggered.connect(self.onclick_open_camera)
        self.actionCamera_Parameters.triggered.connect(self.cam_params_window)
        self.actionSave_Image.triggered.connect(self.save_image)
        self.action_accessibility.triggered.connect(self.onclick_accessibility)
        self.comboBox_zoom.activated.connect(self.combo_percentage_zoom)

        # connect button to function
        self.btn_Open_Image.clicked.connect(self.open_image)
        self.btn_Open_Video.clicked.connect(self.onclick_load_video)
        self.btn_Open_Cam.clicked.connect(self.onclick_open_camera)
        self.btn_Save_Image.clicked.connect(self.save_image)
        self.btn_normal.clicked.connect(self.onclick_view_normal)
        self.listWidget.currentItemChanged.connect(self.saved_image_activated)
        self.btn_show_help.clicked.connect(self.onclick_help)
        self.pushButton_29.clicked.connect(Help.about_us)
        self.pushButton_18.clicked.connect(self.onclick_help_moil)
        self.actionAbout_Apps.triggered.connect(Help.help_moilApp)
        self.actionCreatePlugins.triggered.connect(Help.help_create_plugin)
        self.actionAbout_Us.triggered.connect(Help.about_us)
        self.actionHelpPlugins.triggered.connect(Help.help_plugin)
        self.actionMaximize.triggered.connect(self.maximize_view)
        self.actionMinimize.triggered.connect(self.minimize_view)
        self.button_menu.clicked.connect(self.control_frame_view_button)

        self.btn_play_pouse.clicked.connect(self.video_controller.onclick_play_pause_button)
        self.btn_stop_video.clicked.connect(self.video_controller.stop_video)
        self.btn_prev_video.clicked.connect(self.video_controller.prev_video)
        self.btn_skip_video.clicked.connect(self.video_controller.skip_video)
        self.actionRecord_video.triggered.connect(self.video_controller.action_record_video)
        self.btn_Record_video.clicked.connect(self.video_controller.recordVideo)
        self.slider_Video.valueChanged.connect(self.video_controller.changeValueSlider)

        self.btn_Rotate_Left.clicked.connect(self.manipulate.rotate_left)
        self.btn_Rotate_Right.clicked.connect(self.manipulate.rotate_right)
        self.btn_Zoom_in.clicked.connect(self.manipulate.zoom_in)
        self.btn_Zoom_out.clicked.connect(self.manipulate.zoom_out)
        self.btn_clear.clicked.connect(self.onclick_clear)

    def onclick_clear(self):
        if self.cam:
            self.video_controller.stop_video()
            self.cap.release()
            self.video_controller.set_button_disable()
        self.label_Result_Image.clear()
        self.label_Result_Image.setMaximumSize(QtCore.QSize(1080, 810))
        self.label_Result_Image.setMinimumSize(QtCore.QSize(1080, 810))
        self.label_Original_Image.clear()
        self.reset_mode_view()
        self.comboBox_zoom.removeItem(8)
        self.comboBox_zoom.setCurrentIndex(0)
        self.label_Application.setText("MoilApp")
        self.parent.setWindowTitle("MoilApp")
        self.image = None

    def open_image(self):
        """
        Open Dialog to search the file image from directory. This function also will read the comment from
        metadata image.

        """
        filename = MoilUtils.selectFile(self.parent, "Image Files", "../SourceImage", "(*.jpeg *.jpg *.png *.gif "
                                                                                      "*.bmg)")
        if filename:
            self.reset_mode_view()
            if self.cam:
                self.video_controller.stop_video()
                self.cap.release()
            self.parent.setWindowTitle("MoilApp - " + filename)
            self.type_camera = MoilUtils.readCameraType(filename)
            # print(self.type_camera)
            self.image = MoilUtils.readImage(filename)
            self.h, self.w = self.image.shape[:2]
            self.video_controller.set_button_disable()
            self.show_to_window()
            self.show_percentage()
            self.cam = False
            self.label_Application.setText("Camera: " + self.type_camera)

    def onclick_load_video(self):
        """
        Open Dialog to search video file from Directory. after you select the video file, it will show the prompt
        to select the type of camera.

        """
        video_source = MoilUtils.selectFile(self.parent,
                                            "Select Video Files",
                                            "../",
                                            "Video Files (*.mp4 *.avi *.mpg *.gif *.mov)")
        if video_source:
            self.reset_mode_view()
            self.type_camera = MoilUtils.selectCameraType()
            if self.type_camera is not None:
                self.parent.setWindowTitle("MoilApp - " + video_source)
                self.label_Application.setText("Camera: " + self.type_camera)
                self.running_video(video_source)

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
        self.reset_mode_view()
        camera_source = self.winOpenCam.camera_source_used()
        self.type_camera = MoilUtils.selectCameraType()
        if self.type_camera is not None:
            self.parent.setWindowTitle("MoilApp - " + self.type_camera)
            self.label_Application.setText("Camera: " + self.type_camera)
            self.running_video(camera_source)

    def running_video(self, video_source):
        """
        Open Video following the source given.

        Args:
            video_source (): the source of media, can be camera and video file.

        """
        self.video_controller.set_button_enable()
        self.cap = cv2.VideoCapture(video_source)
        success, self.image = self.cap.read()
        if success:
            self.h, self.w = self.image.shape[:2]
            self.cam = True
            self.video_controller.next_frame_slot()
            self.show_percentage()
        else:
            QtWidgets.QMessageBox.information(self.parent, "Information", "No source camera founded")

    def cam_params_window(self):
        """
        Open the window of camera parameter form, this window you can update, add, and
        delete the camera parameter from database.

        """
        self.camParams.show()

    def onclick_view_normal(self):
        """
        Showing the original image into Label frame in UI.

        """
        if self.image is not None:
            self.reset_mode_view()
            self.normal_view = True
            self.panorama_view = False
            self.anypoint_view = False
            self.angle = 0
            self.show_to_window()
            self.frame_navigator.hide()
            self.frame_panorama.hide()
            self.show_percentage()
            self.status_alpha.setText("Alpha: 0")
            self.status_beta.setText("Beta: 0")

    def show_to_window(self):
        """
        Showing the processing result image into the frame UI.

        """
        self.zoom_area = False
        image = self.image.copy()
        h, w = image.shape[:2]
        radius = 6 if self.h < 800 else 10
        if self.normal_view:
            self.point = (round(w / 2), round(h / 2))
            image = MoilUtils.drawPoint(image, self.point, radius)
            MoilUtils.showImageToLabel(self.label_Original_Image,
                                       image,
                                       self.width_original_image)
            MoilUtils.showImageToLabel(self.label_Result_Image,
                                       self.image,
                                       self.width_result_image, self.angle, plusIcon=True)

        elif self.panorama_view:
            # image = MoilUtils.draw_polygon(
            #     self.image.copy(),
            #     self.mapX_pano,
            #     self.mapY_pano)
            mapX = np.load(
                './maps_pano/mapX.npy')
            mapY = np.load(
                './maps_pano/mapY.npy')
            # rho = self.panorama.rho

            self.result_image = cv2.remap(
                self.image.copy(),
                mapX,
                mapY,
                cv2.INTER_CUBIC)
            # self.result_image = self.result_image[round(rho):self.h, 0:self.w]
            # print(self.result_image)
            image = MoilUtils.drawPoint(image, self.point, radius)
            MoilUtils.showImageToLabel(self.label_Original_Image,
                                       image,
                                       self.width_original_image)
            MoilUtils.showImageToLabel(self.label_Result_Image,
                                       self.result_image,
                                       self.width_result_image, self.angle)

        else:
            image = MoilUtils.drawPolygon(self.image.copy(), self.mapX, self.mapY)
            image = MoilUtils.drawPoint(image, self.point, radius)
            self.result_image = cv2.remap(
                self.image,
                self.mapX,
                self.mapY,
                cv2.INTER_CUBIC)
            result = MoilUtils.drawLine(self.result_image.copy())
            MoilUtils.showImageToLabel(self.label_Result_Image,
                                       result,
                                       self.width_result_image, self.angle, plusIcon=True)
            MoilUtils.showImageToLabel(self.label_Original_Image,
                                       image,
                                       self.width_original_image)

    def save_image(self):
        """
        Save image into local directory, it can save original image or
        result image from panorama or anypoint processing.

        """
        if self.image is not None:
            image = self.image if self.normal_view else self.result_image
            if self.dir_save is None or self.dir_save == "":
                self.video_controller.pause_video()
                self.dir_save = MoilUtils.selectDirectory(self)
            if self.dir_save:
                self.name_saved = MoilUtils.saveImage(image, self.dir_save, self.type_camera)
                self.addWidget(image)
                QtWidgets.QMessageBox.information(
                    self.parent, "Information", "Image saved !!\n\nLoc @: " + self.dir_save)

    def addWidget(self, image):
        """
        Add the image widget in the list widget_controller of saved image. it can be reopen when you select.
        Args:
            image (): the image saved.

        """
        height = MoilUtils.calculateHeight(self.image, 140)
        self.listWidget.setIconSize(QtCore.QSize(140, height))
        new_widget = QtWidgets.QListWidgetItem()

        image_ = MoilUtils.resizeImage(image, 140)
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

    def saved_image_activated(self):
        """
        Function that for connect with the event in list widget to reopen the image.

        """
        filename = self.dir_save + "/" + self.listWidget.currentItem().text()
        self.type_camera = MoilUtils.readCameraType(filename)
        if self.cam:
            self.video_controller.pause_video()
            self.reset_mode_view()
            self.image = MoilUtils.readImage(filename)
            self.h, self.w = self.image.shape[:2]
            self.show_to_window()
            if self.listWidget.count() == 1:
                self.listWidget.selectionModel().reset()

    def cropImage(self, rect):
        image = self.convertCv2ToQimage(self.image.copy()) if self.result_image is None \
            else self.convertCv2ToQimage(self.result_image.copy())
        height = MoilUtils.calculateHeight(self.image, self.width_result_image)
        ratio_x = self.w / self.width_result_image
        ratio_y = self.h / height
        x = rect.x() * ratio_x
        y = rect.y() * ratio_y
        width = rect.width() * ratio_x
        height = rect.height() * ratio_y
        rect = QtCore.QRect(x, y, width, height)
        croppedImage = image.copy(rect)
        point_1 = (round(x), round(y))
        point_2 = (round(x + width), round(y + height))
        ori_image = self.image.copy() if self.normal_view else self.result_image.copy()
        image = MoilUtils.drawRectangle(ori_image, point_1, point_2)
        return image, self.convertQImageToMat(croppedImage)

    @classmethod
    def convertCv2ToQimage(cls, im):
        qim = QtGui.QImage()
        if im is None:
            return qim
        if im.dtype == np.uint8:
            if len(im.shape) == 2:
                qim = QtGui.QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QtGui.QImage.Format_Indexed8)
                qim.setColorTable([QtGui.qRgb(i, i, i) for i in range(256)])
            elif len(im.shape) == 3:
                if im.shape[2] == 3:
                    qim = QtGui.QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QtGui.QImage.Format_RGB888)
                elif im.shape[2] == 4:
                    qim = QtGui.QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QtGui.QImage.Format_ARGB32)
        return qim

    @classmethod
    def convertQImageToMat(cls, incomingImage):
        """  Converts a QImage into an opencv MAT format  """
        incomingImage = incomingImage.convertToFormat(4)
        width = incomingImage.width()
        height = incomingImage.height()
        ptr = incomingImage.bits()
        ptr.setsize(incomingImage.byteCount())
        arr = np.array(ptr).reshape(height, width, 4)  # Copies the data
        return cv2.cvtColor(arr, cv2.COLOR_BGR2RGB)

    def show_percentage(self):
        count = self.comboBox_zoom.count()
        if count == 8:
            self.comboBox_zoom.addItem("")
        self.comboBox_zoom.setCurrentIndex(8)
        size = round((self.width_result_image / self.w) * 100)
        self.comboBox_zoom.setItemText(8, (str(size) + "%"))

    def combo_percentage_zoom(self):
        if self.image is not None:
            self.comboBox_zoom.removeItem(8)
            percent = self.comboBox_zoom.currentText()
            percent = int(percent.replace("%", ""))
            self.width_result_image = round((self.w * percent) / 100)
            self.show_to_window()

    def reset_mode_view(self):
        """
        Update the properties widget_controller when you reset.

        """
        self.result_image = None
        self.width_result_image = 1080
        self.normal_view = True
        self.anypoint.resetAlphaBeta()
        self.btn_Record_video.setChecked(False)
        self.frame_navigator.hide()
        self.frame_panorama.hide()

    def control_frame_view_button(self):
        """
        control the button in anypoint and panorama mode.

        """
        # print(self.button_menu.isChecked())
        if self.button_menu.isChecked():
            if self.anypoint_view:
                self.frame_navigator.hide()
                # self.label_34.hide()
            elif self.panorama_view:
                self.frame_panorama.hide()
                # self.label_34.hide()
            else:
                print("coming soon")
        else:
            if self.anypoint_view:
                self.frame_navigator.show()
                # self.label_34.show()
            elif self.panorama_view:
                self.frame_panorama.show()
            else:
                print("coming soon")

    def maximize_view(self):
        """
        Control the widget on user interface to make possible in maximum size.

        """
        self.label_saved_image.hide()
        self.listWidget.hide()
        self.frame_original_image.hide()
        self.frame_help.hide()
        self.frame_feature.hide()
        self.frame_2.hide()
        self.frame_Open_Source.hide()
        self.frame_rotate.hide()
        self.frame_zoom.hide()
        self.frame_save.hide()
        self.label_Application.hide()
        self.frame_13.hide()
        self.frame_16.hide()
        self.frame_17.hide()
        self.frame_18.hide()
        self.label_time_recent.hide()
        self.slider_Video.hide()
        self.label_time_end.hide()
        self.frame_apps.hide()
        self.frame_clear.hide()
        self.statusbar.hide()

    def minimize_view(self):
        """
        Control the widget on user interface to make possible in minimum size.

        """
        self.label_saved_image.show()
        self.listWidget.show()
        self.frame_original_image.show()
        self.frame_help.show()
        self.frame_feature.show()
        self.frame_2.show()
        self.frame_Open_Source.show()
        self.frame_rotate.show()
        self.frame_zoom.show()
        self.frame_save.show()
        self.label_Application.show()
        self.frame_13.show()
        self.frame_16.show()
        self.frame_17.show()
        self.frame_18.show()
        self.label_time_recent.show()
        self.slider_Video.show()
        self.label_time_end.show()
        self.frame_apps.show()
        self.frame_clear.show()
        self.statusbar.show()

    def onclick_accessibility(self):
        """
        Open prompt for accessibility MoilApp
        Returns:

        """
        QtWidgets.QMessageBox.information(
            self.parent, "Accessibility", "MoilApp Accessibility\n\n"
                                          "Information !!\n"
                                          "Crtl + I\t: Open Image\n"
                                          "Ctrl + V\t: Open Video\n"
                                          "Ctrl + C\t: Open cam\n"
                                          "= \t: Zoom In\n"
                                          "- \t: Zoom Out\n"
                                          "Ctrl + Left\t: Prev video\n"
                                          "Space\t: play/pause video\n"
                                          "0 \t: Stop video\n"
                                          "Ctrl+Right\t: skip video\n"
                                          "Up\t: Up View\n"
                                          "Right\t: Right view\n"
                                          "Left\t: Left view\n"
                                          "Down\t: Down View\n"
                                          "Ctrl+Shift+/\t:show help\n\n")

    @classmethod
    def onclick_help(cls):
        """
        Showing the message box to show help information obout this application.

        """
        Help.help_moilApp()

    def onclick_help_moil(self):
        self.dialogHelp.show()

    def onclick_exit(self):
        """

        Returns:

        """
        self.parent.close()

    def closeEvent(self, event):
        """
        Control the close event by ask the question yes or no.
        Args:
            event ():

        Returns:

        """
        if self.cam:
            self.video_controller.pause_video()
        reply = QtWidgets.QMessageBox.question(
            self.parent,
            'Message',
            "Are you sure to quit?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            if self.open_plugin:
                for i in range(len(self.control_plugin.plugins.name_application)):
                    self.control_plugin.plugin_win[i].close()
            self.openCam.close()
            self.camParams.close()
            if self.cam:
                self.cap.release()
            event.accept()
        else:
            event.ignore()
