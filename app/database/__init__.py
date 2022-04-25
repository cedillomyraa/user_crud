from flask import g 

import sqlite3

DATABASE="user.db"

def get_db(): #helper function to an open conecction to our browser 
    db = getattr(g, "_database", None)
    if not db:
        db = g._database = sqlite3.connect(DATABASE)
    return db    