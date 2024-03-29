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
        self.new_account = Account("victor","onyango","0700736350","victoronyango051@gmail.com")


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.first_name,"victor")
        self.assertEqual(self.new_account.last_name,"onyango")
        self.assertEqual(self.new_account.phone_number,"0700736350")
        self.assertEqual(self.new_account.email,"victoronyango051@gmail.com")

    def test_save_account(self):
       
        self.new_account.save_account() 
        self.assertEqual(len(Account.account_list),6)

    def test_save_multiple_accounts(self):
        '''
        test_save_multiple_account to check if we can save multiple account
        objects to our account_list
        '''
        self.new_account.save_account()
        test_account = Account("Richie","spice","0712345678","Richiespice@yahoo.com") 
        test_account.save_account()
        self.assertEqual(len(Account.account_list),8)

    def test_delete_contact(self):
        '''
        test_delete_account to test if we can remove a account from our account list
        '''
        self.new_account.save_account()
        test_account = Account("Richie","spice","0712345678","Richiespice@yahoo.com") 
        test_account.save_account()

        self.new_account.delete_account()
        self.assertEqual(len(Account.account_list),3)

    def test_find_account_by_number(self):
        '''
        test to check if we can find a account by phone number and display information
        '''

        self.new_account.save_account()
        test_account = Account("Richie","spice","0712345678","Richiespice@yahoo.com") 
        test_account.save_account()

        found_account = Account.find_by_number("0712345678")

        self.assertEqual(found_account.email,test_account.email)

    def test_account_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''

        self.new_account.save_account()
        test_account = Account("Richie","spice","0712345678","Richiespice@yahoo.com") 
        test_account.save_account()

        account_exists = Account.account_exist("0712345678")

        self.assertTrue(account_exists)
        
    def test_display_all_accounts(self):
        '''
        method that returns a list of all accounts saved
        '''

        self.assertEqual(Account.display_account(),Account.account_list)

 

if __name__ == '__main__':
    unittest.main()
    
   