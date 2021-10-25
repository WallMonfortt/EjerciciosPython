# Contador de palabras: actualizar el script anterior que lea un archivo de texto y 
# retorne las 10 palabras más repetidas. 
# Usando clases, métodos, instancias y lo previamente visto en clase.

import re, string
from collections import Counter

file = input('Ingrese el nombre del archivo que desea abrir: ')
numWords = input('Ingrese el número de palabras comunes que desea obtener: ')
words = list()

try:
  file = open(file)
  numWords = int(numWords)
except (ValueError, FileNotFoundError) as error:
  print(error)
  exit()


class File:
  @staticmethod
  def clean(text):
    return re.sub('[%s]' % re.escape(string.punctuation), '', text)

  @staticmethod
  def word(words,numWords):
    mCommons = Counter(words).most_common(numWords)
    i = 0
    for c_word in mCommons:
      i+=1
      print((i),'.-palabra: "',c_word[0],'"\n Veces en el texto: ', c_word[1])

for line in file:
  line = line.strip()
  newText = File.clean(line)
  newText = newText.split(" ")
  for word in newText:
    if word != '' and word.isnumeric() == False:
      words.append(word)


File.word(words,numWords)





