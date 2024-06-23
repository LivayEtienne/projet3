class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def afficher(self):
        print(f"Le nom: {self.nom}, age: {self.age}")