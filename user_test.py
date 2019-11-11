import unittest # Importing the unittest module
from password import Account # Importing the Account class

class TestAccount(unittest.TestCase):
    '''
    Test class that defines test cases for the account class behaviours.
    
    Args:
    unittest.TestCase: TestCase class that helps in creating  test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Account("vique","254","12345v") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.first_name,"vique")
        self.assertEqual(self.new_account.last_name,"254")
        self.assertEqual(self.new_account.password,"12345v")

    def test_save_account(self):
       
        self.new_account.save_account() 
        self.assertEqual(len(Account.account_list),2)

    def test_save_multiple_account(self):
        '''
        test_save_multiple_account to check if we can save multiple account
        objects to our account_list
        '''
        self.new_account.save_account()
        test_account = Account("Richie","spice","00000") # new account
        test_account.save_account()
        self.assertEqual(len(Account.account_list),4)

    def test_delete_contact(self):
        '''
        test_delete_account to test if we can remove a account from our account list
        '''
        self.new_account.save_account()
        test_account = Account("Richie","spice","00000") 
        test_account.save_account()

        self.new_account.delete_account()
        self.assertEqual(len(Account.account_list),1)

if __name__ == '__main__':
    unittest.main()
    
   