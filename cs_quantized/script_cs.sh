#!/bin/bash

sudo chmod +x rpi_button_push_vgg16.py

ls ./log 2>/dev/null||mkdir ./log

python3 rpi_button_push_vgg16.py | tee ./log/out.txt