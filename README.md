# Matrix-Clock
## Introduction
Inspired by [@NoaNoa's BIFRÖST LED matrix](https://www.printables.com/model/434061-bifrost-led-matrix-case) on printables, I started my own version of a clock based around a 32x8 WS2812B neopixel matrix. I liked the sleek design of his version, which I took as an inspiration for my hardware design. Using a white 3D-printed diffuser especially gives it a more polished look. On the software side however, I wanted to make something new from the ground up. Instead of reusing WLED for this project, I opted to make my own implementation based around a Flask webserver and python backend. This made it possible to implement features specifically for this usecase, without overloading it with things, that aren't needed. To allow for a more robust and faster web interface, I opted to use a Raspberry Pi Zero W instead of a microcontroller like the ESP 32. Even though this is somewhat overkill, it enables more flexibility while also being relatively cheap.
![alt text](https://github.com/cyrillvalentini/Matrix-Clock/blob/main/images/title.png?raw=true)
## Features
Currently the clock has two modes which can be selected. Either, the whole matrix can be used to display an image, which can be drawn in the buit-in editor. The other mode diplays the time, while also allowing the rest of the diplay to be colored.  For both modes there's an option to download and upload a design. The brightness can be manually adjusted or set to auto, which will change the brightness acording to the time. 

More feautures can always be added.
![alt text](https://github.com/cyrillvalentini/Matrix-Clock/blob/main/images/page.png?raw=true)

## Materials
### Electronics
- Raspberry Pi Zero W
- 32x8 WS2812B neopixel matrix
- Micro USB cable
- 5V 10A PSU
- barrel jack
- 300 Ohm resitor
- 1000 uF capacitor
- wires
### Hardware
- 14x M2 10mm screws
- 4x M2 5mm screws
- 6x M2 nuts
- 326x87x2mm clear acrylic panel
- 326x87mm tint foil
### 3D prints
- white filament (diffuser left & diffuser right)
- colored filament e.g. black ( cage left, cage right, shell left, shell right, 4x standoff)

PLA filament seems to be sufficient, although more temperature resistant filament like PETG might be more suitable.
## Assembly
The assembly of the clock is relaively simple. First, the two parts of the cage can be bolted together with the M2 10mm screws and nuts. After pressing in the four standoffs for the display, all the electronics can be mounted an soldered together. By shure to install the operating system on the SD card first and to enable SSH so that the Raspberry Pi can be configured wirelessly. The rest of the assembly follows a sandwich structure. On top of the display, the two parts of the diffuser can be laid on top followed by the acrylic panel. Optionally, the panel can be tinted using a foil intended for tinting windows. This gives the Clock a more "retro" look. Although the process of fitting the foil onto the acryl panel hard to be done without bubbles. For the last part, the two parts of the shell can be slid on. To hold everything in place, eight M2 10mm screws can be bolted into the holes on the sides.
![alt text](https://github.com/cyrillvalentini/Matrix-Clock/blob/main/images/assembly.png?raw=true)
### Wiring
The display runs on 5V. To connnect the raspberry Pi to the same power input, a micro USB cable can be cut apart and soldered to the input. The signal wire from the display is connected to pin 18 over a 300 Ohm resistor.
![alt text](https://github.com/cyrillvalentini/Matrix-Clock/blob/main/images/wiring-diagram.png?raw=true)
## Installation

### Installing Raspbian
As an operating system Raspian Bookworm was used, although other distributions should work fine as well. Be shure to configure the wifi to which the clock should later connect, as well as enabling SSH access.
### Installing dependencies
For the Matrix Clock to work, following dependencies have to be installed.
```bash
# update system
sudo apt update && upgrade
# installing dependencies
sudo apt install git python3 python3-pip ufw
# installing required python modules
sudo pip3 install Flask rpi_ws281x adafruit-circuitpython-neopixel
sudo python3 -m pip install --force-reinstall adafruit-blinka
```
### Clone repository
```bash
#Clone repository in preferred directory
git clone https://github.com/cyrillvalentini/Matrix-Clock
```
### Configure systemd and start service
For the clock to start automatically, a systemd service must be configured. 

In matrix-clock.service both the working directory as well as the path to the executable main.py has to be changed from <directory> to the actual directory.

```bash
[Unit]
Description="Matrix Clock server"
After=network.target

[Service]
User=root
WorkingDirectory=<directory>
ExecStart=/usr/bin/python3 <directory>/main.py
Restart=always

[Install]
WantedBy=multi-user.target
```
The service needs to be run as root, because GPIO peripherals demand root accesss.

After that matrix-clock.service can be copied to /etc/systemd/system/

```bash
sudo cp matrix-clock.service /etc/systemd/system
```
At last the service can be enabled and started.

```bash
sudo systemctl daemon-reload
sudo systemctl enable matrix-clock
sudo systemctl start matrix-clock
#check status of service
systemctl status matrix-clock.service
```
When accessing http://\<IP-address> the configuration page of the Matrix-Clock should appear. 