FROM bentorobotics/rosbox:robot

WORKDIR /bento_ws

# Get sources
RUN git clone https://github.com/Bento-Robotics/bento_drive src/bento_drive	&&\
    git clone https://github.com/christianrauch/camera_ros src/camera_ros	&&\
    git -C ./src/camera_ros checkout fix_dynamic_extent

# Build workspace
RUN apt-get update &&\
    apt-get install ros-humble-rplidar-ros &&\
    bash -c " \
        . /opt/ros/$ROS_DISTRO/setup.bash &&\
        rosdep install --from-paths src --ignore-src --skip-keys='image_view ament_lint_auto ament_cmake_clang_format ament_cmake_cppcheck ament_cmake_flake8 ament_cmake_lint_cmake ament_cmake_mypy ament_cmake_pep257 ament_cmake_pyflakes ament_cmake_xmllint' &&\
        colcon build --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release \
    " &&\
    rm -rf /var/lib/apt/lists/*

# Build workspace
RUN bash -c " \
	 . /opt/ros/$ROS_DISTRO/setup.bash &&\
         colcon build --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release \
	 "

# Set entrypoint again (it seems to forget the rosbox one)
ENTRYPOINT [ "/entrypoint.sh" ]
