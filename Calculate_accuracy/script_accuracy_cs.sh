#!/bin/bash


sudo chmod +x ./Test_code_for_RPi/CS.py

ls ./log 2>/dev/null||mkdir ./log


python3 ./Test_code_for_RPi/CS.py | tee ./log/cs.txt