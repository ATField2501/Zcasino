#!/usr/bin/python2
# -*- coding: utf8 
# auteur: <atfield2501@gmail.com>
# Jeu de casino

import random
from math import ceil

soldeB = 1000000
soldeJ = 500


def Fonction_verif():
    global soldeJ
    soldeJ=int(soldeJ)
    if soldeJ == 0:
        print"\n * Vous n'êtes plus solvable * "  
        exit()    
    else:        
        Fonction_choix() 


def Fonction_choix():
    try:
        choiX = raw_input("\nVoulez-vous: j= Jouer ou q= Quiter  ? :")  
    except:
        print"\n * Mauvaise entrée... Veillez recommencez * \n"

    if choiX == "q":
        exit()               
    elif choiX == 'j':
        Fonction_Jeu()
    else:    
        print"  ---------------- "    
        print"\n * Mauvaise entrée... Veillez recommencez * \n"
        Fonction_choix()



def Fonction_Jeu():    
    global soldeJ
    print"  ---------------- "
    with open("Fichier_Joueurs.txt", "r") as f:
        print(f.readline())
    try:
        mise = input("Votre Mise : ")
        print"  ---------------- "
    except:
        print" * Mauvaise entrée... Veillez recommencez * \n"
        Fonction_Jeu()
    if mise > soldeJ:
        print"\n * Mauvaise entrée... Veillez recommencez * \n"
        Fonction_Jeu()
    else:
        nbJoueur = input("Votre Numéro 1/50: ")
        print"  ---------------- "
        if nbJoueur > 50 :
            print" * Mauvaise entrée... Veillez recommencez * \n"
            Fonction_Jeu()
        else:
            print"\n * les jeux sont fait...Rien ne vas plus... * \n"
            from random import randrange
            numero = random.randint(1,50)
            yy=str(numero)
            print(" ___      ___      ___")
            print("\n ***       " + yy + "      ***")
            print(" ___      ___      ___\n")

            yy=int(yy)
            nbJoueur=int(nbJoueur)
            soldeJ=int(soldeJ)
            if yy == nbJoueur:
                print"       * Victoire *"
                nMise= mise * 3 + 500

                soldeJ= soldeJ + nMise
                xx=str(nMise) 
                with open("Fichier_Joueurs.txt", "w") as f:
                    f.write(joueur + " - Solde  : " + xx + "$")
                with open("Fichier_Joueurs.txt", "r") as f:
                    print(f.readline())
                    Fonction_verif()
            elif yy % 2 == nbJoueur % 2: # Hum.. subtil snippet O.C.R
                 soldeE = ceil(mise * 0.5)
                 soldeJ += soldeE  
                 print"   * Couleur Gagnante * \n" 
                 xx=str(soldeJ)                
                 with open("Fichier_Joueurs.txt", "w") as f:
                    f.write(joueur + " - Solde  : " + xx + "$")
                 with open("Fichier_Joueurs.txt", "r") as f:
                    print(f.readline())
                    Fonction_verif()

            else :
                print"\n       * Perdue *  \n"  

                soldeJ=int(soldeJ)                  
                soldeJ= soldeJ - mise
                xx=str(soldeJ)                
                with open("Fichier_Joueurs.txt", "w") as f:
                    f.write(joueur + " - Solde  : " + xx + " $")
                with open("Fichier_Joueurs.txt", "r") as f:
                    print(f.readline())
                Fonction_verif()             

# Début du programme.. #########################  
print"  ---------------- "                                  
print"  -   Zcasino    - "                                  
print"  ---------------- "
print"    version  1.0   "
print""

try:
    joueur = raw_input("Votre Nom : ")
except:
    print"\n * Mauvaise entrée... Veillez recommencez * \n"

print"  ---------------- "
print("\n * Bienvenue dans le Zcasino *\n")
print"  ---------------- \n"
print("      * " + joueur + " * ")
print"\n  ---------------- "


soldeJ=str(soldeJ)
with open("Fichier_Joueurs.txt", "w") as f:
    f.write(joueur + " - Solde  : " + soldeJ + " $")

with open("Fichier_Joueurs.txt", "r") as f:
    print(f.readline())
Fonction_choix()


