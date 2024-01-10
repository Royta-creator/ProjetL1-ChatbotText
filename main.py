from functions import *
directory = "./speeches"
files_names = list_of_files(directory, "txt")
files_names2 = list_of_files2(directory, "txt")
DictName = {
    "Chirac": "Jacques",
    "Giscard D'Estaing": "Valery",
    "Hollande": "François",
    "Macron": "Emmanuel",
    "Mitterrand": "François",
    "Sarkozy": "Nicolas"
}
DictFrequence = FrequenceDansToutText(files_names2)
DictioIDF, Toutmot = DictIDF(files_names2)
TFIDF = DictTFIDF(files_names2, DictFrequence, DictioIDF, Toutmot)    
matrix = [[0 for _ in Toutmot] for _ in files_names2]
lst = [ListeNomsPresident(files_names, DictName), print_zero_tfidf_words(TFIDF), print_highest_tfidf_words(TFIDF)]
if __name__ == '__main__':
    chatbot(lst)
