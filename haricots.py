from datetime import datetime, time
import time as sleep

enceinte_1 = False # Au départ, toutes les lumières sont éteintes
enceinte_2 = False
enceinte_3 = False
enceinte_4 = False
# La 5ème enceinte reste toujours allumée, elle n'est donc pas présente dans le programme


heure_allumage_enceintes = time(0, 0) # Les LED vont s'allumer à minuit
heure_extinction_enceinte_1 = time(15, 0) # On paramètre les heures où les enceintes vont s'éteindre dans des instances time
heure_extinction_enceinte_2 = time(17, 15)
heure_extinction_enceinte_3 = time(19, 30)
heure_extinction_enceinte_4 = time(21, 45)

def haricots():
    global enceinte_1, enceinte_2, enceinte_3, enceinte_4 # on déclare les variables "enceinte" comme globales pour qu'elles soient utilisables dans la fonction
    while True:
        temps_actuel = datetime.now().time()
        if temps_actuel >= heure_allumage_enceintes and enceinte_1 == False: # lorsque l'enceinte est éteinte et qu'il est l'heure de l'allumer
            enceinte_1 = True
        if temps_actuel >= heure_allumage_enceintes and enceinte_2 == False:
            enceinte_2 = True
        if temps_actuel >= heure_allumage_enceintes and enceinte_3 == False:
            enceinte_3 = True
        if temps_actuel >= heure_allumage_enceintes and enceinte_4 == False:
            enceinte_4 = True

        if temps_actuel >= heure_extinction_enceinte_1 and enceinte_1 == True: # lorsque l'enceinte est allumée et qu'il est l'heure de l'éteindre
            enceinte_1 = False
        if temps_actuel >= heure_extinction_enceinte_2 and enceinte_2 == True:
            enceinte_2 = False
        if temps_actuel >= heure_extinction_enceinte_3 and enceinte_3 == True:
            enceinte_3 = False
        if temps_actuel >= heure_extinction_enceinte_4 and enceinte_4 == True:
            enceinte_4 = False

        status() # on print le statut des variables
 
        sleep.sleep(10) # on "dort" 10 secondes pour ne pas surcharger le programme



        

def status(): # la fonction "status" print l'état des 4 variables "enceinte" 
    temps = datetime.now().time()
    temps = temps.strftime("%H:%M:%S")
    print(f"Il est {temps}")
    print(f"Enceinte 1 = {enceinte_1}")
    print(f"Enceinte 2 = {enceinte_2}")
    print(f"Enceinte 3 = {enceinte_3}")
    print(f"Enceinte 4 = {enceinte_4}")
    print("") # On saute une ligne pour que la console soit plus claire


haricots() # On lance le programme en appelant la fonction "haricots"
        
            


