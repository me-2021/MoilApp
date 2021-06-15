import serial
import logging


class ThreadAxisAPI(object):
    def __init__(self):
        self.serial_port = None
        self.ser = serial.Serial(self.serial_port, 9600, timeout=0.5)
        logging.basicConfig(
            filename='../log/Axis_control.log',
            filemode='w',
            format='%(asctime)s: %(name)s - %(levelname)s - %(message)s',
            datefmt='%d-%b-%y %H:%M:%S')

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.logger.info("SYSTEM STARTED")

    def axis_init(self):
        """
        Move the axis in init position.

        Returns:
            None
        """
        self.ser.write(str.encode('H \r\n'))
        self.logger.info("BACK to init position: 0 mm")

    def reset(self):
        """
        Define the position and seed in default value.

        Returns:
            None
        """
        self.absolute_moving(0)
        self.default_speed()
        self.logger.info("SYSTEM RESET")

    def absolute_moving(self, distance):
        """
        Moving the axis with Absolute motion is the change of
        position from one absolute place to another.

        Args:
            distance (): distance value

        Returns:
            None
        """
        self.ser.write(str.encode('MA ' + str(distance) + '\r\n'))
        self.logger.info("Absolute_moving:" + str(distance) + "mm")

    def related_moving(self, distance):
        """
        Move the axis from one relative place to another.

        Args:
            distance ():distance value

        Returns:
            None
        """
        self.ser.write(str.encode('MR ' + str(distance) + '\r\n'))
        self.logger.info("Related_moving:" + str(distance) + "mm")

    def default_speed(self):
        """
        Set the speed value to default.

        Returns:
            None
        """
        self.ser.write(str.encode('VM=500 \r\n'))
        self.logger.info("Set default speed:500RPS")

    def set_speed(self, speed):
        """
        Set the speed value to speed value given by user.

        Args:
            speed (): speed value

        Returns:
            None
        """
        self.ser.write(str.encode('VM=' + str(speed) + '\r\n'))
        self.logger.info("set speed:" + str(speed) + "RPS")

    def show_position(self):
        """
        Show the current position of axis.

        Returns:
            None
        """
        self.ser.write(str.encode('?PC \r\n'))
        self.read_position()

    def connect_serial(self, serial_port):
        """
        Connect the serial port axis controller to the system.

        Args:
            serial_port (): the serial port of axis controller

        Returns:
            None
        """
        self.serial_port = serial_port
        self.ser = serial.Serial(self.serial_port, 9600, timeout=0.5)
        self.logger.info('SYSTEM CONNECTED')

    def disconnect_serial(self):
        """
        Disconnect the serial port axis controller.

        Returns:
            None
        """
        self.ser.close()
        self.logger.info('SYSTEM DISCONNECTED')

    def read_position(self):
        """
        Read the axis current position.

        Returns:
            None
        """
        data = self.ser.read(1024)
        data_str = data.decode(encoding='UTF-8')
        data_split = data_str.split('\r\n')
        print(data_split)
        print('Current Position: ' + str(data_split[-2]) + " mm")