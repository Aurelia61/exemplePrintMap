#Je recupere ma variable de type list qui contient ma map (voir map.txt)
import mapInListe


# Je crée un premier compteur qui va indiquer la ligne en cours de lecture
compteur1 = 0
y = 1
x = 1
#je parcours ma liste
for index in mapInListe.mapListe:
    #je crée un deuxieme compteur qui m'indiquera lui la colonne en cours de lecture
    compteur2 = 0
    #j'initialise ou reinitialise une var qui representera la ligne en cours d'impression
    ligne = ""
    #je partours toutes mes colonnes de la ligne en cours
    while compteur2 < len(mapInListe.mapListe[0]):
        #je rajoute le nouvel item dans ma string en cours qui represente la ligne en cours d'impression
        if compteur1 == y and compteur2 == x:
            ligne = f"{ligne}@"
        else:
            ligne = str(ligne) + str(mapInListe.mapListe[compteur1][compteur2])
        #j'incremente la colonne pour passer à la suivante
        compteur2 = compteur2 + 1
    #j'incremente la ligne pour passer à la suivante
    compteur1 = compteur1 + 1
    #je print ma ligne terminée
    print(ligne)