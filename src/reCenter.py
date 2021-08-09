from moilutils import MoilUtils
from PyQt5 import QtWidgets


class RecenterImage(object):
    def __init__(self, parent):
        super(RecenterImage, self).__init__()
        self.parent = parent
        self.icx = None
        self.icy = None
        self.alpha = None
        self.beta = None
        self.alphaMax = None

    def onclickRecenter(self):
        if self.parent.type_camera:
            self.parent.moildev = MoilUtils.connectToMoildev(self.parent.type_camera)
            self.alphaMax = self.parent.moildev.getCameraFov()/2
            self.parent.setIcx.setValue(self.parent.moildev.getIcx())
            self.parent.setIcy.setValue(self.parent.moildev.getIcy())
            self.icx = self.parent.setIcx.value()
            self.icy = self.parent.setIcy.value()
            self.parent.show_to_window()

        else:
            QtWidgets.QMessageBox.information(self.parent.parent,
                                              "Warning", "This image not support for this application. \n "
                                                         "Please contact developer!!")

    def returnImage(self, alpha=None, beta=None):
        if alpha is None and beta is None:
            alpha = self.alpha
            beta = self.beta
        else:
            alpha = alpha
            beta = beta
        recImage = self.parent.moildev.reverseImage(self.parent.image.copy(), self.alphaMax, alpha, beta)
        # print(recImage)
        return recImage

    def positionCoorX(self):
        """Change the position coordinate center X on image recenter process
        """
        self.icx = self.parent.setIcx.value()
        self.icy = self.parent.setIcy.value()
        self.parent.point = (self.icx, self.icy)
        self.alpha, self.beta = self.parent.moildev.getAlphaBeta(self.icx, self.icy)
        self.parent.show_to_window()

    def positionCoorY(self):
        """Change the position coordinate center Y on image recenter process
        """
        self.icx = self.parent.setIcx.value()
        self.icy = self.parent.setIcy.value()
        self.parent.point = (self.icx, self.icy)
        self.alpha, self.beta = self.parent.moildev.getAlphaBeta(self.icx, self.icy)
        self.parent.show_to_window()
