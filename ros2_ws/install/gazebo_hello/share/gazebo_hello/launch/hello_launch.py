from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    pkg_path = get_package_share_directory('gazebo_hello')
    urdf_path = os.path.join(pkg_path, 'urdf', 'pan_tilt.urdf')

    gazebo = ExecuteProcess(
        cmd=['gazebo', '--verbose', urdf_path, '-s', 'libgazebo_ros_factory.so'],
        output='screen'
    )


    pan_tilt_motion = Node(
        package="gazebo_hello",
        executable="pan_tilt_motion",
        name="pan_tilt_motion",
        output="screen"
    )

    return LaunchDescription([
        gazebo,
        pan_tilt_motion
    ])
