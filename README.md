# ros_stack
MP files for ECE 498 **principles of safe autonomy**

## Run the code
Complete the following steps
1. In the terminal window type the following
```
nvidia-docker  run --env="DISPLAY" -e "KEY=API_KEY" -e "PORTAL_URL=https://illini.righthook.io" -v /tmp/.X11-unix:/tmp/.X11-unix:rw -v /usr/lib/x86_64-linux-gnu/libXv.so.1:/usr/lib/x86_64-linux-gnu/libXv.so.1 --ulimitnofile=65535:65535 rh_sim/minimaps:c000140725e017ab00810eea6ab55e1cc9310182
```
**Note:API_KEY will be given to you**

2. Start a new terminal and clone this repository
```
git clone https://github.com/pulkitkatdare/ros_stack.git
```
3. change directory to this repository 
```
cd ros_stack
```
4. build the ros repository
```
catkin_make
```
5. run ros set configuration files
```
./setup.sh
```
6. start the simulation 
```
./run.sh
```
### End Simulation 
7. End simulation
```
./kill.sh
```
