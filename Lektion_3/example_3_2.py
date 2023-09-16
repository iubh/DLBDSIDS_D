################################################################################################################################################
#                                                                                                                                              #
#    Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt                                                      #
#                                                                                                                                              #
################################################################################################################################################

##################################################################################################
#                                                                                                # 
#   PYTHON ROUTINE zur Berechnung von Spezifizität und Sensitivität für ein Zweiklassenproblem   #
#                                                                                                # 
################################################################################################## 

##############################################################################################################################################################################
#                                                                                                                                                                            #          
#   Few (original) parts of this source code have been used from https://machinelearningmastery.com/roc-curves-and-precision-recall-curves-for-classification-in-python/     #
#                                                                                                                                                                            #              
##############################################################################################################################################################################

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from matplotlib import pyplot


# Konstruiere eine Menge an Klassen mit zwei möglichen Labels 1 und 2
A_1, B_1 = make_classification(n_samples=10000, n_classes=2, random_state=1)
A_2, B_2 = make_classification(n_samples=10000, n_classes=2, random_state=100)
A_3, B_3 = make_classification(n_samples=10000, n_classes=2, random_state=10000)

# Splitte die zwei Datenmengen in einen Traings- und in einen Testdatensatz 
Training_A_1, Testing_A_1, Training_B_1, Testing_B_1 = train_test_split(A_1, B_1, test_size = 0.5, random_state = 2)
Training_A_2, Testing_A_2, Training_B_2, Testing_B_2 = train_test_split(A_2, B_2, test_size = 0.5, random_state = 2)
Training_A_3, Testing_A_3, Training_B_3, Testing_B_3 = train_test_split(A_3, B_3, test_size = 0.5, random_state = 2)

# Fitte das Klassfizierungsmodell zu einem Datensatz
model_1 = LogisticRegression(solver='lbfgs')
model_1.fit(Training_A_1, Training_B_1)

model_2 = LogisticRegression(solver='lbfgs')
model_2.fit(Training_A_2, Training_B_2)

model_3 = LogisticRegression(solver='lbfgs')
model_3.fit(Training_A_3, Training_B_3)

# Berechen die Wahrscheinlichkeiten 
model_1_prob = model_1.predict_proba(Testing_A_1)
model_2_prob = model_2.predict_proba(Testing_A_2)
model_3_prob = model_3.predict_proba(Testing_A_3)

# Wähle die berechneten Wahrscheinlichkeiten, um neue Wahrscheinlichkeiten zu berechnen 
model_1_prob = model_1_prob[:, 1]
model_2_prob = model_2_prob[:, 1]
model_3_prob = model_3_prob[:, 1]

# Berechne Bewertungen für die Wahrscheinlichkeiten
model_1_score = roc_auc_score(Testing_B_1, model_1_prob)
model_2_score = roc_auc_score(Testing_B_2, model_2_prob)
model_3_score = roc_auc_score(Testing_B_3, model_3_prob)

# Quantifizieren Sie die BEwertungen für die ausgewählten Modelle
print('Model Score for Logistic Regression 1 (10^3*1 samples): %.3f' % (model_1_score))
print('Model Score for Logistic Regression 2 (10^3*10^2 samples): %.3f' % (model_2_score))
print('Model Score for Logistic Regression 3 (10^3*10^4 samples): %.3f' % (model_3_score))

# Berechne die ROC Diagramme
model_1_x, model_1_y, _ = roc_curve(Testing_B_1, model_1_prob)
model_2_x, model_2_y, _ = roc_curve(Testing_B_2, model_2_prob)
model_3_x, model_3_y, _ = roc_curve(Testing_B_3, model_3_prob)

# Zeichne die ROC Diagramme
pyplot.plot(model_1_x, model_1_y, marker='.', label='Logistic Regression 1')
pyplot.plot(model_2_x, model_2_y, marker='.', label='Logistic Regression 2')
pyplot.plot(model_3_x, model_3_y, marker='.', label='Logistic Regression 3')

# Setze die Achsenlabels und speichere die Figur
pyplot.xlabel('specivity', fontsize = 12)
pyplot.ylabel('sensitivity', fontsize = 12)
pyplot.xticks(fontsize=10)
pyplot.yticks(fontsize=10)
pyplot.savefig('fig_3_2.png') # Find anf set directory path with 'pwd'
