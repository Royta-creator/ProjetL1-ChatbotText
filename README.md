# ProjetL1-ChatbotText

Projet d'Analyse de Texte et de Synthèse Vocale
Vue d'ensemble
Ce projet consiste en l'analyse d'une collection de documents textuels, notamment des discours de divers présidents, et inclut une fonctionnalité de conversion de texte en parole. Les principales fonctionnalités comprennent le traitement et le nettoyage des données textuelles, le calcul des fréquences de mots et des valeurs TF-IDF, ainsi qu'une interface interactive semblable à un chatbot fournissant des informations sur le contenu.

Fonctionnalités
Nettoyage et Traitement de Texte : Nettoie et traite les documents textuels, en supprimant la ponctuation et en les préparant pour l'analyse.
Analyse de la Fréquence des Mots : Calcule la fréquence des mots dans l'ensemble du corpus de documents.
Calcul de TF-IDF : Calcule les valeurs de Fréquence de Terme-Inverse de la Fréquence Documentaire (TF-IDF) pour identifier l'importance des mots dans les documents.
Synthèse Vocale : Convertit les réponses textuelles en paroles à l'aide de la bibliothèque pyttsx3.
Chatbot Interactif : Une interface interactive semblable à un chatbot qui fournit des informations basées sur l'analyse des discours.
Installation
Pour exécuter ce projet, vous aurez besoin de Python installé sur votre système ainsi que des bibliothèques suivantes :

pandas
pyttsx3
regex

Vous pouvez installer ces dépendances en utilisant pip

Utilisation
Exécutez main.py pour démarrer le programme. Le programme vous invitera de manière interactive à choisir différentes options pour analyser les discours et fournira des réponses parlées.

Description des Fichiers
functions.py : Contient toutes les fonctions de traitement de texte, d'analyse et de synthèse vocale.
main.py : Le script principal qui utilise les fonctions de functions.py pour interagir avec l'utilisateur et fournir des informations basées sur l'analyse du texte.
Contributions
