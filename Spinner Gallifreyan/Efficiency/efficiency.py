import csv
from nltk.corpus import words

# ---- functions ---- #
# -- converts digraphs into one letter -- #
def digraph(word):
    wordList = list(word)
    newWord = ""
    for i in range(len(digraphs)):
        for j in range(len(wordList)):
            if wordList[j-1:j+1] == list(digraphs[i]):
                wordList[j-1] = ""
                wordList[j] = "x"
                
    for i in range(len(wordList)):
        newWord += wordList[i]
        
    return newWord

# -- counts how many rings -- #
def units(y,word) -> int:
    word = word.lower()

    if y:
        word = ["V" if c in "aeiouy" else "C" for c in word]
    else:
        word = ["V" if c in "aeiou" else "C" for c in word]
        
    count = 0

    while word:
        if ''.join(word[:2]) in ('CV', 'VC'):
            word.pop(0)
            
        word.pop(0)
        count += 1
          
    return count

# -- the main calculation loop -- #
def mainLoop(inNum,inWord,di,y):
    newWord = digraph(word)
    length = len(word)
    unitCount = units(y, newWord if di else word) #puts the digraph-converted word in if digraphs are enabled
    efficiency = round((1 - (unitCount / length)),2)
    writer.writerow([inNum,inWord,length,unitCount,efficiency])
    


# ---- vars ---- #
digraphs = ["th","gh","nd","ng","ch","ck","qu","wh","sh","st"]
wordList = words.words()


# ---- main program ---- #
# -- digraphs, y vowel -- #
with open("digraphs, Y vowel.csv", mode= "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(["Number","Word","Length","Units","Efficiency"])

    num = 1
    for word in (wordList):
        mainLoop(num,word,True,True) #number of the loop, input word, digraphs enabled, y vowel enabled
        num += 1

# -- digraphs, no y vowel -- #
with open("digraphs, no Y vowel.csv", mode= "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(["Number","Word","Length","Units","Efficiency"])

    num = 1
    for word in (wordList):
        mainLoop(num,word,True,False)
        num += 1

# -- no digraphs, y vowel -- #
with open("no digraphs, Y vowel.csv", mode= "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(["Number","Word","Length","Units","Efficiency"])

    num = 1
    for word in (wordList):
        mainLoop(num,word,False,True)
        num += 1

# -- no digraphs, no y vowel -- #
with open("no digraphs, no Y vowel.csv", mode= "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(["Number","Word","Length","Units","Efficiency"])

    num = 1
    for word in (wordList):
        mainLoop(num,word,False,False)
        num += 1
