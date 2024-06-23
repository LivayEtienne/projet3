from personne import Personne

class Professeur(Personne):
    def __init__(self, nom, age, employe_id, cours_enseignes):
        super().__init__(nom, age)
        self.emplye_id = employe_id
        self.cours_enseignes = cours_enseignes

    def affiche_professeur(self):
        print(f"Nom du prof: {self.nom}, age : {self.age}, id : {self.emplye_id}, cour : {self.cours_enseignes}")