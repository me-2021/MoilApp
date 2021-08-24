from plugin_store.tutorial_sample.ui.dialog_second_window import Ui_DialogSecondWindow


class UiControllerSecondWindow(Ui_DialogSecondWindow):

    def __init__(self, current_window, parent_window):
        super(UiControllerSecondWindow, self).__init__()
        self.current_window = current_window
        self.parent_window = parent_window
        self.setupUi(self.current_window)

        self.connect_event()

    def connect_event(self):
        pass
