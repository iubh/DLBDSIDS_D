################################################################################################################################################
#                                                                                                                                              #
#    Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt                                                      #
#                                                                                                                                              #
################################################################################################################################################

# PYTHON ROUTINE zur Normierung von Matrizen #

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
from sklearn import preprocessing

A = [[ 1., -1.,  2.], [ 2.,  0.,  0.], [ 0.,  1., -1.]] # Implementiere die Matrix ohne Normalisierung 

print('')
print('Matrix Norm 1')

A_normalized_1 = preprocessing.normalize(A, norm='l1') # Normiere die Matrix A mit Matrixnorm 1 

print(A_normalized_1) # Gebe die normierte Matrix mit Matrixnorm 1 aus
print('')

print('Matrix Norm 2')

A_normalized_2 = preprocessing.normalize(A, norm='l2') # Normiere die Matrix A mit Matrixnorm 1

print(A_normalized_2) # Gebe die normierte Matrix mit Matrixnorm 2 aus
print('')

print('Matrix Norm max')

A_normalized_max = preprocessing.normalize(A, norm='max') # Normiere die Matrix A mit Matrixnorm 1 
print(A_normalized_max) # Gebe die normierte Matrix mit Matrixnorm max aus

print('')
