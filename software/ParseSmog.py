#DustSim IRL :)
#Allows us to play around and model real dust particles using le Gauss
#Also enables some smart mode switching between peak-detect and bgdetect.
#@Alto et al.

#Imports - verify if they are on Your machine :)
import serial
import turtle
import math
import random
import time
import statistics

#Globals
size = 200 #Amount of data points

values = [0 for i in range(size)] #Array with data
peaks = [0 for i in range(size)] #Peaks Array

#Init
turtle.speed(0)

#Functions
def renderNew():
    """Redraws our display."""
    turtle.pu()
    turtle.goto(-(len(values) / 2), -(max(values) / 2))
    turtle.pd()
    for i in range(len(values)):
        turtle.goto(-(len(values) / 2) + i, -(max(values) / 2) + values[i])

def renderBase(a, b, y):
    """Creates the mean 0 line on display. From (a) to (b) @ altitude (y)"""
    turtle.pu()
    turtle.goto(-(len(values) / 2) + a, -(max(values) / 2) + y)
    turtle.pd()
    for i in range(b - a):
        turtle.goto(-(len(values) / 2) + a + i, -(max(values) / 2) + y)

def refresh():
    """Completely redraws the display w/o removing any data."""
    turtle.clear()
    turtle.color("blue")
    renderNew()
    turtle.color("black")
    renderBase(0, 900, 0)

def largeNoise(delta):
    """For simulating our dust particle, makes a nice Gaussian Distribution"""
    level = random.randint(0, delta) #Select noise range
    length = random.randint(0, len(values))
    start = random.randint(0, len(values) - length)

    for i in range(random.randint(0, length)):
        values[i + start] += level

def smallNoise(delta):
    """Creates random values that emulate bg noise in system based on (delta)"""
    for i in range(len(values)):
        values[i] += random.randint(0, delta) #Random small hum

def squeeze(delta):
    """Squeezes the graph vertically by a semirandom (delta) value"""
    level = random.randint(1, delta) #Select squeeze strength
    
    for i in range(len(values)):
        values[i] /= level

def addGauss(size, where):
    """Overlays a gauss of a set (size), placin it (where) we need to"""
    gauss = [0 for i in range(20)]
    for i in range(20):
        gauss[i] = getGauss(10, 10, i)

    for i in range(20):
        values[where + i - 10] += gauss[i] * size
        #print(gauss[i] * size)

def getGauss(mu, sigmaSquare, x):
    """Finds our gauss values. Not needed to understand, used in addGauss()"""
    return (1 / math.sqrt(2 * math.pi * sigmaSquare)) * math.e ** ((-0.5) * (x - mu) ** 2 / sigmaSquare)


def discoverPeaks(a, b, height):
    """Reliably detects most gauss peaks from (a) to (b) with (height)"""
    avgDelta = sum(values[a:b]) / len(values[a:b]) #Average
    medDelta = statistics.median(values) #Median
    #print("AvgDelta: {}".format(avgDelta))
    turtle.color("red")
    renderBase(a, b, avgDelta)

    for i in range(b - a):
        if values[a + i] - avgDelta > height:
            peaks[a + i] = 1

    #print(peaks)

def renderPeaks():
    """Displays us the peaks that are added via the discover operation."""
    turtle.pu()
    turtle.goto(-(len(peaks) / 2), -(max(peaks) / 2))
    turtle.pd()
    
    hopps = 0
    hoppSize = 0
    wasPeak = False
    
    for i in range(len(peaks)):
        turtle.goto(-(len(peaks) / 2) + i, -(max(peaks) / 2) + peaks[i] * 100)
        if (peaks[i] == 1 and wasPeak == False):
            wasPeak = True
            hoppSize += 1
        if (peaks[i] == 1 and wasPeak == True):
            hoppSize += 1
        if (peaks[i] == 0 and wasPeak == False):
            wasPeak = False
            hoppSize = 0
        if (peaks[i] == 0 and wasPeak == True):
            #print("Peak size: {}".format(hoppSize))
            if (hoppSize > 2):
                hopps += 1
                turtle.circle(hoppSize)
            wasPeak = False
            hoppSize = 0
        
    #print("Total peaks: {}".format(hopps))
    

#Prep dataset
#print("Creating dataset...")

DV_PORT = 'COM5' #set to the device location or detect automatically w. library

ser = serial.Serial(DV_PORT, 9600) #REMEMBER - 9600 as from Arduino File

iterx = 0

turtle.tracer(0) #set max refresh rates for TkInter

resize = 1 #allow resize automatically to ease reading of display (incode)
while True:
    if iterx % 30 == 0: #gather data if 30 frames have passed
        try:
            cur = ser.readline().decode().strip()
            values = values[1:] + [int(cur) / resize]
            print(cur)
        except:
            print("[ ! ] Warning! Error parsing value fromn FEED.")

        #print(values)

        turtle.clear()

        #uncomment to add extra data (not recommended - unstable)
        #turtle.color("black")
        #for i in range(5):
        #    renderBase(0, size, i * 10)
        #    turtle.pu(); turtle.fd(5); turtle.lt(90); turtle.fd(-4); turtle.rt(90); turtle.pd();
        #    turtle.write(i * 10 * resize, font=("Consolas", 6, "normal"))
        
        turtle.color("blue");
        renderNew()

        #renders the peaks that we need to see to make debug easier:
        peaks = peaks[1:] + [0]
        coarse = 8
        for i in range(coarse):
            discoverPeaks(int(len(values) / coarse) * i, int(len(values) / coarse) * (i + 1), 15)

        turtle.color("green")
        renderPeaks()
        
        turtle.update() #redraw display
        
    iterx += 1 #increment current frame number
