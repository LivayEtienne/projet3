from personne import Personne
from etudiant import Etudiant
from professeur import Professeur
from cours import Cours

def main():
    personne = Personne("Etienne", 72)
    personne.afficher()

    etudiant = Etudiant("Habib", 19, 13, "Mathematique")
    etudiant.etudiant_affiche()

    professeur = Professeur("Diallo", 53, 1, "Alogo")
    professeur.affiche_professeur()

    cour = Cours()
    nom = input("Veillez entrer le nom de l'etudiant: ").strip()
    somme = int(input("Veillez entrer la somme: "))
    cour.info_cour()
    cour.inscrire_etudiant(nom, somme)
    cour.attribut_notes(nom)


main()