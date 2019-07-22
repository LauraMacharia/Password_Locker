import unittest
from login import Login

class TestLogin(unittest.TestCase):
    '''
    Test class that defines test cases for the login class behaviour.
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_login = Login("snapchat","Laura","Macharia","LauraMacharia","ruvy") # create login object
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_login.social,"snapchat")
        self.assertEqual(self.new_login.firstname,"Laura")
        self.assertEqual(self.new_login.lastname,"Macharia")
        self.assertEqual(self.new_login.username,"LauraMacharia")
        self.assertEqual(self.new_login.password,"ruvy")

    def test_save_login(self):
        '''
        test_save_login test case to test is the login object is saved into the login
        '''
        self.new_login.save_login()#saving the new user
        self.assertEqual(len(Login.login),1)


    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Login.login=[]

    def test_save_multiple_login(self):
        '''
        test_save_multiple_login to check if we can save multiple login object to our login
        '''
        self.new_login.save_login()
        test_login = Login("Test","Laura","Macharia","LauraMacharia","ruvy")
        test_login.save_login()
        self.assertEqual(len(Login.login),2)
        
    def test_login_exists(self):
        '''
        test to check if we can return a Boolean if we cannot find the login.
        '''
        self.new_login.save_login()
        test_login = Login("Test","Laura","Macharia","LauraMacharia","ruvy")#new user
        test_login.save_login()
        login_exists = Login.login_exist("ruvy")
        self.assertTrue(login_exists)

    def test_display_all_login(self):
        '''
        method that returns a list of all logins saved saved
        '''
        self.assertEqual(Login.display_login(),Login.login)


if __name__ == '__main__':
        unittest.main()
