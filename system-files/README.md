# general
```
sudo apt install docker.io docker-compose dnsmasq-base git gh can-utils btop tree iperf3 
sudo usermod -aG docker bento 
<restart session (logout & login again)>
git clone https://github.com/Bento-Robotics/Schaeufele/
cd Schaeufele/container
docker-compose up
```

> [!NOTE]
> Host configuration in `Schaeufele/system-files/README.md`



# set up CAN interfaces

> /boot/firmware/config.txt (under `[all]`)
```
dtoverlay=spi1-2cs
dtoverlay=mcp251xfd,spi0-0,oscillator=40000000,interrupt=25
dtoverlay=mcp251xfd,spi0-1,oscillator=40000000,interrupt=13
dtoverlay=mcp251xfd,spi1-0,oscillator=40000000,interrupt=24
```

> /etc/systemd/network/80-can.network
```
sudo systemctl enable systemd-networkd
```

> [!IMPORTANT]
> reboot to make changes take effect


# USB Ethernet Gadget (eth over usb-c port)

> /boot/firmware/config.txt (under `[all]`)
```
dtoverlay=dwc2
```

> /boot/firmware/cmdline.txt (after `rootwait`)
```
<...rootwait> modules-load=dwc2,g_ether <other stuff after rootwait can be here>
```

> [!IMPORTANT]
> reboot to make changes take effect


# networking

> /etc/sysctl.conf

> /etc/NetworkManager/system-connections/*
```
sudo chmod 600 ./*
sudo chown root ./*
sudo chgrp root ./*
```

*set country (with `sudo raspi-config`) (to US)*

Make 'bento-dev' route to pi's IP (currently not working)
> /etc/hosts (any line really)
```
192.168.56.10	bento-dev
```


> [!IMPORTANT]
> reboot to make changes take effect
