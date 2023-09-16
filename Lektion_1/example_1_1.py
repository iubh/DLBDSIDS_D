################################################################################################################################################
#                                                                                                                                              #
#    Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt                                                      #
#                                                                                                                                              #
################################################################################################################################################

# PYTHON ROUTINE zur Berechnung von Funktionswerten einer Cosinusfunktion #

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,100) # Definiere lineares Gitter mit festen Abstand
f = np.cos(x) # Definiere eine Cosinusfunktion auf dem Gitter

plt.figure(1) # Initiere Figur 1 
plt.xlabel('x', fontsize = 12)
plt.ylabel('cos(x)', fontsize = 12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.plot(x,f) # Plot the figure
plt.savefig('fig_cosinus.png') # Speichere Figur 1 in den korrekten Pfad.


