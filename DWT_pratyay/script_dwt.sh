#!/bin/bash

sudo chmod +x rpi_button_push_dwt.py

ls ./log 2>/dev/null||mkdir ./log

python3 rpi_button_push_dwt.py | tee ./log/out.txt