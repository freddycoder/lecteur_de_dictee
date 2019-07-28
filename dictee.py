import datetime

class IDictee:
    def obtenir_titre(self):
        raise NotImplementedError

    def obtenir_text(self):
        raise NotImplementedError

class Dictee:
    def __init__(self, titre=datetime.datetime.now().__str__(), text="", cheminFichier=""):
        self.titre = titre
        self.text = text
        self.cheminFichier = cheminFichier

    def sauvegarder(self, cheminFichier : str):
        fichier = open(cheminFichier, 'w+')

        if fichier.mode != 'w+':
            print("Échec lors de l'ouverture de " + cheminFichier + " en mode écriture.")

        fichier.write(self.titre + "\n")
        fichier.writelines(self.text)

        fichier.close()

        self.cheminFichier = cheminFichier

    def charger(self, cheminFichier : str):
        fichier = open(cheminFichier, "r")

        if fichier.mode != "r":
            print("Échec lors de l'ouverture de " + cheminFichier + " en mode lecture.")

        self.titre = fichier.readline()

        line = " "
        while line != '':
            line = fichier.readline()
            self.text += line

        fichier.close()

        self.cheminFichier = cheminFichier