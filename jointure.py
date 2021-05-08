class Jointure :
    def __init__ (self, data1, data2):
        self.data1=data1
        self.data2=data2
    
    
    def fusions(self):
        n=len(self.data1)
        new_data=[]
        for ligne in self.data1:
            for l in self.data2[self.data2.index(ligne)]:
                ligne.append(l)
            new_data.append(ligne)
        return new_data
     
        