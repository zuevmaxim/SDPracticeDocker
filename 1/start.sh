#! /bin/bash

chmod +x docker_routine.sh
d=`pwd`
sudo docker run \
  -v $d:/home/m \
  -it ubuntu \
  /home/m/docker_routine.sh

