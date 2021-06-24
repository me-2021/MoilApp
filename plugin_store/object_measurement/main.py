from .controller import ControllerMain
from base_plugin import Plugin


class ObjectMeasurement(Plugin):
    def __init__(self):
        """
        The class that represent the plugins application, class name will be read as
        the name of application.
        """
        super().__init__()
        self.apps = None
        self.description = "This is default application"

    def perform_operation(self, argument):
        """
        The main application will execute this function when click button open.

        Args:
            argument (): is the object widget from main application class.

        Returns:
            Will show the window of application.

        """
        self.apps = ControllerMain(argument)
        argument.show()
