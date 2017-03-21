from flask import Flask, render_template, request
import tagcloud as tc


app = Flask(__name__)
filename = 'testfile.txt'

@app.route('/')
def index():
  ''' Function will render word cloud file 
      created by tagcloud.py 
  '''
  return render_template('word_cloud.html')

@app.route('/wordlink')
def link():
  '''Fuction will find availability of words 
     in text file and display 
  '''
  word = request.args['word']
  line = ''
  with open(filename, 'r') as f:
    for ln in f:
      if word in ln:
        line +=ln
  line+='<p><a href="/">BACK</a></p>'
  return line

if __name__ == '__main__':
  app.run(debug=True)
