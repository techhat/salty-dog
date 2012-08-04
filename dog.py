# all the imports
from flask import Flask, request, session, g, redirect, url_for, \
             abort, render_template, flash

DEBUG = True
SECRET_KEY = 'devkey'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# the dataset below is just a representation of what
# some function can do to get the values to pass along

response = {
        'menuitem': 'home',
        'active_nodes':
            [ 'node1', 'node2', 'node3', 'node4' ],
        'inactive_nodes':
            [ 'node5', 'node6', 'node7', 'node8' ],
        }

@app.route('/')
def return_main():
    return render_template('main.html', response=response)

if __name__ == '__main__':
    app.run()


