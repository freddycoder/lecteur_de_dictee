# Lecteur de dictée

## Description

Ce projet est un lecteur de dictée permettant de s'entrainer à écrire. Le programme est très simple à utiliser. Premièrement, on colle le code de la dictée dans la fenêtre. Il est possible d'ajuster trois paramètres : le nombre de fois que chaque bout de phrase est prononcé, le nombre de mots par bout de phrase prononcé et la durée des pauses entre les phrases prononcées. Ensuite on appuie sur 'Lire' et la dictée est lue selon les paramètres. Il est possible de changer les paramètres pendant la dictée. 

Pour l'instant la personne qui utilise le programme doit se corriger elle-même.

## Dépendance

* python 3.6 
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

## TODOs

* Utiliser un mécanisme de jeton pour couper le text 
* Améliorer la gestion des pause en fonction de la longueur des phrases 
* Ajouter un mecanisme de correction 
    * Ajouter une fenêtre pour écrire le text 
    * et/ou 
    * Ajouter la possiblité d'utiliser la camera pour photographier le text 
    * Ajouter la reconnaissance de caractère 
* Ajouter la possibilité de charger des dictée 
* Ajouter la possibilité de sauvegarder des dictée 
* Améliorer la gestion des fichiers audio
