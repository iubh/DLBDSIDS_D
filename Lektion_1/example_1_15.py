################################################################################################################################################
#                                                                                                                                              #
#    Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt                                                      #
#                                                                                                                                              #
################################################################################################################################################

# PYTHON ROUTINE zur Normierung von Matrizen #

# Original source from : 
# Authors: Clay Woolam <clay@woolam.org>
# License: BSD

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

from sklearn import datasets
from sklearn.semi_supervised import LabelSpreading
from sklearn.metrics import classification_report, confusion_matrix

digits = datasets.load_digits() # Importiere Daten aus dem Datensatz 'datasets'
rng = np.random.RandomState(0) # Generiere einen zufälligen Anfangszustand 
indices = np.arange(len(digits.data)) # Zähle die Anzahl der Indizes eines Datensatzes
rng.shuffle(indices) # Lege einen zufälligen Sample für den Datensatz fest
X = digits.data[indices[:330]] # Implementiere einen Vektor X für eine Anzahl von festen Indizes
y = digits.target[indices[:330]] # Implementiere einen Vektor y für eine Anzahl von festen Indizes
images = digits.images[indices[:330]] # Implementiere ein Abbild eines Vektors für eine gegebene Anzahl von Indizes
n_total_samples = len(y) # Lege die Anzahl der Datenpunkte in y fest
n_labeled_points = 10 # Lege die Anzahl der Labels fest
max_iterations = 5 # Lege die maximale Anzahl von Iterationen fest, um die Modellgenauigkeit zu erreichen
unlabeled_indices = np.arange(n_total_samples)[n_labeled_points:] # Zähle die Anzahl der ungelabtelten Indizes
f = plt.figure() # Zeige Figur in der Ausgabe

for i in range(max_iterations): # Trainiere das Modell mit bis zu 30 Fittign Parametern (maximal 5 Iterationen)
        
    if len(unlabeled_indices) == 0:

        print("No unlabeled items left to label.")

        break

    y_train = np.copy(y) # Trainiere den y Vektor des Modells 
    y_train[unlabeled_indices] = -1 # Lege die untrainierte Datenmenge auf -1 fest

    lp_model = LabelSpreading(gamma=0.25, max_iter=20) # Lege den Modellparameter für den X Anteil des Modells fest
    lp_model.fit(X, y_train) # Fitte das Modell in X an die trainierten Daten in y 
    
    predicted_labels = lp_model.transduction_[unlabeled_indices] # Speichere die echten Labels der Realisierung an Indizes
    true_labels = y[unlabeled_indices]

    cm = confusion_matrix(true_labels, predicted_labels, labels=lp_model.classes_) # Implementiere die Konfusionsmatrix
    print("Iteration %i %s" % (i, 70 * "_")) # Zeige die Anzahl der Iterationen mit einer Konfusionsmatrix

    print(
        "Label Spreading model: %d labeled & %d unlabeled (%d total)"
        % (n_labeled_points, n_total_samples - n_labeled_points, n_total_samples)
    )

    print(classification_report(true_labels, predicted_labels)) # Gebe einen Klassifizierungsreport aus 
    print("Confusion matrix") # Gebe das Label für den Klassifizierungsreport aus
    print(cm)

    # Berechne die Entropien für die Labelverteilungen
    pred_entropies = stats.distributions.entropy(lp_model.label_distributions_.T)

    # Wähle bis zu 5 Stellen zur Klassifizerung aus
    uncertainty_index = np.argsort(pred_entropies)[::-1]

    uncertainty_index = uncertainty_index[
        np.in1d(uncertainty_index, unlabeled_indices)
    ][:5]

    # Notiere alle Indizies für die Labels erzeugt werden
    delete_indices = np.array([], dtype=int)

    # Falls die Anzahl der Iterationen größer als 5 ist, visualisiere den Zuwachs nur für die ersten 5 
     
    if i < 5:
        f.text(
            0.05,
            (1 - (i + 1) * 0.183),
            "model %d\n\nfit with\n%d labels" % ((i + 1), i * 5 + 10),
            size=10,
        )

    for index, image_index in enumerate(uncertainty_index):
        image = images[image_index]

        # Falls die Anzahl der Iterationen größer als 5 ist, visualisiere den Zuwachs nur für die ersten 5 
        if i < 5:
            sub = f.add_subplot(5, 5, index + 1 + (5 * i))
            sub.imshow(image, cmap=plt.cm.gray_r, interpolation="none")
            sub.set_title(
                "predict: %i\ntrue: %i"
                % (lp_model.transduction_[image_index], y[image_index]),
                size=10,
            )
            sub.axis("off")

        # Hier werden 5 weiteren Labels unabhängig von den vorherigen Labels festgelegt
        (delete_index,) = np.where(unlabeled_indices == image_index)
        delete_indices = np.concatenate((delete_indices, delete_index))

    unlabeled_indices = np.delete(unlabeled_indices, delete_indices)
    n_labeled_points += len(uncertainty_index)

f.suptitle(
    "Active learning with Label Propagation.\nRows show 5 most "
    "uncertain labels to learn with the next model.",
    y=1.15,
)
plt.subplots_adjust(left=0.2, bottom=0.03, right=0.9, top=0.9, wspace=0.2, hspace=0.85) # Zeige die Modellergebnisse
plt.show()