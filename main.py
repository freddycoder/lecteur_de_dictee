from tkinter import Tk, Label, Button, Text
from gtts import gTTS
from time import sleep
import os
from playsound import playsound
import threading
import uuid
from parametres_lecture import ParametresLecture

def couperEnPhrase(text : str):
    return text.split('.')

def couperEnPhraseDeDictee(phrase : str, nombreMotsParPhrase : int):
    mots = phrase.split(' ')
    for i in range(int(1 + len(mots) / nombreMotsParPhrase)):
        p = mots[i*nombreMotsParPhrase:min((i*nombreMotsParPhrase)+nombreMotsParPhrase, len(phrase))]
        text = ""
        for m in p:
            text += m + ' '
        yield text

def lire_dictee(fenetre):
    count = 0
    for phrase in couperEnPhrase(fenetre.TextDictee.get('1.0', 'end')):
        for phraseDictee in couperEnPhraseDeDictee(phrase, int(fenetre.NbMotAvantPause.get('1.0', 'end'))):
            filename = 'tmp/phrase_courrante' + str(count) +'.mp3'
            count += 1
            try:
                tts = gTTS(text=phraseDictee, lang='fr')
                tts.save(filename)
                for _ in range(int(fenetre.NombreLectureParPhrase.get('1.0', 'end'))):
                    playsound(filename)
                    sleep(int(fenetre.DureePause.get('1.0', 'end')))

                if (count != 1):
                    os.remove('tmp/phrase_courrante' + str(count - 1) + '.mp3')
            except AssertionError as e: # Quand une chaine vide est envoyer à gTTS(text=" ", ...) on attrape l'exception
                print(e)
                

    os.remove('tmp/phrase_courrante0.mp3')
    os.remove('tmp/phrase_courrante' + str(count - 1) + '.mp3')

class FenetrePrincipale(Tk):
    def __init__(self, options_lecture=ParametresLecture()):
        Tk.__init__(self)
        self.title("Lecteur de dictée")
        self.thread_lecture = None # quand l'utilisateur appuie sur Lire, la référence est initialisé

        # Texte de la dictée
        self.IndicationColler = Label(self, text="Coller le texte de la dictée ici!")
        self.IndicationColler.pack()

        self.TextDictee = Text(self, height=25, width=75)
        self.TextDictee.pack()

        # Nombre de lecture par phrase
        self.NombreLectureParPhraseLabel = Label(self, text="Nombre de lecture par phrase : ")
        self.NombreLectureParPhraseLabel.pack()

        self.NombreLectureParPhrase = Text(self, height=1, width=4)
        self.NombreLectureParPhrase.insert('1.0', str(options_lecture.nb_lecture_par_phrase))
        self.NombreLectureParPhrase.pack()

        # Nombre de mots avant une pause
        self.NombreMotsAvantPauseLbl = Label(self, text="Nombre de mots avant une pause : ")
        self.NombreMotsAvantPauseLbl.pack()

        self.NbMotAvantPause = Text(self, height=1, width=4)
        self.NbMotAvantPause.insert('1.0', str(options_lecture.nb_mots_par_phrase_prononce))
        self.NbMotAvantPause.pack()

        # Durée des pauses 
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

    def lire_dictee_commande(self):
        if self.thread_lecture == None or self.thread_lecture.is_alive() == False:
            self.thread_lecture = threading.Thread(target=lire_dictee, args=(self,))
            self.thread_lecture.start()


if __name__ == "__main__" :
    # Création des dossiers tmp et utl s'ils n'existent pas
    os.makedirs("tmp", exist_ok=True)
    os.makedirs("utl", exist_ok=True)

    # TODO : Charger les options enregistrer dans 'utl/options_lecture.json'

    # Exécution principale
    fen = FenetrePrincipale()
    fen.mainloop()

    # Réccupérer les options de lectures
    options = ParametresLecture()
    options.nb_lecture_par_phrase = int(fen.NombreLectureParPhrase.get("1.0", "end"))
    options.nb_mots_par_phrase_prononce = int(fen.NbMotAvantPause.get("1.0", "end"))
    options.nb_seconde_entre_pause = int(fen.DureePause.get("1.0", "end"))

    # TODO : Enregistrer les options dans 'utl/options_lecture.json'