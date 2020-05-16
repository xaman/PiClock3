# Raspberry Pi Zero - Unicorn Mini Hat

### [Raspbian](https://www.raspberrypi.org/downloads/raspbian/)
### [UnicornHatMini Library](https://github.com/pimoroni/unicornhatmini-python)
### [Scroll pHat HD Library](https://github.com/pimoroni/scroll-phat-hd/tree/1b0625786b20d173205f1c461d0b66bba36b77d0)

### Prepare SD Card

```
# Replace disk2 with the disk name
diskutil list
diskutil unmountDisk /dev/disk2
sudo dd if=<PATH_TO_IMG> of=/dev/rdisk2 bs=4m
sync
```

### Enable SSH over USB

[Tutorial](https://desertbot.io/blog/ssh-into-pi-zero-over-usb)

Create this file `touch /Volumes/boot/ssh`

Edit `/Volumes/boot/config.txt` and add `dtoverlay=dwc2`

Edit `/Volumes/boot/cmdline.txt` and add `modules-load=dwc2,g_ether`

Connect with `ssh pi@raspberrypi.local` and the pass `raspberry`

### Setup WiFi

Use `sudo raspi-config` > **Network Options**

### Setup SPI

Use `sudo raspi-config` > **Interfacing Options**

It is also possible to setup the WiFi modifying the file `/etc/wpa_supplicant/wpa_supplicant.conf`:

```
# Network 1
network={
    ssid="SSID1"
    psk="password1"
    key_mgmt=WPA-PSK
}

# Network 2
network={
    ssid="SSID2"
    psk="password2"
    key_mgmt=WPA-PSK
} 
```

### Install Unicorn Hat

```
# Main Python dependency
sudo apt-get install python3
# Package manager
sudo apt-get install python3-pip
# Virtual environments
sudo apt-get install python3-venv
# Python Images Library
sudo apt-get install python3-pil
```

[Creating a virtual Python environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)

```
# Create environment
python3 -m venv env
# Enter the environment
source env/bin/activate
```

**Install project dependencies with PIP**
```
sudo pip3 install unicornhatmini
sudo pip3 install RPi.GPIO
sudo pip3 install spidev
sudo pip3 install gpiozero
sudo pip3 install pycurl
sudo pip3 install schedule
sudo pip3 install tweepy
sudo pip3 install numpy
# Dependencies of the scroll pHat HD library
sudo pip3 install scrollphathd
sudo apt-get install libatlas-base-dev
sudo apt-get install python3-smbus
```

Latest/development library from GitHub:

* `git clone https://github.com/pimoroni/unicornhatmini-python`
* `cd unicornhatmini-python`
* `sudo ./install.sh`
