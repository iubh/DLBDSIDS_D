################################################################################################################################################
#                                                                                                                                              #
#    Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt                                                      #
#                                                                                                                                              #
################################################################################################################################################

########################################################################
#                                                                      # 
#   PYTHON ROUTINE zum Vertauschen zweiter Spalten in einem CSV File   #
#                                                                      # 
######################################################################## 

import csv
import random
import pandas

i = j = k = 0

num_cols = 10 # Definiere die Anzahl der Spalten
num_rows = 10 # Definiere die Anzahl der Zeilen

data_field = [0.0]*num_cols # Definiere das Datenfeld
fieldnames = ['Spalte 1', 'Spalte 2', 'Spalte 3', 'Spalte 4', 'Spalte 5', 'Spalte 6', 'Spalte 7', 'Spalte 8', 'Spalte 9', 'Spalte 10'] # Definiere den Spaltennamen als vektor mit n_column Einträgen
        
with open('import_file.csv', 'w') as f: # Adressenpfad für File Pfad
    
    writer = csv.writer(f) # Ins CSV File schreiben 
    writer.writerow(fieldnames) # In den Header des CSV Files schreiben 
    
    for i in range(0, num_rows):

        for j in range(0, num_cols):

            data_field[j] = float(random.uniform(0.0, 1000.0)) # Schreibe in den Header des CSV Files
            
        writer.writerow(data_field) # Schreibe die Daten des CSV Files 
        
df = pandas.read_csv('import_file.csv') # Einlesen der Daten aus dem CSV File - setze den korrekten Pfad mit pwd
print(df) # Schreibe und verifiziere die Daten aus dem CSV File 

for i in range(0, num_cols): # Initiiere den Austausch von Daten zwischen Spalten 1 und 4
    
    buffer = df['Spalte 1'][i] # Puffer die Daten aus der Spalte 1 

    df['Spalte 1'][i] = df['Spalte 4'][i] # Schreibe die Daten aus der Spalte 4 in die Spalte 1
    df['Spalte 4'][i] = buffer # Schreibe die Daten aus dem Puffer in die Spalte 4
    
print(df) # Verifiziere den Wechsel der Spalten 1 und 4