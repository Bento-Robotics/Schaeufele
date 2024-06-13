FROM ros:humble

WORKDIR /root/

# get libcamera sources
RUN apt-get update && apt-get install -y \
	build-essential \
	meson \
	ninja-build \
	pkg-config \
	libyaml-dev \
	python3-yaml \
	python3-ply \
	python3-jinja2 \
	libssl-dev \
	openssl \
	libudev-dev \
	libevent-dev \
	libdrm-dev \
	git \
	udev \
	&& rm -rf /var/lib/apt/lists/*

# build libcamera
RUN git clone https://git.libcamera.org/libcamera/libcamera.git	&&\
    cd libcamera	&&\
    meson setup build	&&\
    ninja -C build install

# build camera_ros 'fix_dynamic_extent' branch (fixes some cameras)
RUN mkdir -p /camera_ws/ &&\
    cd /camera_ws/ &&\
    git clone https://github.com/christianrauch/camera_ros.git src/camera_ros &&\
    cd src/camera_ros &&\
    git checkout fix_dynamic_extent &&\
    cd - &&\
    apt-get update &&\
    bash -c " \
        . /opt/ros/$ROS_DISTRO/setup.bash &&\
        rosdep install --from-paths src --ignore-src -y --skip-keys='libcamera image_view ament_lint_auto ament_cmake_clang_format ament_cmake_cppcheck ament_cmake_flake8 ament_cmake_lint_cmake ament_cmake_mypy ament_cmake_pep257 ament_cmake_pyflakes ament_cmake_xmllint' &&\
        colcon build --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release \
    " &&\
    rm -rf /var/lib/apt/lists/*

# insert before last line (no. 6)
RUN sed -i '6i\source "/camera_ws/install/setup.bash" --\' /ros_entrypoint.sh

ENTRYPOINT [ "/ros_entrypoint.sh" ]
