from moilutils.moilutils import MoilUtils


class AnypointView(object):
    def __init__(self, Parent):
        """
        The class for anypoint process.

        Args:
            Parent (): The Main class of this application
        """
        self.parent = Parent
        self.alpha = 0
        self.beta = 0
        self.zoom_any = 4
        self.anypoint_mode = 1
        self.moildev = None
        self.parent.radio_btn_mode_1.setChecked(True)
        self.parent.btn_anypoint.clicked.connect(self.process_to_anypoint)
        self.parent.btn_Up_View.clicked.connect(self.__up)
        self.parent.btn_Right_view.clicked.connect(self.__right)
        self.parent.btn_left_view.clicked.connect(self.__left)
        self.parent.btn_center_view.clicked.connect(self.__center)
        self.parent.btn_Down_view.clicked.connect(self.__down)
        self.parent.radio_btn_mode_1.clicked.connect(self.__anypoint_mode_1)
        self.parent.radio_btn_mode_2.clicked.connect(self.__anypoint_mode_2)
        # self.parent.lineedit_alpha_2.valueChanged.connect(self.process_to_anypoint)
        # self.parent.lineedit_beta_2.valueChanged.connect(self.process_to_anypoint)
        # self.parent.anypoint_zoom_2.valueChanged.connect(self.process_to_anypoint)

    def process_to_anypoint(self):
        """
        This function is to process the image and show on anypoint mode.

        """
        if self.parent.image is not None:
            if self.parent.type_camera:
                self.moildev = MoilUtils.connect_to_moildev(self.parent.type_camera)
                self.anypoint()

    def anypoint(self):
        """
        Anypoint widget_controller algorithm.

        """
        self.parent.normal_view = False
        self.parent.panorama_view = False
        self.parent.anypoint_view = True
        self.parent.angle = 0
        self.parent.label_34.show()
        self.parent.frame_navigator.show()
        self.parent.frame_panorama.hide()
        self.parent.mapX, self.parent.mapY, = self.moildev.getAnypointMaps(
            self.alpha, self.beta, self.zoom_any, self.anypoint_mode)

        self.parent.show_to_window()

    def __anypoint_mode_1(self):
        """
        Execute the anypoint process mode 1.

        Returns:
            None.
        """
        self.anypoint_mode = 1
        self.resetAlphaBeta()
        self.process_to_anypoint()

    def __anypoint_mode_2(self):
        """
        Execute the anypoint process mode 2.

        Returns:
            None.
        """
        self.anypoint_mode = 2
        self.resetAlphaBeta()
        self.process_to_anypoint()

    def resetAlphaBeta(self):
        """
        The method for reset alpha, beta, zoom, and angle.

        Returns:
            None.
        """
        self.alpha = 0
        self.beta = 0
        self.zoom_any = 4
        self.parent.point = (round(self.parent.w / 2), round(self.parent.h / 2))
        self.anypoint()

    def __up(self):
        """
        The method showing anypoint widget_controller in specific area.
        """
        self.parent.point = None
        if self.parent.radio_btn_mode_1.isChecked():
            self.alpha = 75
            self.beta = 0
        elif self.parent.radio_btn_mode_2.isChecked():
            self.alpha = 50
            self.beta = 0
        self.anypoint()

    def __left(self):
        """
        The method showing anypoint widget_controller in specific area.
        """
        self.parent.point = None
        if self.parent.radio_btn_mode_1.isChecked():
            self.alpha = 65
            self.beta = -90
        elif self.parent.radio_btn_mode_2.isChecked():
            self.alpha = 0
            self.beta = -75
        self.anypoint()

    def __center(self):
        """
        The method showing anypoint widget_controller in specific area.
        """
        self.parent.point = None
        if self.parent.radio_btn_mode_1.isChecked():
            self.alpha = 0
            self.beta = 0
        elif self.parent.radio_btn_mode_2.isChecked():
            self.alpha = 0
            self.beta = 0
        self.anypoint()

    def __right(self):
        """
        The method showing anypoint widget_controller in specific area.
        """
        self.parent.point = None
        if self.parent.radio_btn_mode_1.isChecked():
            self.alpha = 65
            self.beta = 90
        elif self.parent.radio_btn_mode_2.isChecked():
            self.alpha = 0
            self.beta = 65
        self.anypoint()

    def __down(self):
        """
        The method showing anypoint widget_controller in specific area.
        """
        self.parent.point = None
        if self.parent.radio_btn_mode_1.isChecked():
            self.alpha = 65
            self.beta = 180
        elif self.parent.radio_btn_mode_2.isChecked():
            self.alpha = -65
            self.beta = 0
        self.anypoint()
