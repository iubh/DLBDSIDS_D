################################################################################################################################################
#                                                                                                                                              #
#    Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt                                                      #
#                                                                                                                                              #
################################################################################################################################################

# PYTHON ROUTINE für die Erzeugung eines Wellenpakets aus der tanh Funktion #

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

plt.figure(1) # Initiiere Figur 1
 
for i in range(10): # Iteriere die Funktionen über i bis zu 10 mal

    df = nd.Derivative(np.tanh, n=i) # Berechne die i-te Ableitung der tanh-Funktion
    y = df(x) # Ordne den Ableitungen Werte im Bereich für x = -2 bis x = 2 zu
    
    plt.xlabel('x', fontsize = 12)
    plt.ylabel('tanh(x)', fontsize = 12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    h = plt.plot(x, y/np.abs(y).max()) # Zeichen die Ableitungen der Funktion tanh

plt.savefig('fig_1_8.png') # Speichere die Figur in den richtigen Pfad