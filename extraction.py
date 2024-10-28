import csv
from classes import Fleuve, Bassin
from connectpg import  connecter_db

# fonction pour ouvrir le csv,  creer des objets de type Fleuve et les charger dans une liste de type Bassin

def lire_fichier(fichierCSV):

    bassin = Bassin()
    
    with open(fichierCSV) as fi:
        # ignorer la 1ere ligne
        lines = fi.readlines()[1:]

    for line in lines:
        token = line.split(",")
        region = token[0]
        variable = token[1]
        rid = token[2]
        yq = token[3]
        value = token[4]
        year = token[5]

        bassin.ajouter_fleuve(Fleuve(region, variable, int(rid), float(yq), int(value), int(year)))
    
    return bassin


def ecrire_fichier(fichierCSV, bassin):
    with open(fichierCSV, "a", newline="\n") as fo:
        ecriteur = csv.writer(fo, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
        # Nom des colonnes
        ecriteur.writerow( ("region", "variable", "rid", "yq", "value", "year") )
        for elm in bassin.destination:
            # serialisation
            ecriteur.writerow( (elm.region, elm.variable, elm.rid, elm.yq, elm.value, elm.year) )


#fichier = "C:/Users/user/Documents/vscode/etl-multiSources/water-fichier1.csv"
#sortie = "C:/Users/user/Documents/vscode/etl-multiSources/sortie.csv"

#liste = lire_fichier(fichier)
#liste.afficher_fleuves()
#print(liste.taille_bassin())
#ecrire_fichier(sortie, liste)

#fl = Fleuve("NELSON", "Change in Lakes", 17, 1996.4, 0, 1996)
#weeb = Bassin()
#weeb.ajouter_fleuve(fl)
#weeb.afficher_fleuves()

def extraire_table():

    # se connecter à la bd WATER2 de postgres
    db_connexion = connecter_db()
    curseur = db_connexion.cursor()

    # executer la requette
    query = "select region, variable, rid, yq, value, year from public.water"
    curseur.execute(query)

    # charger le resultat de la requette dans un objet de type Bassin
    bassin = Bassin()

    for ligne in curseur:
        bassin.ajouter_fleuve(Fleuve(ligne[0], 
                                           ligne[1],
                                           ligne[2],
                                           ligne[3],
                                           ligne[4],
                                           ligne[5])
                                           )
    return bassin

#b = extraire_table()
#b.afficher_fleuves()

