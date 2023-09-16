################################################################################################################################################
#                                                                                                                                              #
#    Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt                                                      #
#                                                                                                                                              #
################################################################################################################################################

# PYTHON ROUTINE zur einfachen Illustration des Aufbaus künstlicher Intelligenz #

import os
import sys
import math

jg = 0.0 # Einkommen pro Jahr
sl = 0.0 # Einkommen pro Stunde

ghk = ''; # Einkommensklasse

print('Bitte geben Sie den vorgeschlagenen Stundenlohn in Euro an :')

sl = input()

jg = 12.0*float(sl)*160.0 # Einommen pro Jahr bei einem mittleren Arbeitsvolumen von 160 Stunden pro Monat. 

if (jg < 15000.0) : ghk = 'Geringverdiener'
if (jg >= 15000.0) : ghk = 'Normalverdiener'

print('Bitte geben Sie den vorgeschlagenen Stundenlohn in Euro an :')

sl_neu = input()

jg_neu = 12.0*float(sl_neu)*160.0 # Einkommen pro Jahr bei einem Arbeitsvolumen von 160 Stunden pro Jahr.

if (jg < 15000.0 and jg_neu < 15000) : ghk = 'Geringverdiener'
if (jg >= 15000.0 and jg_neu < 15000) : ghk = 'Geringverdiener bis Normalverdiener'
if (jg < 15000.0 and jg_neu > 15000) : ghk = 'Geringverdiener bis Normalverdiener'
if (jg >= 15000.0 and jg_neu > 15000) : ghk = 'Normalverdiener'

print (('Mit einem durchschnittlichen Jahresgehalt von'), float(jg+jg_neu)/2.0, (' Euro sind Sie : '), ghk)
