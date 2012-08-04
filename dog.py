# all the imports
from flask import Flask, request, session, g, redirect, url_for, \
             abort, render_template, flash

DEBUG = True
SECRET_KEY = 'devkey'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/')
def return_main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run()


