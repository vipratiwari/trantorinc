import clearwords
from nltk import bigrams, FreqDist
from operator import itemgetter

def processfile(filename, noise = False, cloud = False):
    ''' Function will split the file and
        remove punctuation and numbers and
        will return the frequncy of words'''
    noiselist = ["a", "and", "is", "the", "at"]
    with open(filename) as f:
        if cloud:
            return clearwords.clearwords(f.read(),cloud = True, noisewords = noiselist)
        filetokens = clearwords.clearwords(f.read(), cloud = False, noisewords = noiselist) if noise  else clearwords.clearwords(f.read())
    frequency = findfrequency(filetokens)
    print("Frequncy of words in file : ", frequency)
    return frequency


def findfrequency(words):
    ''' Function will return tuple of words with 
        number of occurence in file '''
    frequency = FreqDist(bigrams(words))
    freq = sorted(frequency.items(), key=itemgetter(1), reverse=True)
    return freq

if __name__ == "__main__":
    filename = input("Please enter a text file name with path : ")
    processfile(filename)
    filename = input("Please enter a text file name contain noise words with path : ")
    processfile(filename, True)
