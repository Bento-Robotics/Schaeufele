import os
import yaml

from launch import LaunchDescription
from launch_ros.actions import Node

from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch.actions import GroupAction
from launch_ros.actions import PushRosNamespace

from launch.substitutions import EnvironmentVariable, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    bento_drive = Node(
        package='bento_drive',
        executable='bento_drive_node',
        name='bento_drive_node',
        parameters=[ PathJoinSubstitution([ './', 'parameters', 'schaeufele.yaml' ]) ],
        output='screen',
	emulate_tty=True,
    )

    camera_ros_1 = Node(
        package='camera_ros',
        executable='camera_node',
        name='camera_node_1',
        parameters=[ PathJoinSubstitution([ './', 'parameters', 'camera_ros-1.yaml' ]) ],
        namespace="cam1",
        emulate_tty=True,
    )

    camera_ros_2 = Node(
        package='camera_ros',
        executable='camera_node',
        name='camera_node_2',
        parameters=[ PathJoinSubstitution([ './', 'parameters', 'camera_ros-2.yaml' ]) ],
        namespace="cam2",
        emulate_tty=True,
    )

    lidar = Node(
        name='rplidar_composition',
        package='rplidar_ros',
        executable='rplidar_composition',
        output='screen',
        emulate_tty=True,
        parameters=[{
            'serial_port': '/dev/ttyUSB0',
            'serial_baudrate': 115200,  # A1 / A2
            # 'serial_baudrate': 256000, # A3
            'frame_id': 'laser',
            'inverted': False,
            'angle_compensate': True,
        }],
    )

    tf2_node = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='base_link_to_base_tof',
        arguments=["--x", "0.0","--y", "0.0","--z", "0.1","--roll", "0.0","--pitch", "0.0","--yaw", "0.0",
        #TODO add values
        "--frame-id", "base_link","--child-frame-id", "laser"],
        output="screen"
    )

    return LaunchDescription([
        GroupAction(
        actions=[
            PushRosNamespace(EnvironmentVariable( 'EDU_ROBOT_NAMESPACE', default_value="bento" )),

            camera_ros_1,
            camera_ros_2,
            bento_drive,
        ]),
	lidar,
        tf2_node
    ])
