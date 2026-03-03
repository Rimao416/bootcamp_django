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
        print(f"{i}. {livre['titre']} - {livre['auteur']} ({livre['annee']}) [{statut}]")
        
def marquer_comme_lu(titre):
    for livre in bibliotheque:
        if livre['titre'].lower()== titre.lower():
            livre['lu']=True
            print(f"Livre {titre} marqué comme Lu")
    print(f"Livre non trouvé")


def compter_livres():
    lus=sum(1 for livre in bibliotheque if livre["lu"])
    non_lus=len(bibliotheque) - lus
    
    print(f"Lus : {lus}")
    print(f"Non Lus : {non_lus}")
    

def chercher_par_auteur(auteur):
    resultats=[livre for livre in bibliotheque if livre['auteur'].lower()== auteur.lower()]
    if not resultats:
        print(f"Aucun livre trouvé pour l'auteur {auteur}")
        return 
    print(f"Livre(s) de {auteur}")
    for livre in resultats:
        statut="Lu" if livre["lu"] else "Non lu"
        print(f" - {livre['titre']} ({livre['annee']}) [{statut}]")

def afficher_par_annee(annee):
    resultats=[livre for livre in bibliotheque if livre['annee'] == annee]
    if not resultats:
        print(f"Aucun livre trouvé pour l'année {annee}")
        return
    print(f"Livre(s) de {annee}")
    for livre in resultats:
        statut="Lu" if livre["lu"] else "Non lu"
        print(f" - {livre['titre']} ({livre['annee']}) [{statut}]")
    

if __name__=="__main__":
    ajouter_livre("1984","George Orwell",1949)
    ajouter_livre("L'Alchimiste","Paulo Coelho",1988,True)
    ajouter_livre("Clean Code","Robert C.Martin",2008)
    
    print("\n --- Tous les livres ---")
    afficher_livres()
    
    print("\n --- Marquer comme lu ---")
    marquer_comme_lu("1984")
    
    print("\n --- Recherche par auteur ---")
    chercher_par_auteur("Paulo Coelho")
    
    print("\n --- Compter les livres ---")
    compter_livres()
    
    print("\n --- Livres par année ---")
    afficher_par_annee(2008)
    
        
    
        
        
        
    
    