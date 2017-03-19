import wordfrequency as wf
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


def wordcloud(string):
    '''Convert all the required text into a single string here 
       and store them in word_string '''

    #you can specify fonts, stopwords, background color and other options
    wordcloud = WordCloud(font_path='/home/vipra/Vipra/openx/lib/pear/Image/Canvas/Fonts/arial.ttf',
                          stopwords=STOPWORDS,
                          background_color='white',
                          width=1200,
                          height=1000
                         ).generate(string)

    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    filename = input("Please enter filename with path : ")
    string = wf.processfile('testfile.txt', cloud = True)
    wordcloud(string)

