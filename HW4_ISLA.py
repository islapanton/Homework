## Task 1: Git and GitHub ##
# GIT WORKFLOW FUNDAMENTALS:
# Working Directory: These are the files you are working on on your computer that have not yet
# been finalised enough to use 'git add' to put them into the staging area.

# Staging Area: Files in the staging area have been added and are awaiting being 'commit'ted to
# github, which will be done in  the next commit.
# Local Repo (head): This is the current branch that you are working on. These files have been
# uploaded using commit, but have not been merged with other users work, as in the master ?

# Remote repo (master): The remote repository is found online or on github and can be accessed by
# users with the right permissions e.g. team members. Individuals' work can be committed to the
# central repository (on a branch) and it is then possible to combine work/changes from different
# branches to create a master copy.

# WORKING DIRECTORY STATES:
# Staged: This means one of two things: either the file was not in the last commit, or it has had
# changes made to it since the last commit. These staged files have been added to the staging area
# via git add, but have yet to be commited to the central repository.

# Modified: This means that changes have been made to a file since the last commit, but these have
# not yet been commited to git yet.

# Committed: These files have been uploaded and are now stored in the central repository and are
# available for other team members etc. to access.

# GIT COMMANDS:
# Git add: This command will allow you to add any changes to a file from the working directory to the staging
# area. However, these changes are not final until they are committed as below.

# Git commit: This command saves all changes made (through Git add) that are sitting in the staging area to
# the remote (or central) repository. This will allow files/changes to files to be examined by other users
# of the repository.

# Git push: This command essentially uploads files from local repository (or on your machine) to the remote
# repository. Any changes or new files can then be accessed by other users of the repository.

# Git fetch: This command allows the user to download files (with changes/commits) from the central
# repository into the local. This essentially means you are able to look at or examine code or files from
# other users but unlike pull, the fetch command does not automatically merge your existing work in the
# local with any new/changed work from the central repository.

# Git merge: This will allow you to merge any changes from the central repository with your files in
# the local repository. Can be useful when wanting to merge your own work with the work of other team members.

# Git pull: This is somewhat similar to fetch in that the command downloads from the central repository to be
# accessed in the local repository. However, using pull will also perform a merge between local and central
# files and commit it ready for upload.


## Task 2: Exception Handling ##
##  ATM Programme ##
# Enter pin
count = 0
pin = '9743'
# Giving 3 chances and then exiting programme if incorrect
while count < 3:
    pin1 = (input(str('Please enter your four digit pin:   ')))
    if pin == pin1:
        print('Credentials are correct. Please proceed to main menu. Press any key to continue')
        break
    else:
        print('Something went wrong. Incorrect pin. Please try again')
        count +=1
if count >= 3:
    raise Exception ('You have entered the pin incorrectly THREE times. \n Account is now locked. Please call customer services. ')
# Setting balance to £100
account_bal = 100

def main_menu():
    print(' Main Menu \n For the following services, please press the relevant key: \n 1. Display balance \n 2. Deposit \n 3. Withdraw')


# Displaying menu
main_menu()
option = input('Which service do you require today? ')

# Display balance
def balance():
        print(f'Your account balance is: {account_bal:.2f}')
        return_menu = input('Would you like to go back to the main menu?   ')
        if return_menu in ('n', 'N', 'No',):
            print('Thanks for using our banking services. Have a nice day! ')
        else:
            main_menu()
            option = input('Which service do you require today? ')
# Deposit
def deposit():
        dep = input('How much are you depositing today? ')
        new_bal = account_bal + int(dep)
        print(f'Your new account balance is: {new_bal:.2f}')
        return_menu = input('Would you like to go back to the main menu?   ')
        if return_menu in ('n', 'N', 'No',):
            print('Thanks for using our banking services. Have a nice day! ')
        else:
            main_menu()
            option = input('Which service do you require today? ')

def withdraw():
        wd = input('How much are you looking to withdraw today?   ')
        wd = int(wd)
        try:
            if wd > account_bal:
                raise Exception('Error. You cannot have a negative balance. \nYou do not have sufficient funds to withdraw your desired amount')
            else:
                new_bal = account_bal - int(wd)
                print(f'The updated account balance is: {new_bal:.2f}')
        except Exception as ex:
            print(ex)
        finally:
                return_menu = input('Would you like to go back to the main menu?   ')
                if return_menu in ('n', 'N', 'No',):
                        print('Thanks for using our banking services. Have a nice day! ')

# Running Options
if option == '1':
    balance()
elif option == '2':
    deposit()
elif option == '3':
    withdraw()
else:
    raise Exception('Invalid option. Your card will now be returned. \nHave a nice day!')















import unittest
class ATMTestCase(unittest.TestCase)
    def test_pin(self):

