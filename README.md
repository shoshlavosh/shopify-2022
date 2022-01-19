INSTRUCTIONS / HOW TO INSTALL:

Set up and activate a virtual environment:
>virtualenv env
>source env/bin/activate

Install frameworks & libraries:
>pip3 install -r requirements.txt

Seed the database with fake inventory items & users:
>python3 seed.py

To run "is_user1()" test in tests.py, enter the following in the command line: 
>python3 -m doctest -v tests.py