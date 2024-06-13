import os
import yaml

from launch import LaunchDescription
from launch_ros.actions import Node

from launch.substitutions import EnvironmentVariable, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    bento_drive = Node(
        package='bento_drive',
        executable='bento_drive_node',
        name='bento_drive_node',
        parameters=[ PathJoinSubstitution([ './', 'parameters', 'schaeufele.yaml' ]) ],
        namespace=EnvironmentVariable( 'EDU_ROBOT_NAMESPACE', default_value="bento" ),
        output='screen',
	emulate_tty=True,
    )

    camera_ros = Node(
        package='camera_ros',
        executable='camera_node',
        name='camera_node',
        parameters=[ PathJoinSubstitution([ './', 'parameters', 'camera_ros.yaml' ]) ],
        namespace=EnvironmentVariable( 'EDU_ROBOT_NAMESPACE', default_value="bento" ),
    )

    return LaunchDescription([
        bento_drive,
        camera_ros,
    ])
