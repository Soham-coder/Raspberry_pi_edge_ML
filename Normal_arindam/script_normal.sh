#!/bin/bash

sudo chmod +x rpi_button_push_normal.py

if [ -d ./log ]; then
  # Take action if log DIR exists. #
  echo "echo creating log DIR ..."
  mkdir -p log
fi

python3 rpi_button_push_normal.py | tee ./log/out.txt