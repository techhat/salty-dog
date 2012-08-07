# hack to run the server with an __init__.py
# makes the app more portable later on

import sys, os
sys.path.append(os.path.expanduser('.'))


from dog import app
app.run(debug=True)
