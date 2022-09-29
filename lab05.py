
########################################################################
##
## CS 101 Lab
## Program # Week 6; Lab 5
## Name: Hayleigh Arnold
## Email: hca8qp@umsystem.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import string

# functions
def character_value(char):
    value = ord(char)
    value = value - 65
    return value

def get_school(string): 
    if string[5] == "1":
        return "School of Computing and Engineering SCE"
    elif string[5] == "2":
        return "School of Law"
    elif string[5] == "3":
        return "College of Arts and Sciences"
    else:
        return "Invalid School"

def get_grade (library_card):
    if library_card[6] == '1':
        return "Freshman"
    elif library_card[6] == '2':
        return "Sophomore"
    elif library_card[6] == '3':
        return "Junior"
    elif library_card[6] == '4':
        return "Senior"
    else:
        return "Invalid Grade"

def get_check_digit(library_card): # the formula to calculate the check digit was (index+1)*value
    sum = 0
    for i in range (len(library_card)):
        value = character_value(library_card[i])
        sum += (i + 1)*value
    total = sum
    check_digit = sum%10
    return check_digit

def verify_check_digit(library_card):

    if len(library_card) != 10:
        return False, "The length of the number given must be 10"

    for i in range (0,5):
        if (ord(library_card[i]) < 65) or (ord(library_card[i]) > 90):
            error = str(library_card[i])
            i = str(i)
            return (False, "The first 5 characters must be A-Z, the invalid character is at " + i + " is " + error)

    for i in range(7,10):
        if (library_card[i] < '0') or (library_card[i] > '9'):
            error = str(library_card[i])
            i = str(i)
            return (False, "The last 3 characters must be 0-9, the invalid character is at " + i + " is " + error) #Here I am concatenating the strings.

    
    if (library_card[5] != '1' and library_card[5] != '2' and library_card[5] != '3'):
            return (False, "The sixth character must be 1 2 or 3")
    
    if (library_card[6] != '1' and library_card[6] != '2' \
        and library_card[6] != '3' and library_card[6] != '4'):
            return (False, "The seventh character must be 1 2 3 or 4")
    
    correctval = get_check_digit(library_card)
    index9 = int(library_card[9])
    
    if index9 != correctval:
        explan = "Check Digit " + str(index9) + " does not match calculated value " \
               + str(correctval) + "."
        return (False,explan)
        
    return (True,'')



def main():
    '''The main function allows for me to be able to repeat rhis process without reprinting the steps over and over''' 
    while(1):
        library_card = input("Enter Library Card. Hit Enter to Exit ==> ") 
        (result,explan) = verify_check_digit(library_card)
        
        if result == True:
            print("\nLibrary card is valId.")
            print("The card belongs to a student in " + get_school(library_card))
            print("The card belongs to a " + get_grade(library_card))
                
        else:
            print("Library card is invalid.")
            print(explan)

if __name__ == "__main__":

    # main program
    print(f'{"Linda Hall":^60}')
    print(f'{"Library Card Check":^60}')
    print("==" * 30)

    print(main())
