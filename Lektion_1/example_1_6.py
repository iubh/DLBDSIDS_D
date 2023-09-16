################################################################################################################################################
#                                                                                                                                              #
#    Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt                                                      #
#                                                                                                                                              #
################################################################################################################################################

# PYTHON ROUTINE für die Berechnung einfacher Eigenwertgleichungen #

import os
import sys
import math
import numpy
import numpy as np

A = [[1,2,5],[4,1,3],[3,2,1]] # Definiere eine Matrix A

lb, W = np.linalg.eig(A) # Berechne die Eigenwerte und Eigenvektoren der Matrix A

print('Eigenvektor 1: ', W[0], 'Eigenwert 1: ',lb[0]) # Gebe den ersten Eigenwert und Eigenvektor der Matrix A aus.
print('Eigenvektor 2: ', W[1], 'Eigenwert 2: ',lb[1]) # Gebe den zweiten Eigenwert und Eigenvektor der Matrix A aus. 
print('Eigenvektor 3: ', W[2], 'Eigenwert 3: ',lb[2]) # Gebe den dritten Eigenwert und Eigenvektor der MAtrix A aus. 
