from . import ui_mainwindow


class UiController(ui_mainwindow.Ui_MainWindow):
    def __init__(self, mainWindow):
        super(UiController, self).__init__()
        self.parent = mainWindow
        self.setupUi(self.parent)
