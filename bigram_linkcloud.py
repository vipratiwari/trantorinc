from flask import Flask, render_template, request
import tagcloud as tc
import urllib


app = Flask(__name__)
filename = 'testfile.txt'

@app.route('/')
def index():
  ''' Function will render word cloud file 
      created by tagcloud.py 
  '''
  return render_template('word_cloud_bigram.html')

@app.route('/wordlink')
def link():
  '''Fuction will get pair or words and find availability of words 
     in text file and display 
  '''
  word = urllib.parse.unquote(request.args['word']).replace("'", "").replace('(', '').replace(')', '').split(',')
  line = ''
  with open(filename, 'r') as f:
    for ln in f:
      if word[0] in ln:
        line +=ln
      if word[1] in ln:
        line +=ln
  line+='<p><a href="/">BACK</a></p>'
  return line

if __name__ == '__main__':
  app.run(debug=True)
