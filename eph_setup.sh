#!/bin/bash
sudo apt-get -y install libi2c-dev i2c-tools python-smbus libfuse-dev python-imaging ttf-freefont
make rpi
sudo make rpi-install
