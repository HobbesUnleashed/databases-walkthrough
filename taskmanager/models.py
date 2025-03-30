# Define the databases, the columns in the databases and the relationships between them

# Will need to import the database for this to work
from taskmanager import db


# db.Model - we have imported db and .Model is the declarative base from SQLAlchemy
class Category(db.Model):
    # schema for the Category model
    # Unique identifier that is a number and increments automatically
    id = db.Column(db.Integer, primary_key=True)
    # A string of max 25 chars, must be unique and cannot be blank
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    # Mark the relationship between the tables, link back to itself, identify all tasks associated and delete, identify any task linked to the category
    tasks = db.relationship(
        "Task", backref="category", cascade="all, delete", lazy=True
    )

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        # Once the columns are created, we can return them using .columnName
        return self.category_name


# db.Model - we have imported db and .Model is the declarative base from SQLAlchemy
class Task(db.Model):
    # schema for the Task model
    # Unique identifier that is a number and increments automatically
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    # db.Text gives a text box, rather than an input field
    task_description = db.Column(db.Text, nullable=False)
    # A True/False option that is defaulted to False
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    # Could also use DateTime or Time depending on needs
    due_date = db.Column(db.Date, nullable=False)
    # timepick = db.Column(db.Time, nullable=False)
    # Link between the tables. Foreign Key names the table (Category) using lowercase only and then .column (ID)
    # CASCADE creates a one-many relationship due to the category id being able to be used for many different tasks
    # CASCADE will not just delete the id column, but the whole task(s) associated with it
    category_id = db.Column(
        db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False
    )

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        # Return what information you require to have displayed - 2 options of how to do this listed below.

        # return "#{0} - Task: {1} | Urgent: {2}".format(self.id, self.task_name, self.is_urgent)
        return f"#{self.id} - Task: {self.task_name} | Urgent: {self.is_urgent}"
