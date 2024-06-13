FROM bentorobotics/rosbox:robot

WORKDIR /bento_ws

# Install dependencies & utilities
RUN apt-get update && apt-get install -y \
	ros-humble-camera-ros \
	&& rm -rf /var/lib/apt/lists/*

# Get sources
RUN cd src/		&&\
    git clone https://github.com/Bento-Robotics/bento_drive	&&\
    cd -

# Build workspace
RUN bash -c " \
	 . /opt/ros/$ROS_DISTRO/setup.bash &&\
         colcon build --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release \
	 "

# Set entrypoint again (it seems to forget the rosbox one)
ENTRYPOINT [ "/entrypoint.sh" ]
