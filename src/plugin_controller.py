from PyQt5 import QtWidgets
import shutil
from moilutils.moilutils import MoilUtils
from plugin_collection import PluginCollection


class PluginController(object):
    def __init__(self, main_controller):
        super(PluginController, self).__init__()
        self.main_controller = main_controller
        self.plugin_win = None
        self.plugins = PluginCollection("plugins")
        self.init_plugin_win()
        self.main_controller.comboBox.addItems(self.plugins.name_application)
        self.connect_button()

    def connect_button(self):
        self.main_controller.btn_open_app.clicked.connect(self.open_application)
        self.main_controller.btn_add_apps.clicked.connect(self.add_application)
        self.main_controller.btn_delete_app.clicked.connect(self.delete_apps)

    def init_plugin_win(self):
        self.plugin_win = []
        for i in range(len(self.plugins.name_application)):
            self.plugin_win.append(QtWidgets.QMainWindow())

    def open_application(self):
        """
        Open application depend on selected application available on comboBox.

        Returns:
            Will hide the main apps window and show the selection application.
        """
        self.main_controller.open_plugin = True
        __index = self.main_controller.comboBox.currentIndex()
        if __index == -1:
            QtWidgets.QMessageBox.warning(None, "Warning", " No Instalation Plugin, please add frist !!")
        else:
            self.plugins.application(self.plugin_win[__index], __index)

    def delete_apps(self):
        """
        Delete selected application from the list.

        Returns:
            None.
        """
        __index = self.main_controller.comboBox.currentIndex()
        if __index == -1:
            QtWidgets.QMessageBox.warning(None, "Warning", " No Instalation Plugin, please add frist !!")
        else:
            name = self.plugins.name_application[__index]
            path = self.plugins.path_folder[__index]
            path = path.split(".")[1]
            path = "./plugins/" + path
            reply = QtWidgets.QMessageBox.question(
                self.main_controller.parent,
                'Message',
                "Are you sure want to delete \n" +
                name +
                " application ?\n",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                shutil.rmtree(path, ignore_errors=True)
                self.plugins.reload_plugins()
                new_list = self.plugins.name_application
                self.main_controller.comboBox.clear()
                self.main_controller.comboBox.addItems(new_list)
                self.init_plugin_win()

    def add_application(self):
        """
        Add application plugin collection.

        Returns:
            None.
        """
        dir_plugin = QtWidgets.QFileDialog.getExistingDirectory(
            self.main_controller.parent, 'Select Application Folder')
        if dir_plugin:
            original = dir_plugin
            target = 'plugins/'
            MoilUtils.copy_directory(original, target)
            self.plugins.reload_plugins()
            new_list = self.plugins.name_application
            self.main_controller.comboBox.clear()
            self.main_controller.comboBox.addItems(new_list)
            self.init_plugin_win()
