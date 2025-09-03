# Name:  Pramitha Dhanraj

import json

def inputInt(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input, enter a valid integer.")

def inputSomething(prompt):
    while True:
        input_value = input(prompt)
        if input_value.strip():
            return input_value.strip()
        else:
            print("Invalid input, try again.")

def saveChanges(dataList):
    f= open("data.txt", "w") 
    json.dump(data, f)
    

try:
    f= open("data.txt", "r")
    data = json.load()
    f.close()
except:
    data = []
    
print("Welcome to the Joke Bot Admin Program.")

while True:
    print("Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete, [q]uit.")
    choice = input('> ').lower()
        
    if choice == 'a':
        setup = inputSomething("Enter the setup for the joke: ")
        punchline = inputSomething("Enter the punchline for the joke: ")
        new_joke = {
            "setup": setup.lower(),
            "punchline": punchline.lower(),
            "numOfRatings": 0,
            "sumOfRatings": 0,
        }
        data.append(new_joke)
        saveChanges(data)
        print("Joke is successfully added")

    
    elif choice == 'l':
         if len(data) == 0:
            print("No jokes saved")
         else:
            print("List of jokes:")
            for i, joke in enumerate(data):
               print(f"{i}) {joke['setup']}")


    elif choice == 's':
        search_term = inputSomething("Enter a search term: ").lower()
        matching_jokes = []
        for i, joke in enumerate(data):
            if search_term in joke["setup"] or search_term in joke["punchline"]:
                matching_jokes.append((i, joke))
        if len(matching_jokes) == 0:
            print("No matching jokes found")
        else:
            print("Search results:")
            for i, joke in matching_jokes:
                print(f"{i}) {joke['setup']}")


    elif choice == 'v':
        if len(data) == 0:
            print("No jokes saved")
        else:
            index = inputInt("Enter joke number to view: ")
            if index < 0 or index > len(data):
                print("Invalid index number")
            else:
                joke = data[index]
                print(f"{joke['setup']} \n{joke['punchline']}")
                if joke["numOfRatings"] == 0:
                    print("Joke has not been rated")
                else:
                    average_rating = round(joke["sumOfRatings"] / joke["numOfRatings"], 1)
                    print(f"Rated {joke['numOfRatings']} time(s). Average rating is {average_rating}/5.")

    elif choice == 'd':
        if len(data) == 0:
            print("No jokes saved")
        else:
            index = inputInt("Enter an index number: ")
            if index < 0 or index > len(data):
                print("Invalid Index number.")
            else:
                
                del data[index]
                saveChanges(data)
                print("Joke deleted")
            

    elif choice == 'q':
        print("Goodbye!")
        break

    else:
        print("Invalid choice")

