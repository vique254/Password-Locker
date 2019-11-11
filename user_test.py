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


if __name__ == '__main__':
    unittest.main()
    
    def test_save_account(self):
       
        self.new_account.save_account() # saving the new contact
        self.assertEqual(len(Account.account_list),1)

if __name__ ==  '__main__':
    unittest.main()