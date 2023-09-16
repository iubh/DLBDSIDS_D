################################################################################################################################################
#                                                                                                                                              #
#    Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt                                                      #
#                                                                                                                                              #
################################################################################################################################################

################################################################################
#                                                                              # 
#   PYTHON ROUTINE zur Berechnung von Gewinnen aus der Monty Hall Stategie     #
#                                                                              # 
################################################################################ 

import math
import random

# Definiere die Parameter 

win_standard = [] # Anzahl der Gewinne in einer Standard Lotterie Startegie 
win_clever = [] # Anzahl der Gewinne in einer Monty Hall Lotterie Strategie

main_win = 45000.0 # Wert des Gesamtgewinns
k = j = 0

sample_size = 100000 # Anzahl der Iterationen bzw. Realisierungen

# Standard Strategie

for m in range(sample_size):

    j = random.randint(0,2) # Erstelle eine Zufallsdarstellung pro Realisierung 
    ran_seq = [0.0, 0.0, 0.0] # Initialer Vektor
    
    for k in range(0,3): # Generiere den entsprechenden Vektor
        
        if (k == j): ran_seq[k] = main_win

    l = random.randint(0,2) # Erstelle eine Zufallszahl pro Ziehung
    if (ran_seq[l] == main_win) : win_standard.append(main_win) # Zähle alle Gewinne in der Standard Strategie    

# Monty Strategie

for m in range(sample_size):

    j = random.randint(0,2) # Erstelle eine Zufallsdarstellung pro Realisierung 
    ran_seq = [0.0, 0.0, 0.0] # Initialer Vektor
    
    for k in range(0,3): # Generiere den entsprechenden Vektor
        
        if (k == j): ran_seq[k] = main_win

    j = random.randint(0,2) # Erstelle eine Zufallszahl pro Ziehung

    if (ran_seq[j] == main_win) : win_clever.append(main_win) # Zähle alle Gewinne in der ersten Monty Strategie    
    if (ran_seq[j] != main_win) : # Zähle alle Gewinne in der switch to win Monty Strategie

        l = random.randint(0,2) # Erstelle eine Zufallszahl pro Auswahl in der switch to win Ziehung

        while (l == j) : 
            
            l = random.randint(0,2) # Prüfe Nicht-Gleichheit der Zufallszahlen

        win_clever.append(ran_seq[l]) # Summiere den zusätzlichen Gewinn in der switch to win Ziehung (Monty Hall Strategie)

win_s = 0.0
win_monty = 0.0

length_standard = len(win_standard)
length_monty = len(win_clever)

for k in range(length_standard):

    win_s = win_s + win_standard[k]/float(sample_size)

for k in range(length_monty):

    win_monty = win_monty + win_clever[k]/float(sample_size)

print('How much is the probability and win increased in the Monty Hall strategy?', math.fabs(math.fabs(win_s)-math.fabs(win_monty))/math.fabs(main_win)*100.0, 'per cent')