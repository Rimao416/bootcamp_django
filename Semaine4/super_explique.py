class Vehicule:
    def __init__(self,marque,couleur,modele):
        self.marque=marque
        self.couleur=couleur
        self.modele=modele
        
    def demarrer(self):
        print(f"La voiture {self.marque} est entrain de demarrer")
        
class VoitureElectrique(Vehicule):
    def __init__(self,marque, couleur, modele, autonomie):
        super().__init__(marque,couleur,modele)
        self.autonomie=autonomie
        self.batterie=100
    
    def afficher_batterie(self):
        print(f"Batterie {self.batterie}")
        
    def demarrer(self):
        super().demarrer()
        print("Mode électrique activé")
        self.afficher_batterie()

ma_tesla=VoitureElectrique("Tesla","Rouge","Model 3",100)
ma_tesla.demarrer()