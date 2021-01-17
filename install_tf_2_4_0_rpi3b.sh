#!/bin/bash


#command -v git >/dev/null 2>&1 || {echo >&2 "Git is not installed.Installing..."; sudo apt-get install git} 
echo "Tensorflow installed version is -->"
sudo pip3 show tensorflow
echo "Uninstalling present tensorflow..."
sudo pip3 uninstall protobuf
sudo pip3 uninstall tensorflow
sudo pip3 uninstall tensorflow-cpu
sudo pip3 uninstall tensorflow-gpu
echo "Uninstalling tensorflow related to python3-pip just for cross check..."
python3 -m pip uninstall protobuf
python3 -m pip uninstall tensorflow
python3 -m pip uninstall tensorflow-cpu
python3 -m pip uninstall tensorflow-gpu

echo "Checking current os, python and pip versions"
cat /etc/os-release 
python3 --version
pip3 --version

echo "Upgrading pip, setup_tools, and installing tensorflow 2.x dependencies ..."
sudo pip install --upgrade pip
sudo pip3 install --upgrade setuptools
sudo pip3 install numpy==1.19.0

sudo apt-get install -y libhdf5-dev libc-ares-dev libeigen3-dev gcc gfortran python-dev libgfortran5 \
                          libatlas3-base libatlas-base-dev libopenblas-dev libopenblas-base libblas-dev \
                          liblapack-dev cython libatlas-base-dev openmpi-bin libopenmpi-dev python3-dev
sudo pip3 install keras_applications==1.0.8 --no-deps
sudo pip3 install keras_preprocessing==1.1.0 --no-deps
sudo pip3 install h5py==2.9.0
sudo pip3 install pybind11
pip3 install -U --user six wheel mock

echo "Getting tensorflow-2.4.0..."
wget "https://raw.githubusercontent.com/PINTO0309/Tensorflow-bin/master/tensorflow-2.4.0-cp37-none-linux_armv7l_download.sh"
chmod +x tensorflow-2.4.0-cp37-none-linux_armv7l_download.sh
./tensorflow-2.4.0-cp37-none-linux_armv7l_download.sh
echo "Installing tensorflow=2.4.0 in rpi3b+ ARM..."
sudo pip3 uninstall tensorflow
sudo -H pip3 install tensorflow-2.4.0-cp37-none-linux_armv7l.whl

echo "Installation finished! :) Restart terminal and check"

echo "How to Check installation?"
echo "@@@@@@@@@@@@@@@@@@"
echo "$ python3"
echo ">>> import tensorflow"
echo ">>> tensorflow.__version__"
echo "2.4.0"
echo ">>> exit()" 
