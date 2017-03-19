import wordfrequency as wf
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

#Convert all the required text into a single string here 
#and store them in word_string

#with open('testfile.txt','r') as f:
#    word_string = f.read()

word_string = wf.processfile('testfile.txt', cloud = True)

#you can specify fonts, stopwords, background color and other options

wordcloud = WordCloud(font_path='/home/vipra/Vipra/openx/lib/pear/Image/Canvas/Fonts/arial.ttf',
                          stopwords=STOPWORDS,
                          background_color='white',
                          width=1200,
                          height=1000
                         ).generate(word_string)


plt.imshow(wordcloud)
plt.axis('off')
plt.show()

