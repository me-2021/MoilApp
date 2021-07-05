import ctypes
import os
import platform
import cv2
import json
import math
import numpy as np

dir_path = os.path.dirname(os.path.realpath(__file__))
if platform.system() == "Windows":
    path = os.path.join(dir_path, "moildev.dll")
    shared_lib_path = path
else:
    path = os.path.join(dir_path, "moildev.so")
    shared_lib_path = path

try:
    lib = ctypes.cdll.LoadLibrary(shared_lib_path)
except Exception as e:
    print(e)


class Moildev(object):
    def __init__(self, parameter_path, camera_type):
        """
        This is the initial configuration that you need provide the parameter. The camera parameter is the result from
        calibration camera by MOIL laboratory. before the successive functions can work correctly,configuration is
        necessary in the beginning of program.

        Args:
            parameter_path ():
            camera_type ():

        for more detail, please reference https://github.com/MoilOrg/moildev
        """
        """
        This is the initial configuration that you need provide the parameter. The camera parameter is the result from
        calibration camera by MOIL laboratory. before the successive functions can work correctly,configuration is
        necessary in the beginning of program.

        Args:
            . camera_name - A string to describe this camera
            . sensor_width - Camera sensor width (cm)
            . sensor_height - Camera Sensor Height (cm)
            . Icx - image center X coordinate(pixel)
            . Icy - image center Y coordinate(pixel)
            . ratio : Sensor pixel aspect ratio.
            . imageWidth : Input image width
            . imageHeight : Input image height
            . parameter0 .. parameter5 : calibration's parameters
            . calibrationRatio : input image with/ calibrationRatio image width

        for more detail, please reference https://github.com/MoilOrg/moildev
        """
        super(Moildev, self).__init__()
        self.__PI = 3.1415926
        self.__alphaToRho_Table = []
        self.__rhoToAlpha_Table = []
        self.__moildev = None
        if parameter_path is None:
            pass
        else:
            with open(parameter_path) as f:
                data = json.load(f)
                if camera_type in data.keys():
                    self.__camera = data[camera_type]["cameraName"]
                    self.__sensor_width = data[camera_type]['cameraSensorWidth']
                    self.__sensor_height = data[camera_type]['cameraSensorHeight']
                    self.__Icx = data[camera_type]['iCx']
                    self.__Icy = data[camera_type]['iCy']
                    self.__ratio = data[camera_type]['ratio']
                    self.__imageWidth = data[camera_type]['imageWidth']
                    self.__imageHeight = data[camera_type]['imageHeight']
                    self.__calibrationRatio = data[camera_type]['calibrationRatio']
                    self.__parameter0 = data[camera_type]['parameter0']
                    self.__parameter1 = data[camera_type]['parameter1']
                    self.__parameter2 = data[camera_type]['parameter2']
                    self.__parameter3 = data[camera_type]['parameter3']
                    self.__parameter4 = data[camera_type]['parameter4']
                    self.__parameter5 = data[camera_type]['parameter5']
                    self.__import_moildev()
                    self.__initAlphaRho_Table()

                else:
                    print(
                        "Error 1: camera parameter not available, please check your camera type")

    def __initAlphaRho_Table(self):
        """
        Create and calculate a list for initial alpha proportionate with rho image (height image).

        Returns:
            Initial alpha proportionate with rho image table.
        """
        for i in range(1800):
            alpha = i / 10 * 3.1415926 / 180
            self.__alphaToRho_Table.append(
                (self.__parameter0 *
                 alpha *
                 alpha *
                 alpha *
                 alpha *
                 alpha *
                 alpha +
                 self.__parameter1 *
                 alpha *
                 alpha *
                 alpha *
                 alpha *
                 alpha +
                 self.__parameter2 *
                 alpha *
                 alpha *
                 alpha *
                 alpha +
                 self.__parameter3 *
                 alpha *
                 alpha *
                 alpha +
                 self.__parameter4 *
                 alpha *
                 alpha +
                 self.__parameter5 *
                 alpha) *
                self.__calibrationRatio)
            i += 1

        i = 0
        index = 0
        while i < 1800:
            while index < self.__alphaToRho_Table[i]:
                self.__rhoToAlpha_Table.append(i)
                index += 1
            i += 1

        while index < 3600:
            self.__rhoToAlpha_Table.append(i)
            index += 1

    def __import_moildev(self):
        """
        Create Moildev instance from Moildev SDK share object library.

        Returns:

        """
        lib.moildev_new.argtypes = [
            ctypes.c_char_p,
            ctypes.c_double,
            ctypes.c_double,
            ctypes.c_double,
            ctypes.c_double,
            ctypes.c_double,
            ctypes.c_double,
            ctypes.c_double,
            ctypes.c_double,
            ctypes.c_double,
            ctypes.c_double,
            ctypes.c_double,
            ctypes.c_double,
            ctypes.c_double,
            ctypes.c_double]
        lib.moildev_new.restype = ctypes.c_void_p

        self.__moildev = lib.moildev_new(
            self.__camera.encode('utf-8'),
            self.__sensor_width,
            self.__sensor_height,
            self.__Icx,
            self.__Icy,
            self.__ratio,
            self.__imageWidth,
            self.__imageHeight,
            self.__parameter0,
            self.__parameter1,
            self.__parameter2,
            self.__parameter3,
            self.__parameter4,
            self.__parameter5,
            self.__calibrationRatio)
        self.__map_x = np.zeros(
            (self.__imageHeight,
             self.__imageWidth),
            dtype=np.float32)
        self.__map_y = np.zeros(
            (self.__imageHeight,
             self.__imageWidth),
            dtype=np.float32)
        self.__res = self.__create_map_result_image()

    def __create_map_result_image(self):
        """
        Create Maps image from zeroes matrix for result image

        Returns:
            Zeroes matrix.
        """
        size = self.__imageHeight, self.__imageWidth, 3
        return np.zeros(size, dtype=np.uint8)

    def test(self):
        """
        Test to link with Moildev share library

        Returns:
            Hello from C++
        """
        if self.__moildev is not None:
            if platform.system() == "Windows":
                lib.test.argtypes = [ctypes.c_void_p]
                lib.test.restype = ctypes.c_char_p
                print((lib.test(self.__moildev)).decode())
            else:
                lib.test.argtypes = [ctypes.c_void_p]
                lib.test.restype = ctypes.c_void_p
                return lib.test(self.__moildev)
        else:
            return None

    def clean(self):
        """
        clean the memory of pointer.

        Returns:
            None
        """
        lib.cleanup_moildev.argtypes = [ctypes.c_void_p]
        lib.cleanup_moildev.restype = ctypes.c_void_p
        return lib.cleanup_moildev(self.__moildev)

    def getIcx(self):
        """
        Get center image from width image (x axis).

        Returns:

        """
        return self.__Icx

    def getIcy(self):
        """
        Get center image from height image (y axis).

        Returns:

        """
        return self.__Icy

    def getImageWidth(self):
        """
        Get image width.

        Returns:

        """
        return self.__imageWidth

    def getImageHeight(self):
        """Get image height.

        :return: image height
        :rtype: int
        """
        return self.__imageHeight

    def getCalibrationRatio(self):
        """

        Returns:

        """
        return self.__calibrationRatio

    def getAnypointMaps(self, alpha, beta, zoom, mode=1):
        """The purpose is to generate a pair of X-Y Maps for the specified alpha, beta and zoom parameters,
        the result X-Y Maps can be used later to remap the original fisheye image to the target angle image.

        Args:
            :param alpha: alpha
            :type alpha: float
            :param beta: beta
            :type beta: float
            :param zoom: decimal zoom factor, normally 1..12
            :type zoom: int
            :param mode: selection anypoint mode(1 or 2)
            :type mode: int

        Return:
            :return: map_x, map_y
            :rtype: float

        Examples:
            please reference: https://github.com/MoilOrg/moildev
        """
        if self.__moildev is not None:
            if mode == 1:
                if beta < 0:
                    beta = beta + 360
                if alpha < -90 or alpha > 90 or beta < 0 or beta > 360:
                    alpha = 0
                    beta = 0

                else:
                    alpha = -90 if alpha < -90 else alpha
                    alpha = 90 if alpha > 90 else alpha
                    beta = 0 if beta < 0 else beta
                    beta = 360 if beta > 360 else beta
                lib.moil_anypointM.argtypes = [
                    ctypes.c_void_p,
                    ctypes.POINTER(
                        ctypes.c_float),
                    ctypes.POINTER(
                        ctypes.c_float),
                    ctypes.c_int,
                    ctypes.c_int,
                    ctypes.c_double,
                    ctypes.c_double,
                    ctypes.c_double,
                    ctypes.c_double]
                lib.moil_anypointM.restype = None
                mapX = self.__map_x.ctypes.data_as(
                    ctypes.POINTER(ctypes.c_float))
                mapY = self.__map_y.ctypes.data_as(
                    ctypes.POINTER(ctypes.c_float))
                lib.moil_anypointM(
                    self.__moildev,
                    mapX,
                    mapY,
                    self.__imageWidth,
                    self.__imageHeight,
                    alpha,
                    beta,
                    zoom,
                    self.__ratio)

            else:
                if alpha < - 90 or alpha > 90 or beta < -90 or beta > 90:
                    alpha = 0
                    beta = 0

                else:
                    alpha = -90 if alpha < -90 else alpha
                    alpha = 90 if alpha > 90 else alpha
                    beta = -90 if beta < -90 else beta
                    beta = 90 if beta > 90 else beta
                lib.moil_anypointM2.argtypes = [
                    ctypes.c_void_p,
                    ctypes.POINTER(
                        ctypes.c_float),
                    ctypes.POINTER(
                        ctypes.c_float),
                    ctypes.c_int,
                    ctypes.c_int,
                    ctypes.c_double,
                    ctypes.c_double,
                    ctypes.c_double,
                    ctypes.c_double]
                lib.moil_anypointM2.restype = None

                mapX = self.__map_x.ctypes.data_as(
                    ctypes.POINTER(ctypes.c_float))
                mapY = self.__map_y.ctypes.data_as(
                    ctypes.POINTER(ctypes.c_float))
                lib.moil_anypointM2(
                    self.__moildev,
                    mapX,
                    mapY,
                    self.__imageWidth,
                    self.__imageHeight,
                    alpha,
                    beta,
                    zoom,
                    self.__ratio)
            return self.__map_x, self.__map_y
        else:
            return None, None

    def getPanoramaMaps(self, alpha_min, alpha_max):
        """ To generate a pair of X-Y Maps for alpha within 0..alpha_max degree, the result X-Y Maps can be used later
        to generate a panorama image from the original fisheye image..

        Args:
            :param alpha_min: alpha min
            :type alpha_min: float
            :param alpha_max: alpha max
            :type alpha_max: float

        Return:
            :return: pair maps x-y
            :rtype: array

        Examples:
            please reference: https://github.com/MoilOrg/moildev
        """
        lib.moil_panoramaX.argtypes = [
            ctypes.c_void_p,
            ctypes.POINTER(
                ctypes.c_float),
            ctypes.POINTER(
                ctypes.c_float),
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_double,
            ctypes.c_double,
            ctypes.c_double]
        lib.moil_panoramaX.restype = None
        mapX = self.__map_x.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        mapY = self.__map_y.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        lib.moil_panoramaX(
            self.__moildev,
            mapX,
            mapY,
            self.__imageWidth,
            self.__imageHeight,
            self.__ratio,
            alpha_max,
            alpha_min)
        return self.__map_x, self.__map_y

    def anypoint(self, image, alpha, beta, zoom, mode=1):
        """Generate anypoint widget_controller.for mode 1, the result rotation is betaOffset degree rotation around the
        Z-axis(roll) after alphaOffset degree rotation around the X-axis(pitch). for mode 2, The result rotation
        is thetaY degree rotation around the Y-axis(yaw) after thetaX degree rotation around the X-axis(pitch).

        Args:
            :param image: source image
            :type image: array
            :param alpha: alpha
            :type alpha: float
            :param beta: beta
            :type beta: float
            :param zoom: zoom
            :type zoom: int
            :param mode: mode anypoint widget_controller
            :type mode: int

        Return:
            :return: anypoint widget_controller
            :rtype: array

        Examples:
            please reference: https://github.com/MoilOrg/moildev
        """
        map_x, map_y = self.getAnypointMaps(alpha, beta, zoom, mode)
        image = cv2.remap(image, map_x, map_y, cv2.INTER_CUBIC)
        return image

    def panorama(self, image, alpha_min, alpha_max):
        """The panorama image centered at the 3D direction with alpha = iC_alpha_degree and beta = iC_beta_degree

        Args:
            :param image: Original image
            :type image: array
            :param alpha_min: min of alpha. by default it 10 degree.
            :type alpha_min: float
            :param alpha_max: max of alpha. The recommended value is half of camera FOV. For example, use
                        90 for a 180 degree fisheye images and use 110 for a 220 degree fisheye images.
            :type alpha_max: float

        Returns:
            :return: panorama image
            :rtype: array

        Examples:
            please reference: https://github.com/MoilOrg/moildev
        """
        if alpha_min < 10:
            print(
                "Oops!  That was no valid number on alpha_min.  the value must equal or more than 10")
            return None
        else:
            map_x, map_y = self.getPanoramaMaps(alpha_min, alpha_max)
            image = cv2.remap(image, map_x, map_y, cv2.INTER_CUBIC)
            return image

    def __PanoramaM_Rt(self, alpha_max, iC_alpha_degree, iC_beta_degree):
        """
        To generate a pair of X-Y Maps for alpha within 0..alpha_max degree, the result X-Y Maps can be used later
        to generate a panorama image from the original fisheye image. The panorama image centered at the 3D
        direction with alpha = iC_alpha_degree and beta = iC_beta_degree.

        Args:
            . mapX : memory pointer of result X-Map
            . mapY : memory pointer of result Y-Map
            . w : width of the Map (both mapX and mapY)
            . h : height of the Map (both mapX and mapY)
            . magnification : input imageWidth / sensor_width, m_ratio is normally equal to 1.
            . alpha_max : max of alpha. The recommended value is half of camera FOV. For example, use
              90 for a 180 degree fisheye images and use 110 for a 220 degree fisheye images.
            . iC_alpha_degree : alpha angle of panorama center.
            . iC_beta_degree : beta angle of panorama center.

        Returns:
            New mapX and mapY.

        Examples:
            please reference: https://github.com/MoilOrg/moildev
        """
        lib.moil_panoramaM_Rt.argtypes = [
            ctypes.c_void_p,
            ctypes.POINTER(
                ctypes.c_float),
            ctypes.POINTER(
                ctypes.c_float),
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_double,
            ctypes.c_double,
            ctypes.c_double,
            ctypes.c_double]
        lib.moil_panoramaM_Rt.restype = None

        mapX = self.__map_x.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        mapY = self.__map_y.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
        lib.moil_panoramaM_Rt(
            self.__moildev,
            mapX,
            mapY,
            self.__imageWidth,
            self.__imageHeight,
            self.__ratio,
            alpha_max,
            iC_alpha_degree,
            iC_beta_degree)
        return self.__map_x, self.__map_y

    def reverseImage(self, image, alpha_max, alpha, beta):
        """To generate the image reverse image from panorama that can change the focus direction from the original
        images. The panorama reverse image centered at the 3D direction with alpha_max = max of alpha and beta =
        iC_beta_degree.

        Args:
            :param image: source image
            :type image: array
            :param alpha_max: alpha max
            :type alpha_max: float
            :param alpha: alpha
            :type alpha: float
            :param beta: beta
            :type beta: float

        Return:
            :return: reverse widget_controller image
            :rtype: array

        Examples:
            please reference: https://github.com/MoilOrg/moildev
        """
        map_x, map_y = self.__PanoramaM_Rt(alpha_max, alpha, beta)
        panorama_image = cv2.remap(image, map_x, map_y, cv2.INTER_CUBIC)
        if platform.system() == "Windows":
            print("revPanorama available at Moildev library version 1.3.0 \n"
                  "make sure you have install OpenCV and Visual Studio code")
        else:
            lib.moil_revPanorama.argtypes = [
                ctypes.c_void_p,
                ctypes.POINTER(
                    ctypes.c_void_p),
                ctypes.POINTER(
                    ctypes.c_void_p),
                ctypes.c_int,
                ctypes.c_int,
                ctypes.c_double,
                ctypes.c_double,
            ]
            lib.moil_revPanorama.restype = None
            panoramaImage = panorama_image.ctypes.data_as(
                ctypes.POINTER(ctypes.c_void_p))
            res = self.__res.ctypes.data_as(ctypes.POINTER(ctypes.c_void_p))
            lib.moil_revPanorama(
                self.__moildev,
                panoramaImage,
                res,
                self.__imageWidth,
                self.__imageHeight,
                alpha_max,
                beta)
        return self.__res

    def getAlphaFromRho(self, rho):
        """Get the alpha from rho image.

        Args:
            :param rho: rho image
            :type rho: int

        Return:
            :return: alpha
            :rtype: float

        Examples:
            please reference: https://github.com/MoilOrg/moildev
        """
        if rho >= 0:
            return self.__rhoToAlpha_Table[rho] / 10
        else:
            return -self.__rhoToAlpha_Table[-rho] / 10

    def getRhoFromAlpha(self, alpha):
        """Get rho image from alpha given.

        Args:
            :param alpha:alpha
            :type alpha: float

        Return:
            :return: rho image
            :rtype: int

        Examples:
            please reference: https://github.com/MoilOrg/moildev
        """
        return self.__alphaToRho_Table[round(alpha * 10)]

    def getAlphaBeta(self, coordinateX, coordinateY, mode=1):
        """Get the alpha beta from specific coordinate image.

        Args:
            :param mode: the anypoint mode.
            :type mode: int
            :param coordinateX: the coordinate point X axis.
            :type coordinateX: int
            :param coordinateY: the coordinate point Y axis.
            :type coordinateY: int

        Return:
            :return: alpha, beta
            :rtype: float

        Examples:
            please reference: https://github.com/MoilOrg/moildev
        """
        if self.__moildev is not None:
            delta_x = round(coordinateX - self.__imageWidth * 0.5)
            delta_y = round(- (coordinateY - self.__imageHeight * 0.5))
            if mode == 1:
                r = round(
                    math.sqrt(
                        math.pow(
                            delta_x,
                            2) +
                        math.pow(
                            delta_y,
                            2)))
                alpha = self.getAlphaFromRho(r)

                if delta_x == 0:
                    angle = 0
                else:
                    angle = (math.atan2(delta_y, delta_x) * 180) / self.__PI

                beta = 90 - angle

            else:
                alpha = self.getAlphaFromRho(delta_y)
                beta = self.getAlphaFromRho(delta_x)

            return alpha, beta
        else:
            return None, None
