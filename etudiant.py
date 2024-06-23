from personne import Personne

class Etudiant(Personne):
    def __init__(self, nom, age, matricule, cour_suivi):
        super().__init__(nom, age)
        self.matricule = matricule
        self.cour_suivi = cour_suivi

    def etudiant_affiche(self):
        print(f"Nom: {self.nom}, Age: {self.age}, Le matricule est : {self.matricule}, cour suivie: {self.cour_suivi}")
