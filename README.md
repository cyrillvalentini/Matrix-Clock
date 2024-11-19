# Matrix-Clock
## Introduction
Inspired by [@NoaNoa's BIFRÖST LED matrix](https://www.printables.com/model/434061-bifrost-led-matrix-case) on printables, I started my own version of a clock based around a 32x8 WS2812B neopixel matrix. I liked the sleek design of his version, which I took as an inspiration for my hardware design. Using a white 3D-printed diffuser especially gives it a more polished look. On the software side however, I wanted to make something new from the ground up. Instead of reusing WLED for this project, I instead opted to make my own implementation based around a Flask webserver and python backend. This made it possible to implement features specifically for this usecase, without overloading it with things, that aren't needed. To allow for a more robust and faster web interface, I opted to use a Raspberry Pi Zero W instead of a microcontroller like the ESP 32. Even though this is somewhat overkill, it enables more flexibility while also being relatively cheap.
![alt text](https://github.com/cyrillvalentini/Matrix-Clock/blob/main/images/cad.PNG?raw=true)
## Features
Currently the clock has two modes which can be selected. Either, the whole matrix can be used to display an image, which can be drawn in the buit-in editor. The other mode diplays the time, while also allowing the rest of the diplay to be colored.  For both modes there's an option to download and upload a design. The brightness can be manually adjusted or set to auto, which will change the brightness acording to the time. 

More feautures can always be added.
![alt text](https://github.com/cyrillvalentini/Matrix-Clock/blob/main/images/page.PNG?raw=true)

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
### Wiring
The display runs on 5V. To connnect the raspberry Pi to the same power input, a micro USB cable can be cut apart and soldered to the input. The signal wire from the display is connected to pin 18 over a 300 Ohm resistor.
TBD
## Installation
TBD