"""CRUD operations"""

from model import db, User, Item, app, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    #check to see if email and password are the correct data types 
    #before adding & committing user to the database
    assert type(email) == str
    assert type(password) == str

    db.session.add(user)
    db.session.commit()

    return user


def get_users():
    """Return all users."""

    return User.query.all()


def print_users():
    """Print all users in the database"""

    users = get_users()

    for user in users:
        print(user)


def get_user_by_id(user_id):
    """Return a user by their user id"""

    return User.query.get(user_id)


def create_item(item_name, item_description,
            date_added, qty_in_lbs):

    item = Item(item_name=item_name, item_description=item_description,
            date_added=date_added, qty_in_lbs=qty_in_lbs)

    #check to see if item name, description, date, and quantity are the 
    #correct data types before adding & committing inventory item to the 
    #database
    assert type(item_name) == str
    assert type(item_description) == str
    assert type(date_added) == str
    assert type(qty_in_lbs) == int

    db.session.add(item)
    db.session.commit()

    return item


def get_item():
    """Return all inventory items"""

    return Item.query.all()


def item_search(keyword):
    """Return an item by keyword"""

    items = get_items()

    #this seems to only return one inventory item - in the future, I'd 
    #like to rewrite it so that it returns all items that match the keyword
    for item in items:
        if keyword in item.item_description or keyword in item.item_name:
            return item


def print_all_items():
    """Print all items in inventory database"""

    items = get_items()

    for item in items:
        print(item)


if __name__ == '__main__':
    connect_to_db(app)