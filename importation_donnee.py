import csv   # importer le module csv de python
import json  # Importer le module json
class Importation_donnee :
    def __init__(self,folder, file_name):
        ''' importation des données 
        attributes
        _________
        folder: str
        file_name: str
        '''
        self.folder=folder
        self.file_name=file_name

    def import_csv(self):
        '''
        importation des dossiers csv
        
        return : 
        _____
        list
        '''
             
        data = []
        with open(self.folder + self.file_name, encoding='ISO-8859-1') as csvfile :
            covidreader = csv.reader(csvfile, delimiter= ';')
            for row in covidreader :
                data.append(row)
                
            supprime_tete=data.pop(0)      
        return data
        
    def import_json(self):
        # Dossier où se trouve le fichier :
        '''
        importation des dossiers json
        return
        ______
        list
        '''
        data = []
        with open(self.folder + self.file_name) as json_file :
            covidreader = json.load(json_file)
            for row in  covidreader:
                data.append(row)
            supprime_tete=data.pop(0)
            return data

        
        
            
       
       
