################################################################################################################################################
#                                                                                                                                              #
#    Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt                                                      #
#                                                                                                                                              #
################################################################################################################################################

# PYTHON ROUTINE zur einfachen Illustration von Aufbau künstlicher Intelligenz #

import os
import sys
import math

jg = 0.0 # Einkommen pro Jahr
sl = 0.0 # Einkommen pro Stunde

ghk = ''; # Einkommensklasse

print('Bitte geben Sie den vorgeschlagenen Stundenlohn in Euro an :')

sl = input()

jg = 12.0*float(sl)*160.0 # Einkommen pro Jahr bei einem mittleren Einkommen von 160 Stunden pro Monat. 
print (jg)

if (jg < 15000.0) : ghk = 'Geringverdiener'
if (jg >= 15000.0 and jg < 50000.0) : ghk = 'Normalverdiener'
if (jg > 50000.0) : ghk = 'Vielverdiener'

print ('Mit einem Jahresgehalt von'), jg, (' Euro sind Sie : '), ghk