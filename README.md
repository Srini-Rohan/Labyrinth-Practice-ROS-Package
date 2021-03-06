# Labyrinth-Practice-ROS-Package

This Repository contains practice package for event Labyrinth - Technex 2022.

### Recommended System Requirements

1. Ubuntu 18.04
2. ROS Melodic
3. Gazebo 9.0

To run package in ROS Noetic do the following changes

In [spy.py](spy/src/spy.py) change the below line
```python
#!/usr/bin/env python
```
to
```python
#!/usr/bin/env python3
```

### Run the Simulation

Clone this repository in the `src` folder of your catkin workspace.

```bash
gedit .bashrc
# A window will be opened add the below command
source catkin_ws/devel/setup.bash
```

Inside your workspace folder, run catkin_make.

```bash
roscd labyrinth
pwd
```

Copy the output of the above command
```bash
cd
gedit .bashrc
```
A window will be opened add the below command and save it
```bash
export GAZEBO_MODEL_PATH=<Copied Output>/worlds$GAZEBO_MODEL_PATH
```
In a new terminal run the below command to launch the practice arena with husky

```bash
roslaunch labyrinth labyrinth_husky_arena.launch 
```
