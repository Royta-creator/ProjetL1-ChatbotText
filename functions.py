import os
import re
import pandas as pd
import pyttsx3
from math import log10

engine = pyttsx3.init()
# Fonction avec qui rend UN document par président
def list_of_files(directory, extension):
 
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension) and ('2' not in str(filename)):
            files_names.append(filename)
    
    return files_names
# Fonction qui rend TOUT les documents
def list_of_files2(directory, extension):
 
    ListFichier = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            ListFichier.append(filename)
    
    return ListFichier

# Rend les nom et prénom de chaque président sur les documents
def findName(name, DictName):
    for key, values in DictName.items():
        if key in name:
            return values, key
# Prend les textes de /speeches, les nettoie puis les met dans une variable Text content pour ensuite crée un fichier nettoyer dans un dossier cleaned
def cleaned(ListFichier):
    for i in range(len(ListFichier)):
        with open("speeches/{}".format(str(ListFichier[i])), "r", encoding='utf-8') as file:
            TextContent = nettoyer_texte((file.read()).lower())
        with open("Cleaned/{}".format(ListFichier[i]), "w", encoding='utf-8') as file1:
            file1.write(TextContent)

# Remplace les ponctuations par des espaces
def nettoyer_texte(text):
    text = re.sub(r'-|,|\'|\"|\.|\!|:|  ', ' ', text)
    return text

#donne les noms issue dans une liste en se basant sur les clée et valeur d'un dictionnaire
def ListeNomsPresident(namelist, dictname):
    return [findName(namelist[i], dictname) for i in range(len(namelist))]

# donne la frequence des mots dans un seul texte et stock les valeurs dans un dictionnaire
def FrequenceDans1Text(text, Dict):
    text = text.split()
    for i in range(len(text)):
        if text[i] in Dict:
            Dict[text[i]] += 1
        else:
            Dict[text[i]] = 1
        Dict[text[i]] = Dict[text[i]]/len(text)
    return Dict
# frequence de tout les mots de tout les textes d'une liste de fichier
def FrequenceDansToutText(ListFichier):
    DictTotal = {}
    for i in range(len(ListFichier)):
        Dict = {}
        with open("Cleaned/{}".format(str(ListFichier[i])), "r", encoding='utf-8') as file:
            Dict = FrequenceDans1Text(file.read(), Dict)
        DictTotal[ListFichier[i]] = Dict
    return DictTotal
# donne l'indice idf d'un mot precis
def IDF(mot, ListFichier, nbrDocuments = 8):
        Occurence = 0
        for i in range(len(ListFichier)):
            with open("Cleaned/{}".format(ListFichier[i]), "r", encoding='utf-8') as file1:
                text = file1.read()
                if mot in text:
                     Occurence += 1
        return log10(nbrDocuments/(Occurence))
# donne l'indice idf de tout les mots et rend une dictionnaire et la litte de tout les mot d'une lsite de fichier
def DictIDF(ListFichier):
    Toutmot = ''
    for i in range(len(ListFichier)):
        with open(f'Cleaned/{ListFichier[i]}', 'r', encoding='utf-8') as file:
            Toutmot += (file.read())
    Toutmot = list(set(Toutmot.split()))
    Dict = {}
    for i in range(len(Toutmot)):
        Dict[Toutmot[i]] = IDF(Toutmot[i], ListFichier)
    return Dict, Toutmot
# affiche les mots avec un score de 0 dans un dataframe
def print_zero_tfidf_words(TFIDF):
    Zeros = {"Mots": {}}
    for document, word_scores in TFIDF.items():
        for word, score in word_scores.items():
            if score == 0:
                Zeros["Mots"][word] = f"0, {document}" 
    return pd.DataFrame(Zeros)

# affiche les mots avec un score de 0.002 ou plus dans un dataframe         
def print_highest_tfidf_words(TFIDF):
    Highest = {"Mots":{}}
    for document, word_scores in TFIDF.items():
        for word, score in word_scores.items():
            if 0.002 < score:
                Highest["Mots"][word] = f"{score}, {document}" 
    return pd.DataFrame(Highest)

# dictionaire TFIDF de tout les mots
def DictTFIDF(ListeDeFichier, DictFrequence, DictioIDF, Toutmot):
    TFIDF = {}
    for filename in ListeDeFichier:
        TFIDF[filename] = {} 
        for word in Toutmot:   
            TFIDF[filename][word] = DictFrequence[filename].get(word, 0) * DictioIDF.get(word, 0)
    return TFIDF


def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

#chatbot qui prend en parametre une liste de fonction
def chatbot(listFonction):
    text_to_speech("Bonjour je suis un chatbot de texte crée par Roy Et Michael")
    print("1 - Afficher la liste des noms des présidents étudiés\n"
                "2 - Afficher la liste des mots les moins importants dans le corpus de documents \n"
                "3 - Afficher le mot ayant le score TD-IDF le plus élevé \n"
                "4 - Afficher le mot le plus répété par le président Chirac\n"
                "5 - Afficher les noms des présidents qui ont mentionné 'Nation' et celui qui l'a répété le plus de fois\n"
                "6 - Afficher le premier présidant ayant parlé de climat et d'écologie\n"
                "7 - Afficher les noms du des présidents qui a ont parlé du climat et/ou de l'écologie \n"
                "8 - Mode ChatBot\n"
                "9 - Quitter le programme\n")
    ListeChoix = {"1": "Voici les noms des présidents étudiés:", "2": "Bien sur! Voici la liste des mots les moins importants dans le corpus de documents:", "3":"Voici la liste des mots les plus importants dans le corpus de documents:","4":"Voici le mot le plus répété par le président Chirac","5":"Voici les noms des présidents qui ont mentionné 'Nation'","6":"Et celui qui l'a répété le plus de fois","7":"Voici les noms des présidents qui ont parlé du climat et/ou de l'écologie:","8":"Mode ChatBot","9":"Merci et à bientôt !"}
    Choix = input("Choisissez: ")
    while int(Choix) != 9:
        if int(Choix) not in range(0, len(listFonction)):
            print("Désoler nous n'avons pas pu faire cette partie")
            text_to_speech("Désoler nous n'avons pas pu faire cette partie")
            Choix = input("Choisissez: ")
        else:
            text_to_speech(ListeChoix[Choix])
            print(ListeChoix[Choix], listFonction[int(Choix) - 1])
            Choix = input("Choisissez: ")
    print("Au revoir!")
    text_to_speech("Au revoir")
