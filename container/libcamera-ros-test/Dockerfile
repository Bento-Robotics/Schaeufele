FROM ros:humble

WORKDIR /root/

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
	ros-humble-camera-ros \
	&& rm -rf /var/lib/apt/lists/*

RUN git clone https://git.libcamera.org/libcamera/libcamera.git	&&\
    cd libcamera	&&\
    meson setup build	&&\
    ninja -C build install
