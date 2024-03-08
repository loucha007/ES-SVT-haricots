from datetime import datetime, time
from time import sleep
import gpiozero

enceinte_1 = gpiozero.OutputDevice(26, active_high = True, initial_value = False)
enceinte_2 = gpiozero.OutputDevice(19, active_high = True, initial_value = False)
enceinte_3 = gpiozero.OutputDevice(13, active_high = True, initial_value = False)
enceinte_4 = gpiozero.OutputDevice(6, active_high = True, initial_value = False)
# La 5ème enceinte reste toujours allumée, elle n'est donc pas présente dans le programme

status_led = gpiozero.LED(5)

heure_allumage_enceintes = time(0, 0) # Les LED vont s'allumer à minuit
heure_extinction_enceinte_1 = time(15, 0) # On paramètre les heures où les enceintes vont s'éteindre dans des instances time
heure_extinction_enceinte_2 = time(17, 15)
heure_extinction_enceinte_3 = time(19, 30)
heure_extinction_enceinte_4 = time(21, 45)

def haricots():    
    while True:
        temps_actuel = datetime.now().time()
        if temps_actuel >= heure_allumage_enceintes and enceinte_1.value == 0: # lorsque l'enceinte est éteinte et qu'il est l'héure de l'allumer
            enceinte_1.on()
        if temps_actuel >= heure_allumage_enceintes and enceinte_2.value == 0:
            enceinte_2.on()
        if temps_actuel >= heure_allumage_enceintes and enceinte_3.value == 0:
            enceinte_3.on()
        if temps_actuel >= heure_allumage_enceintes and enceinte_4.value == 0:
            enceinte_4.on()

        if temps_actuel >= heure_extinction_enceinte_1 and enceinte_1.value == 1: # lorsque l'enceinte est allumée et qu'il est l'héure de l'éteindre
            enceinte_1.off()
        if temps_actuel >= heure_extinction_enceinte_2 and enceinte_2.value == 1:
            enceinte_2.off()
        if temps_actuel >= heure_extinction_enceinte_3 and enceinte_3.value == 1:
            enceinte_3.off()
        if temps_actuel >= heure_extinction_enceinte_4 and enceinte_4.value == 1:
            enceinte_4.off()

        status() # on print le statut des variables et on fait clignoter la led de statut

         
        sleep(10) # on "dort" 10 secondes pour ne pas surcharger le programme

        status_led.off()
        
        

def status(): # la fonction "status" print l'état des 4 variables "enceinte" 
    temps = datetime.now().time()
    temps = temps.strftime("%H:%M:%S")
    print(f"Il est {temps}")
    print(f"Enceinte 1 = {enceinte_1.value}")
    print(f"Enceinte 2 = {enceinte_2.value}")
    print(f"Enceinte 3 = {enceinte_3.value}")
    print(f"Enceinte 4 = {enceinte_4.value}")
    print("") # On saute une ligne pour que la console soit plus claire
    status_led.on()
    sleep(0.25)
    status_led.off()


haricots() # On lance le programme en appelant la fonction "haricots"
        
            


