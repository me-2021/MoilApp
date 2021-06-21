#########################################################################
#   MoilApp (Applications for sophisticated fisheye image processing)   #
#   Written by Haryanto (haryanto@o3635.mcut.edu.tw)                    #
#   Based on Moil-Lab (Ming Chi University of Technology)               #
#########################################################################
import numpy as np
import cv2
from PyQt5 import QtWidgets, QtGui, QtCore
import datetime
from moilutils.moilutils import MoilUtils
from help.help import Help
from plugin_controller import PluginController
from Exif.exif_lib import MetaImage
from moilutils.select_source_camera import OpenCameraSource
from user_interface.Ui_MainWindow import Ui_MainWindow
from processing.panorama import PanoramaView
from widget_controller.manipulate_view import ManipulateView
from widget_controller.control_frame import FrameWidgets
from widget_controller.mouse_control_event import MouseController
from moilutils.camera_parameters import CameraParameters
from video_controller import VideoController


class Controller(Ui_MainWindow):
    resized = QtCore.pyqtSignal()

    def __init__(self, parent):
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
        self.type_camera = "Raspi"
        self.num = 0
        self.pos_x = 0
        self.w = 0
        self.h = 0
        self.point = None
        self.result_image = None
        self.width_original_image = 300
        self.width_result_image = 1400
        self.angle = 0
        self.connect_event()

        self.openCam = QtWidgets.QDialog()
        self.winOpenCam = OpenCameraSource(self, self.openCam)

        self.camParams = QtWidgets.QDialog()
        self.winCamParams = CameraParameters(self, self.camParams)
        self.video_controller = VideoController(self)
        self.panorama = PanoramaView(self)
        self.control_mouse = MouseController(self)
        self.manipulate = ManipulateView(self)
        self.control_frame = FrameWidgets(self)
        self.control_plugin = PluginController(self)

        self.video_controller.set_button_disable()
        self.frame_panorama.hide()
        self.frame_navigator.hide()
        self.label_34.hide()

    def connect_event(self):
        """
        Connect every event on user interface like button event, mouse event
        and etc to the function processing.

        """
        # action from menubar
        self.parent.closeEvent = self.closeEvent
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
        self.pushButton_18.clicked.connect(Help.open_user_guide_moildev)
        self.actionAbout_Apps.triggered.connect(Help.help_moilApp)
        self.actionCreatePlugins.triggered.connect(Help.help_create_plugin)
        self.actionAbout_Us.triggered.connect(Help.about_us)
        self.actionHelpPlugins.triggered.connect(Help.help_plugin)

    def open_image(self):
        """
        Open Dialog to search the file image from directory. This function also will read the comment from
        metadata image.

        """
        self.reset_mode_view()
        if self.cam:
            self.video_controller.stop_video()
            self.cap.release()
        filename = MoilUtils.select_file(self.parent, "Image Files", "../SourceImage", "(*.jpeg *.jpg *.png *.gif "
                                                                                       "*.bmg)")
        if filename:
            self.parent.setWindowTitle("MoilApp - " + filename)
            img = MetaImage(filename)
            self.type_camera = img.read_comment()
            print(self.type_camera)
            self.image = MoilUtils.read_image(filename)
            self.h, self.w = self.image.shape[:2]
            self.video_controller.set_button_disable()
            self.show_to_window()
            self.show_percentage()
            self.cam = False
            self.label_Application.setText("Camera: " + self.type_camera)
            img.close()

    def onclick_load_video(self):
        """
        Open Dialog to search video file from Directory. after you select the video file, it will show the prompt
        to select the type of camera.

        """
        self.reset_mode_view()
        video_source = MoilUtils.select_file(self.parent,
                                             "Select Video Files",
                                             "../",
                                             "Video Files (*.mp4 *.avi *.mpg *.gif *.mov)")
        if video_source:
            self.type_camera = MoilUtils.select_camera_type()
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
        self.type_camera = MoilUtils.select_camera_type()
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
        success, image = self.cap.read()
        self.w = image.shape[1]
        if success:
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
            self.normal_view = True
            self.panorama_view = False
            self.anypoint_view = False
            self.angle = 0
            self.show_to_window()
            self.frame_navigator.hide()
            self.label_34.hide()
            self.frame_panorama.hide()
            self.show_percentage()

    def show_to_window(self):
        """
        Showing the processing result image into the frame UI.

        """
        image = self.image.copy()
        if self.normal_view:
            self.point = (round(self.w / 2), round(self.h / 2))
            image = MoilUtils.drawPoint(image, self.point)
            MoilUtils.showing_original_image(self.label_Original_Image,
                                             image,
                                             self.width_original_image)
            MoilUtils.showing_result_image(self.label_Result_Image,
                                           self.image,
                                           self.width_result_image, self.angle)

        else:
            if self.panorama_view:
                # image = MoilUtils.draw_polygon(
                #     self.image.copy(),
                #     self.mapX_pano,
                #     self.mapY_pano)
                mapX = np.load(
                    './processing/maps_pano/mapX.npy')
                mapY = np.load(
                    './processing/maps_pano/mapY.npy')
                # rho = self.panorama.rho

                self.result_image = cv2.remap(
                    self.image,
                    mapX,
                    mapY,
                    cv2.INTER_CUBIC)
                # self.result_image = self.result_image[round(rho):self.h, 0:self.w]
                # print(self.result_image)
                # image = MoilUtils.drawPoint(image, point)
                MoilUtils.showing_original_image(self.label_Original_Image,
                                                 image,
                                                 self.width_original_image)
            else:
                image = MoilUtils.draw_polygon(self.image.copy(), self.mapX, self.mapY)
                image = MoilUtils.drawPoint(image, self.point)
                self.result_image = cv2.remap(
                    self.image,
                    self.mapX,
                    self.mapY,
                    cv2.INTER_CUBIC)
                MoilUtils.showing_original_image(self.label_Original_Image,
                                                 image,
                                                 self.width_original_image)
            MoilUtils.showing_result_image(self.label_Result_Image,
                                           self.result_image,
                                           self.width_result_image, self.angle)

    def save_image(self):
        """
        Save image into local directory, it can save original image or
        result image from panorama or anypoint processing.

        """
        if self.image is not None:
            image = self.image if self.normal_view else self.result_image
            if self.dir_save is None or self.dir_save == "":
                self.dir_save = MoilUtils.selectDir(self)
            if self.dir_save:
                MoilUtils.save_image(image, self.dir_save, self.type_camera)
                self.addWidget(image)
                QtWidgets.QMessageBox.information(
                    self.parent, "Information", "Image saved !!\n\nLoc @: " + self.dir_save)

    def addWidget(self, image):
        """
        Add the image widget in the list widget_controller of saved image. it can be reopen when you select.
        Args:
            image (): the image saved.

        """
        height = MoilUtils.calculate_height(self.image, 140)
        self.listWidget.setIconSize(QtCore.QSize(140, height))
        new_widget = QtWidgets.QListWidgetItem()

        image_ = MoilUtils.resize_image(image, 140)
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
            self.reset_mode_view()
            self.image = MoilUtils.read_image(filename)
            self.h, self.w = self.image.shape[:2]
            img.close()
            self.show_to_window()

    def cropImage(self, rect):
        if self.result_image is None:
            image = self.convertCv2ToQimage(self.image.copy())
        else:
            image = self.convertCv2ToQimage(self.result_image.copy())
        ratio_x = self.w / self.label_Result_Image.width()
        ratio_y = self.h / self.label_Result_Image.height()
        x = rect.x() * ratio_x
        y = rect.y() * ratio_y
        width = rect.width() * ratio_x
        height = rect.height() * ratio_y
        rect = QtCore.QRect(x, y, width, height)
        croppedImage = image.copy(rect)
        return self.convertQImageToMat(croppedImage)

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
        # self.comboBox_zoom.addItem((str(size) + "%"))
        self.comboBox_zoom.setItemText(8, (str(size) + "%"))

    def combo_percentage_zoom(self):
        self.comboBox_zoom.removeItem(8)
        percent = self.comboBox_zoom.currentIndex()
        if percent == 0:
            print("here")
            self.width_result_image = round((self.w * 25) / 100)
            print(self.width_result_image)
        elif percent == 1:
            self.width_result_image = round((self.w * 50) / 100)
        elif percent == 2:
            self.width_result_image = round((self.w * 75) / 100)
        elif percent == 3:
            self.width_result_image = round((self.w * 100) / 100)
        elif percent == 4:
            self.width_result_image = round((self.w * 125) / 100)
        elif percent == 5:
            self.width_result_image = round((self.w * 150) / 100)
        elif percent == 6:
            self.width_result_image = round((self.w * 175) / 100)
        elif percent == 7:
            self.width_result_image = round((self.w * 200) / 100)
        else:
            pass
        # print(self.width_result_image)
        self.show_to_window()

    def reset_mode_view(self):
        """
        Update the properties widget_controller when you reset.

        """
        self.normal_view = True
        self.btn_Record_video.setChecked(False)

    def onclick_accessibility(self):
        """
        Open prompt for accessibility MoilApp
        Returns:

        """
        QtWidgets.QMessageBox.information(
            self.parent, "Accessibility", "MoilApp Accessibility\n"
                                          "Please connect to your devices and input your password\n\n"
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
            event.accept()
        else:
            event.ignore()
