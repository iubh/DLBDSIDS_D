################################################################################################################################################
#                                                                                                                                              #
#    Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt                                                      #
#                                                                                                                                              #
################################################################################################################################################

# PYTHON ROUTINE für die Berechnung von Extremwerten #

import os
import sys
import math
from unittest import result
import numpy
import numpy as np
import numdifftools as nd
import matplotlib.pyplot as plt

# Importiere sympy 
from sympy import *
 
x = np.linspace(-2, 2, 100)

maximum = []
minimum = []

df = nd.Derivative(np.tanh, n=6) # Berechne die i-te Ableitung der tanh-Funktion
y = df(x) # Ordne den Ableitungen Werte an der Stelle x = -2 bis x = 2 zu.
    
plt.xlabel('x', fontsize = 10)
plt.ylabel('tanh(x)', fontsize = 10)

h = plt.plot(x, y/np.abs(y).max()) # Zeichne die Ableitungen der tanh-Funktion
plt.savefig('function_tanh.png') # Speichere die Funktionen in den richtigen Pfad.

for k in range(len(y)-1):

    if (y[k]/np.abs(y).max() < 0.0 and y[k+1]/np.abs(y).max() > 0.0) : # Die Nullwerte der positiven Ableitungen definieren das Maximum der zu integrierenden Funktion.
                    
        maximum.append(x[k]) # Speichere alle Maxima 

    if (y[k]/np.abs(y).max() > 0.0 and y[k+1]/np.abs(y).max() < 0.0) : # Die Nullen der negativen Ableitung definieren das Maximum der integrierten Funktion
            
        minimum.append(x[k]) # Sammle allen Maxima

        # Zeichne die Ableitungen der tanh-Funktion 
        
print (maximum, minimum) # Zeichne alle Maxima und Minima