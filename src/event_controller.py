from PyQt5 import QtCore, QtWidgets
# from anypoint import Anypoint
from moilutils.moilutils import MoilUtils
import cv2


class MouseEvent(object):
    def __init__(self, main_controller):
        """
        Mouse event controller.
        Args:
            main_controller (): The main class of this application
        """
        self.parent = main_controller
        # self.anypoint = Anypoint(self.parent)
        self.__connect_event()

    def __connect_event(self):
        self.parent.label_Original_Image.mouseDoubleClickEvent = self.mouseDoubleclick_event
        self.parent.label_Result_Image.mouseDoubleClickEvent = self.mouseDoubleclick_event
        self.parent.label_Original_Image.mousePressEvent = self.mouse_event
        self.parent.label_Result_Image.mousePressEvent = self.mouse_result_press
        self.parent.label_Original_Image.wheelEvent = self.mouse_wheelEvent_ori_label
        self.parent.label_Result_Image.wheelEvent = self.mouse_wheelEvent
        self.parent.label_Result_Image.mouseReleaseEvent = self.mouse_release_event
        self.parent.label_Original_Image.mouseMoveEvent = self.mouseMovedOriImage
        self.parent.label_Result_Image.mouseMoveEvent = self.mouseMoveEvent

    def mouse_event(self, e):
        """
        Specify coordinate from mouse left event to generate anypoint widget_controller and recenter image.

        Args:
            e (): Coordinate point return by pyqt core

        Returns:

        """
        if self.parent.image is not None:
            if e.button() == QtCore.Qt.LeftButton:
                pos_x = round(e.x())
                pos_y = round(e.y())
                ratio_x, ratio_y = self.init_ori_ratio(self.parent.image)
                coordinate_X = round(pos_x * ratio_x)
                coordinate_Y = round(pos_y * ratio_y)
                self.parent.point = (coordinate_X, coordinate_Y)
                if self.parent.normal_view:
                    pass

                if self.parent.anypoint_view:
                    self.parent.anypoint.alpha, self.parent.anypoint.beta = self.parent.anypoint.moildev.getAlphaBeta(
                        coordinate_X, coordinate_Y, self.parent.anypoint.anypoint_mode)
                    # print(self.anypoint.alpha, self.anypoint.beta)
                    self.parent.anypoint.process_to_anypoint()

                elif self.parent.panorama_view:
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
        if self.parent.image is not None:
            if self.parent.normal_view:
                pass
            elif self.parent.anypoint_view:
                self.parent.anypoint.resetAlphaBeta()
                self.parent.anypoint.process_to_anypoint()
                self.parent.show_percentage()
            else:
                pass

    def mouse_wheelEvent(self, e):
        """
        Resize image using mouse wheel event.
        """
        if self.parent.image is not None:
            modifiers = QtWidgets.QApplication.keyboardModifiers()
            if modifiers == QtCore.Qt.ControlModifier:
                wheel_counter = e.angleDelta()
                if wheel_counter.y() / 120 == -1:
                    if self.parent.width_result_image < 600:
                        pass
                    else:
                        self.parent.width_result_image -= 100

                elif wheel_counter.y() / 120 == 1:
                    if self.parent.width_result_image > 6000:
                        pass
                    else:
                        self.parent.width_result_image += 100
                self.parent.show_to_window()
                self.parent.show_percentage()

    def mouse_wheelEvent_ori_label(self, e):
        """
        Resize image using mouse wheel event.
        """
        if self.parent.image is not None:
            modifiers = QtWidgets.QApplication.keyboardModifiers()
            if modifiers == QtCore.Qt.ControlModifier:
                wheel_counter = e.angleDelta()
                if wheel_counter.y() / 120 == -1:
                    if self.parent.anypoint_view:
                        if self.parent.anypoint.zoom_any == 14:
                            pass
                        else:
                            self.parent.anypoint.zoom_any += 1
                            self.parent.anypoint.anypoint()

                if wheel_counter.y() / 120 == 1:
                    if self.parent.anypoint_view:
                        if self.parent.anypoint.zoom_any == 2:
                            pass
                        else:
                            self.parent.anypoint.zoom_any -= 1
                            self.parent.anypoint.anypoint()

    def mouse_result_press(self, event):
        if self.parent.image is not None:
            self.parent.rubberband.hide()
            self.origin = event.pos()  # self.parent.label_Result_Image.mapFromParent(event.pos())
            self.parent.rubberband.setGeometry(QtCore.QRect(self.origin, QtCore.QSize()))
            self.parent.rubberband.show()

    def mouseMoveEvent(self, event):
        if self.parent.image is not None:
            if self.parent.zoom_area:
                pass
            else:
                if self.parent.rubberband.isVisible():
                    self.parent.rubberband.setGeometry(QtCore.QRect(self.origin, event.pos()))

    def mouse_release_event(self, e):
        """
        Mouse release event right click to show menu. the menu can select is show maximum, show minimum,
        save image, and show info.

        Args:
            e ():

        Returns:
            None.
        """
        if self.parent.image is not None:
            rect = self.parent.rubberband.geometry()
            if rect.width() > 20 and rect.height() > 20:
                image, selectedImage = self.parent.cropImage(rect)
                self.parent.rubberband.hide()
                MoilUtils.showImageToLabel(self.parent.label_Original_Image, image, 300)
                MoilUtils.showImageToLabel(self.parent.label_Result_Image, selectedImage, 1200)
                self.parent.comboBox_zoom.setCurrentIndex(8)
                self.parent.comboBox_zoom.setItemText(8, "Zoom Area")
                self.parent.zoom_area = True

            if e.button() == QtCore.Qt.RightButton:
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
        maxi = menu.addAction("Show Maximized")
        maxi.triggered.connect(self.parent.maximize_view)
        mini = menu.addAction("Show Minimized")
        mini.triggered.connect(self.parent.minimize_view)
        save = menu.addAction("Save Image")
        info = menu.addAction("Show Info")
        save.triggered.connect(self.parent.save_image)
        info.triggered.connect(self.parent.onclick_help)
        menu.exec_(e.globalPos())

    def mouseMovedOriImage(self, e):
        """
        Mouse move event to look in surrounding widget_controller in result label image.

        Args:
            e ():

        Returns:

        """
        pos_x = round(e.x())
        pos_y = round(e.y())
        if self.parent.image is not None:
            ratio_x, ratio_y = self.init_ori_ratio(self.parent.image)
            coordinate_X = round(pos_x * ratio_x)
            coordinate_Y = round(pos_y * ratio_y)
            if e.buttons() == QtCore.Qt.NoButton:
                if self.parent.normal_view:
                    pass
                elif self.parent.anypoint_view:
                    self.parent.anypoint.alpha, self.parent.anypoint.beta = self.parent.anypoint.moildev.getAlphaBeta(
                        coordinate_X, coordinate_Y, self.parent.anypoint.anypoint_mode)
                    self.parent.status_alpha.setText("Alpha: %.2f" % self.parent.anypoint.alpha)
                    self.parent.status_beta.setText("Beta: %.2f" % self.parent.anypoint.beta)

            elif e.buttons() == QtCore.Qt.LeftButton:
                self.parent.point = (coordinate_X, coordinate_Y)
                if self.parent.normal_view:
                    pass
                elif self.parent.anypoint_view:
                    self.parent.anypoint.alpha, self.parent.anypoint.beta = self.parent.anypoint.moildev.getAlphaBeta(
                        coordinate_X, coordinate_Y, self.parent.anypoint.anypoint_mode)
                    self.parent.anypoint.process_to_anypoint()
                elif self.parent.panorama_view:
                    print("coming soon")

    def init_ori_ratio(self, image):
        """
        Calculate the initial ratio of the image.

        Returns:
            ratio_x : ratio width between image and ui window.
            ratio_y : ratio height between image and ui window.
            center : find the center image on window user interface.
        """
        h = self.parent.label_Original_Image.height()
        w = self.parent.label_Original_Image.width()
        height, width = image.shape[:2]
        ratio_x = width / w
        ratio_y = height / h
        return ratio_x, ratio_y

    def init_result_ratio(self, image):
        """
        Calculate the initial ratio of the image.

        Returns:
            ratio_x : ratio width between image and ui window.
            ratio_y : ratio height between image and ui window.
            center : find the center image on window user interface.
        """
        h = self.parent.label_Result_Image.height()
        w = self.parent.label_Result_Image.width()
        height, width = image.shape[:2]
        ratio_x = width / w
        ratio_y = height / h
        return ratio_x, ratio_y
