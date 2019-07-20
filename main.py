from tkinter import Tk, Label, Button, Text
from gtts import gTTS
from time import sleep
import os
from playsound import playsound
import threading

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
            filename = 'phrase_courrante' + str(count) +'.mp3'
            count += 1
            tts = gTTS(text=phraseDictee, lang='fr')
            tts.save(filename)
            for _ in range(int(fenetre.NombreLectureParPhrase.get('1.0', 'end'))):
                playsound(filename)
                sleep(int(fenetre.DureePause.get('1.0', 'end')))

            if (count != 1):
                os.remove('phrase_courrante' + str(count - 1) + '.mp3')

    os.remove('phrase_courrante0.mp3')
    os.remove('phrase_courrante' + str(count) + '.mp3')

class Main:
    def __init__(self, master):
        self.master = master
        master.title("Lecteur de dictée")

        # Texte de la dictée
        self.IndicationColler = Label(master, text="Coller le texte de la dictée ici!")
        self.IndicationColler.pack()

        self.TextDictee = Text(root, height=25, width=75)
        self.TextDictee.pack()

        # Nombre de lecture par phrase
        self.NombreLectureParPhraseLabel = Label(master, text="Nombre de lecture par phrase : ")
        self.NombreLectureParPhraseLabel.pack()

        self.NombreLectureParPhrase = Text(root, height=1, width=4)
        self.NombreLectureParPhrase.insert('1.0', "2")
        self.NombreLectureParPhrase.pack()

        # Nombre de mots avant une pause
        self.NombreMotsAvantPauseLbl = Label(master, text="Nombre de mots avant une pause : ")
        self.NombreMotsAvantPauseLbl.pack()

        self.NbMotAvantPause = Text(root, height=1, width=4)
        self.NbMotAvantPause.insert('1.0', "7")
        self.NbMotAvantPause.pack()

        # Durée des pauses 
        self.DureePauseLabel = Label(master, text="Durée des pause entre les phrases : ")
        self.DureePauseLabel.pack()

        self.DureePause = Text(root, height=1, width=4)
        self.DureePause.insert('1.0', "7")
        self.DureePause.pack()

        # Boutton lecture
        self.greet_button = Button(master, text="Lire", command=self.read)
        self.greet_button.pack()

        # Bouton fermer
        self.close_button = Button(master, text="Fermer", command=master.quit)
        self.close_button.pack()

    def read(self):
        x = threading.Thread(target=lire_dictee, args=(self,))
        x.start()

        
root = Tk()
my_gui = Main(root)
root.mainloop()