# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 21:29:02 2022

@author: Nuno Santos

Taxi Booking System
"""

from taxidatabase import *
import re
import sys
import random
from datetime import datetime, timedelta

# creating database name variable to use it later
taxidatabase = "taxidata.db"

# create a database connection
conn = create_connection(taxidatabase)

if not conn:
    print("Error establishing connection with the database.")
    exit()

create_tables(conn)

current_user = None
passPayment = None


def passRegister(): #This allows passengers to register
    global current_user
    global passPayment
    
    title = input("Please enter your title:\n").title()
    firstName = str(input("Please enter your first name:\n")).title()
    lastName = str(input("Please enter your last name:\n")).title()
    
    '''The following code is to validate the email entered...
               
    Email addresses have 5 parts:
        1) 1 to 20 lower or upper case characters containing letters, numbers, - and _
        2) The @ symbol
        3) 2 to 20 lower or upper case characters containing letters or numbers
        4) the . character
        5) 2 to 3 lower or upper case characters
                    
    So the patterns should be: [\w-]{1,20}@\w{2,20}\.\w{2,3}$
    Breaking it down:
        1) [\w-]{1,20} because we need to add the '-' character
        2) @
        3) \w{2,20}
        4) \.
        5) \w{2,3}$ with '$' indicating that there are no more characters.
    '''
    while True:
                
        def validEmail(aEmail):
            return re.match(r'[\w-]{1,20}@\w{2,20}\.\w{2,3}$', aEmail) #We use r' so we can write pattern in raw format
            return True
                
        email = input("Please enter your email address:\n") #Asks user to enter email address
                
        if validEmail(email):
            break
        else:
            print("The email ", email," does not have the correct format.") #Lets user know email address has incorrect format
                    
            
    mobNumber = input("Please enter your mobile number:\n") #This asks the customer for their mobile number
        
    #The following code is to ensure that the password meets requirements
        
    print("Please select a password. The password must be at least 6 characters long and contain at least one number.")
    while True:
            
        def validPassword(aPass):
            if not re.search('[a-z]', aPass): #This searches for a character between a to z
                return False
            if not re.search('[0-9]', aPass): ##This searches for a character between 0 to 9
                print("Password must contain a numerical character '0-9'.")
                return False
            if not re.search('[A-Z]', aPass): #This searches for an upper case character between a to z
                print("Password must contain a capital letter.")
                return False
            if len(aPass) < 6: #This is to ensure it is at least 6 characters long
                print("Password must be at least 6 characters long.")
                return False
            return True
            
        password = input("Password: ") #Asks user to enter a password
            
        if validPassword(password): #If password meets requirement it asks the user to confirm password
            custVerPass = input("Please confirm password: ")
            while (custVerPass != password): #Checks is passwords match
                print("Passwords do not match.")
                custVerPass = input("Please confirm password: ")
                print("Your password has successfully been created.")
            break
        else:
            print("Password does not meet requirements. Please try again.")
                
    postcode = input("Please enter your post code:\n") #This asks the customer for their post code
        
    address = input("Please enter your address:\n") #This asks the customer for their address
        
    town = input("Please enter your town:\n") #This asks the customer for their town
        
    county = input("Please enter your county:\n") #This asks the customer for their county
        
    paymentMethod = input("Please enter your payment method:\n") #This asks the customer for their payment method
                
    data = (title,
            firstName,
            lastName,
            email,
            mobNumber,
            password,
            postcode,
            address,
            town,
            county,
            paymentMethod
            )
    current_user = create_passenger(conn, data)
    passPayment = paymentMethod
    
    print("Your account has successfully been created.")
    
    show_menu()
    

def driverRegister(): #This allows drivers to register
    
    global current_user
    
    title = input("Please enter your title:\n").title()
    firstName = str(input("Please enter your first name:\n")).title()
    lastName = str(input("Please enter your last name:\n")).title()
    34
    '''
    The following code is to validate the email entered...
               
    Email addresses have 5 parts:
        1) 1 to 20 lower or upper case characters containing letters, numbers, - and _
        2) The @ symbol
        3) 2 to 20 lower or upper case characters containing letters or numbers
        4) the . character
        5) 2 to 3 lower or upper case characters
                    
    So the patterns should be: [\w-]{1,20}@\w{2,20}\.\w{2,3}$
    Breaking it down:
        1) [\w-]{1,20} because we need to add the '-' character
        2) @
        3) \w{2,20}
        4) \.
        5) \w{2,3}$ with '$' indicating that there are no more characters.
    '''
    while True:
                
        def validEmail(aEmail):
            return re.match(r'[\w-]{1,20}@\w{2,20}\.\w{2,3}$', aEmail) #We use r' so we can write pattern in raw format
            return True
                
        email = input("Please enter your email address:\n") #Asks user to enter email address
                
        if validEmail(email):
            break
        else:
            print("The email ", email," does not have the correct format.") #Lets user know email address has incorrect format
                    
            
    mobNumber = input("Please enter your mobile number:\n") #This asks the customer for their mobile number
        
    #The following code is to ensure that the password meets requirements
        
    print("Please select a password. The password must be at least 6 characters long and contain at least one number.")
    while True:
            
        def validPassword(aPass):
            if not re.search('[a-z]', aPass): #This searches for a character between a to z
                return False
            if not re.search('[0-9]', aPass): ##This searches for a character between 0 to 9
                print("Password must contain a numerical character '0-9'.")
                return False
            if not re.search('[A-Z]', aPass): #This searches for an upper case character between a to z
                print("Password must contain a capital letter.")
                return False
            if len(aPass) < 6: #This is to ensure it is at least 6 characters long
                print("Password must be at least 6 characters long.")
                return False
            return True
            
        password = input("Password: ") #Asks user to enter a password
            
        if validPassword(password): #If password meets requirement it asks the user to confirm password
            custVerPass = input("Please confirm password: ")
            while (custVerPass != password): #Checks is passwords match
                print("Passwords do not match.")
                custVerPass = input("Please confirm password: ")
                print("Your password has successfully been created.")
            break
        else:
            print("Password does not meet requirements. Please try again.")
                
    regNum = input("Please enter your car's registration number:\n") #This asks the customer for their post code
    
    data = (title,
            firstName,
            lastName,
            email,
            mobNumber,
            password,
            regNum
            )
    current_user = create_driver(conn, data)
    
    print("Your account has successfully been created.")
    
    driver_menu() 


#This code is to allow passengers to login
def passLogin():
    
    global passPayment
    global current_user

    email = input("Email: ")
    password = input("Password: ")

    data = (email,password)
    
    try: #Checks if user email and password match
        user = login_passenger(conn, data)
        user_id = user[0]
        user_first_name = user[2]
        current_user = user_id
        user_payment = user[11]
        passPayment = user_payment
    except:
        print("You have entered an incorrect email or password. Please try again.")
        passLogin()

    print(f"Hello {user_first_name}, you have been successfully logged in.\n")
    show_menu()
    

#This code is to allow drivers to login
def driverLogin():
    
    global current_user

    email = input("Email: ")
    password = input("Password: ")

    data = (email,password)
    
    try: #Checks if user email and password match
        user = login_driver(conn, data)
        user_id = user[0]
        user_first_name = user[2]
        current_user = user_id
    except:
        print("You have entered an incorrect email or password. Please try again")
        driverLogin()

    print(f"Hello {user_first_name}, you have been successfully logged in.")
    driver_menu()
    

def make_booking(): #This code is to allow user to make bookings
    global passPayment
    
    drivers = get_drivers(conn)
    
    randomDriver = random.randint(0, (len(drivers) - 1)) #This selects a random driver from database

    driverid = drivers[randomDriver][0]
    passengerid = current_user
 
    
    currentTime = datetime.now()
    #This is to add 30 minutes to time
    addTime = 30
    finishTime = currentTime + timedelta(minutes=addTime) #Adds 30mins to currentTime so endTime is always 30mins after booking made
    currentTime_str = currentTime.strftime('%H:%M:%S') #Converts end time into string
    finishTime_str = finishTime.strftime('%H:%M:%S') #Converts end time into string
    dateBooked_str = currentTime.strftime('%m-%d-%Y') #Converts date into string
    
    startTime = currentTime_str
    dateBooked = dateBooked_str
    startAddress = input("Please enter the pick up address: ")
    endTime = finishTime_str
    destinationAddress = input("Please enter your destination address: \n")
    paymentMethod = passPayment

    data = (driverid, passengerid, dateBooked, startTime, startAddress, endTime, destinationAddress, paymentMethod)
    trip = create_booking(conn, data)
    
    print("Booking created.\n"+
          "Your driver is", drivers[randomDriver][2], drivers[randomDriver][3]+'.\n')

    show_menu()


def show_bookings(): #This code allows user to see their bookings
    trips = get_bookings(conn)
    if not trips:
        print("You currently have no bookings.")
    else:
        print("Your bookings:")
        for i, getTrip in enumerate(trips, 1): #Start point becomes 1, not 0
            print(str(i)+".",str(getTrip[3])+", "+str(getTrip[4]), "to",str(getTrip[7])+'.\n')
            
    show_menu()
    

def remove_trip(): #This code allows user to delete a booking
    global current_user
    
    trips = get_bookings(conn)
    if not trips:
        print("You currently have no bookings.")
    else:
        print("Please select a booking to delete:")
        for i, getTrip in enumerate(trips, 1): #Start point becomes 1, not 0
            print(str(i)+".",str(getTrip[3])+", "+str(getTrip[4]), "to",str(getTrip[7])+'.\n')
            
    _input = input("Select which booking to delete: ")
    index = int(_input)
    getTrip = trips[index-1]
    bookingid = getTrip[0]
    print("Booking is: ", getTrip)
    print("Booking id: ",bookingid)
    
    delete_booking(conn, bookingid)
    print("Booking has been deleted.")
            
    show_menu()


#This code is for the home page
def show_menu():
    if(not current_user):
        welcomeScreen = """Welcome, what would you like to do today?
1. Register as a passenger.
2. Register as a driver.
3. Login to passenger portal.
4. Login to driver portal.
"""           
        print(welcomeScreen)
        menuInput = input("Please select an option:\n")

        if menuInput == "1":
            passRegister()
            
        elif menuInput == "2":
            driverRegister()
            
        elif menuInput == "3":
            passLogin()
            
        elif menuInput == "4":
             driverLogin()

    else:
        
        homeScreen = """Please select one of the below options to continue:
1. Make a booking.
2. View your bookings.
3. Cancel a booking.
4. Log out
"""           
        print(homeScreen)   
        
        menuInput = input()

        if menuInput == "1":
            make_booking()

        elif menuInput == "2":
            show_bookings()

        elif menuInput == "3":
            remove_trip()
        
        elif menuInput == "4":
            print("You have been logged out.")
            sys.exit()
            

#This code is for driver home page
def driver_menu():
    if(not current_user):
        welcomeScreen = """Welcome, what would you like to do today?
1. Register as a passenger.
2. Register as a driver.
3. Login to passenger portal.
4. Login to driver portal.
"""           
        print(welcomeScreen)
        menuInput = input("Please select an option:\n")

        if menuInput == "1":
            passRegister()
            
        elif menuInput == "2":
            driverRegister()
            
        elif menuInput == "3":
            passLogin()
            
        elif menuInput == "4":
             driverLogin()

    else:
        
        homeScreen = """Please select one of the below options to continue:
1. View your bookings.
2. Cancel a booking.
3. Log out
"""           
        print(homeScreen)   
        
        menuInput = input()

        if menuInput == "1":
            show_bookings()

        elif menuInput == "2":
            remove_trip()

        elif menuInput == "3":
            print("You have been logged out.")
            sys.exit()
            
show_menu() #This shows the user the home page.