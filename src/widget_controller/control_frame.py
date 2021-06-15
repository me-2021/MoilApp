
class FrameWidgets(object):
    def __init__(self, mainwindow):
        self.parent = mainwindow
        self.parent.actionMaximize.triggered.connect(self.maximize_view)
        self.parent.actionMinimize.triggered.connect(self.minimize_view)
        self.parent.button_menu.clicked.connect(self.control_frame_view_button)

    def control_frame_view_button(self):
        """
        control the button in anypoint and panorama mode.

        """
        # print(self.button_menu.isChecked())
        if self.parent.button_menu.isChecked():
            if self.parent.anypoint_view:
                self.parent.frame_navigator.hide()
            elif self.parent.panorama_view:
                self.parent.frame_panorama.hide()
            else:
                print("coming soon")
        else:
            if self.parent.anypoint_view:
                self.parent.frame_navigator.show()
            elif self.parent.panorama_view:
                self.parent.frame_panorama.show()
            else:
                print("coming soon")

    def maximize_view(self):
        """
        Control the widget on user interface to make possible in maximum size.

        """
        self.parent.label_saved_image.hide()
        self.parent.listWidget.hide()
        self.parent.frame_original_image.hide()
        self.parent.frame_help.hide()
        self.parent.frame_feature.hide()
        self.parent.frame_2.hide()
        self.parent.frame_Open_Source.hide()
        self.parent.frame_rotate.hide()
        self.parent.frame_zoom.hide()
        self.parent.frame_save.hide()
        self.parent.label_Application.hide()
        self.parent.frame_13.hide()
        self.parent.frame_16.hide()
        self.parent.frame_17.hide()
        self.parent.frame_18.hide()
        self.parent.label_time_recent.hide()
        self.parent.slider_Video.hide()
        self.parent.label_time_end.hide()
        self.parent.frame_apps.hide()

    def minimize_view(self):
        """
        Control the widget on user interface to make possible in minimum size.

        """
        self.parent.label_saved_image.show()
        self.parent.listWidget.show()
        self.parent.frame_original_image.show()
        self.parent.frame_help.show()
        self.parent.frame_feature.show()
        self.parent.frame_2.show()
        self.parent.frame_Open_Source.show()
        self.parent.frame_rotate.show()
        self.parent.frame_zoom.show()
        self.parent.frame_save.show()
        self.parent.label_Application.show()
        self.parent.frame_13.show()
        self.parent.frame_16.show()
        self.parent.frame_17.show()
        self.parent.frame_18.show()
        self.parent.label_time_recent.show()
        self.parent.slider_Video.show()
        self.parent.label_time_end.show()
        self.parent.frame_apps.show()