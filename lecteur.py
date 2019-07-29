from gtts import gTTS
from time import sleep
import os
import uuid
from playsound import playsound
from parametres_lecture import IParametresLecture

def tableau_de_phrases(text : str):
    return text.split('.')

def tableau_phrases_dictée(phrase : str, nombreMotsParPhrase : int):
    mots = phrase.split(' ')
    for i in range(int(1 + len(mots) / nombreMotsParPhrase)):
        p = mots[i*nombreMotsParPhrase:min((i*nombreMotsParPhrase)+nombreMotsParPhrase, len(phrase))]
        text = ""
        for m in p:
            text += m + ' '
        yield text

def lire_dictee(fenetre : IParametresLecture):
    # Le count est utiliser pour incrémenter le nom du fichier mp3
    fichiers = []
    for phrase in tableau_de_phrases(fenetre.TextDictee.get('1.0', 'end')):
        for phraseDictee in tableau_phrases_dictée(phrase, fenetre.nb_mots_par_phrases()):
            fichiers.append('tmp/' + uuid.uuid1().__str__() + '.mp3')
            try:
                tts = gTTS(text=phraseDictee, lang='fr')

                lire_phrase(tts, fichiers[len(fichiers) - 1], fenetre)

                if len(fichiers) > 1:
                    os.remove(fichiers.pop(0))

            except PermissionError as e: # Quand le nom de fichier existe déjà dans le dossier temp
                print("Erreur de permission sur le fichier " + fichiers[len(fichiers) - 1] + ". Tentative avec un autre uuid")

                fichiers.append('tmp/' + uuid.uuid1().__str__() + '.mp3')

                lire_phrase(tts, fichiers[len(fichiers) - 1], fenetre)

                if len(fichiers) > 1:
                    os.remove(fichiers.pop(0))

            except AssertionError as e: # Quand une chaine vide est envoyée à gTTS(text=" ", ...) on attrape l'exception
                print(e)

            except FileNotFoundError as e: # Quand une tentative de suppression tombe sur un fichier inexistant
                print(str(e))
                
    while len(fichiers) != 0:
        os.remove(fichiers.pop(0))

def lire_phrase(tts : gTTS, nom_fichier : str, fenetre : IParametresLecture):
    tts.save(nom_fichier)
    for _ in range(fenetre.nb_lecture_par_phrase()):
        playsound(nom_fichier)
        sleep(fenetre.duree_des_pauses())
