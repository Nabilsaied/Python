#Exo Python Orienté Objet :
#1) Créer une classe abstraite Personnage
#2) Créer une ou plusieurs classe héritée(s) de la classe Personnage
#3) Créer une classe Arme (créer 2 variantes, arme à 2 main et arme dans chaque main)
#4) Créer une classe Armure (donner des propriétés pour chaque partie d'armure)
#5) Créer une classe Inventaire
#6) Créer des méthodes pour chacune des classes
#6) Intégrer dans les paramètres des classes héritées de la classe Personnage (étape 2)
#les objets créés à partir des classes Arme, Armure et Inventaire
#7) Créer 2 objets des classes héritées de la classe Personnage (étape 2) afin d'avoir 2 persos

from abc import ABC, abstractmethod

class Personnage(ABC):
    def __init__(self, nom):
        self.nom = nom
        self.arme = None
        self.armure = None
        self.inventaire = Inventaire()

    @abstractmethod
    def se_presenter(self):
        pass

    def presenter_arme(self):
        if self.arme:
            print(self.nom,f" t'es armé avec {self.arme.nom}, qui fait {self.arme.degats} de dégâts et est une arme à {self.arme.type_arme}.")

    def presenter_armure(self):
        if self.armure:
            print(self.nom,f"tu portes une armure composée d'un {self.armure.casque}, d'un {self.armure.plastron}, de {self.armure.jambieres} et de {self.armure.bottes}.")

    def presenter_inventaire(self):
        self.inventaire.lister_objets()

class Guerrier(Personnage):
    def se_presenter(self):
        super().se_presenter()
        self.nom=input('Le Nom du Guerrier est :')
        return self.nom
class Champion(Personnage):
    def se_presenter(self):
        super().se_presenter()
        self.nom=input('Le Nom du champion est :')
        return self.nom

class Arme:
    def __init__(self, nom, degats, type_arme):
        self.nom = nom
        self.degats = degats
        self.type_arme = type_arme

class Armure:
    def __init__(self, casque, plastron, jambieres, bottes):
        self.casque = casque
        self.plastron = plastron
        self.jambieres = jambieres
        self.bottes = bottes

class Inventaire:
    def __init__(self):
        self.objets = []

    def ajouter_objet(self, objet):
        self.objets.append(objet)

    def lister_objets(self):
        print("Objets dans ton inventaire:")
        for objet in self.objets:
            print(f"- {objet.nom}")


guerrier = Guerrier(Personnage)
guerrier.arme = Arme("épée longue du XIII e siècle", 150, "deux mains")
guerrier.armure = Armure("masque de fer", "Plastron en acier", "Jambières en cuir", "Bottes en cuir")
objet_guerrier = Arme("Dague mystérieuse 🗡️", 30, "une main")
guerrier.inventaire.ajouter_objet(objet_guerrier)



champion = Champion(Personnage)
champion.arme = Arme("épée longue du XV e siècle", 500, "deux mains")
champion.armure = Armure("Casque d'or", "Plastron en acier", "Jambières en cuir", "Bottes en or")
objet_champion2=Arme("Dague mystérieuse 🗡️", 30, "une seul  main")
objet_champion=Arme("Sniper ▄︻デ══━一", 200, "deux mains")
objet_champion1=Arme("pistolet 🔫 ", 100, "une seul  main")


champion.inventaire.ajouter_objet(objet_champion)
champion.inventaire.ajouter_objet(objet_champion1)
champion.inventaire.ajouter_objet(objet_champion2)




print('Guerrier ⤵️ ')
guerrier.se_presenter()
guerrier.presenter_arme()
guerrier.presenter_armure()
guerrier.presenter_inventaire()

print("☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️")
print('Champion ⤵️')
champion.se_presenter()
champion.presenter_arme()
champion.presenter_armure()
champion.presenter_inventaire()
