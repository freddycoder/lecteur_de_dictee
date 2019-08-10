# Lecteur de dictée

## Description

Ce projet est un lecteur de dictée permettant de s'entrainer à écrire. Le programme est très simple à utiliser. Premièrement, on colle le text de la dictée dans la fenêtre. Il est possible d'ajuster trois paramètres : le nombre de fois que chaque bout de phrase est prononcé, le nombre de mots par bout de phrase prononcé et la durée des pauses entre les phrases prononcées. Ensuite on appuie sur 'Lire' et la dictée est lue selon les paramètres. Il est possible de changer les paramètres pendant la dictée. 

À l'ouverture du programme, l'état où le programme se trouvait à la fermeture est repris. Il est possible d'enregistrer une dictée avec le menu 'Fichier > Enregister'. Il est aussi possible d'en ouvrir avec le menu 'Fichier > Charger'. Pour que le programme enregistre l'état de la fenêtre, il faut utiliser le bouton 'Fermer' en bas de la fenêtre ou le menu 'Fichier > Quitter'. Le 'X' en haut à droite n'enregistre pas les paramètres.

Pour l'instant la personne qui utilise le programme doit se corriger elle-même.

## Image
<p align=center>
   <i>Capture d'écran de la fenêtre principale</i><br/>
   <img src="img/demo_readme.JPG" alt="Apperçu de la fenêtre principale" /><br/>
   <i>Le texte présent dans la fenêtre a été trouvé sur ce site : https://www.ccdmd.qc.ca/fr/exercices_pdf/?id=37#</i>
</p>

## Dépendance

* Python 3.6 <a href="https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe">Télécharger 3.6.8 pour windows</a>
* TKinter 
* Gtts 
* Playsound

## Installation

Windows 
```
pip install Gtts
pip install playsound 
```

Linux 
```
pip3 install Gtts
pip3 install playsound 
```

## Démarer

Sur windows double cliquer sur `start.bat`. Sur linux il faut faire la commande `python3 main.py`

## TODOs

* Utiliser un mécanisme de jeton pour couper le text 
* Faire en sorte que la liste dans 'Fichier > Ouvrir' s'actualise lorsqu'on enregistre un fichier
* Faire prononcer les signes de ponctuation
* Ajouter un signal pour dire que la dictée est finie
* Ajouter un compteur du nombre de mots dans la fenêtre
* Ajouter un mécanisme de correction 
    * Ajouter une fenêtre pour écrire le texte 
    * et/ou 
    * Ajouter la possibilité d'utiliser la caméra pour photographier le texte 
    * Ajouter la reconnaissance de caractère 
