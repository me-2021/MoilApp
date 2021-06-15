from PyQt5 import QtCore, QtGui, QtWidgets
from moilutils import MoilUtils
import datetime
import cv2
import os


class VideoController(object):
    def __init__(self, MainWindow):
        """
        This is the video controller methode that has function to control the video player button
        like play, pause skip, prev and etc. This class need include parent class to access the attribute.
        MainWindow is the parent class.

        Args:
            MainWindow ():
        """
        self.parent = MainWindow
        self.w = None
        self.h = None
        self.fps = None
        self.pos_frame = None
        self.frame_count = None
        self.minute = None
        self.minutes = None
        self.seconds = None
        self.sec = None
        self.play = False
        self.record = False
        self.videoDir = None
        self.video_writer = None
        self.timer = QtCore.QTimer()
        self.parent.btn_play_pouse.clicked.connect(self.onclick_play_pause_button)
        self.parent.btn_stop_video.clicked.connect(self.stop_video)
        self.parent.btn_prev_video.clicked.connect(self.prev_video)
        self.parent.btn_skip_video.clicked.connect(self.skip_video)
        self.parent.actionRecord_video.triggered.connect(self.action_record_video)
        self.parent.btn_Record_video.clicked.connect(self.recordVideo)
        self.parent.slider_Video.valueChanged.connect(self.changeValueSlider)

    def set_button_disable(self):
        """
        Disable video control button when the application not using camera or video mode.

        """
        self.parent.btn_play_pouse.setDisabled(True)
        self.parent.btn_prev_video.setDisabled(True)
        self.parent.btn_stop_video.setDisabled(True)
        self.parent.btn_skip_video.setDisabled(True)
        self.parent.slider_Video.setDisabled(True)

    def set_button_enable(self):
        """
        Enable video control button when application using camera or video mode.

        """
        self.parent.btn_play_pouse.setEnabled(True)
        self.parent.btn_prev_video.setEnabled(True)
        self.parent.btn_stop_video.setEnabled(True)
        self.parent.btn_skip_video.setEnabled(True)
        self.parent.slider_Video.setEnabled(True)

    # migrate to video controller
    def next_frame_slot(self):
        """
        looping the frame showing in label user interface.

        """
        _, self.parent.image = self.parent.cap.read()
        if self.parent.image is None:
            self.pause_video()
        else:
            self.h, self.w = self.parent.image.shape[:2]
            self.fps = self.parent.cap.get(cv2.CAP_PROP_FPS)
            self.pos_frame = self.parent.cap.get(cv2.CAP_PROP_POS_FRAMES)
            # self.pos_msec = self.parent.cap.get(cv2.CAP_PROP_POS_MSEC)
            self.frame_count = float(self.parent.cap.get(cv2.CAP_PROP_FRAME_COUNT))
            duration_sec = int(self.frame_count / self.fps)
            self.minutes = duration_sec // 60
            duration_sec %= 60
            self.seconds = duration_sec
            sec_pos = int(self.pos_frame / self.fps)
            self.minute = int(sec_pos // 60)
            sec_pos %= 60
            self.sec = sec_pos
            self.controller()
            self.parent.show_to_window()
            if self.parent.btn_Record_video.isChecked():
                self.video_writer.write(self.parent.image)
            # else:
            #     self.parent.show_to_window()
            #     if self.parent.btn_Record_video.isChecked():
            #         print("coming soon")

    def reset_time(self):
        """
        Reset the time when open the new video.

        """
        current = self.parent.label_time_recent
        current.setAlignment(QtCore.Qt.AlignCenter)
        current.setText("00:00")

        end_time = self.parent.label_time_end
        end_time.setAlignment(QtCore.Qt.AlignCenter)
        end_time.setText("00:00")

    def control_camera_mode(self):
        """
        Control the widget when on camera mode.
        ex: time slider will disabled

        """
        pass

    def onclick_play_pause_button(self):
        """
        Control the play and pause video controller button
        for example, if play is true: it will change the icon button

        """
        if self.play:
            self.pause_video()
            self.play = False

        else:
            self.play_video()
            self.play = True

    def pause_video(self):
        """
        Pause the frame in video or camera mode.

        """
        self.timer.stop()
        self.parent.btn_play_pouse.setIcon(
            QtGui.QIcon("images/play.png"))

    def play_video(self):
        """
        Play video by connect to timer function.

        """
        if self.parent.cap.isOpened():
            self.parent.btn_play_pouse.setIcon(
                QtGui.QIcon("images/pause.png"))
            self.timer.timeout.connect(self.next_frame_slot)
            self.timer.start(1000. / self.fps)
        else:
            pass

    def controller(self):
        """
        Manage the video to setup the current timer.

        """
        dst_value = self.pos_frame * \
            (self.parent.slider_Video.maximum() + 1) / self.frame_count
        self.parent.slider_Video.blockSignals(True)
        self.parent.slider_Video.setValue(dst_value)
        self.parent.slider_Video.blockSignals(False)

        current = self.parent.label_time_recent
        current.setAlignment(QtCore.Qt.AlignCenter)
        current.setText("%02d : %02d" % (self.minute, self.sec))

        if self.minutes > 1000:
            "this is for live camera, when the times more than 1000 minutes, it will set to 00:00"
            my_label3 = self.parent.label_time_end
            my_label3.setAlignment(QtCore.Qt.AlignCenter)
            my_label3.setText("00:00")

        else:
            my_label3 = self.parent.label_time_end
            my_label3.setAlignment(QtCore.Qt.AlignCenter)
            my_label3.setText("%02d : %02d" %
                              (self.minutes, self.seconds))

    def stop_video(self):
        """
        Stop video and set the time as a beginning, including the slider time

        """
        self.play = False
        self.parent.btn_play_pouse.setIcon(QtGui.QIcon("images/play.png"))
        if self.parent.cap.isOpened():
            self.timer.stop()
            self.parent.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            self.next_frame_slot()
            self.reset_label_time()
        else:
            pass

    def reset_label_time(self):
        """
        Reset the time when open the new video.

        """
        current = self.parent.label_time_recent
        current.setAlignment(QtCore.Qt.AlignCenter)
        current.setText("00:00")

        current_1 = self.parent.label_time_end
        current_1.setAlignment(QtCore.Qt.AlignCenter)
        current_1.setText("00:00")

    def prev_video(self):
        """
        Previous video is 5 seconds.

        """
        if self.parent.cap.isOpened():
            position = self.pos_frame - 5 * self.fps
            self.parent.cap.set(cv2.CAP_PROP_POS_FRAMES, position)
            self.next_frame_slot()
        else:
            pass

    def skip_video(self):
        """
        skip video in 5 seconds.

        """
        if self.parent.cap.isOpened():
            position = self.pos_frame + 5 * self.fps
            self.parent.cap.set(cv2.CAP_PROP_POS_FRAMES, position)
            self.next_frame_slot()
        else:
            pass

    def changeValueSlider(self, value):
        """
        Set and control the slider to control the video.

        Args:
            value (): Value from slider

        """
        if self.parent.cap.isOpened():
            dst_frame = self.frame_count * value / self.parent.slider_Video.maximum() + 1
            self.parent.cap.set(cv2.CAP_PROP_POS_FRAMES, dst_frame)
            self.next_frame_slot()
            self.timer.stop()
        else:
            pass

    def recordVideo(self):
        """
        Create video writer to save video.

        """
        # print(self.parent.ui.btn_Record_video.isChecked())
        if self.parent.cam:
            if self.parent.btn_Record_video.isChecked():
                self.timer.stop()
                ss = datetime.datetime.now().strftime("%m%d%H_%M%S")
                frame_width = int(self.parent.cap.get(3))
                frame_height = int(self.parent.cap.get(4))
                filename = "Original" if self.parent.normal_view else "result"

                if self.videoDir is None or self.videoDir == "":
                    self.videoDir = MoilUtils.selectDir()
                print(self.videoDir)
                if self.videoDir:
                    name = self.videoDir + "/" + filename + "_" + str(ss) + ".avi"
                    answer = QtWidgets.QMessageBox.information(
                        None,
                        "Information",
                        " Start Record Video !!",
                        QtWidgets.QMessageBox.Yes,
                        QtWidgets.QMessageBox.No)

                    if answer == QtWidgets.QMessageBox.Yes:
                        self.timer.start()
                        self.video_writer = cv2.VideoWriter(
                            name, cv2.VideoWriter_fourcc(
                                *'XVID'), 15, (frame_width, frame_height))
                        os.makedirs(os.path.dirname(name), exist_ok=True)
                        self.parent.btn_Record_video.setIcon(QtGui.QIcon("images/record_start.png"))
                else:
                    self.parent.btn_Record_video.setChecked(False)

            else:
                if self.video_writer is None:
                    pass
                else:
                    self.video_writer.release()
                    self.timer.stop()
                    QtWidgets.QMessageBox.information(
                        None,
                        "Information",
                        "Video saved !!\n\nLoc: " +
                        self.videoDir)
                    self.timer.start()
                    self.parent.btn_Record_video.setIcon(QtGui.QIcon("images/video-record.png"))

    def action_record_video(self):
        """
        Create video writer to save video.

        """
        # print(self.parent.ui.btn_Record_video.isChecked())
        if self.parent.cam:
            if self.parent.actionRecord_video.isChecked():
                self.timer.stop()
                ss = datetime.datetime.now().strftime("%m%d%H_%M%S")
                frame_width = int(self.parent.cap.get(3))
                frame_height = int(self.parent.cap.get(4))
                filename = "Original" if self.parent.normal_view else "result"

                if self.videoDir is None or self.videoDir == "":
                    self.videoDir = MoilUtils.selectDir()
                print(self.videoDir)
                if self.videoDir:
                    name = self.videoDir + "/" + filename + "_" + str(ss) + ".avi"
                    answer = QtWidgets.QMessageBox.information(
                        None,
                        "Information",
                        " Start Record Video !!",
                        QtWidgets.QMessageBox.Yes,
                        QtWidgets.QMessageBox.No)

                    if answer == QtWidgets.QMessageBox.Yes:
                        self.timer.start()
                        self.video_writer = cv2.VideoWriter(
                            name, cv2.VideoWriter_fourcc(
                                *'XVID'), 15, (frame_width, frame_height))
                        os.makedirs(os.path.dirname(name), exist_ok=True)
                        self.parent.btn_Record_video.setIcon(QtGui.QIcon("images/record_start.png"))
                else:
                    self.parent.actionRecord_video.setChecked(False)

            else:
                if self.video_writer is None:
                    pass
                else:
                    self.video_writer.release()
                    self.timer.stop()
                    QtWidgets.QMessageBox.information(
                        self.parent,
                        "Information",
                        "Video saved !!\n\nLoc: " +
                        self.videoDir)
                    self.timer.start()
                    self.parent.btn_Record_video.setIcon(QtGui.QIcon("images/video-record.png"))

    def selectDir(self):
        """
        Select destination directory to save the video file.

        """
        self.videoDir = QtWidgets.QFileDialog.getExistingDirectory(self.parent, 'Select Save Folder')
        if self.videoDir:
            self.recordVideo()
        else:
            self.parent.btn_Record_video.setChecked(False)
            self.timer.start()
