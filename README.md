# Smog-detector-kit
This open-hardware project allows anyone to build their own DIY particular matter detector and experiment with setting it up for various particle sizes (from 2.5 μm to 10 μm and larger). 

It is designed to make use only of off-the-shelf products, which can be easily purchased in hardware and electronic equipment stores worldwide. Customizable parts were designed for 3D printing and everyone is welcome to contribute to the project by improving on simple designs provided here. All relevant airflow and photodiode sensitivity calculators have been provided to help with improving the design.

Authors: Aleksy Chwedczuk, Krzysztof Dziardziel, Karolina Kamińska, Mateusz Mazurczak, Ryszard Nowacki, Igor Roszczyk, Bianka Scott (under supervision by Jakub Bochiński).

Smog detector kit is freely available on MIT License (see below).

# Introduction
We are a group of students based in Poland who teamed up to discover new solutions to a chosen world issue. Smog - the widespread problem that affects most of us is what we wanted to focus on. We chose to bring awareness to precisely how much air pollution affects our life expectancy while allowing other students from Poland to follow our steps, creating the device and spreading awareness among their local communities. 

# Hardware Specification
Product Tree
Rysiek / Krzysztof
# Detector Diagram
Image here.
Rysiek + JB
# Getting Started with Smog Detector Kit
Short step by step tutorial here.
Karolina 
# How to program Smog Detector Kit
The software necessary to operate the Smog Detector is very simple. It is
composed of two seperate scripts, written in Arduino C++ and Python 3.<br>
The first one operates on the Arduino located in our design, and it is extremely
simple. The only purpose of that code is to open a serial, then continously
read the current on the photosensitive diode and send the data every 100 ms.<br>
The second program in Python 3 listens for this data on the recieving computer and
displays a simple graph of what the current light level is and what the average
from the past time period was. By using this data the algorithm can easily
calculate where there are peaks in intensity. Alternatively, when another mode
is needed, the script can calculate the mean value of the intensity and based
on that measure continous tiny peaks that compute to a general increase in tiny
particulate matter that would be normally below the detectable range for a DIY
device. This is also really simple as it is simply computing a dampened average.
Both outputs are visible in a TkInter window. There is also a test mode allowing
the introduction of gaussian distribution spikes into data with background noise
and emulating the detector in silico. That way, we can check if the hardware and
software will work correctly.<br>
There is no calibration necessary from a software standpoint, and the computer
used to recieve data only needs a standard Python 3 install. The Arduion can also
be any device, it does not need to be a genuino. Calibration can be conducted if
needed by modifying the variables `size` and `coarse`, which control the length of the
displayed data and the precision with which peaks should be searched for,
respectively.
# Hardware Resource 
## 3D Models
Aleksik Kleksik
## BOM (Bill of Materials)
Aleksik Kleksik

## License

**MIT License**

Copyright (c) 2020 aleksychwedczuk

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
