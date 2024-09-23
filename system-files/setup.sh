YELLOW='\033[1;33m'
NC='\033[0m'

set_owner_and_group_to_root () {
  sudo chown root "$1"
  sudo chgrp root "$1"
}

DEST_SYSCON_ETH="/etc/NetworkManager/system-connections/Schaeufele_Ethernet.nmconnection"
if [ -e $DEST_SYSCON_ETH ]; then
  printf "${YELLOW}WARN: file '$DEST_SYSCON_ETH' already exists. Overwrite? (y/n)${NC}%s "
  read -r YN
else
  YN="Y"
fi
if [ "$YN" = "y" ]||[ "$YN" = "Y" ]; then
  cp "./etc/NetworkManager/system-connections/Schaeufele_Ethernet.nmconnection" $DEST_SYSCON_ETH
  chmod 600 $DEST_SYSCON_ETH
  set_owner_and_group_to_root $DEST_SYSCON_ETH
fi
unset YN


DEST_SYSCON_WIFI="/etc/NetworkManager/system-connections/Schaeufele_Wi-Fi.nmconnection"
if [ -e $DEST_SYSCON_WIFI ]; then
  printf "${YELLOW}WARN: file '$DEST_SYSCON_WIFI' already exists. Overwrite? (y/n)${NC}%s "
  read -r YN
else
  YN="Y"
fi
if [ "$YN" = "y" ]||[ "$YN" = "Y" ]; then
  cp "./etc/NetworkManager/system-connections/Schaeufele_Wi-Fi.nmconnection" $DEST_SYSCON_WIFI
  chmod 600 $DEST_SYSCON_WIFI
  set_owner_and_group_to_root $DEST_SYSCON_WIFI
fi
unset YN


DEST_SYSD_CAN="/etc/systemd/network/80-can.network"
if [ -e $DEST_SYSD_CAN ]; then
  printf "${YELLOW}WARN: file '$DEST_SYSD_CAN' already exists. Overwrite? (y/n)${NC}%s "
  read -r YN
else
  YN="Y"
fi
if [ "$YN" = "y" ]||[ "$YN" = "Y" ]; then
  cp "./etc/systemd/network/80-can.network" $DEST_SYSD_CAN
  chmod 644 $DEST_SYSD_CAN
  set_owner_and_group_to_root $DEST_SYSD_CAN
fi
unset YN
