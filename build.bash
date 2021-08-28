source /opt/ros/foxy/setup.bash
rm -rf ~/ros2_ws/install
rm -rf ~/ros2_ws/build
cd ~/ros2_ws/ && colcon build --symlink-install