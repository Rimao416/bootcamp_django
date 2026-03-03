PI = 3.14159

def aire_rectangle(longueur, largeur):
    """Calcule l'aire d'un rectangle"""
    return longueur * largeur
def aire_cercle(rayon):
    """Calcule l'aire d'un cercle"""
    return PI * rayon ** 2

def perimetre_cercle(rayon):
    """Calcule le périmètre (circonférence) d'un cercle"""
    return 2 * PI * rayon

def aire_triangle(base, hauteur):
    """Calcule l'aire d'un triangle"""
    return (base * hauteur) / 2

def aire_carre(cote):
    """Calcule l'aire d'un carré"""
    return cote ** 2

def perimetre_carre(cote):
    """Calcule le périmètre d'un carré"""
    return 4 * cote

# Code de test (s'exécute seulement si on exécute ce fichier directement)
if __name__ == "__main__":
    print("Test du module geometrie")
    print(f"Aire rectangle 10x5: {aire_rectangle(10, 5)}")
    print(f"Aire cercle rayon 5: {aire_cercle(5)}")