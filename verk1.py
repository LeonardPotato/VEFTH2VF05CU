import os
from bottle import run, route

@route('/')
def index():
    return '<a href="/about">About</a> <br>'\
           '<a href="/biography">Biography</a> <br>'\
           '<a href="/pictures">Pictures</a>'

@route('/about')
def about():
    return 'About'


@route('/biography')
def biography():
    return 'Biography'


@route('/pictures')
def pictures():
    return 'Pictures'


run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
