#!/usr/bin/env python3.6
from password import Account

def create_account(fname,lname,phone,email):
    '''
    Function to create a new account
    '''
    new_account = Account(fname,lname,phone,email)
    return new_account

def save_accounts(account):
    '''
    Function to save account
    '''
    account.save_account()