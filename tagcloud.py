import string
import datetime
import wordfrequency as wf 
import webbrowser

HTML_BIG    = 96      # the largest font size produced
HTML_LITTLE = 14      # the smallest font size produced
filename = "word_cloud"
high_count = 20
low_count  =  1


def make_html_word(word, count, high, low):
    '''Make an HTML tag containing the word with a font size determined
       by the word count.  The font size is scaled between HTML_BIG and
       HTML_LITTLE.  high and low represent the highest and lowest
       word counts in the document.
    '''
    
    ratio    = (count-low) / float(high-low)
    fontsize = (ratio * HTML_BIG) + ((1-ratio) * HTML_LITTLE)
    fontsize = int(fontsize)
    word_str = '<span style=\"font-size:%spx;\">%s</span> '
    return word_str % (str(fontsize), word)

def make_html_box(body):
    '''Make an HTML tag containing a string in a box.
    '''
    
    box_str = '''<div style=\"
    width: 800px;
    background-color: rgb(250,250,250);
    border: 1px grey solid;
    text-align: center\">%s</div>
    '''
    
    return box_str % (body)

def print_html_file(body, title):
    '''Create a standard HTML page with titles, header, and metadata.
       The page is written to a file named is [filename.html]
    '''

    template = '''
    <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML//EN">
    <html> <head>
    <title>Tag Cloud </title>
    </head>

    <body>
    <h1>TAG CLOUD </h1>
    %s
    <hr>
    <address></address>
    <!-- html start -->
      Last modified: %s
    <!-- html end -->
    </body> </html>
    '''

    filename = title+'.html'
    time_now = datetime.datetime.now().ctime()
    the_str  = template % (body, time_now)
    
    output = open(filename, 'w')
    output.write(the_str)
    output.close()

if __name__ == "__main__":
    getfile = input("Please enter filename with path : ")
    pairs = wf.processfile(getfile)
    body  = ''

    for word, count in pairs:
        body = body + make_html_word(word, count, high_count, low_count)

    html = make_html_box(body)
    print_html_file(html, filename)
    filename = filename+".html"
    webbrowser.open_new_tab(filename)
