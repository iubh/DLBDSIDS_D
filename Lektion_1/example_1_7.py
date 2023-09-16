################################################################################################################################################
#                                                                                                                                              #
#    Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt                                                      #
#                                                                                                                                              #
################################################################################################################################################

# PYTHON ROUTINE für die Berechnung von Ableitungen einer Funktion #

import os
import sys
import math
from unittest import result
import numpy
import numpy as np
import numdifftools as nd
import matplotlib.pyplot as plt

# Import sympy 

from sympy import *
 
x = Symbol('tanh(x)') # Erstelle ein Symbol "symbol", welches x genannt ist
f = tanh(x) # Definiere eine Funktion
 
derivative_f = f.diff(x) # Berechne die Ableitung von f an der Stelle x
print('The formal derivate is defined as : ', derivative_f) # Gebe den formalen Wert der Ableitung der Funktion f an der Stelle x aus

f_prime = lambdify(x,derivative_f) # Ordne dem formalen Wert der Ableitung der Funktion f einen quantitativen Wert zu
print('The value of the formal derivative at x = 4 is : ', f_prime(4)) # Berechnen Sie den Wert der Ableitung an der Stelle x = 4