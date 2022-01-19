"""Seeds the database"""

import os #imports Python module from standard library
from datetime import datetime 
from random import choice, randint #for testing

import crud
import model
from model import User, Item, app


#drop and recreate the database
os.system('dropdb inventory')
os.system('createdb inventory')

model.connect_to_db(app, echo=False) #connect to the db through model.py
#echo=False to cut down on terminal output so it's easier to see error messages
model.db.create_all()

#create fake users to add to database
for n in range(10):
    email = f'user{n}@test.com'
    password = 'test'

    user = crud.create_user(email, password)


#create fake inventory items to add to the database
for n in range(20):
    item_name = f"{n} test item"
    item_description = f"{n} test item description"
    date_added = "2022-01-01"
    qty_in_lbs = n

    item = crud.create_item(item_name, item_description,
            date_added, qty_in_lbs)


