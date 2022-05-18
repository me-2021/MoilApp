#########################################################################
#   MoilApp (Applications for sophisticated fisheye image processing)   #
#   Written by Haryanto (haryanto@o3635.mcut.edu.tw)                    #
#   Based on Moil-Lab (Ming Chi University of Technology)               #
#########################################################################

import sys
from PyQt5 import QtWidgets
from Moilapp_Controller import Controller


def main():
    """
    Create instance Main window to create the main window of Application.

    Returns:
        None.
    """

    apps = QtWidgets.QApplication(sys.argv)
    # QApplicatiom is a class of QtWidgets package
    # An QApplication instance is created, named as apps

    as_root = QtWidgets.QMainWindow()
    # QMainWindow is a class of QtWidgets package
    # An QMainWindow instance is created, named as MainWindow

    ui = Controller(as_root)  #__new__(), __init__()
    # Controller is customer designed
    # Its __init__() locates ui components to MainWindow

    as_root.show()
    #  MainWindow.show() is called

    sys.exit(apps.exec_())
    # apps.exec_() is endless loop to process event, such as user's clicking


if __name__ == '__main__':
    main()

# except ImportError as err:
#     print("\nThe environment not match requirement, "
#           "\nPlease install all the library, or read the Readme doc to do it.")
#     print("-----------------------------------------------------------------")
#     print(err)
