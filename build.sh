#!/bin/bash

function print_blue(){
	printf "\033[34;1m"
	printf "$@ \n"
	printf "\033[0m"
}

print_blue '===================================================='
print_blue "Install all dependencies library to run this project"
sudo apt update -y
sudo apt-get install -y python3-venv \
      build-essential \
      libexiv2-dev \
      python3-dev \
      qttools5-dev-tools \
      qttools5-dev

echo -e ""
print_blue "1. Create Virtual environment"
python3 -m venv venv
source ./venv/bin/activate
pip install pip --upgrade

echo -e ""
print_blue "2. Install the requirements library"
pip install -r requirement.txt
c++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) \
    src/moilutils/exif.cpp -o src/moilutils/exif$(python3-config --extension-suffix) \
    `pkg-config --cflags --libs python3` -I/usr/local/include -L/usr/local/lib -lexiv2

echo -e ""
print_blue ">>Good Luck, Haryanto<<"
print_blue '===================================================='
