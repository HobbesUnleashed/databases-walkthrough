# Imports the templates and needs to be linked to the 'templates' folder
# Templates folder should be at the same level as this file - the database folder, not the root

# Import the variables from the __init__.py file - app and db
# Because the __init__ file is within the database folder, we can use the name of the database - taskmanager

from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("base.html")
