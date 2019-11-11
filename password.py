class Account:
    """
    Class that generates new instances of passwords
    """

    account_list = [] # Empty account list
    
    def save_account(self): 

        Account.account_list.append(self)
    def __init__(self,first_name,last_name,password):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.password = password
