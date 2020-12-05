# Smog-detector-kit
This open-hardware project allows anyone to build their own DIY particular matter detector and experiment with setting it up for various particle sizes (from 2.5 μm to 10 μm and larger). 

It is designed to make use only of off-the-shelf products, which can be easily purchased in hardware and electronic equipment stores worldwide. Customizable parts were designed for 3D printing and everyone is welcome to contribute to the project by improving on simple designs provided here. All relevant airflow and photodiode sensitivity calculators have been provided to help with improving the design.

Authors: Aleksy Chwedczuk, Krzysztof Dziardziel, Karolina Kamińska, Mateusz Mazurczak, Ryszard Nowacki, Igor Roszczyk, Bianka Scott (under supervision by Jakub Bochiński).

Smog detector kit is freely available under CERN Open Hardware License and MIT Software License ([see below](#license)).

# Table of contents
* [Introduction](#introduction)
* [Hardware Specification](#hardware-specification)
* [Detector Diagram](#detector-diagram)
* [Getting started with Smog Detector Kit](#getting-started-with-smog-detector-kit)
* [How to program Smog Detector Kit](#how-to-program-smog-detector-kit)
* [Hardware Resources](#hardware-resources)
  * [3D Models](#3d-models)
  * [Bill of Materials](#bill-of-materials)
* [License](#license)


# Introduction
We are a group of students based in Poland who teamed up to discover new solutions to a chosen world issue. Smog - the widespread problem that affects most of us is what we wanted to focus on. We chose to bring awareness to precisely how much air pollution affects our life expectancy while allowing other students from Poland to follow our steps, creating the device and spreading awareness among their local communities. 

Our smog detector kit, thanks to it’s plug based component design, is modifiable and extendable. It works by detecting particles in the air as they cross the laser and calculates smog levels, also converting them into other statistics. The machine is quiet and self-calibrating, making it user friendly and easy to set up.

Whether it's a science project or a curiosity for what's in the air in your house, the Smog detector kit is for you. All remaining components are available at your local hardware store so your job is to assemble it and collect data for the program to process.

By assembling the smog detector kit you are investing in developing your engineering skills, regardless of your level of expertise, and a way of collecting data by yourself. It is cheaper than many alternatives out there, easy to use and provides an interesting outlook on the impact of the air polution on your health. Moreover, assembling such a kit with your team will introduce you into the engineering world in a practical manner by allowing you to implement your theoretical knowledge from the class to the reality.

All necessary information for construction of the smog detector kit can be found below alongside with a list of all components. Our team strongly encourages you to attempt the construction of your own detector.

# Hardware Specification
< INTRO NEEDED > 

![Product Tree](/images/Smog_Detectives_Kit-Product_Tree.jpg)

< EXPLANATION OF THE PRODUCT TREE NEEDED >

# Detector Diagram
Rysiek + JB

![Detector Diagram](/images/SDK_photo_desc.png)

# Getting Started with Smog Detector Kit
Short step by step tutorial here.
Karolina 

In case you were wondering what is happening inside of the Smog Detector Kit, here is a handy cross section:

![Detector cross section](/images/SDK_photo_desc2.png)

# How to program Smog Detector Kit

The software necessary to operate the Smog Detector is very simple. It is
composed of two seperate scripts, written in Arduino C++ and Python 3.

## Arduino Software

The first one operates on the Arduino located in our design, and it is extremely
simple. The only purpose of that code is to open a serial, then continously
read the current on the photosensitive diode and send the data every 100 ms.
The only potential adjustments the code needs for it to function on any hardware is
the modification of `READ_PIN` to the designated analog pin on the arduino. The
default value for this definition is `A0`.

## Workstation/Laptop Software

The second program in Python 3 listens for this data on the recieving computer and
displays a simple graph of what the current light level is and what the average
from the past time period was. By using this data the algorithm can easily
calculate where there are peaks in intensity. Alternatively, when another mode
is needed, the script can calculate the mean value of the intensity and based
on that measure continous tiny peaks that compute to a general increase in tiny
particulate matter that would be normally below the detectable range for a DIY
device. This is also really easy to understand as it is simply computing a dampened average.
Both outputs are visible in a TkInter window. There is also a test mode allowing
the introduction of gaussian distribution spikes into data with background noise
and emulating the detector in silico. That way, we can check if the hardware and
software will work correctly.

## Calibration & Precision

There is no calibration necessary from a software standpoint, and the computer
used to recieve data only needs a standard Python 3 install. The Arduion can also
be any device, it does not need to be a genuino. Calibration can be conducted if
needed by modifying the variables `size` and `coarse`, which control the length of the
displayed data and the precision with which peaks should be searched for,
respectively.

![Demo of DustDetect Script](/images/image.png)

This is what the ParseSmog library is able to do - detect, locate, enumerate and analyze peaks in a signal. Based on this data we can calculate the number of particles of a given type or size in a given volume of air. The black line is the base line, the blue line is the scaled raw feed, the red lines are local averages, the green peaks are percieved anomalies in the background humm function (psi) and the circles show peak size. Peaks that do not have circles are not counted, since they do not follow the correct reflective patterns of an idealised spherical dust particle (or multiple stacked particles). The minimum anomaly (delta) can be adjusted to account for certain properties of the inside of a detector, which is what calibration of this script boils down to.
# Hardware Resources 
## 3D Models
The following files are uploaded in the 3D folder:

Beam dump files:<br>
[beamdump.f3d](https://github.com/aleksychwedczuk/Smog-detector-kit/blob/main/3d-models/beamdump.f3d) <br>
[beamdump.step](https://github.com/aleksychwedczuk/Smog-detector-kit/blob/main/3d-models/beamdump.step) <br>
[beamdump_part_1.stl](https://github.com/aleksychwedczuk/Smog-detector-kit/blob/main/3d-models/beamdump_part_1.stl) <br>
[beamdump_part_2.stl](https://github.com/aleksychwedczuk/Smog-detector-kit/blob/main/3d-models/beamdump_part_2.stl) <br>
[beamdump_part_3.stl](https://github.com/aleksychwedczuk/Smog-detector-kit/blob/main/3d-models/beamdump_part_3.stl) <br>

*First two files are editable and constitute of the beamdump part which is composed of three different components. The beamdump is split in order to ensure easy printing without the need of any raft on an FDM-type printer. Because of that there are three STL files as the beamdump itself has free parts which connect together without any additional adhesive due to their geometry.*

Photodiode rod files:<br>
[photodiode_rod.f3d](https://github.com/aleksychwedczuk/Smog-detector-kit/blob/main/3d-models/photodiode_rod.f3d)<br>
[photodiode_rod.step](https://github.com/aleksychwedczuk/Smog-detector-kit/blob/main/3d-models/photodiode_rod.step)<br>
[photodiode_rod.stl](https://github.com/aleksychwedczuk/Smog-detector-kit/blob/main/3d-models/photodiode_rod.stl)<br>

Laser holder files:<br>
*EDITABLE FILES MISSING*<br>
*EDITABLE FILES MISSING*<br>
[laser_holder.stl](https://github.com/aleksychwedczuk/Smog-detector-kit/blob/main/3d-models/laser_holder.stl)<br>

Fan mount files:<br>
*EDITABLE FILES MISSING*<br>
*EDITABLE FILES MISSING*<br>
[fan_holder.stl](https://github.com/aleksychwedczuk/Smog-detector-kit/blob/main/3d-models/fan_holder.stl)<br>

In order to create a copy of the original smog detective detector all STL files listed should be printed: <br>
[beamdump_part_1.stl](https://github.com/aleksychwedczuk/Smog-detector-kit/blob/main/3d-models/beamdump_part_1.stl) <br>
[beamdump_part_2.stl](https://github.com/aleksychwedczuk/Smog-detector-kit/blob/main/3d-models/beamdump_part_2.stl) <br>
[beamdump_part_3.stl](https://github.com/aleksychwedczuk/Smog-detector-kit/blob/main/3d-models/beamdump_part_3.stl) <br>
[photodiode_rod.stl](https://github.com/aleksychwedczuk/Smog-detector-kit/blob/main/3d-models/photodiode_rod.stl)<br>
[laser_holder.stl](https://github.com/aleksychwedczuk/Smog-detector-kit/blob/main/3d-models/laser_holder.stl)<br>
[fan_holder.stl](https://github.com/aleksychwedczuk/Smog-detector-kit/blob/main/3d-models/fan_holder.stl)<br>

Otherwise if a need to edit any of the files arises they are available both in the editable STEP format as well as the AUTODESK FUSION 360 ARCHIVE FILES format compatible with autodesk CAD software.


## Bill of Materials
Aleksik Kleksik

# License

## Hardware
Hardware used in this project, where designed by the Smog Detectives Kit team, is released under the CERN-OHL-P v2 License.
 
**CERN-OHL-P v2 License**

Copyright (c) 2020 by Smog Detectives team (Aleksy Chwedczuk, Krzysztof Dziardziel, Karolina Kamińska, 
Mateusz Mazurczak, Ryszard Nowacki, Igor Roszczyk, Bianka Scott & Jakub Bochiński).

Source: https://github.com/aleksychwedczuk/Smog-detector-kit

This source describes Open Hardware and is licensed under the CERN-OHL-P v2
You may redistribute and modify this documentation and make products
using it under the terms of the CERN-OHL-P v2 (https:/cern.ch/cern-ohl).
This documentation is distributed WITHOUT ANY EXPRESS OR IMPLIED
WARRANTY, INCLUDING OF MERCHANTABILITY, SATISFACTORY QUALITY
AND FITNESS FOR A PARTICULAR PURPOSE. Please see the CERN-OHL-P v2
for applicable conditions


## Software
Software used in this project is released under MIT License. 

**MIT License**

Copyright (c) 2020 by Smog Detectives team (Aleksy Chwedczuk, Krzysztof Dziardziel, Karolina Kamińska, 
Mateusz Mazurczak, Ryszard Nowacki, Igor Roszczyk, Bianka Scott & Jakub Bochiński).

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
