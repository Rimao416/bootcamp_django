class Etudiant:
    def __init__(self,nom,age,notes):
        self.nom=nom
        self.age=age
        self.notes=notes
    def calculer_moyenne(self):
        return sum(self.notes) / len(self.notes)
    
    def afficher(self):
        moy=self.calculer_moyenne()
        print(f"{self.nom}, {self.age} ans, Moyenne {moy:.2f} ")
    
etudiant1=Etudiant("Ahmed",22,[15,12,13])
etudiant2=Etudiant("Omari",19,[13,15,13])

etudiant1.afficher()
etudiant2.afficher()