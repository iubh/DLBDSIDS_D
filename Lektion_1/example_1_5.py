################################################################################################################################################
#                                                                                                                                              #
#    Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt                                                      #
#                                                                                                                                              #
################################################################################################################################################

# PYTHON ROUTINE für die Implementierung einer MapReduce Instanz #

import os
import sys
import math

M = [[1,4,3], [2,4,4], [3,3,3]] # Erste Matrix M
N = [[2,4,3], [6,6,7], [2,2,1]] # Zweite Matrix N

def product(m, n) : # Function for matrix multiplication

    result = [[sum(a*b for a,b in zip(M_row,N_col)) for N_col in zip(*N)] for M_row in M] # Führe Matrixmultiplikation aus
    
    return result

map_instance = list(map(product, M, N)) # Multipliziere zwei Matrizen in drei unterschiedlichen Blöcken
reduce_instance = map_instance[0] # Verwende nur den ersten von drei Matrixblöcken
print(map_instance) # Zeige das Ergebnis
