import math

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
def units(word) -> int:
    word = word.lower()
    word = ["V" if c in "aeiouy" else "C" for c in word]
    count = 0

    while word:
        if ''.join(word[:2]) in ('CV', 'VC'):
            word.pop(0)
            
        word.pop(0)
        count += 1
          
    return count

# -- the main calculation loop -- #
def mainLoop(word):
    newWord = digraph(word)
    unitCount = units(newWord)
    return unitCount
    

# ---- vars ---- #
digraphs = ["wh","th","ng","ck","qu","sk"]            

# ---- main program ---- #

while True:
    string1  = str(input("Enter sentence to check (no punctuation): ")).lower()
    wordsList = string1.split(" ") 
    totalUnits = 0
    
    for word in (wordsList):
        currentNum = mainLoop(word)
        totalUnits += currentNum

    discs  = math.ceil(totalUnits / 4)
    blanks = 4 - (totalUnits % 4)
    if blanks == 4:
        blanks = 0  # there are better ways to do this but i cba
    
    print("Discs:", discs)
    print("Blank quarters:", blanks)
    print()

