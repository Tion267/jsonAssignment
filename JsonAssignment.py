import json # Import json module
import requests # Import requests module

print("****************************************")
print("*        Welcome to the Magical        *")
print("*                  of                  *")
print("*             Harry Potter             *")
print("****************************************")
print()
print("What would you like to learn about today")
print("Please select from the list below")
print("1. Houses")
print("2. Spells")
print("3. Elixirs")
print("4. Ingredients - Warning this is just a long list of ingredients")
print("0. To Exit")
userChoice = int(input("Please enter the number of your required option: ")) # Request user entry to enter required option 
while userChoice <=-1 or userChoice >= 5: # check to insure that entry is valid
    print("that is not a valid option")
    print("entered number must be between 0-4")
    userChoice = int(input("Please enter the number of your required option: ")) # Request user entry to enter a valid option 
if userChoice == 1: # if loop created depending on selected option
    url = 'https://wizard-world-api.herokuapp.com/Houses' # Set required url
    Count = 1 # Set counter to one to avaid the use of 0 for the first entry
    r = requests.get(url) # Sets value of r and links request to specified url
    data = json.loads(r.text) # Sets data as variable to contain returned data from the request
    for item in data: # for loop to cycle through returned data and print data in the 'name' key pair along with count to indicate location in the data set
        print(Count,"- ", item['name'])
        Count += 1
    userImp = input("Do you want to know more? Y/N: ") # Require user entry to continue and find out more 
    while userImp == "Y" or userImp == "y": # Set to treat anything other than the specified options as a negative entry
        userSelec = int(input("Please enter the number of the House you wish to know about: "))
        while userSelec <= 0 or userSelec >= Count: # Checkentry fits within available options
            userSelec = int(input("Please enter a valid number: "))
        userSelec -= 1 # subtract 1 from user selection to align with actual location in data set
        print("House Name -", data[userSelec]['name']) # Print information from the data series key pairs as identified by the user
        print("House Colours -", data[userSelec]['houseColours'])
        print("House Founder -", data[userSelec]['founder'])
        print("House Animal -", data[userSelec]['animal'])
        print("House Element -", data[userSelec]['element'])
        print("House Ghost -", data[userSelec]['ghost'])
        print("House Common Room -", data[userSelec]['commonRoom'])
        userImp = input("Do you want to look at another House Y/N: ") # Give option to look at another entry
        if userImp == "Y" or userImp == "y":
            continue # Continue loop if correct response provided
        else:
            break # If any other response break loop
elif userChoice == 2: # repeats all code used for option 1 with appropriate changes to text and url
    url = 'https://wizard-world-api.herokuapp.com/Spells'
    Count = 1
    r = requests.get(url)
    data = json.loads(r.text)
    for item in data:
        print(Count,"- ", item['name'])
        Count += 1
    userImp = input("Do you want to know more? Y/N: ")
    while userImp == "Y" or userImp == "y":
        userSelec = int(input("Please enter the number of the Spell you wish to know about: "))
        while userSelec <= 0 or userSelec >= Count:
            userSelec = int(input("Please enter a valid number: "))
        userSelec -= 1
        print("Spell Name -", data[userSelec]['name'])
        print("Spell Incantation -", data[userSelec]['incantation'])
        print("Spell Effect-", data[userSelec]['effect'])
        print("Spell Type -", data[userSelec]['type'])
        print("Spell Light -", data[userSelec]['light'])
        userImp = input("Do you want to look at another Spell Y/N: ")
        if userImp == "Y" or userImp == "y":
            continue
        else:
            break
elif userChoice == 3: # repeats all code used for option 1 with appropriate changes to text and url
    url = 'https://wizard-world-api.herokuapp.com/Elixirs'
    Count = 1
    r = requests.get(url)
    data = json.loads(r.text)
    for item in data:
        print(Count,"- ", item['name'])
        Count += 1
    userImp = input("Do you want to know more? Y/N: ")
    while userImp == "Y" or userImp == "y":
        userSelec = int(input("Please enter the number of the Spell you wish to know about: "))
        while userSelec <= 0 or userSelec >= Count:
            userSelec = int(input("Please enter a valid number: "))
        userSelec -= 1
        print("Elixir Name -", data[userSelec]['name'])
        print("Elixir Effect-", data[userSelec]['effect'])
        print("Elixir Side Effects -", data[userSelec]['sideEffects'])
        print("Elixir Characteristics -", data[userSelec]['characteristics'])
        print("Elixir Difficulty -", data[userSelec]['difficult'])
        userImp = input("Do you want to look at another Elixir Y/N: ")
        if userImp == "Y" or userImp == "y":
            continue
        else:
            break
elif userChoice == 4: # repeats all code used for option 1 without additional options to search list as no further information avalable
    url = 'https://wizard-world-api.herokuapp.com/Ingredients'
    Count = 1
    r = requests.get(url)
    data = json.loads(r.text)
    for item in data:
        print(Count,"- ", item['name'])
        Count += 1
    print("I warned you its just a long list")
else:
    print("Sorry to hear that, I hope you'll be back soon.")
    
    








