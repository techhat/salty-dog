# all the imports
from flask import Flask, request, session, g, redirect, url_for, \
             abort, render_template, flash

from salt.cli import key
from salt import client
from salt import config

DEBUG = True
SECRET_KEY = 'devkey'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# the dataset below is just a representation of what
# some function can do to get the values to pass along

response = {
        'menuitem': 'status',
        'active_nodes':
            [ 'node1', 'node2', 'node3', 'node4' ],
        }

def _populate_nodes():
    active_nodes = []
    inactive_nodes = []

    '''
    Print a list of up and down minions
    '''

    __opts__ = config.master_config('/etc/salt/master')

    c = client.LocalClient(__opts__['conf_file'])
    k = key.Key(__opts__)
    minions = c.cmd('*', 'test.ping', timeout=__opts__['timeout'])
    keys = k._keys('acc')

    response['inactive_nodes'] = sorted(keys - set(minions))

    active_nodes = c.cmd('*', 'test.ping', timeout=__opts__['timeout'])
    response['active_nodes'] = sorted(active_nodes)

@app.route('/')
def return_main():

    _populate_nodes()

    return render_template('main.html', response=response)

if __name__ == '__main__':
    app.run()


