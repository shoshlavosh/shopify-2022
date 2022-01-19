"""Models for items in inventory"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        """Show info about user"""
        return f'<User user_id={self.user_id} email={self.email}>'


class Item(db.Model):
    """An item in inventory"""

    __tablename__ = 'items'

    item_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'))
    item_name = db.Column(db.String)
    item_description = db.Column(db.String)
    date_added = db.Column(db.DateTime)
    qty_in_lbs = db.Column(db.Integer)

    def __repr__(self):
        """Show info about inventory item"""
        return f'<Item item_id={self.item_id} item_name={self.item_name} item_description={self.item_description} qty_in_lbs={self.qty_in_lbs}>'


def connect_to_db(app, db_uri="postgresql:///inventory", echo=True):
    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_ECHO"] = echo
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)

    print("Connected to the db!")


if __name__ == '__main__':
    connect_to_db(app)