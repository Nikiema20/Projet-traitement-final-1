"""import csv
from datetime import date
from table import Table

# creation de la table covid_hospit_incid_reg qui est une instance de la classe Table
fich = open("covid_hospit_incid_reg.csv", "r")
lect = csv.reader( fich, delimiter = ';')
list_lignes_covid_hospit_incid_reg=[]
for row in lect:
    print(type(row[3]))

nom_colonnes = ["jour", "nomReg", "numReg", "incid_rea"]

table_covid_hospit_incid_reg = Table(nom_colonnes , list_lignes_covid_hospit_incid_reg)"""
from datetime import date
ch=' {} ;'
ch1 = 3 * ch
print(ch1)

"""l = [1 ,5 ,5, (2,1), date(2021,4,7)]
ch1 = "{}, "*5
ch = ch1.format(l[0], l[1], l[2], l[3] , l[4])
ch2 = ch + ch1

ch1 = ch1.format(i for i in l)
l1 = [i for i in l]"""

ch = "{0"+"["+str(5)+"]" + "}; "
print(ch)





