"""Gestionnaire de bibliothèque personnelle
Fonctionnalités à implémenter:
1. Ajouter un livre (titre, auteur, année, lu/non lu)
2. Afficher tous les livres
3. Marquer un livre comme lu
4. Chercher des livres par auteur
5. Compter les livres lus vs non lus
6. Afficher les livres d'une année spécifique
Structure d'un livre:
{
    "titre": "...",
    "auteur": "...",
    "annee": 2024,
    "lu": True/False
}"""
# Il va contenir tous les livres
bibliotheque=[]
def ajouter_livre(titre,auteur,annee,lu=False):
    livre={
        "titre":titre,
        "auteur":auteur,
        "annee":annee,
        "lu":lu
    }
    bibliotheque.append(livre)
    print(f"Livre '{titre} ajouté avec succès")

def afficher_livres():
    if not bibliotheque:
        print("La bibliothèque est vide")
        return # Le programme s'arrete ici
    for i, livre in enumerate(bibliotheque, start=1):
        statut= "Lu" if livre["lu"] else "Non lu"
        
    
    