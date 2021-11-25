# Install the spinnaker SDK to use EasyPySpin library

EasyPySpin is an unofficial wrapper for FLIR [Spinnaker SDK](https://www.flir.com/products/spinnaker-sdk/). This wrapper provides much the same way as the Open-CV Video Capture class. In order to use the easypyspin library, you must first install PySpin and open-CV. The instructions for installing PySpin from scratch may be found here.

1. Download Spinnaker SDK from [here](https://www.flir.com/support-center/iis/machine-vision/downloads/spinnaker-sdk-and-firmware-download/).

   ![](/home/anto/Documents/MoilApp/assets/spin_1.png)

   

2. Choose a folder that corresponds to your computer's Operating System (OS).

   ![](/home/anto/Documents/MoilApp/assets/spin_2.png)

3. This is an example when you select a Linux folder

   ![](/home/anto/Documents/MoilApp/assets/spin_3.png)

4. Then select the precise version you're running; you'll be given the option of using an ARM or AMD-based processor. Then, depending on what you use, download one.

   ![](/home/anto/Documents/MoilApp/assets/spin_4.png)

5. Once you've downloaded the file, unzip it and navigate to the installation location, then follow the instructions in the readme. The installation command line for this SDK is as follows: 

   ```
   $ sudo sh install_spinnaker.sh
   ```

   

6. After you've completed the installation, you'll need to install PySpin for Python. Depending on your Python version, you can download the file here.

   ![](/home/anto/Documents/MoilApp/assets/spin_5.png)

7. After you've downloaded the file, you'll need to unzip it. Install the library by opening the directory and use the command line bellow. Make sure it's installed in the **MoilApp virtual environment**.

   ```
   $ pip install --user spinnaker_python-2.x.x.x-cp36-cp36m-linux_x86_64.whl
   ```

   

8. the final step is Installing the easyPySpin library. You simply need to run the command line below; if all of the requirements are met, you will not receive an error message and this library will be available for usage.

   ```
   $ pip install EasyPySpin
   ```

   