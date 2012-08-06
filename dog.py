# all the imports
from flask import Flask, request, session, g, redirect, url_for, \
             abort, render_template, flash


import sys
sys.path.append('/home/clints/Projects')

from salty_dog.plugins import nodes

DEBUG = True
SECRET_KEY = 'devkey'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# the dataset below is just a representation of what
# some function can do to get the values to pass along

resp = {
        'menuitem': 'status',
}

@app.route('/')
def return_main():

    r = nodes._populate()
    response = dict(resp, **r)

    return render_template('main.html', response=response)

if __name__ == '__main__':
    app.run()


