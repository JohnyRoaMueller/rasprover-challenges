#!/bin/bash

# Set XDG runtime dir manually (important for audio, PulseAudio, etc.)

##-> set user-session without active login (just threw the starting script)
#sudo loginctl enable-linger FlottiRobotti

##-> set user-session manuelly
#export XDG_RUNTIME_DIR=/run/user/1000
#mkdir -p $XDG_RUNTIME_DIR
#chmod 700 $XDG_RUNTIME_DIR

# Optional: ensure pulse subdir exists
#mkdir -p $XDG_RUNTIME_DIR/pulse
#chmod 700 $XDG_RUNTIME_DIR/pulse

[ -f ~/.bashrc ] && source ~/.bashrc
cd ~/ugv_rpi/ && source ugv-env/bin/activate && jupyter lab --ip=0.0.0.0 --port=8888 --no-browser
