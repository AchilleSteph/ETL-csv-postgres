
#from connectpg import 
from classes import Bassin, Fleuve
from extraction import lire_fichier, ecrire_fichier, extraire_table

def main():
    print("Processus ETL, source de destination: fichier csv")
    ETL = "C:/Users/user/Documents/vscode/etl-multiSources/ETL-water.csv"
    print("Sources multiple, Source 1: fichier csv, source 2 : table dans une base de données Postgres")
    print("="*100)
    
    # extraire les données du fichier csv: source 1
    
    source1 = fichier = "C:/Users/user/Documents/vscode/etl-multiSources/water-fichier1.csv"
    print("Début d'extraction du fichier csv " + "- "*30)
    bassin1 = lire_fichier(source1)
    print(" "*50)
    print("Fin d'extraction et début du chargement "  + "- "*40)
    ecrire_fichier(ETL, bassin1)
    print(" "*50)
    print("Fin du chargement. Nombre d'unités  chargées en ETL: {}".format (bassin1.taille_bassin()))
    print(" "*50)

    # extraire les données de la table nommée public.water: source 2
    print("Début d'extraction de la table Postgres " + "- "*30)
    bassin2 = extraire_table()
    print(" "*50)
    print("Fin d'extraction de la table et début du chargement "  + "- "*30)
    ecrire_fichier(ETL, bassin2)
    print(" "*50)
    print("Fin du chargement de la table. Nombre d'unités  chargées en ETL: {}".format (bassin2.taille_bassin()))
    print(" "*30)
    print("="*30)
    print("ETL réussi")
    print("La source de destination contient: {}" .format(bassin1.taille_bassin() + 
                                                                      bassin2.taille_bassin()))
    print("Copier le lien ci-dessous et coller dans un browser pour visualiser le fichier final: ")
    print("     lien: {}" . format(ETL))



    
if __name__=="__main__":
    main()