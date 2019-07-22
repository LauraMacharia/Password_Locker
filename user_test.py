import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviour.
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Laura","Macharia","0712036591","lauramacharia@gmail.com","LauraMacharia","ruvy") 


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Laura")
        self.assertEqual(self.new_user.last_name,"Macharia")
        self.assertEqual(self.new_user.phone_number,"0712036591")
        self.assertEqual(self.new_user.email,"lauramacharia@gmail.com")
        self.assertEqual(self.new_user.username,"LauraMacharia")
        self.assertEqual(self.new_user.password,"ruvy")


    def test_save_user(self):
        '''
        test_save_user test case to test is the user object is saved into the user
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user=[]

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user object to our user
        '''
        self.new_user.save_user()
        test_user = User("Test","user","0712036591","lauramacharia@gmail.com","LauraMacharia","ruvy")
        test_user.save_user()
        self.assertEqual(len(User.user),2)

#more test above
    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user
        '''
        self.new_user.save_user()
        test_user = User("Test","user","0712036591","lauramacharia@gmail.com","LauraMacharia","ruvy")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user), 1)
        
    def test_find_user_by_number(self):
        '''
        test to check if we can find a user by phone number and display information
        '''
        self.new_user.save_user()
        test_user = User("Test","user","0712036591","lauramacharia@gmail.com","LauraMacharia","ruvy")
        test_user.save_user()

        found_user = User.find_by_number("0712036591")
        self.assertEqual(found_user.email, test_user.email)
    def test_user_exist(self):
        '''
        test to check if we can return a Boolean if we cannot find the user.
        '''
        self.new_user.save_user()
        test_user = User("Test","user","0712036591","lauramacharia@gmail.com","LauraMacharia","ruvy")
        test_user.save_user()
        user_exists = User.user_exist("LauraMacharia")
        self.assertTrue(user_exists)


    def test_display_all_user(self):
        '''
        method that returns a list of all users saved
        '''
        self.assertEqual(User.display_user(),User.user)

if __name__ == '__main__':
        unittest.main()