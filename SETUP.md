# Raspberry Pi Zero - Unicorn Mini Hat

## [Raspbian](https://www.raspberrypi.org/downloads/raspbian/)
## [Python 3 library](https://github.com/pimoroni/unicornhatmini-python)

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
sudo aptitude install python3
sudo aptitude install python3-pip
sudo aptitude install python3-pil
```

```
sudo pip3 install unicornhatmini
sudo pip3 install scrollphathd
sudo pip3 install RPi.GPIO
sudo pip3 install spidev
sudo pip3 install gpiozero
sudo pip3 install pycurl
sudo pip3 install schedule
sudo pip3 install tweepy
```

Latest/development library from GitHub:

* `git clone https://github.com/pimoroni/unicornhatmini-python`
* `cd unicornhatmini-python`
* `sudo ./install.sh`
