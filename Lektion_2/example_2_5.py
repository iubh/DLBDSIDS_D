################################################################################################################################################
#                                                                                                                                              #
#    Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt                                                      #
#                                                                                                                                              #
################################################################################################################################################

##############################################################################################################
#                                                                                                            #
#   PYTHON ROUTINE zur Berechnung eines quantenmechanischen Wellenfeldes mit Darstellung als 2D Histogramm   #
#                                                                                                            #
##############################################################################################################

import math
import random
import numpy
import matplotlib.pyplot as plt
import operator

maxmode = 250 # Typische Modengröße: 500 - 2500 modes
ptn = 1000 # Typische Teilchenanzahl: 10^3 - 10^5
sample = 10000 # Typische Samplegröße: 10^5 - 10^8 

omx = 2.0*math.pi*42.0 # Frequenzkomponente in x Richtung 
omy = 2.0*math.pi*42.0 # Frequenzkomponente in y Richtung 
omz = 2.0*math.pi*120.0 # Frequenzkomponente in z Richtung 

start_temp = 2.5 # in Einheiten von nK
rhbkb = 7.63822291E-3 # in Einheiten von nK

norm = 0.0
int_norm = 0
drop = 0
prob = 0.0
phase_0 = 0.0
z_start = start_temp
mu_start = 0.0
mu_k = 0.0

print ('Trap depth [nK]: '), maxmode*omz*rhbkb # Fallentiefe
print ('Critical temperature [nK]: '), rhbkb*pow(ptn,1.0/3.0)*pow(omx*omy*omz,1.0/3.0)/pow(1.202,1.0/3.0) # kritische Temperatur

en_x = ['']*maxmode
en_y = ['']*maxmode
en_z = ['']*maxmode

pols_x = ['']*maxmode
pols_y = ['']*maxmode
pols_z = ['']*maxmode

pols = ['']*maxmode

x = ['']*ptn
y = ['']*ptn

mu_x = [] # Sammle alle Realteile eines integrierten Quantenfeldes
mu_y = [] # Sammle alle Imaginärteile eines integrierten Quantenfeldes

for l in range(1, sample):
          
    drop = 1
    z = random.uniform(1, ptn) # Zufälliges Sampling eines Nicht-Kondensat Feldes
    temp = start_temp

    mu = 0.0
    norm = 0.0
    
    print(('Sample step Nr. '), str(l))
                  
    for k in range(1, maxmode):
        
        en_x[k] = rhbkb*k*omx/temp # Energie in x Richtung
        en_y[k] = rhbkb*k*omy/temp # Energie in y Richtung
        en_z[k] = rhbkb*k*omz/temp # Energie in z Richtung
     
        pols_x[k] = 1.0/(1.0-math.exp(-en_x[k])) # Komplexe Pole in der x-Richtung
        pols_y[k] = 1.0/(1.0-math.exp(-en_y[k])) # Komplexe Pole in der y-Richtung
        pols_z[k] = 1.0/(1.0-math.exp(-en_z[k])) # Komplexe Pole in der z-Richtung
                    
    for k in range(1, maxmode):
    
        pols[k-1] = pols_x[maxmode-k]*pols_y[maxmode-k]*pols_z[maxmode-k]-1.0 # Berechnung der Pole
    
    pols[maxmode-1] = -(ptn-z_start)

    prob = complex(0.0,0.0)
    p = ['']*maxmode
    phase_0 = 0.0
   
    x = numpy.roots(pols) # Komplexe Wurzeln aus der Erhaltungsgleichung der Teilchenzahl
    
    for k in range(0,len(x)):

        p[k] = random.uniform(0.0,1.0)   # Zufällige Amplituden 
        norm = norm + p[k]*p[k]*(x[k].real**2+x[k].imag**2) # Norm
        
    norm = math.sqrt(norm)
    
    for k in range(0,len(x)): # Berechne die Phase eines Kondensatwellenfeldes
        	
        p[k] = p[k]/norm # Zufällige Amplituden
    	
        if (operator.gt(x[k].real**2 + x[k].imag**2,0.0)):
                
            if (operator.gt(x[k].real,0.0)):
            
                phase_0 = math.atan(x[k].imag/x[k].real)
        
            if (operator.iand(operator.lt(x[k].real,0.0),operator.ge(x[k].imag,0.0))):
            
                phase_0 = math.atan(x[k].imag/x[k].real) + math.pi
    
            if (operator.iand(operator.lt(x[k].real,0.0),operator.lt(x[k].imag,0.0))):
	            
                phase_0 = math.atan(x[k].imag/x[k].real) - math.pi
    
            if (operator.iand(operator.eq(x[k].real,0.0),operator.gt(x[k].imag,0.0))):
            
                phase_0 = 0.5*math.pi

            if (operator.iand(operator.eq(x[k].real,0.0),operator.lt(x[k].imag,0.0))):
            
                phase_0 = -0.5*math.pi
        	       
            mu += x[k]*p[k] # Zufällige Amplitude mal der Phase
            mu_k = x[k]*p[k] # Kondensat Quantenfeld
            
            if operator.ne(phase_0,0.0):
    	
                prob += complex(0.5*p[k]*p[k]*math.log(math.fabs(x[k].real**2 + x[k].imag**2)), p[k]*p[k]*phase_0) # Calculate transition probability
    	
            prob = math.sqrt(prob.real**2 + prob.imag**2) 
    	
    if (operator.gt(min((math.exp(prob))/(math.exp(mu_start)),1.00),random.uniform(0.00,1.00))): # Übergangswahrscheinlichkeit
        
        mu_start = prob
        z_start = z
        drop = 0
	    
    if (operator.ne(drop,1)):	
		
        mu_x.append(1.0*mu.real) # Sammle alle Nicht-Kondensat Quantenfelder in X-Richtung
        mu_y.append(1.0*mu.imag) # Sammle alle Nicht-Kondensatfelder in Y-Richtung

        mu_x.append(-1.0*mu.real) # Sammle alle Kondensatfelder in X-Richtung
        mu_y.append(1.0*mu.imag) # Sammle alle Kondensatfelder in Y-Richtung

        if (operator.gt(mu.real,0.0)): # Positive X-Achse 
        
            phase_0 = math.atan(mu.imag/mu.real) + math.pi
        			
        if (operator.iand(operator.lt(mu.real,0.0),operator.ge(mu.imag,0.0))): # Erste Viertelebene
            
    	    phase_0 = math.atan(mu.imag/mu.real) + math.pi + math.pi
    
        if (operator.iand(operator.lt(mu.real,0.0),operator.lt(mu.imag,0.0))): # Zweite Viertelebene
	            
            phase_0 = math.atan(mu.imag/mu.real) - math.pi + math.pi
    
        if (operator.iand(operator.eq(mu.real,0.0),operator.gt(mu.imag,0.0))): # Dritte Viertelebene
            
            phase_0 = 0.5*math.pi + math.pi

        if (operator.iand(operator.eq(mu.real,0.0),operator.lt(mu.imag,0.0))): # Vierte Viertelebene
            
            phase_0 = -0.5*math.pi + math.pi
    	    	        

plt.figure(1)
plt.hist(mu_x, bins = 250)
plt.tick_params(axis='both', which='major', labelsize = 16)
plt.xlabel('$Re(\Psi_0)$', fontsize = 18)
plt.ylabel('$\pi[Re(\Psi_0)]$', fontsize = 18)
plt.savefig('fig_re.png')

plt.figure(2)
plt.hist(mu_y, bins = 250)
plt.tick_params(axis='both', which='major', labelsize = 16)
plt.xlabel('$Im(\Psi_0)$', fontsize = 18)
plt.ylabel('$\pi[Im(\Psi_0)]$', fontsize = 18)
plt.savefig('fig_im.png')
