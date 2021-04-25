from importation_donnee import Importation_donnee
from table import Table
#from graphique import Graphique
#from clustering import Clustering


if __name__ == "__main__":
   # a=Don
    # importation des donnes hopitaliere
    covid_hospit=Importation_donnee('P:\\Projet_de_Traitemant\\Projet\\',"donnees_hospitalieres_covid.csv")
    covid_hospit.import_csv()
   # print(*covid_hospit.import_csv(),sep="\n")
    
    # importation des données donnees_hospitalieres_classe_age_covid
    #covid_hospit_class=Donnees('P:\\Projet_de_Traitemant\\Projet\\',"donnees_hospitalieres_classe_age_covid.csv")
   # print(*covid_hospit_class.import_csv(),sep="\n")
    
     # importation des données hospitalieres_etablissements_covid
  #  covid_hospit_etab=Donnees('P:\\Projet_de_Traitemant\\Projet\\',"donnees_hospitalieres_etablissements_covid.csv")
  #  print(*covid_hospit_etab.import_csv(),sep="\n")
    
    
    # importation des données hospitalieres_nouveaux_covid
  #  covid_hospit_nouv=Donnees('P:\\Projet_de_Traitemant\\Projet\\',"donnees_hospitalieres_nouveaux_covid.csv")
  #  print(*covid_hospit_nouv.import_csv(),sep="\n")
    
   # creation d'une tables
   
    a=Table(['dep','sexe','jour','hosp','rea','rad','dc'], ['2','M','2021-04-25','25','12','0'])
   
    a.ajouter_lignes(['2','M','2021-04-25','25','12','0'])
    
    b=Table(['dep','sexe','jour','hosp','rea','rad','dc'], covid_hospit.import_csv())
    b.ajouter_lignes(['2','M','2021-04-25','25','12','0'])
    print(*covid_hospit.import_csv(),sep="\n")
   # print(a.moyenne('hosp'))
   
   # print(a.nombre_totale('rea'))
    
   # d= MethodesDescriptives(covid_hospit_class.import_csv())
   # print(d.moyenne('hosp'))
    
   # print(d.nombre_totale('rea'))
  #  print(a.total_vacance("2021-01-01","2021-01-31","jour","hosp"))
    # vacance
    #print(a.total_vacance("2021-02-03","2021-03-03","jour","hosp"))
   # print(total_vacance_specifique("2021-02-03","2021-03-03","jour","hosp","76"))
    #c=Clustering(a)
   #"c.donnee_centre
    #b=Graphique(a)
    #b.boxplot('hosp','rea')
    
    #a.affichageRegion("hosp")
   # covid_hospit=Donnees('P:\\Projet_de_Traitemant\\Projet\\',"donnees_hospitalieres_covid.csv")
   # print(*covid_hospit.import_csv(),sep="\n")
 
    #  affichage(covid_region)
   

    
 #   for row in read : # parcours du lecteur avec une boucle
  #  print (row) # affichage ligne à ligne

#file.close ( )


