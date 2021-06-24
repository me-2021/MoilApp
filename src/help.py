from help_source.ui_help import Ui_Help
from help_source import help_moilapp
import webbrowser
from PyQt5 import QtWidgets, QtGui


class Help(Ui_Help):
    def __init__(self, MainWindow, recentWindow):
        """
         >> Main window is the the inheritance from the main UI this program
         >> Recent window is the UI for this window.
         this make it possible to communication between this two UI
        """

        self.parent_win = MainWindow
        self.parent_dialog = recentWindow

        self.setupUi(self.parent_dialog)
        self.eventButton()
        self.listWidget.setCurrentRow(0)
        self.selectItem()

    @classmethod
    def open_user_guide_moildev(cls):
        # file = os.path.realpath('./plugins/Thread_inspection/help/index.html')
        # print(file)
        # webbrowser.open('file://' + file)
        webbrowser.open('https://www.youtube.com/watch?v=irpWmNmgAz4')
        # self.dialogHelp.show()

    @classmethod
    def about_us(cls):
        """
        Showing prompt About us information (MOIL LAB).

        Returns:
            None.
        """
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("About Us")
        msgbox.setText(
            "MOIL \n\nOmnidirectional Imaging & Surveillance Lab\nMing Chi University of Technology\n")
        msgbox.setIconPixmap(QtGui.QPixmap('icon/moildev2.png'))
        msgbox.exec()

    @classmethod
    def help_create_plugin(cls):
        """
        Showing prompt About us information (MOIL LAB).

        Returns:
            None.
        """
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("Create Plugin")
        msgbox.setText(
            "Comming soon !!!!!!!!\n")
        msgbox.setIconPixmap(QtGui.QPixmap('icon/moildev2.png'))
        msgbox.exec()

    @classmethod
    def help_plugin(cls):
        """
        Showing prompt About us information (MOIL LAB).

        Returns:
            None.
        """
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("Help Plugin")
        msgbox.setText(
            "Comming soon !!!!!!!!\n")
        msgbox.setIconPixmap(QtGui.QPixmap('icon/moildev2.png'))
        msgbox.exec()

    @classmethod
    def help_moilApp(cls):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("About MoilApps")
        msgbox.setText(
            "Moildev-Apps\n\n"
            "Moildev-Apps is software to process fisheye "
            "image with the result panorama widget_controller and Anypoint"
            " widget_controller. \n\nThe panoramic widget_controller may present a horizontal"
            "widget_controller in a specific immersed environment to meet the"
            "common human visual perception, while the Anypoint"
            "widget_controller is an image that has been undistorted in a certain"
            "area according to the input coordinates."
            "\n\nMore reference about Moildev, contact us\n\n")
        msgbox.setIconPixmap(QtGui.QPixmap('icon/moildev2.png'))
        msgbox.exec()

    def eventButton(self):
        self.listWidget.itemSelectionChanged.connect(self.selectItem)

    def selectItem(self):
        apps = self.listWidget.currentItem().text()
        if apps == 'MoilApp':
            self.moilapp()
        elif apps == "Add-Ons":
            self.add_ons()
        elif apps == 'Multiple View':
            self.multiple_view()
        elif apps == "Axis Controller":
            self.axis_controller()
        elif apps == "Object Measurement":
            self.object_measurement()
        else:
            self.another()

    def moilapp(self):
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">MoilApp</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Moildev-Apps is a software to process fisheye image with the result panorama view and Anypoint view. The panoramic view may present a horizontal view in a specific immersed environment to meet the common human visual perception, while the Anypoint view is an image that has been undistorted in a certain area according to the input coordinates.</p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">In addition, this software is also developed for various applications in industry and vehicle security systems. images from anypoint and panoramic views will be further processed such as middle level and high-level processing.</p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/Moilapp/Moilapp.png\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Explanation</span>:</p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">MenuBar</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:24px;\">This is container stores various button     </p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\"><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">File</span>    </li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:2; text-indent:24px;\">File contains <span style=\" font-weight:600;\"> </span>Load image, Load video, Open cam, Cam Parameter, Record Video, Save Image, and Exit    </p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Window</span>    </li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:2; text-indent:24px;\">Window contains  Maximize and Minimize    </p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Apps</span>    </li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:2; text-indent:24px;\">Apps contains <span style=\" font-weight:600;\"> </span>Add, Open, Delete, Create and Help for Add-Ons    </p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Help</span>    </li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:2; text-indent:24px;\">Help contains<span style=\" font-weight:600;\">  </span>About Apps, About Us and Accesibility</p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Name of Application</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">This part will give information about app name </p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Source Button</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">The source button consists of 3 buttons, the first and second button are to Load Images and  Load Videos from the directory and the third button is to open the camera in real time which can choose USB Cam or Web Cam. </p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Rotate Button</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">Rotate your image right and left 10 degree</p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Zoom Button</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">Zoom in or Zoom out your image and provide information of zoom ratio percentage </p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Saving Button</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">Save Image and Record Video</p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Add-Ons</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">Add-Ons will provide information, install, remove and open Add-Ons application</p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Application Name/ Information  of Camera</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">This part will first show the name of the MoilApp application but when open the image it will change to camera information on the image used</p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">View Button</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">There are 3 view buttons, the first is Normal View which corresponds to the original image, Anypoint which point can see all sides of the image and Panorama which makes the image a panorama</p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Help Button</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">Help button will givr information about MoilApp and Moil-lab</p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Support Button</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">This button will show other tools that help in processing anypoint and panoramic images</p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Result window</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">Showing the resulting image after processing, this is the main image viewer </p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Image saved viewer</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">This will contain the image frame saved and allow to show it again in the result image viewer</p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Video Controller</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">This will contain some important tools for the video controller such as the previous button, play/pause button, skip button, stop button, slider time, and recent time viewer of the video</p>\n"
"<li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Original Image View</span></li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:50px;\">Showing the original image frame and keep it to show the difference before and after processing</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")



    def add_ons(self):
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Add-Ons</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Because the applications are very diverse, we implemented the Add-Ons framework so that users can choose the application according to their needs. Add-Ons are software components that add certain features to an existing computer program. To control MoilApp add-ons, features are provided as shown in the following image:</p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/Moilapp/addons.png\" /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Add-Ons</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">You can add as many add-ons as you want. You can also open it as many times as you need and can delete it again if you don\'t need it. Some examples of Add-Ons is:</p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Multiple View        </li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:24px;\">Display any point at once in six different views            </p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Axis Controller        </li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:24px;\">Move the tool to make it easier to take pictures or record videos            </p>\n"
"<li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Add other...    </li></ul></body></html>")

    def multiple_view(self):
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Multiple View</span></p>\n"
    "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
    "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Multiple View</span></p>\n"
    "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Multiple views will process images into 6 views at once so that it can facilitate the observation process and several other things such as the ADAS project.</p>\n"
    "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Original View Image</span></p>\n"
    "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Original view will only display the image according to the original image as shown below</p>\n"
    "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/Moilapp/multiori.png\" /></p>\n"
    "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Original View Image</p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Six View Image</span></p>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Six view will provide a view at the same time that includes:</p>\n"
    "<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Left View</li>\n"
    "<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Center View</li>\n"
    "<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Right View</li>\n"
    "<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Left BottomView</li>\n"
    "<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Bottom View</li>\n"
    "<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Right Bottom View</li></ol>\n"
    "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">You can also select the view directly by selecting the number or clicking the image in the window</p>\n"
    "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/Moilapp/multipleview2.png\" /></p>\n"
    "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Six AnyPoint View</p></body></html>")

    def axis_controller(self):
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Axis Controller</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Axis controller is a tool controller plugin that is useful in moving the camera that will take pictures or videos. </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">User Interface</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">User interface and functions are explained bellow:</p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/Moilapp/axis.png\" /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">User Interface of Axis Controller</p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Connect</li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Connect your application to device</p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Disconnect</li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Disconnect application with device</p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Help</li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Give information about Axis Controller Add-Ons</p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Reset All</li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Reset position become 0 and speed becamo 500 RPM</p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Backward</li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Backward 20 mm</p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Forward</li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Forward 20 mm</p>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Absolute Move</li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Window contains  Maximize and Minimize</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Device</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">The devices used are also specifically as in the following picture. These devices are prepared by MOIL-Lab. In this device consists of a specimen, a camera controlled by a raspberry pi, a power supply and a usb connected to the user labtop</p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/Moilapp/axis.jpg\" /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Device to Capture Image</p></body></html>")

    def object_measurement(self):
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Object Measurement</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">These add-ons allow us to <span style=\" font-weight:600;\">measure</span> an object size from images. It takes two cameras or two images to be able to use this feature. By determining the <span style=\" font-weight:600;\">points</span> to be measured from the two images, we can determine the size of the object. The user interface of this application is as shown in the following picture:</p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/Moilapp/Webp.net-resizeimage.png\" /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Measuring Object</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")

    def another(self):
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Moil-Lab</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Omnidirectional Imaging &amp; Surveillance Lab</p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ming Chi University of Technology</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">|</p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">|</p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">|</p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">|</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">if you have any questions please contact us</p></body></html>")