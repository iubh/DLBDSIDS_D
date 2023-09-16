################################################################################################################################################
#                                                                                                                                              #
#    Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt                                                      #
#                                                                                                                                              #
################################################################################################################################################

########################################################################################################
#                                                                                                      # 
#   PYTHON ROUTINE zur Berechnung der Gewinne als Funktion der Investition in eine 6 aus 49 Lotterie   #
#                                                                                                      # 
######################################################################################################## 


import random
import matplotlib.pyplot as plt

choose_numbers = {0,0,0,0,0,0}
numbers = {0,0,0,0,0,0}

profit = [0.0, 0.0, 0.0, 10.0, 50.0, 500.0, 10000.0]
random_number = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

sample_size = 5000
lot_numbers = 0

total_average_profit = 0.0

ticket_price = 2.50
paid_price = 0.0

price_1 = []
price_2 = []

for n in range(0, sample_size):

    total_profit = 0.0
    paid_price = 0.0
    rnd = 0

    lot_numbers = random.randint(1, sample_size)

    for k in range(1, lot_numbers):

        paid_price = paid_price + ticket_price
        m = n = 0

        while (m < 7): # Definiere die Anzahl der Zahlen in der Lotterie
            
            rnd = random.randint(1, 49)

            if (rnd not in random_number): 
                
                random_number[m] = rnd
                m = m + 1

        numbers = {}
        numbers = {random_number[0], random_number[1], random_number[2], random_number[3], random_number[4], random_number[5], random_number[6]}

        random_number = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        
        while (n < 6) : # Wähle die Anzahl der Zahlen in der Lottrie
            
            rnd = random.randint(1, 49)

            if (rnd not in random_number): 
                
                random_number[n] = rnd
                n = n + 1

        choose_numbers = {}
        choose_numbers = {random_number[0], random_number[1], random_number[2], random_number[3], random_number[4], random_number[5]}

        if (len(numbers.intersection(choose_numbers)) in range(0, 6)) : total_profit = total_profit + profit[len(numbers.intersection(choose_numbers))]

    price_1.append(paid_price)    
    price_2.append(total_profit)    

plt.figure(10) # Initiiere die Figur 1 
plt.xlabel('Gezahlter Preis', fontsize = 10)
plt.ylabel('Mittlerer Gewinn', fontsize = 10)
plt.xlim(0.0,100.0)
plt.ylim(0.0,100.0)
plt.hist2d(price_1, price_2, bins = 25, cmap=plt.cm.BuPu) # Zeichne die Figur 
plt.savefig('fig_3_3.png') # Speichere die Figur zum richtigen Pfad (finde den Pfad mit pwd)