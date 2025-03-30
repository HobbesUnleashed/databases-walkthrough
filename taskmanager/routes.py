# Imports the templates and needs to be linked to the 'templates' folder
# Templates folder should be at the same level as this file - the database folder, not the root

# Import the variables from the __init__.py file - app and db
# Because the __init__ file is within the database folder, we can use the name of the database - taskmanager

# Import the request, redirect and url_for to ensure these work in the add_category route
from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")


# New page to be linked to within the website
@app.route("/categories")
def categories():
    # Pulls all data and then orders it
    # Order_by will overwrite the default of using the primary key and allows us to define how it is ordered
    # Define the class and the column in the order_by
    # Convert into a list by wrapping this in a list
    categories = list(Category.query.order_by(Category.category_name).all())
    # categories.html=categories variable in line above
    return render_template("categories.html", categories=categories)


# CREATE INFORMATION

# Render a template used to add a new category
# This will interact with the database so need to include the methods "GET" and "POST"


# GET method will return the template page of 'add_category.html' (final line)
# POST method will add to the DB and must be indented in the function
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        # Variable category calls the Class of Category from the models.py
        # Then declare the column needed in a new variable (use the same name)
        # Attach the request.form.get("Column name") to this new variable
        category = Category(category_name=request.form.get("category_name"))
        # Add the above to the session
        db.session.add(category)
        # Commit it to the DB
        db.session.commit()
        # Redirect the user back to the categories page using the route declared
        return redirect(url_for("categories"))
    return render_template("add_category.html")


# UPDATING INFORMATION
# Must put the argument for the link to this page into the route - /type:new variable name for link (check the categories.html link for "edit")
@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
# Pass the variable directly into the function so that it is available to use within the function
def edit_category(category_id):
    # Variable category = the Category class and look for the _id variable or return a 404 error page
    category = Category.query.get_or_404(category_id)
    # Add the POST method functionality to this route to push the changes from our edit
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)


# DELETE INFORMATION
# REMEMBER to include some validation - possibly through a modal
# Check the categories.html page for an example of how this can be done


# Using the same variable as the update function is ideal for the deletion of the category
@app.route("/delete_category/<int:category_id>")
# Pass the variable into the function
def delete_category(category_id):
    # Create a new variable to call upon the variable passed in and store it
    category = Category.query.get_or_404(category_id)
    # Pass the variable to be deleted
    db.session.delete(category)
    # Commit the delete
    db.session.commit()
    # Return to the categories page
    return redirect(url_for("categories"))


# CREATE INFORMATION

# Render a template used to add a new category
# This will interact with the database so need to include the methods "GET" and "POST"


# GET method will return the template page of 'add_category.html' (final line)
# POST method will add to the DB and must be indented in the function
@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    # Pulls all data and then orders it
    # Order_by will overwrite the default of using the primary key and allows us to define how it is ordered
    # Define the class and the column in the order_by
    # Convert into a list by wrapping this in a list
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        # The variable task will pull all the information from the model Task
        task = Task(
            # Using each field as again - pull the information entered in the inputs
            task_name=request.form.get("task_name"),
            task_description=request.form.get("task_description"),
            # If the check box is marked - it is true, otherwise it is defaulted to false
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("due_date"),
            category_id=request.form.get("category_id"),
        )
        # Add the above to the session
        db.session.add(task)
        # Commit it to the DB
        db.session.commit()
        # Redirect the user back to the Home page using the route declared
        return redirect(url_for("home"))
    # Return the template to add another task, as well as the information from the categories lists
    return render_template("add_task.html", categories=categories)
