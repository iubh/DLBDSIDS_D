################################################################################################################################################
#                                                                                                                                              #
#    Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt                                                      #
#                                                                                                                                              #
################################################################################################################################################

# PYTHON ROUTINE zum Gaußschen Grenzwertsatz #

import os
from re import X
import sys
import math
from unittest import result
import numpy
import numpy as np
import numdifftools as nd
import matplotlib.pyplot as plt
from sympy import *
import random  
 
a = [25.0, 50.0, 75.0, 100.0, 125.0] # Definiere eine Liste von Mittelwerten
b = [5.0, 7.5, 10.0, 12.5, 15.0] # Definiere eine Liste von Varianzen

M = 10000000 # Definiere eine Anzahl von Iterationen
L = 5 # Lege die Anzahl von Zufallsvariablen mit Gaußverteilung fest

f = [] # Sammle alle Werte der Funktion f

random_var = 0.0 # Lege eine Variable für die Summe der Zufallsvariablen fest 

for l in range(M):

    random_var = 0.0 # Setze die Zufallsvaribalen auf den Wert 0 
    print('Step Nr. :', l) # Gebe die Anzahl der Iterationen aus
    
    for k in range(L):

        random_var = random_var + random.gauss(a[k],b[k]) # Summe über die Gaußverteilten Zufallsvariablen 
        
    f.append(random_var) # Sammle alle Zufallsvariablen 
    
plt.figure(1) # Initiere die Figur 1 
plt.xlabel('$\mu=\mu_1+\mu_2+\mu_3+\mu_4+\mu_5$', fontsize = 12)
plt.ylabel('$f(\mu)$', fontsize = 12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.hist(f, bins = 500) # Zeichne die Figur
plt.savefig('fig_1_11.png') # Speichere die Figur in den richtigen Pfad
