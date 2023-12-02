import os
import re
def list_of_files(directory, extension):
 
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension) and '2' not in filename:
            files_names.append(filename)
    
    return files_names

def list_of_files2(directory, extension):
 
    files_names2 = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names2.append(filename)
    
    return files_names2

directory = "./speeches"
files_names = list_of_files(directory, "txt")
files_names2 = list_of_files2(directory, "txt")

DictName = {
    "Chirac": "Jacque",
    "Giscard": "Valery",
    "Hollande": "François",
    "Macron": "Emmanuel",
    "Mitterrand": "François",
    "Sarkozy": "Nicolas"
}
def findName(name):
    for key, values in DictName.items():
        if key in name:
            return values, key

ListFirstNames = [findName(files_names[i]) for i in range(len(files_names))]

print(ListFirstNames)

def cleaned():
    for i in range(len(files_names2)):
        with open("speeches/{}".format(str(files_names2[i])), "r", encoding='utf-8') as file:
            TextContent = nettoyer_texte((file.read()).lower())
        with open("Cleaned/{}".format(files_names2[i]), "w", encoding='utf-8') as file1:
            file1.write(TextContent)

def nettoyer_texte(text):
    text = re.sub(r'-|,|\'|\"|\.|\!|:|  ', ' ', text)
    return text

if __name__ == '__main__':
    cleaned()



