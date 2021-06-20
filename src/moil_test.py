from Moildev import Moildev
import cv2

image = cv2.imread("../SourceImage/image.jpg")
camera_type = "Raspi"

moil = Moildev("cam_params/camera_parameters.json", camera_type)
mapx, mapy = moil.getAnypointMaps(0, 50, 4, 2)
image = cv2.remap(image, mapx, mapy, cv2.INTER_CUBIC)
result = cv2.resize(image, (800, 600), interpolation=cv2.INTER_AREA)

cv2.imshow("Result", result)
cv2.waitKey()