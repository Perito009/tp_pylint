"""Module de gestion des notes des étudiants."""

class Etudiant:
    """Classe représentant un étudiant avec ses notes."""
    def __init__(self, nom, age):
        """Initialise un nouvel étudiant.
        
        Args:
            nom (str): Nom de l'étudiant
            age (int): Age de l'étudiant
        """
        self.nom = nom
        self.age = age
        self.notes = []

    def ajouter_note(self, note):
        """Ajoute une note à la liste des notes.
        
        Args:
            note (float): Note à ajouter
        """
        if not isinstance(note, (int, float)):
            raise TypeError("La note doit être un nombre")
        self.notes.append(float(note))

    def moyenne(self):
        """Calcule la moyenne des notes.
        
        Returns:
            float: Moyenne des notes ou 0 si aucune note
        """
        if not self.notes:
            return 0
        return sum(self.notes) / len(self.notes)

    def afficher_infos(self):
        """Affiche les informations de l'étudiant."""
        print("Nom de l'étudiant :", self.nom)
        print("Age :", self.age)
        print("Moyenne :", self.moyenne())

def main():
    """Fonction principale du programme."""
    etudiant = Etudiant("Alice", 20)
    etudiant.ajouter_note(14)
    etudiant.ajouter_note(16)
    etudiant.ajouter_note(18)
    etudiant.afficher_infos()

if __name__ == "__main__":
    main()
