#librerie utilizzate
import matplotlib.pyplot as plt
import numpy as np

#--------------------------------------------------------------------------
#Grafici per la temperatura di 30 gradi
#nota: in questo caso il grafico non viene "graduato" correttamente, per vedere
#una versione graduata vedere quello a 40 gradi
#modificare in caso anche questo
plt.figure('Curve di crescita dei lieviti a 30 gradi')
#Dati
wildtype_30 = [0, 0.0819250031684836, 0.761725004762411, 0.66034998682638]
rad6_30 = [0, 0.0816083274160822, 0.488508333762487, 0.394783333564798]
rad17_30 = [0, 0.149174997893473, 0.704958339532216, 0.578133340304097]
#asse x: il tempo
times = [0, 3, 18, 24]
#aggiunta dei tre vettori nel grafico
plt.plot(times, wildtype_30, marker='.', color='#6495ed')
plt.plot(times, rad6_30, marker='.', color='#32cd32')
plt.plot(times, rad17_30, marker='.', color='#FF8C00')
#etichette dei tre grafici
labels = ['wildtype', 'Δrad6', 'Δrad17']
plt.legend(labels)
#impostazione di gca come axes e setup dei limiti e dei ticks per l'asse x e y
axes = plt.gca()
axes.set_ylim([0.000001, 0.83001])
axes.set_yticks(np.round(np.arange(0.0,0.83, 0.05), 2), minor=False)
axes.set_xlim([0,25])
axes.set_xticks(np.arange(0,25, 1), minor=False)
#axes.set_yticklabels(np.arange(0.0, 0.83, 0.01), fontsize=8)
#titoli e etichette degli assi
plt.ylabel('Optical Density')
plt.title('Temperature = 30°C')
plt.xlabel('Time [hours]')
#linee orizzontali corrispondenti ai valori della densità ottica
plt.axhline(y=0.0819250031684836, color='#dcdcdc', linestyle='--', lw = 0.5)
plt.axhline(y=0.761725004762411, color='#dcdcdc', linestyle='--', lw = 0.5)
plt.axhline(y=0.66034998682638, color='#dcdcdc', linestyle='--', lw = 0.5)
plt.axhline(y=0.0816083274160822, color='#dcdcdc', linestyle='--', lw = 0.5)
plt.axhline(y=0.488508333762487, color='#dcdcdc', linestyle='--', lw = 0.5)
plt.axhline(y=0.394783333564798, color='#dcdcdc', linestyle='--', lw = 0.5)
plt.axhline(y=0.149174997893473, color='#dcdcdc', linestyle='--', lw = 0.5)
plt.axhline(y=0.704958339532216, color='#dcdcdc', linestyle='--', lw = 0.5)
plt.axhline(y=0.578133340304097, color='#dcdcdc', linestyle='--', lw = 0.5)
#linee verticali corrispondenti ai valori del tempo
plt.axvline(x=3, color='#a9a9a9', linestyle='--', lw = 0.5)
plt.axvline(x=18, color='#a9a9a9', linestyle='--', lw = 0.5)
plt.axvline(x=24, color='#a9a9a9', linestyle='--', lw = 0.5)

#-------------------------------------------------------------------------------
#Grafici per la temperatura di 40 gradi
#Nota: nel grafico successivo il tempo corrisponde, dato che e' numero e non stringa
#con #MODIFICATO indico dove ho modificato il codice in modo tale da farlo così
plt.figure('Curve di crescita dei lieviti a 40 gradi')
#Dati
#asse y
wildtype_40 = [0, 0.0784750025098523, 0.62122500843058, 0.543658356803159]
rad6_40 = [0, 0.0744416654730836, 0.334558339479069, 0.268041668770214]
rad17_40 = [0, 0.159441671334207, 0.572374986174206, 0.373224991994599]
# asse x: il tempo
times = [0, 3, 18, 24]
#aggiunta dei tre vettori nel grafico
plt.plot(times, wildtype_40, marker='.', color='#6495ed')
plt.plot(times, rad6_40, marker='.', color='#32cd32')
plt.plot(times, rad17_40, marker='.', color='#FF8C00')
#etichette dei tre grafici
labels = ['wildtype', 'Δrad6', 'Δrad17']
plt.legend(labels)
#impostazione di gca come axes e setup dei limiti e dei ticks per l'asse y e x
axes = plt.gca()
axes.set_ylim([0.000001, 0.65001])
axes.set_yticks(np.round(np.arange(0.0,0.65, 0.05), 2), minor=False)
axes.set_xlim([0,25])
axes.set_xticks(np.arange(0,25, 1), minor=False)
#titoli e etichette degli assi
plt.ylabel('Optical Density')
plt.title('Temperature = 40°C')
plt.xlabel('Time [hours]')
#linee orizzontali corrispondenti ai valori della densità ottica
plt.axhline(y=0.0784750025098523, color='#a9a9a9', linestyle='--', lw = 0.5)
plt.axhline(y=0.62122500843058, color='#a9a9a9', linestyle='--', lw = 0.5)
plt.axhline(y=0.543658356803159, color='#a9a9a9', linestyle='--', lw = 0.5)
plt.axhline(y=0.0744416654730836, color='#a9a9a9', linestyle='--', lw = 0.5)
plt.axhline(y=0.334558339479069, color='#a9a9a9', linestyle='--', lw = 0.5)
plt.axhline(y=0.268041668770214, color='#a9a9a9', linestyle='--', lw = 0.5)
plt.axhline(y=0.159441671334207, color='#a9a9a9', linestyle='--', lw = 0.5)
plt.axhline(y=0.572374986174206, color='#a9a9a9', linestyle='--', lw = 0.5)
plt.axhline(y=0.373224991994599, color='#a9a9a9', linestyle='--', lw = 0.5)
#linee verticali corrispondenti ai valori del tempo
plt.axvline(x=3, color='#a9a9a9', linestyle='--', lw = 0.5)
plt.axvline(x=18, color='#a9a9a9', linestyle='--', lw = 0.5)
plt.axvline(x=24, color='#a9a9a9', linestyle='--', lw = 0.5)

#il grafico è visibile con questa linea di codice
plt.show()
