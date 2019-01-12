source /opt/ros/kinetic/setup.bash
CONTAINER_ID=$(docker ps -aq -f status=running)
export HOST_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.Gateway}}{{end}}' $CONTAINER_ID)
export MY_IP=172.17.0.1
export CONTAINER_IP=172.17.0.2
export ROS_MASTER_URI=http://$CONTAINER_IP:11311
export ROS_IP=$HOST_IP
export ROS_HOSTNAME=$HOST_IP
