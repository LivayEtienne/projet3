
class Cours:
    def __init__(self):
        self.etudiants = []

    def info_cour(self):
        self.titre = input("Veillez entrer le titre du cour: ").strip()
        self.code = int(input("Veillez entrer le code du cour: "))
        self.professeur = input("Veillez entrer le prof du cour: ").strip()

        print(f"Cour: {self.titre}, code: {self.code}, professeur: {self.professeur}")

    def inscrire_etudiant(self, nom, somme):
        if(somme < 150000 or not nom):
            print("Impossible d'inscrire l'etudiant")
        else:
                self.etudiants.append({nom, somme})
                print(f"Etudiant {nom} inscrit avec la somme de {somme}")

    def attribut_notes(self, nom):
         if not self.etudiants:
              print("Pas de note à ajouter")
         else:
                notes = int(input("Veillez entrer la note de l'etudiant: "))
                self.etudiants.append(notes)
                print(f"Etudiant {nom} a une note de {notes}/20")