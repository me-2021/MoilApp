class ManipulateView(object):
    def __init__(self, main_controller):
        self.parent = main_controller
        self.parent.btn_Rotate_Left.clicked.connect(self.rotate_left)
        self.parent.btn_Rotate_Right.clicked.connect(self.rotate_right)
        self.parent.btn_Zoom_in.clicked.connect(self.zoom_in)
        self.parent.btn_Zoom_out.clicked.connect(self.zoom_out)

    def zoom_in(self):
        """
        Zoom in image on result label

        """
        if self.parent.image is not None:
            if self.parent.width_result_image == 4000:
                pass
            else:
                self.parent.width_result_image += 100
            self.parent.show_to_window()

    def zoom_out(self):
        """
        Zoom out image on result label

        """
        if self.parent.image is not None:
            if self.parent.width_result_image == 1000:
                pass
            else:
                self.parent.width_result_image -= 100
            self.parent.show_to_window()

    def rotate_left(self):
        """
        Rotate image in anti clockwise.

        """
        if self.parent.image is not None:
            if self.parent.angle == 180:
                pass
            else:
                self.parent.angle += 10
            self.parent.show_to_window()

    def rotate_right(self):
        """
        Rotate image in clockwise.

        """
        if self.parent.image is not None:
            if self.parent.angle == 180:
                pass
            else:
                self.parent.angle -= 10
            self.parent.show_to_window()
