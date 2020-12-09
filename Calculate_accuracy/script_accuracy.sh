#!/bin/bash

sudo chmod +x ./Test code for RPi/DWT.py
sudo chmod +x ./Test code for RPi/Normal.py

ls ./log 2>/dev/null||mkdir ./log

python3 ./Test code for RPi/DWT.py | tee ./log/dwt.txt
python3 ./Test code for RPi/Normal.py | tee ./log/normal.txt