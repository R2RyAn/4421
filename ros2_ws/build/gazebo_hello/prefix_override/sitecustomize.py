import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/rayan/Desktop/test/ros2_ws/install/gazebo_hello'
