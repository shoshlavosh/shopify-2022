"""CRUD operations"""

from model import db, User, Item, app, connect_to_db


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


def edit_item(item_id, attribute, new_value):
    """Edit an item in inventory using its item_id"""

    db.session.query(Item).filter(Item.item_id == item_id).update({attribute:new_value})
    db.session.commit()


def delete_item(item_id):
    """Delete an item from inventory using item_id"""

    del_item = Item.query.filter_by(item_id=item_id).one()

    db.session.delete(del_item)
    db.session.commit()


def print_all_items():
    """Print all items in inventory database"""

    items = get_items()

    for item in items:
        print(item)


def item_search(keyword):
    """Return an item by keyword"""

    items = get_items()

    #this seems to only return one inventory item - in the future, I'd 
    #like to rewrite it so that it returns all items that match the keyword
    for item in items:
        if keyword in item.item_description or keyword in item.item_name:
            return item


def get_items():
    """Return all inventory items"""

    return Item.query.all()


def get_item_by_id(item_id):
    """Return an item by its item id"""

    return Item.query.get(item_id)


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


if __name__ == '__main__':
    connect_to_db(app)