# HERITAGE = Une classe "enfant" qui hérite des attributs et méthodes d'une classe "parent"

class Animal:
    def __init__(self, nom, proprietaire):
        self.nom=nom
        self.proprietaire=proprietaire
    
    def manger(self):
        print(f"L'animal {self.nom} est entrain de manger")
    
    def dormir(self):
        print(f"L'animal {self.nom} est entrain de dormir")
        
class Chien(Animal):
    def __init__(self, nom, proprietaire,race):
        super().__init__(nom,proprietaire)
        self.race=race
    
    def aboyer(self):
        print(f"L'animal {self.nom}, du propriétaire {self.proprietaire} est entrain d'aboyer")
        

mon_chien=Chien("Rex","Omari","Labartor")
mon_chien.aboyer()