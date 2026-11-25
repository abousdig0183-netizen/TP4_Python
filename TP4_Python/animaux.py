
class Animal:
    def parler(self):
        raise NotImplementedError(
            "Cette méthode doit être redéfinie"
        )


class Chien(Animal):
    def parler(self):
        return "Ouaf !"


class Chat(Animal):
    def parler(self):
        return "Miaou !"


class Vache(Animal):
    def parler(self):
        return "Meuh !"


# Classe indépendante : Duck Typing
class Robot:
    def parler(self):
        return "Bonjour ! Je suis un robot."


def faire_parler(animal):
    print(animal.parler())


if __name__ == "__main__":

    # Collection de plusieurs animaux
    animaux = [
        Chien(),
        Chat(),
        Chien(),
        Vache()
    ]

    print("=== Les animaux ===")
    for animal in animaux:
        faire_parler(animal)

    # Démonstration du Duck Typing
    print("\n=== Duck Typing ===")

    robot = Robot()

    objets = [Chien(), Chat(), Vache(), robot]

    for objet in objets:
        faire_parler(objet)
