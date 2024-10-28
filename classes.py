class Fleuve:
    def __init__(self, region, variable, rid, yq, value, year):
        self.region = region
        self.variable = variable
        self.rid = rid
        self.yq = yq
        self.value = value
        self.year = year
    def __str__(self):
        return "region:{}, variable:{}, rid:{}, yd:{}, value:{}, year:{}".format(self.region, 
                                                                           self.variable, self.rid, self.yq, self.value, self.year)
        
        
class Bassin:
    def __init__(self):
        self.destination = []

    def afficher_fleuves(self):
        for elt in self.destination:
            print(elt)

    def taille_bassin(self):
        return len(self.destination)

    def ajouter_fleuve(self, flv):
        self.destination.append(flv)

    def supprimer_fleuve(self, flv):
        self.destination.remove(flv)

    
