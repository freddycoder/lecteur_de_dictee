import os
from dictee import Dictee
from parametres_lecture import ParametresLecture
from fenetre_principale import FenetrePrincipale

if __name__ == "__main__" :
    # Création des dossiers 'tmp' et 'utl' s'ils n'existent pas
    os.makedirs("tmp", exist_ok=True)
    os.makedirs("utl", exist_ok=True)
    os.makedirs("utl/dictees", exist_ok=True)

    parametre = ParametresLecture()
    if os.path.exists("utl/parametres_lecture.val"):
        try:
            parametre.charger("utl/parametres_lecture.val")
        except:
            print("Une erreur est survenue lors du chargement des paramètres. Le contenu du fichier n'est pas valide. Les paramètres par défaut vont être chargés.")
            parametre = ParametresLecture()

    # Chager la dernière dictée non enregistrer
    dictee = Dictee()
    if os.path.exists("utl/dictee_non_enregistree.dct"):
        try:
            dictee.charger("utl/dictee_non_enregistrer.dct")
        except:
            print("Erreur lors du chargement de la dernière dictée non enregistrer")

    # Exécution principale
    fen = FenetrePrincipale(parametre, dictee)
    fen.mainloop()

    # Récupérer les options de lectures
    parametre = ParametresLecture()
    parametre.nb_lecture_par_phrase = fen.nb_lecture_par_phrase()
    parametre.nb_mots_par_phrase_prononce = fen.nb_mots_par_phrases()
    parametre.nb_seconde_entre_pause = fen.duree_des_pauses()
    parametre.sauvegarder("utl/parametres_lecture.val")

    # Enregistrer la dictée en cours
    dictee = Dictee()
    dictee.titre = fen.TitreDictee.get("1.0", "end").replace('\n', '')
    dictee.text = fen.TextDictee.get("1.0", "end")
    dictee.sauvegarder("utl/dictee_non_enregistree.dct")
