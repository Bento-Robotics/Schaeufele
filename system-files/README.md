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

## configure networks (no longer working!)
Set up usb interface:
> /etc/network/interfaces


### networking
*DHCP (& DNS) server to make `ssh bento-dev` possible and automatically assign IPs to computers attached over USB and WiFi*

> /etc/NetworkManager/system-connections/schaeufele_wifi.nmconnection


Make 'bento-dev' route to pi's IP (currently not working)
> /etc/hosts
```
⦗...⦘

192.168.56.10	bento-dev
```
