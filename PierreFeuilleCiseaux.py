
from random import choice
coup = ["Pierre","Feuille", "Ciseaux"]
print("\n-------------------------------------------------------------------------------")
print("Le jeu du : Pierre Feuille Ciseaux")
print("-------------------------------------------------------------------------------\n")


#Mon choix 
a = int (input("Choisir un chiffre:\n0:Pierre \n1: Feuille \n2:Ciseaux\n"))
b = choice(range(3))

print(f"Je joue :{coup[b]}")

if (a== b):
    print ("EGALITE")
elif ((a==2 and b==1) or (a==0)and (b==2)) or (a==1 and b==0) :
    print ("TU AS GAGNE")
else:
    print("TU AS PERDU")