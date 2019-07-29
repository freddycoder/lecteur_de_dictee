class IParametresLecture:
    def nb_lecture_par_phrase(self):
        raise NotImplementedError

    def duree_des_pauses(self):
        raise NotImplementedError

    def nb_mots_par_phrases(self):
        raise NotImplementedError

class ParametresLecture:
    def __init__(self, nb_lecture_par_phrase=2, nb_mots_par_phrase_prononce=7, nb_seconde_entre_pause=7):
        self.nb_lecture_par_phrase = nb_lecture_par_phrase
        self.nb_mots_par_phrase_prononce = nb_mots_par_phrase_prononce
        self.nb_seconde_entre_pause = nb_seconde_entre_pause

    def sauvegarder(self, nomFichier : str):
        fichier = open(nomFichier, "w+")

        if fichier.mode != "w+":
            print("Échec de lors de l'ouverture de : " + nomFichier + " : en écriture")

        fichier.write(str(self.nb_lecture_par_phrase) + "\n")
        fichier.write(str(self.nb_mots_par_phrase_prononce) + "\n")
        fichier.write(str(self.nb_seconde_entre_pause) + "\n")

        fichier.close()

    def charger(self, nomFichier : str):
        fichier = open(nomFichier, "r")

        if fichier.mode != "r":
            print("Échec de lors de l'ouverture de : " + nomFichier + " : en lecture")

        # lire une fois pour savoir si le fichier est vide
        nb_lecture = fichier.readline()
        if nb_lecture != '':
            self.nb_lecture_par_phrase = int(nb_lecture)
            self.nb_mots_par_phrase_prononce = int(fichier.readline())
            self.nb_seconde_entre_pause = int(fichier.readline())

            fichier.close()
        else:
            print("Le fichier " + str(nomFichier) + " a été trouvé, mais il n'y avait aucun contenu")
        
