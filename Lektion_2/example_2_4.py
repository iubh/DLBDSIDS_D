################################################################################################################################################
#                                                                                                                                              #
#    Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt                                                      #
#                                                                                                                                              #
################################################################################################################################################

##########################################################################################################
#                                                                                                        #
#   PYTHON ROUTINE zur Berechnung der Konvergenz bei der Berechnung der Kreiszahl pi mit Zufallszahlen   #
#                                                                                                        #
##########################################################################################################


import random
import matplotlib.pyplot as plt

n_total = 0 # Definiere die Variablen 
n_hits = 0
n_iteration = 100000

a = 1.0
x = [] 

for i in range (n_iteration) : # Iteration über die Anzahl der Realisierungen für das Verhältnis 4.0*float(n_hits)/float(n_total)
    
    m = random.uniform(-a,a) # Setze die Intervalle, um die Zufallszahlen zu durchlaufen 
    n = random.uniform(-a,a)

    n_total = n_total + 1

    if (m**2 + n**2 < a**2) : # Zähle die Häufigkeiten der Werte innerhalb der Fläche pi/4.0 
        
        n_hits = n_hits + 1
 
    x.append(4.0*float(n_hits)/float(n_total)) # Berechne das Verhältnis der beiden Flächen pi und Einheitskreis   
    

plt.figure(1) # Initiiere die Figur 1
plt.xlabel('Quotientenwert von n_hits und n_total', fontsize = 10)
plt.ylabel('Häufigkeit des Quotientenwerts', fontsize = 10)
plt.xlim([3.0, 3.4])
plt.hist(x, bins = 250) # Zeichen Figur 1
plt.savefig('figure_1.png') # Speichere Figur 1 im richtigen Pfad mit dem Command pwd
