import sqlite3

import click
from flask import current_app, g

def get_db():
    if 'db' not in g:
        #connect to file defined in DATABASE config key.
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        #return rows as dictionaries.
        g.db.row_factory = sqlite3.Row

        return g.db
    
def close_db(e=None):
    #pop the database off the stack and if it exists, stop.
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    #open database relative to /flaskr
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

#command line command for initialization.
@click.command('init-db')
def init_db_command():
    """clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

