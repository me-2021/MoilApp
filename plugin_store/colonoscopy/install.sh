#!/bin/bash

echo -e ">>>Install all dependencies library to run colonoscoy<<<<"
#sudo apt update -y

FILE=center_colon.h5
if [ -f "$FILE" ]; then
    echo "$FILE exists."
else 
    echo "$FILE does not exist."
    wget https://github.com/MoilOrg/MoilApp/releases/download/V.3.1/center_colon.h5
fi

source ../../venv/bin/activate

echo -e "\n Install the requirements library"
pip install -r requrements.txt

echo -e ">>Good Luck, Haryanto<<"

