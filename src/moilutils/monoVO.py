import cv2
import numpy as np
from moilutils import MoilUtils


class VisualOdometry(object):
    def __init__(self):
        self.__moildev = None
        self.__threshold = 25
        self.__focal_length = 616.8560
        self.__old_gray = None
        self.__R = np.zeros(shape=(3, 3))
        self.__curr_r = None
        self.__t = np.zeros(shape=(3, 3))
        self.__curr_t = None
        self.__trajectory = np.zeros((400, 400, 3), dtype=np.uint8)
        self.__pose = None
        self.__kMinNumFeature = 1500
        self.__lk_params = dict(winSize=(19, 19),
                              maxLevel=2,
                              criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 30, 0.01))

    def setPosePath(self, file_pose, typeCamera):
        self.__moildev = MoilUtils.connectToMoildev(typeCamera)
        self.__pp = (self.__moildev.getIcx(), self.__moildev.getIcy())
        try:
            with open(file_pose) as f:
                self.__pose = f.readlines()
        except Exception as e:
            print(e)
            raise ValueError("The designated pose_file_path does not exist, please check the path and try again")

    def detector(self, image, draw=True):
        """
        Args:
            image ():
            draw ():
        """
        # detect = cv2.FastFeatureDetector_create(threshold=self.threshold, nonmaxSuppression=True)
        # detect.setNonmaxSuppression(0)
        # point_ref = detect.detect(img)
        surf = cv2.xfeatures2d.SURF_create(400)
        point_ref, des = surf.detectAndCompute(image, None)
        if draw:
            return cv2.drawKeypoints(image, point_ref, None, color=(0, 255, 0))
        else:
            return np.array([x.pt for x in point_ref], dtype=np.float32).reshape(-1, 1, 2)

    def get_ground_truth(self, frame_id):
        pose = self.__pose[frame_id].strip().split()
        x = float(pose[3])
        y = float(pose[7])
        z = float(pose[11])
        return x, y, z

    def get_absolute_scale(self, frame_id):
        """

        :param frame_id:
        :return:
        """
        pose = self.__pose[frame_id - 1].strip().split()
        x_prev = float(pose[3])
        y_prev = float(pose[7])
        z_prev = float(pose[11])
        pose = self.__pose[frame_id].strip().split()
        x = float(pose[3])
        y = float(pose[7])
        z = float(pose[11])
        return np.sqrt((x - x_prev) * (x - x_prev) + (y - y_prev) * (y - y_prev) + (z - z_prev) * (z - z_prev))

    # def showFeatureTracking(self, img):
    #     # Create a mask image for drawing purposes
    #     mask = np.zeros_like(img)
    #     frame_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #     # calculate optical flow
    #     p1, st, err = cv2.calcOpticalFlowPyrLK(self.old_gray, frame_gray, self.prevFeatures, None, **self.lk_params)
    #     # Select good points
    #     if p1 is not None:
    #         good_new = p1[st == 1]
    #         good_old = self.prevFeatures[st == 1]
    #     # draw the tracks
    #     for i, (new, old) in enumerate(zip(good_new, good_old)):
    #         a, b = new.ravel()
    #         c, d = old.ravel()
    #         mask = cv2.line(mask, (int(a), int(b)), (int(c), int(d)), self.color[i].tolist(), 2)
    #         frame = cv2.circle(img, (int(a), int(b)), 5, self.color[i].tolist(), -1)
    #     img = cv2.add(frame, mask)
    #     return img

    def __feature_tracking(self, old_img, new_img, prevFeatures):
        """
        :return:
        """
        point_now, status, err = cv2.calcOpticalFlowPyrLK(old_img, new_img, prevFeatures,
                                                          None, **self.__lk_params)
        # save the good points
        status = status.reshape(status.shape[0])
        kp1 = prevFeatures[status == 1]
        kp2 = point_now[status == 1]
        return kp1, kp2

    def drawTrajectory(self, image=None, scale_factor=3, frame_id=None, draw_ground_truth=True):
        if image is None:
            print("Your Image broken!!")
        else:
            if frame_id == 1:
                self.__old_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            elif frame_id == 2:
                self.__new_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                self.__prevFeatures = self.detector(self.__old_gray, False)
                kp1, kp2 = self.__feature_tracking(self.__old_gray, self.__new_gray, self.__prevFeatures)
                E, mask = cv2.findEssentialMat(kp2, kp1, self.__focal_length,
                                               self.__pp, cv2.RANSAC, 0.999, 1.0)
                _, R, t, _ = cv2.recoverPose(E, kp2, kp1, self.__R,
                                             self.__t, self.__focal_length, self.__pp, mask)
                self.__old_gray = self.__new_gray
                self.__prevFeatures = kp2
                self.__curr_r = R
                self.__curr_t = t

            else:
                self.__new_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                kp1, kp2 = self.__feature_tracking(self.__old_gray, self.__new_gray, self.__prevFeatures)
                E, mask = cv2.findEssentialMat(kp2, kp1, self.__focal_length,
                                               self.__pp, cv2.RANSAC, 0.999, 1.0)
                _, R, t, _ = cv2.recoverPose(E, kp2, kp1, self.__R,
                                             self.__t, self.__focal_length, self.__pp, mask)
                scale = self.get_absolute_scale(frame_id)
                # print(scale)
                if scale > 0.1 and abs(t[2][0]) > abs(t[0][0]) and abs(t[2][0]) > abs(t[1][0]):
                    self.__curr_t = self.__curr_t - scale * self.__curr_r.dot(t)
                    self.__curr_r = R.dot(self.__curr_r)

                if self.__prevFeatures.shape[0] < self.__kMinNumFeature:
                    self.__prevFeatures = self.detector(self.__old_gray, False)
                    kp1, kp2 = self.__feature_tracking(self.__old_gray, self.__new_gray, self.__prevFeatures)

                self.__old_gray = self.__new_gray
                self.__prevFeatures = kp2

                x, y, z = self.__curr_t[0], self.__curr_t[1], self.__curr_t[2]
                # print(x, y, z)
                draw_x = int(-x * scale_factor) + 240  # modify here for different direction
                draw_y = int(z * scale_factor) + 290
                # print(draw_x, draw_y)
                cv2.circle(self.__trajectory, (draw_x, draw_y), 1, (0, 255, 0), 2)

            if draw_ground_truth:
                true_x, true_y, true_z = self.get_ground_truth(frame_id - 1)
                x, y = int(true_x * scale_factor) + 240, int(true_z * scale_factor) + 290
                cv2.circle(self.__trajectory, (x, y), 1, (255, 255, 255), 2)

            return self.__trajectory
