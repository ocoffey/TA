# ## Notes:
# remove subprocess32 from requirements.txt
# add apt-get update to the sh
# change python to python3

#! usr/bin/env bash

apt-get update 

apt-get install -y python3-pip python3-dev

pip3 install -r /autograder/source/requirements.txt

