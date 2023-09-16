##############################################################################################
#                                                                                            #
#   PYTHON ROUTINE zur Berechnung der Genauigkeit der Untermenge an gegeben Messwerten       #                                                         #
#                                                                                            # 
############################################################################################## 


import csv
import random
import pandas

def accuracy(cfs, ncols): # Funktion, welche die Genauigkeit quantifiziert 
    
    arcy = ardg = 0.0

    for i in range(ncols):

        ardg = ardg + cfs[i][i]

        for j in range(ncols):

            arcy = arcy + cfs[i][j]

    return float(ardg/arcy)

i = j = k = 0

num_cols = 10 # Definiere die Anzahl der Spalten 

cfm = [[0.0 for k in range(num_cols)] for l in range(num_cols)] # Definiere das Datenfeld 
data = [0.0]*num_cols

index = ['Spalte 1', 'Spalte 2', 'Spalte 3', 'Spalte 4', 'Spalte 5', 'Spalte 6', 'Spalte 7', 'Spalte 8', 'Spalte 9', 'Spalte 10'] # Definiere die Spaltennamen als Vektor mit n_column Einträgen
        
with open('import_file_2.csv', 'w') as f: # Setze den Adresspfad und öffne das Datenfile
    
    writer = csv.writer(f) # Schreibe ins CSV File
    writer.writerow(index) # Schreibe den Header ins CSV File
    
    for i in range(0, num_cols): # Beschriftung für die Datenspalten

        for j in range(0, num_cols): # Beschriftung für Datenzeilen

            if (i == j) : data[j] = float(random.uniform(0, 10000.0)) # Schreieb den Header des CSV Files
            if (i != j) : data[j] = float(random.uniform(0, 10.0)) # Schreiebe den Header des files ins CSV file 
            
        writer.writerow(data) # Schreieb die Daten ins CSV File
        
df = pandas.read_csv('import_file_2.csv') # Lese die Daten aus dem CSV File zum Vergleich von Strings - setze den richtigen Pfad mit pwd

# Konstruiere die Konfusionmatrix

for i in range(0, num_cols):

    for j in range(0, num_cols): # Initiiere den Austausch von Daten zwischen den Spalten 1 und 4
        
        cfm[i][j] = int(df[index[i]][j]) # Die Konfusionsmatrix wird aus der Float Matrix aus dem import_file.csv konstruiert
        
acu_1 = accuracy(cfm,num_cols) # Genaugkeit der Konfiguration 1
pf = pandas.DataFrame.filter(df, items=['Spalte 1', 'Spalte 4', 'Spalte 8']) # Konfusionsmatrix aus dem reduzierten System mit nur drei Spalten

num_cols = 3 # Setze die Analh der Spalten entsprechend auf drei 
new_index = ['Spalte 1', 'Spalte 4', 'Spalte 8'] # Definiere den neuen Index Attributwert 

for i in range(0, num_cols): # Interiere über die Anzahl der Spalten
    
    for j in range(0, num_cols): # Initiiere den Austuasch von Daten zwischen den Spalten 1 und 4
                
        cfm[i][j] = int(pf[new_index[i]][j]) # Konfusionsmatrix wird aus dem File import_file.csv konstruiert 
        
acu_2 = accuracy(cfm,num_cols) # Genaugkeit der Konfiguration 2 

print('Accuracy improvement : ', (acu_2-acu_1)*100.0, '%') # Berechne und schreieb die Verbesserung der Genaugkeit