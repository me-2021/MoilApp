import cv2
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from .souceIcon import ResourceIcon


class VideoController(object):
    def __init__(self, parent):
        super(VideoController, self).__init__()
        self.parent = parent
        self.__rs = ResourceIcon()
        self.__fps = None
        self.__pos_frame = None
        self.__frame_count = None
        self.__minute = None
        self.__minutes = None
        self.__seconds = None
        self.__sec = None
        self.play = False
        self.playPauseBtn = None
        self.__frameNumber = 1
        self.__timer = QtCore.QTimer()
        self.__timer.timeout.connect(self.nextFrame)

    # migrate to video controller
    def nextFrame(self):
        """
        looping the frame showing in label user interface.

        """
        if self.parent.cam:
            success, self.parent.image = self.parent.cap.read()
            if success:
                self.__fps = self.parent.cap.get(cv2.CAP_PROP_FPS)
                self.__pos_frame = self.parent.cap.get(cv2.CAP_PROP_POS_FRAMES)
                self.__frame_count = float(self.parent.cap.get(cv2.CAP_PROP_FRAME_COUNT))

        else:
            self.__frame_count = len(os.listdir(self.parent.folderOdometry))
            self.__fps = 10
            if self.__frameNumber < self.__frame_count:
                self.__pos_frame = self.__frameNumber
                file = self.parent.folderOdometry + "/" + str(self.__frameNumber) + ".png"
                self.parent.image = cv2.imread(file)
                self.parent.h, self.parent.w = self.parent.image.shape[:2]
                self.__frameNumber += 1

        duration_sec = int(self.__frame_count / self.__fps)
        self.__minutes = duration_sec // 60
        duration_sec %= 60
        self.__seconds = duration_sec
        sec_pos = int(self.__pos_frame / self.__fps)
        self.__minute = int(sec_pos // 60)
        sec_pos %= 60
        self.__sec = sec_pos
        self.__controller()
        self.parent.showToWindow()
        try:
            if self.parent.video_writer is not None:
                image = self.parent.image if self.parent.normal_view else self.parent.result_image
                self.parent.video_writer.write(image)
        except:
            pass

    def playPauseVideo(self, btnName):
        """
        Control the play and pause video controller button
        for example, if play is true: it will change the icon button

        """
        if not btnName:
            btnName = None
        self.playPauseBtn = btnName
        if self.play:
            self.pauseVideo(btnName)

        else:
            self.playVideo(btnName)

    def pauseVideo(self, btnName):
        """
        Pause the frame in video or camera mode.

        """
        try:
            self.__timer.stop()
            self.play = False
            if btnName is not None:
                btnName.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(self.__rs.iconPlay())))

        except:
            QtWidgets.QMessageBox.warning(
                None,
                "Warning!!",
                "No Source Media found !!!")

    def playVideo(self, btnName):
        """
        Play video by connect to timer function.

        """
        try:
            self.__timer.start(1000 / self.__fps)
            self.play = True
            if btnName is not None:
                btnName.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(self.__rs.iconPause())))

        except:
            QtWidgets.QMessageBox.warning(
                None,
                "Warning!!",
                "No Source Media found !!!")

    def __controller(self):
        """
        Manage the video to setup the current timer.

        """
        dst_value = self.__pos_frame * (self.parent.slider_Video.maximum() + 1) / self.__frame_count
        self.parent.slider_Video.blockSignals(True)
        self.parent.slider_Video.setValue(dst_value)
        self.parent.slider_Video.blockSignals(False)

        try:
            current = self.parent.label_time_recent
            current.setAlignment(QtCore.Qt.AlignCenter)
            current.setText("%02d : %02d" % (self.__minute, self.__sec))

            if self.__minutes < 0:
                "this is for live camera, when the times more than 1000 minutes, it will set to 00:00"
                my_label3 = self.parent.label_time_end
                my_label3.setAlignment(QtCore.Qt.AlignCenter)
                my_label3.setText("00 : 00")

            else:
                my_label3 = self.parent.label_time_end
                my_label3.setAlignment(QtCore.Qt.AlignCenter)
                my_label3.setText("%02d : %02d" %
                                  (self.__minutes, self.__seconds))

        except:
            pass

    def stopVideo(self):
        """
        Stop video and set the time as a beginning, including the slider time

        """
        try:
            self.play = False
            if self.playPauseBtn is not None:
                self.playPauseBtn.setIcon(QtGui.QIcon(QtGui.QPixmap.fromImage(self.__rs.iconPlay())))
            if self.parent.cam:
                self.parent.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            else:
                self.__frameNumber = 1
            self.nextFrame()
            self.__reset_label_time()
            self.__timer.stop()

        except:
            QtWidgets.QMessageBox.warning(
                None,
                "Warning!!",
                "No Source Media found !!!")

    def __reset_label_time(self):
        """
        Reset the time when open the new video.

        """
        current = self.parent.label_time_recent
        current.setAlignment(QtCore.Qt.AlignCenter)
        current.setText("00 : 00")

        my_label3 = self.parent.label_time_end
        my_label3.setAlignment(QtCore.Qt.AlignCenter)
        my_label3.setText("%02d : %02d" %
                          (self.__minutes, self.__seconds))

    def rewindVideo(self):
        """
        Previous video is 5 seconds.

        """
        try:
            if self.parent.cam:
                position = self.__pos_frame - 5 * self.__fps
                self.parent.cap.set(cv2.CAP_PROP_POS_FRAMES, position)

            else:
                self.__frameNumber -= 5 * self.__fps
                if self.__frameNumber <= 1:
                    self.__frameNumber = 1
            self.nextFrame()

        except:
            QtWidgets.QMessageBox.warning(
                None,
                "Warning!!",
                "No Source Media found !!!")

    def forwardVideo(self):
        """
        skip video in 5 seconds.

        """
        try:
            if self.parent.cam:
                position = self.__pos_frame + 5 * self.__fps
                self.parent.cap.set(cv2.CAP_PROP_POS_FRAMES, position)

            else:
                self.__frameNumber += 5 * self.__fps
                if self.__frameNumber >= self.__frame_count:
                    self.__frameNumber = self.__frame_count

            self.nextFrame()

        except:
            QtWidgets.QMessageBox.warning(
                None,
                "Warning!!",
                "No Source Media found !!!")

    def sliderController(self, value):
        """
        Set and control the slider to control the video.

        Args:
            value (): Value from slider

        """
        try:
            dst_frame = self.__frame_count * value / self.parent.slider_Video.maximum()
            if self.parent.cam:
                self.parent.cap.set(cv2.CAP_PROP_POS_FRAMES, dst_frame)

            else:
                self.__frameNumber = round(dst_frame)
                if self.__frameNumber <= 1:
                    self.__frameNumber = 1

            self.nextFrame()
            self.pauseVideo()
            self.play = False

        except:
            QtWidgets.QMessageBox.warning(
                None,
                "Warning!!",
                "No Source Media found !!!")