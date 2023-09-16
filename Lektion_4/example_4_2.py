################################################################################################################################################
#                                                                                                                                              #
#    Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt                                                      #
#                                                                                                                                              #
################################################################################################################################################

##################################################################################
#                                                                                # 
#   PYTHON ROUTINE zur Berechnung von Gauss-, Binomial- und Poissonverteilungen  #          
#                                                                                # 
################################################################################## 

import math
import matplotlib.pyplot as plt

from scipy.stats import poisson
from scipy.stats import norm
from scipy.stats import binom

# Definiere die Parameter 

binomial_distribution = [] # Binomial Verteilung
gauss_distribution = [] # Gauss Verteilung
poisson_distribution = [] # Poisson Verteilung

sample_size = 100000 # Anzahl der Samples 

l = 0
n = 0

for l in range(0, sample_size): # Iteration über die Anzahl der Realisierungen
        
    classifier = 0.0
    n = 1
    var_gamma = 1.0

    classifier = binom.rvs(n, var_gamma) # Berechne die Binomialverteilung
    binomial_distribution.append(classifier)

    classifier = 0.0
    mu = 1.0
    sigma = math.sqrt(1.0)

    classifier = norm.rvs(mu,sigma) # Berechne die Gaußverteilung
    gauss_distribution.append(classifier)

    classifier = 0.0
    
    var_lambda = 1.0
    classifier = poisson.rvs(var_lambda) # Berechne die Poissonverteilung

    poisson_distribution.append(classifier)


plt.figure(1) # Initiiere die Figur 1 - Binomialverteilung
plt.xlabel('Var x', fontsize = 10)
plt.ylabel('Binomial Distribution', fontsize = 10)
plt.hist(binomial_distribution, density = True, bins = 100) # Zeichend ie Figur
plt.savefig('fig_4_2_1.png') # Speichere die Figur im richtigen Pfad.

plt.figure(2) # Initiiere die Figur 2 - Gaußverteilung
plt.xlabel('Var x', fontsize = 10)
plt.ylabel('Gauß Distribution', fontsize = 10)
plt.hist(gauss_distribution, density = True, bins = 100) # Plot the figure
plt.savefig('fig_4_2_2.png') # Speichere die Figur im richtigen Pfad.

plt.figure(3) # Initiiere die Figur 3 - Poissonverteilung
plt.xlabel('Var x', fontsize = 10)
plt.ylabel('Poisson Distribution', fontsize = 10)
plt.hist(poisson_distribution, density = True, bins = 100) # Plot the figure
plt.savefig('fig_4_2_3.png') # Speichere die Figur im richtigen Pfad.