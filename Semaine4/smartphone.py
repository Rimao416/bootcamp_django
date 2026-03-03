"""CLASSE Smartphone
├── Attributs
│   ├── marque
│   ├── modele
│   ├── batterie
│   └── applications
└── Méthodes
    ├── allumer()
    ├── appeler(numero)
    ├── envoyer_sms(numero, message)
    └── charger()"""
    
class Smartphone:
    def __init__(self,marque,modele,batterie,applications):
        self.marque=marque
        self.modele=modele
        self.batterie=batterie
        self.applications=applications
    def allumer(self):
        print(f"Le telephone {self.marque} est allumé ")
    
    def appeler(self,numero):
        if self.batterie <= 5:
            print("Batterie insuffisante pour passer l'appel")
        else:
            print(f"Appel en cours vers {numero}")
            self.batterie -=5
    
    def charger(self):
        self.batterie=100
        print("Batterie pleine")
        
    
mon_tel=Smartphone("Samsung","Galaxy S23",50,["Capcut"])
mon_tel.allumer()
mon_tel.appeler('01234567890')
print("Batterie restante ",mon_tel.batterie)
mon_tel.charger()