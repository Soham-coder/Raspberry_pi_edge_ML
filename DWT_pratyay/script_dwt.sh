#!/bin/bash

sudo chmod +x rpi_button_push_dwt.py

if [ -d ./log ]; then
  # Take action if log DIR exists. #
  echo "echo creating log DIR ..."
  mkdir -p log
fi

python3 rpi_button_push_dwt.py | tee ./log/out.txt