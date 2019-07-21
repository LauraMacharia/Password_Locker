import unittest
from user import User

class Testuser(unittest.TestCase):
    """
    test clas define test cases for the user class behaviours.
    
    Args
    unittest.TestCase: TestCase class that help in creating test cases
    """
    def setup(self):
        
        self.new_user = User("Laura", "Macharia", "0712036591", "lauramacharia@gmail.com", "LauraMacharia", "ruvy")
        
    def test_init(self):
        """
        To test if the objects are initialized properly
        """
        
        self.assertEqual(self.new_user.first_name, "Laura")
        self.assertEqual(self.new_user.last_name, "Macharia")
        self.assertEqual(self.new_user.phone_number, "0712036591")
        self.assertEqual(self.new_user.email, "lauramacharia@gmail.com")
        self.assertEqual(self.new_user.user_name, "LauraMacharia")
        self.assertEqual(self.new_user.pasword, "ruvy")
    
    def test_save_user(self):
        """
        Tests if the user has been saved
        """
        
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
        
            
        
if _name_ == '_main_':
    unittest.main()          