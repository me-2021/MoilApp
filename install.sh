#!/bin/bash

sudo apt update
wget https://github.com/MoilOrg/MoilApp/releases/download/v3.2/MoilApp.deb
sudo dpkg -i MoilApp.deb
rm MoilApp.deb
echo "alias moilapp='/opt/MoilApp/MoilApp'" >> ~/.bashrc
source ~/.bashrc
echo -e ">>Good Luck, Haryanto<<"
