The scripts in this directory have been tested with Bookworm.

If you're in doubt, run the following command in terminal: `cat /etc/os-release | grep PRETTY_NAME`. If you get `PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"` then we're on the right track.

1. Boot from USB: `sudo raspi-config` > `6 Advanced Options` > `A4 Boot Order` > `B1 SD Card Boot  Boot from SD Card if available, otherwise boot from NVMe`.
2. Disable power limits: `sudo raspi-config` > `4 Performance Options` > `P4 USB Current` > `Would you like the USB current limit to be disabled?` > `<Yes>`