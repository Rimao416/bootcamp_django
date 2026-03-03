x = 10  # Variable globale

def fonction1():
    x = 20  # Variable locale (différente de la globale)
    print(f"Dans fonction1: x = {x}")

def fonction2():
    x = 30  # Variable locale (différente des deux autres)
    print(f"Dans fonction2: x = {x}")

print(f"Avant les fonctions: x = {x}")
fonction1()
fonction2()
