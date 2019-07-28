from tkinter import Label, Text, Menu, Button, Tk
from functools import partial
from threading import Thread
from datetime import datetime
import os
from lecteur import lire_dictee
from dictee import Dictee
from parametres_lecture import ParametresLecture, IParametresLecture

class FenetrePrincipale(Tk, IParametresLecture):
    def __init__(self, options_lecture=ParametresLecture(), dictee=Dictee()):
        Tk.__init__(self)
        self.title("Lecteur de dictée")
        self.thread_lecture = None # quand l'utilisateur appuie sur Lire, la référence est initialisé

        # Titre de la dictée
        self.TitreDicteeLabel = Label(self, text="Titre : ")
        self.TitreDicteeLabel.pack()

        self.TitreDictee = Text(self, height=1, width=25)
        self.TitreDictee.insert("1.0", dictee.titre)
        self.TitreDictee.pack()

        # Texte de la dictée
        self.TextDicteeLabel = Label(self, text="Coller le texte de la dictée ici!")
        self.TextDicteeLabel.pack()

        self.TextDictee = Text(self, height=25, width=75)
        self.TextDictee.insert("1.0", dictee.text)
        self.TextDictee.pack()

        # Menu
        self.ConfigurerMenu()

        # Nombre de lecture par phrase
        self.NombreLectureParPhraseLabel = Label(self, text="Nombre de lecture par phrase : ")
        self.NombreLectureParPhraseLabel.pack()

        self.NombreLectureParPhrase = Text(self, height=1, width=4)
        self.NombreLectureParPhrase.insert('1.0', str(options_lecture.nb_lecture_par_phrase))
        self.NombreLectureParPhrase.pack()

        # Nombre de mots avant une pause
        self.NombreMotsAvantPauseLable = Label(self, text="Nombre de mots avant une pause : ")
        self.NombreMotsAvantPauseLable.pack()

        self.NombreMotsAvantPause = Text(self, height=1, width=4)
        self.NombreMotsAvantPause.insert('1.0', str(options_lecture.nb_mots_par_phrase_prononce))
        self.NombreMotsAvantPause.pack()

        # Durée des pauses (en seconde)
        self.DureePauseLabel = Label(self, text="Durée des pause entre les phrases : ")
        self.DureePauseLabel.pack()

        self.DureePause = Text(self, height=1, width=4)
        self.DureePause.insert('1.0', str(options_lecture.nb_seconde_entre_pause))
        self.DureePause.pack()

        # Boutton lecture
        self.greet_button = Button(self, text="Lire", command=self.lire_dictee_commande)
        self.greet_button.pack()

        # Bouton fermer
        self.close_button = Button(self, text="Fermer", command=self.quit)
        self.close_button.pack()

    def ConfigurerMenu(self):
        self.BarreMenu = Menu(self)
        self.MenuFichier = Menu(self.BarreMenu, tearoff=0)
        self.MenuOuvrir = Menu(self)
        for nomFichier in os.listdir('utl/dictees'):
            self.MenuOuvrir.add_command(label=nomFichier, command=partial(self.ouvrir_dictee, nomFichier))
        self.MenuFichier.add_command(label="Enregistrer", command=self.enregistrer_dictee)
        self.MenuFichier.add_cascade(label="Ouvrir", menu=self.MenuOuvrir)
        self.MenuFichier.add_command(label="Quitter", command=self.quit)
        self.BarreMenu.add_cascade(label="Fichier", menu=self.MenuFichier)
        self.config(menu=self.BarreMenu)

    def lire_dictee_commande(self):
        if self.thread_lecture == None or self.thread_lecture.is_alive() == False:
            self.thread_lecture = Thread(target=lire_dictee, args=(self,))
            self.thread_lecture.start()
        else:
            print("La lecture est déjà en cours. Veuiller attendre la fin la lecture pour recommencer")

    def enregistrer_dictee(self):
        titre = self.TitreDictee.get("1.0", "end").replace('\n', '')

        dictee = Dictee(titre=titre, text=self.TextDictee.get("1.0", "end"))
        dictee.sauvegarder("utl/dictees/" + titre + ".dct")

    def ouvrir_dictee(self, nom_fichier):
        dictee = Dictee()
        dictee.charger('utl/dictees/' + nom_fichier)

        self.TitreDictee.delete("1.0", "end")
        self.TitreDictee.insert("1.0", dictee.titre)
        self.TextDictee.delete("1.0", "end")
        self.TextDictee.insert("1.0", dictee.text)

    def nb_lecture_par_phrase(self):
        return int(self.NombreLectureParPhrase.get('1.0', 'end'))

    def duree_des_pauses(self):
        return int(self.DureePause.get('1.0', 'end'))

    def nb_mots_par_phrases(self):
        return int(self.NombreMotsAvantPause.get('1.0', 'end'))