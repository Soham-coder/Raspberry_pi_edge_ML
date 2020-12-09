#!/bin/bash

sudo chmod +x rpi_button_push_normal.py

ls ./log 2>/dev/null||mkdir ./log

python3 rpi_button_push_normal.py | tee ./log/out.txt