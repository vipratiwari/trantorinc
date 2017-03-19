import re
from nltk.tokenize import RegexpTokenizer

def getwords(text):
    ''' Function will return words(tokens) in string '''
    tokens = maketokens(text)
    return tokens

def clearwords(text, cloud = False, noisewords = None):
    '''Funtion will remove punctuation,
       remove numaric words and 
       connvert string to lower case '''
    textinlower = text.lower()
    # punctuation and numbers to be removed
    clearstring = re.sub("[-.?!,\"\':;()@#$%^&*|\d+]", "", textinlower)
    if noisewords:
        # remove noise words from string
        remove = '|'.join(noisewords)
        clearstring = re.sub(r'\b'+remove+r'\b', "", clearstring)
    if cloud:
        return clearstring
    tokens = maketokens(clearstring)
    return tokens 

def maketokens(string):
    ''' Function will split string and return list of words '''
    #tokens = string.split()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(string)
    return tokens

if __name__ == "__main__":
    text = input("Please insert a string : ")
    getwords(text)
    clearwords(text)
