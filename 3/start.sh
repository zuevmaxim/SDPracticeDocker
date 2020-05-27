#! /bin/bash

chmod +x docker_routine.sh
d=`pwd`
sudo docker run \
  -p 127.0.0.1:5665:5665 \
  -v $d:/home/m \
  -it ubuntu \
  /home/m/docker_routine.sh

