def shiftChar(character, shift) :
    newAscii = ord(character) + shift
    if newAscii > ord('z') :
        newChar = chr((newAscii-26))
    else:
        newChar = chr(newAscii)
    return newChar

def shiftCipher(phrase, shift):
    newPhrase = ""
    for character in phrase:
        newPhrase = newPhrase + shiftChar(character, shift)
    return newPhrase

def calcFreq(phrase, letters):
    count = 0
    for character in phrase:
        index =ord(character)-97
        letters[index] = letters[index] + 1
    for i in range(0,26):
        letters[i] = letters[i]/len(phrase)

def breakCipher(phrase):
    # taken from https://www3.nd.edu/~busiforc/handouts/cryptography/Letter%20Frequencies.html
    bigrams = ['th', 'he', 'in', 'en', 'nt', 're', 'er', 'an', 'ti', 'es', 'on', 'at', 'se', 'nd', 'or', 'ar', 'al', 'te', 'co', 'de', 'to', 'ra', 'et', 'ed', 'it', 'sa', 'em', 'ro']
    trigrams = ['the', 'and', 'tha', 'ent', 'ing', 'ion', 'tio', 'for', 'nde', 'has', 'nce', 'edt', 'tis', 'oft', 'sth', 'men'] 
    
    counterGrams = [0]*26
    max= 0
    
    for i in range(1,26):
        shifted = shiftCipher(phrase, i)
        for j in range(0,10):
            if shifted.find(trigrams[j]) != -1 :
                counterGrams[i]=counterGrams[i]+1
        for k in range(0,10):
            if shifted.find(bigrams[k]) != -1 :
                counterGrams[i]=counterGrams[i]+1
        if counterGrams[i] > counterGrams[max] :
            max=i
    return shiftCipher(phrase, max)