# if expression:
#       suite_si_vrai

warn = False
system_load = 5
if not warn and system_load >= 10: #si il n'y a pas de warning et que le système load est supérieur ou égal à 10
    print("WARNING: Perte de ressource") #alors on a ce message
    warn = True
    
    