#!/bin/bash

sudo chmod +x ./Test_code_for_RPi/DWT.py


ls ./log 2>/dev/null||mkdir ./log

python3 ./Test_code_for_RPi/DWT.py | tee ./log/dwt.txt
