#!/bin/usr/python 

import time #Used to add delays 
import os #Allows for operating system functionality like clear 
import hashlib #Used for md5 hashing 
import getpass #Used to hide user input 
import string


#**********************************************************************************************************************************************#
#                                                                   Functions                                                                  #
#**********************************************************************************************************************************************#

#A function that checks to make sure that a username can't be re-used. Takes in the username as a parameter 

def checkForDuplicate(username):
    isNew = False #Create a boolean
    with open("database") as dataBase:#Open the database file and give it an alias of database 
        for line in dataBase: #Go through each line individually 
            for part in line.split(): #Splits up the string in the line when a space is found, and adds them to an array 
                if username in part: #If the users name is in the array 
                    isNew = True #Change the value of the boolean
    return isNew 


#A basic salt function I created. It takes in the username and returns the salt at the end

def createSalt(name):
    salt = name #The salt is set to their username
    salt = salt.replace("t","n") #Random letter swap
    salt = salt.replace("d","z") 
    salt = salt.replace("w","b") 
    salt = salt.replace("g","q") 
    #Add random letters and symbols to the salt
    salt = "Ksadfkd45(sfD540SFIOEO)FMODMVidfgmDo$:/^%^*)#" + salt +  "ndu@GlLDQG%xllA&kjSssieIm_X0c5u7$5fKhhwVo)^^xp(c29(kmlsf"
    salt = hashlib.sha512(salt).hexdigest() #Hash the salt using sha512
    return salt


#This function is used to make sure that the password meets the necessary requirements. If it does, it returns true
def checkPassword(password):
    specialCharacters = set(string.punctuation.replace("!@#$%^&*()-_+=:;,.<>/?~`1234567890",""))
    if ((len(password) >= 8) and (any(char in specialCharacters for char in password))): #If the password has at least 8 characters and a special character
        return True
    else:
        return False
      
#A function to create a new user and add them to the database 
def createUser():
    userName = raw_input("Enter name:\n") #Take in their username

    if checkForDuplicate(userName) == False: #If the name is not in the database then create it
        salt = createSalt(userName) #Calls the function and stores the salt
        database = open('database','a') #Opens a file that you can write to store information. The a lets you append to the end of the file 
        #Take in a password and not show what is being typed 
        password = getpass.getpass("Enter a password. The password must be at least 8 characters and contain a special character:\n") 

        if checkPassword(password) == True: #If their password follows certain criteria
            password = password + salt #Combine the salt and password before hashing the password
            hashedInput = hashlib.sha512(password).hexdigest() #Uses sha512 to  hash and store the password 
            database.write(userName+' '+hashedInput+'\n') #Writes the information to the text file 
            print("Your account was successfully created! You will be taken to the login prompt shortly! \n") 
            time.sleep(2) #Waits for two seconds 
            clear = lambda: os.system('clear') #Creates a shortcut to clear the terminal 
            clear() 
            database.close() #Closes the file 
            loginMenu() #Calls the login menu function
        else:
            print("Sorry your password did not meet the requirements")
    else:
        print("Sorry, that username is taken") 


#This function is used to present the user with a login page 
def loginMenu():
    user_name = raw_input("What is your username? \n") #Stores the input as a variable called username 
    salt = createSalt(user_name)
    password = getpass.getpass("Enter your password: \n") #Stores the password as password and hides the text in the terminal 
    password = password + salt 
    with open("database") as dataBase: #Same as above 
        for line in dataBase: 
            for part in line.split(): 
                if user_name in part: 
                    hashed_password = line.split(" ")[1:][0] #Take the last word (AKA the password) and set it to this variable 
                    hashed_input = (hashlib.sha512(password).hexdigest() + '\n') #Perform the sha512 hash operation 
                    if hashed_input == hashed_password: #If the password entered matches the one in the database 
                        print ("Successfully logged in!") 
                    else: 
                        print ("Sorry, that is not correct!") 



#**********************************************************************************************************************************************#
#                                                               Main Function                                                                  #
#**********************************************************************************************************************************************# 
if userInput  =="yes" or userInput == "Yes": 
    createUser() 
else: 
    loginMenu() 

