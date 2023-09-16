################################################################################################################################################
#                                                                                                                                              #
#    Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt                                                      #
#                                                                                                                                              #
################################################################################################################################################

# PYTHON ROUTINE zur Berechnung der Kreiszahl pi mit Zufallszahlen #

import os
from platform import java_ver
import sys
import math
import random
import numpy
import numpy as np
import pylab
import matplotlib.pyplot as plt
import operator

n_total = 0
n_hits = 0
a = 1.0

x_coordinate = []
y_coordinate = []

while 1 < 2 :

    m = random.uniform(-a,a)
    n = random.uniform(-a,a)

    n_total = n_total + 1

    if (m**2 + n**2 < a**2) : 
        
        n_hits = n_hits + 1

        x_coordinate.append(m)
        y_coordinate.append(n)
 
    if (math.fabs(4.0*float(n_hits)/float(n_total) - math.pi) < 1.0E-10) :
        
        print('Anzahl der Rechenschritte', float(n_total))
        print('Berechnete Kreiszahl pi', round(4.0*float(n_hits)/float(n_total),8))

        break

plt.figure(1) # Initiiere die Figur 1 
plt.xlabel('x coordinate', fontsize = 12)
plt.ylabel('y coordinate', fontsize = 12)
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 10)
plt.hist2d(x_coordinate, y_coordinate, bins = 250) # Zeichne die Figur
plt.savefig('fig_1_12.png') # Speichere die Figur 1 in den richtigen Pfad

