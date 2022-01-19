"""Tests"""

import unittest
import crud


#to run the "is_user1()" test, enter the following in the command line: 
#$ python3 -m doctest -v tests.py
def is_user1(name, email):
    """Is this user1?
    >>> is_user1("user1", "user0@test.com")
    True
    >>> is_user1("Jane", "jane@hacks.com")
    False
    >>> is_user1("USER1", "USER0@test.COM")
    True
    >>> is_user1("User1", "User@Test.Com")
    False
    >>> is_user1("User1", "User0@Test.Com")
    True
    """
    
    if name.lower() == "user1" and email.lower() == "user0@test.com":
        return True

    else:
        return False



#Note: I don't actually know how to use the below tests without
#a server with routes to test, so I'm just including the basic 
#set-up and tear-down methods as examples. I really wanted to include
#them but I'm not sure how to do it in this context.
class FlaskTests(unittest.TestCase):

    def setUp(self):
        """Set up that runs before every test"""

        self.client = app.test_client() #uses Flask test client
        app.config['TESTING'] = True

    def tearDown(self):
        """Tear down that runs after every test"""

        db.session.close()
        db.drop_all() 


if __name__ == "__main__":
    unittest.main()