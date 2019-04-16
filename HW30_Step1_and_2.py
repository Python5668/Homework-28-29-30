# Task 1, arduino serial. This is the simplest way to collect serial data using Arduino + Windows
import serial
import matplotlib.pyplot as plt

ser = serial.Serial('COM3', 9600)
n = 0
dataLst = []
while n<200: # collect 200 data points and stop
    print(ser.readline())
    dataPoint = ser.readline()
    dataPoint = int(dataPoint) # the data received are strings
    dataLst.append(dataPoint)
    n+=1
#print(type(dataPoints))
#print(dataPoints)
ser.close() # Dont forget to close the serial port
    
plt.plot(dataLst) # plot the received data afterwards
#plt.show() # if you run this code in Spyder, you dont need this line
f = open("serialData.dat", "w") # saves the data to a file
f.write(str(dataLst)) # string is the only legal format to be written into a file
f.close()
f = open('serialData.dat', 'r')
print(f.read())

# Task 2, use pyqtgraph to plot the data instead of using matplotlib
#import pyqtgraph as pq
#from pyqtgraph.Qt import QtCore, QtGui
#from pyqtgraph import PlotWidget
#import numpy as np
#
### Always start by initializing Qt (only once per application)
#app = QtGui.QApplication([])
### Define a top-level widget to hold everything
#w = QtGui.QWidget()
### create some widgets to be placed inside
#btn = QtGui.QPushButton('Press Me')
#text = QtGui.QLineEdit('Enter Text!')
#listw = QtGui.QListWidget()
#
#pq.setConfigOption('background', 'w')
#plt = pq.PlotWidget() # pq.PlotWidget allows the use of the properties below,
## but pq.plot doesnt
#penn = pq.mkPen('k', width = 2, style = QtCore.Qt.SolidLine)
#plt.plot([1,2,3], [1,2,3], pen = penn, title = 'The first pyqtgraph plot',
#                symbol = 't', symbolSize = 20)
#labelStyle = {'color': '#000', 'font-size':'30px'}
#plt.setLabel('left', 'Voltage', 'V', **labelStyle)
#plt.setLabel('bottom', 'Time', 's', **labelStyle)
#plt.setXRange(0,5)
#plt.setYRange(0,5)
### Create a grid layout to manage the widgets size and position
#layout = QtGui.QGridLayout()
#w.setLayout(layout)
### Add widgets to the layout in their proper positions
#layout.addWidget(btn, 0, 0) # button goes in the uppoer-left
#layout.addWidget(text, 1, 0) # text edit goes in middle-left
#layout.addWidget(listw, 2, 0) # list widget goes in bottom-left
#layout.addWidget(plt, 0, 1, 3, 1) # plot goes on right side, spanning 3 rows
## and 1 column
### Display the widget as a new window
#w.show()
### start the Qt event loop
#app.exec_()