# dependencies
```
sudo apt install -y dnsmasq
```

# usb ethernet gadget
*Make usb→computer connection work as network interface*

## configure raspi
> /boot/firmware/config.txt
```
⦗...[all]⦘

# USB Ethernet Gadget
dtoverlay=dwc2
```

> /boot/firmware/cmdline.txt
```
⦗...rootwait⦘ modules-load=dwc2,g_ether
```

> [!IMPORTANT]
> reboot to make changes take effect

## configure networking
Set up usb interface:
> /etc/network/interfaces


### dnsmasq
*DHCP & DNS server to make `ssh bento-dev` possible and automatically assign IPs to computers attached over USB*

> /etc/dnsmasq.d/bento-dev.conf

Make 'bento-dev' route to pi's IP
> /etc/hosts
```
⦗...⦘

192.168.56.10	bento-dev
```

> [!IMPORTANT]
> reboot or run `systemctl restart dnsmasq.service` to make changes take effect
