################################################################################################################################################
#                                                                                                                                              #
#    Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt                                                      #
#                                                                                                                                              #
################################################################################################################################################

# PYTHON ROUTINE für einen einfachen Lernalgorithmus #

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

learning_rate = -0.01
maximum = 0.0

df = nd.Derivative(np.tanh, n=2) # Berechne die i-te Ableitung der tanh-Funktion 
y = df(x) # Ordne den Ableitungen Werte innerhalb der Gitterpunkte -2 bis 2 zu 

maximum = -0.20

while 1 < 2:

    maximum = maximum - learning_rate*df(maximum)

    if (math.fabs(learning_rate*df(maximum)) < 1.0E-4):
       
        break

print(maximum)