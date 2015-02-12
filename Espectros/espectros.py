# Programa que permite extraer espectros de pixeles solicitados
#
#
#------------------------IFSview.py----------------------------
#
#
#import visvis as vv
from matplotlib.widgets import Cursor
from tkFileDialog import askopenfilename
import matplotlib
matplotlib.use('TkAgg')

from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

from matplotlib.colors import colorConverter
import Tkinter as Tk
import sys

# PREGUNTAR PREGUNTAR PREGUNTAR PREGUNTAR
#def destroy(e): sys.exit()

import sys
import pyfits
import matplotlib
#matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
#plt.jet()
import numpy as np
from mpl_toolkits.mplot3d  import Axes3D
import math, copy
from matplotlib import pyplot, colors, cm

#   We define a function that reads the respective figure

def loadFig(filename):

#   We define a function that recieves the pixels that we are interested in,
#   in order to extract that particular pixel's spectrum

def pixelSelect(pixX, pixY):

#   We define a function that saves the spectrum obtained by the function
#   defined above

def saveImg():
