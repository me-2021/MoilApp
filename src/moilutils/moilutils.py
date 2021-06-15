from PyQt5 import QtWidgets, QtGui, QtCore
import cv2
import os
import shutil
import numpy as np
import datetime
import math
from Exif.exif_lib import MetaImage
from Moildev.Moildev import Moildev


class MoilUtils(object):
    camera_params = "cam_params/camera_parameters.json"

    def __init__(self):
        super(MoilUtils, self).__init__()

    @classmethod
    def select_file(cls, parent, title, dir_path, file_filter):
        """
        Find the file path from the directory computer.

        Args:
            parent (): The parent windows to show dialog always in front of user interface
            title: the title window of open dialog
            file_filter: determine the specific file want to search
            dir_path: Navigate to specific directory

        return:
            file_path: location
        """
        options = QtWidgets.QFileDialog.DontUseNativeDialog
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(parent, title, dir_path,
                                                             file_filter,
                                                             options=options)
        return file_path

    @classmethod
    def copy_directory(cls, srcpath, dstdir):
        """
        Copy directory.

        Args:
            srcpath (): source path or original path folder
            dstdir (): destination directory.

        Returns:
            file copied in destination directory.
        """
        dirname = os.path.basename(srcpath)
        dstpath = os.path.join(dstdir, dirname)
        shutil.copytree(srcpath, dstpath)

    @classmethod
    def draw_polygon(cls, image, mapX, mapY):
        """
        Draw polygon from mapX and mapY given in the original image.

        Args:
            image: Original image
            mapX: map image X from anypoint process
            mapY: map image Y from anypoint process

        return:
            image:
        """
        hi, wi = image.shape[:2]
        X1 = []
        Y1 = []
        X2 = []
        Y2 = []
        X3 = []
        Y3 = []
        X4 = []
        Y4 = []

        x = 0
        while x < wi:
            a = mapX[0, ]
            b = mapY[0, ]
            ee = mapX[-1, ]
            f = mapY[-1, ]

            if a[x] == 0. or b[x] == 0.:
                pass
            else:
                X1.append(a[x])
                Y1.append(b[x])

            if f[x] == 0. or ee[x] == 0.:
                pass
            else:
                Y3.append(f[x])
                X3.append(ee[x])
            x += 10

        y = 0
        while y < hi:
            c = mapX[:, 0]
            d = mapY[:, 0]
            g = mapX[:, -1]
            h = mapY[:, -1]

            # eliminate the value 0 for map X
            if d[y] == 0. or c[y] == 0.:  # or d[y] and c[y] == 0.0:
                pass
            else:
                Y2.append(d[y])
                X2.append(c[y])

            # eliminate the value 0 for map Y
            if h[y] == 0. or g[y] == 0.:
                pass
            else:
                Y4.append(h[y])
                X4.append(g[y])

            # render every 10 times, it will be like 1, 11, 21 and so on.
            y += 10

        p = np.array([X1, Y1])
        q = np.array([X2, Y2])
        r = np.array([X3, Y3])
        s = np.array([X4, Y4])
        points = p.T.reshape((-1, 1, 2))
        points2 = q.T.reshape((-1, 1, 2))
        points3 = r.T.reshape((-1, 1, 2))
        points4 = s.T.reshape((-1, 1, 2))

        # Draw polyline on original image
        cv2.polylines(image, np.int32([points]), False, (0, 255, 0), 10)
        cv2.polylines(image, np.int32([points2]), False, (0, 255, 0), 10)
        cv2.polylines(image, np.int32([points3]), False, (0, 255, 0), 10)
        cv2.polylines(image, np.int32([points4]), False, (0, 255, 0), 10)
        return image

    @classmethod
    def resize_image(cls, image, width):
        """
        Resize image original with our size we want

        Args:
            image (): image original
            width (): image width we want

        Returns:
            result: image has been resize

        """
        h, w = image.shape[:2]
        r = width / float(w)
        hi = round(h * r)
        result = cv2.resize(image, (width, hi),
                            interpolation=cv2.INTER_AREA)
        return result

    @classmethod
    def save_image(cls, image, dir_save, type_camera):
        ss = datetime.datetime.now().strftime("%m%d%H_%M%S")
        name = dir_save + "/" + str(ss) + ".png"
        cv2.imwrite(name, image)
        img = MetaImage(name)
        img.modify_comment(type_camera)
        img.close()

    @classmethod
    def calculate_height(cls, image, image_width):
        """
        Calculate the height image with the same ratio with the size original image.

        Args:
            image: original image
            image_width: size image we want

        Returns:
            height: height image
        """

        h, w = image.shape[:2]
        r = image_width / float(w)
        height = round(h * r)
        return height

    @classmethod
    def read_image(cls, image_path):
        """
        Reading the image from given file path using openCV.

        Args:
            image_path : The path of image file

        return:
            Image: load image
        """
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError("`{}` not cannot be loaded".format(image_path))
        return image

    @classmethod
    def rotate(cls, src, angle, center=None, scale=1.0):
        """
        Turn an image in a clockwise or counterclockwise direction.

        Args:
            src: original image
            angle: the value angle for turn the image
            center: determine the specific coordinate to rotate image
            scale: scale image

        Returns:
            dst image: rotated image
        """
        h, w = src.shape[:2]
        if center is None:
            center = (w / 2, h / 2)
        m = cv2.getRotationMatrix2D(center, angle, scale)
        rotated = cv2.warpAffine(src, m, (w, h))
        return rotated

    @classmethod
    def connect_to_moildev(cls, type_camera, parent=None):
        """
        Connect to Moildev SDK, need provide camera parameter database and type of camera.

        """
        if type_camera:
            moildev = Moildev(cls.camera_params, type_camera)

        else:
            QtWidgets.QMessageBox.warning(
                parent,
                "Warning!!",
                "The image not support for this application, \n\nPlease contact developer!!")
            print("the image not support for this application, please contact developer!!")
            moildev = None

        return moildev

    @classmethod
    def selectDir(cls, parent=None):
        """
        Select directory to save image. This function create to make it not always ask the directory by open dialog,
        after directory save not None, it will pass open dialog prompt.

        Returns:
            None.
        """
        dir_save = QtWidgets.QFileDialog.getExistingDirectory(
            parent, 'Select Save Folder')
        return dir_save

    @classmethod
    def showing_image(cls, label, image, width_image, angle=0):
        """
        Showing image to the window in user interface.

        Args:
            label ():
            image ():
            width_image ():
            angle ():

        Returns:

        """
        height = cls.calculate_height(image, width_image)
        image = cls.resize_image(image, width_image)
        image = MoilUtils.rotate(image, angle)
        label.setMinimumSize(QtCore.QSize(width_image, height))
        # label.setMaximumSize(QtCore.QSize(width_image, height))
        image = QtGui.QImage(image.data, image.shape[1], image.shape[0],
                             QtGui.QImage.Format_RGB888).rgbSwapped()
        label.setPixmap(QtGui.QPixmap.fromImage(image))

    @classmethod
    def corner_detect(cls, image, sigma=3, threshold=0.01):
        """

        Args:
            image ():
            sigma ():
            threshold ():

        Returns:

        """
        # height, width = image.shape
        # shape = (height, width)
        # Calculate the dx,dy gradients of the image (np.gradient doesnt work)
        image = MoilUtils.convert_to_gray(image)
        dx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
        dy = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
        # Get angle for rotation
        _, ang = cv2.cartToPolar(dx, dy, angleInDegrees=True)
        # Square the derivatives (A,B,C of H) and apply apply gaussian filters to each
        sigma = (sigma, sigma)
        Ixx = cv2.GaussianBlur(dx * dx, sigma, 0)
        Ixy = cv2.GaussianBlur(dx * dy, sigma, 0)
        Iyy = cv2.GaussianBlur(dy * dy, sigma, 0)

        H = np.array([[Ixx, Ixy], [Ixy, Iyy]])
        # Find the determinate
        num = (H[0, 0] * H[1, 1]) - (H[0, 1] * H[1, 0])
        # Find the trace
        denom = H[0, 0] + H[1, 1]
        # Find the response using harmonic mean of the eigenvalues (Brown et. al. variation)
        R = np.nan_to_num(num / denom)

        # Adaptive non-maximum suppression, keep the top 1% of values and remove non-maximum points in a 9x9
        # neighbourhood
        R_flat = R[:].flatten()
        # Get number of values in top threshold %
        N = int(len(R_flat) * threshold)
        # Get values in top threshold %
        top_k_percentile = np.partition(R_flat, -N)[-N:]
        # Find lowest value in top threshold %
        minimum = np.min(top_k_percentile)
        # Set all values less than this to 0
        R[R < minimum] = 0
        # Set non-maximum points in an SxS neighbourhood to 0
        s = 9
        for h in range(R.shape[0] - s):
            for w in range(R.shape[1] - s):
                maximum = np.max(R[h:h + s + 1, w:w + s + 1])
                for i in range(h, h + s + 1):
                    for j in range(w, w + s + 1):
                        if R[i, j] != maximum:
                            R[i, j] = 0

        # Return harris corners in [H, W, R] format
        features = list(np.where(R > 0))
        features.append(ang[np.where(R > 0)])
        corners = zip(*features)
        corner_list = cls.__get_corner_list(list(corners))
        return corner_list

    @classmethod
    def draw_corners(cls, corners, image):
        """

        Args:
            corners ():
            image ():

        Returns:

        """
        i = 0
        for h, w in corners:
            cv2.circle(image, (w, h), 3, (0, 0, 255), -1)
            # caption = '{},{}'.format(h, w)
            cv2.putText(image, str(i), (w - 5, h + 10), cv2.FONT_HERSHEY_COMPLEX, 0.3, (0, 255, 0))
            i += 1
        return image

    @classmethod
    def __get_corner_list(cls, corners):
        """

        Args:
            corners ():

        Returns:

        """
        coor = []
        for h, w, r in corners:
            caption = '{},{}'.format(h, w)
            res = tuple(map(int, caption.split(',')))
            coor.append(res)
        return coor

    @classmethod
    def drawPoint(cls, image, label_image, coordinatePoint):
        """

        Args:
            image ():
            label_image ():
            coordinatePoint ():

        Returns:

        """
        cv2.circle(image, coordinatePoint, 3, (0, 255, 0), -1)
        return image

    @classmethod
    def draw_line(cls, image, coordinate_point_1, coordinate_point_2):
        """

        Args:
            image ():
            label_image ():
            coordinatePoint ():

        Returns:

        """
        cv2.line(image, coordinate_point_1, coordinate_point_2, (0, 255, 0), 1)
        return image

    @classmethod
    def distance(cls, point_a, point_b):
        """
        Returns the distance between two points.
        Args:
            point_a ():
            point_b ():

        Returns:

        """
        x0, y0 = point_a
        x1, y1 = point_b
        return math.fabs(x0 - x1) + math.fabs(y0 - y1)

    @classmethod
    def convert_to_gray(cls, image):
        """

        Args:
            image ():

        Returns:

        """
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray

    @classmethod
    def showing_image_object_measurement(cls, label, image, width_image, angle=0):
        """
        Showing image to the window in user interface.

        Args:
            label ():
            image ():
            width_image ():
            angle ():

        Returns:

        """
        height = cls.calculate_height(image, width_image)
        image = cls.resize_image(image, width_image)
        image = MoilUtils.rotate(image, angle)
        label.setMinimumSize(QtCore.QSize(width_image, height))
        # label.resize(width_image, height)
        # label.setMaximumSize(QtCore.QSize(width_image, height))
        image = QtGui.QImage(image.data, image.shape[1], image.shape[0],
                             QtGui.QImage.Format_RGB888).rgbSwapped()
        label.setPixmap(QtGui.QPixmap.fromImage(image))
