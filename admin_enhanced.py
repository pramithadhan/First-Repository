# Name:  Pramitha Dhanraj
# Student Number:10634467  

import json

def inputInt(prompt, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if max_value == (value < 1 or value > max_value):
               print("Invalid input, enter an integer greater than 0 or less than max_value")
            else:
                return value     
        except ValueError:
            print("Invalid input, enter a valid integer.",)

def inputSomething(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip():
            return user_input.strip()
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
    print("Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete, [t]op, [q]uit.")
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
                print(f"{i+1}) {joke['setup']}")


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
                print(f"{i+1}) {joke['setup']}")


    elif choice == 'v':
       if len(data) == 0:
          print("No jokes saved")
       else:
          index = inputInt("Joke number to view: ", len(data))
          if index < 1 or index > len(data):
              print("Invalid index number")
          else:
              joke = data[index - 1]
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
            index = inputInt("Enter an index number: ", len(data))
            if index < 0 or index > len(data):
                print("Invalid Index number.")
            else:
                
                del data[index-1]
                saveChanges(data)
                print("Joke deleted")
                

    elif choice == 't':
        top_jokes = []
        for i, joke in enumerate(data):
            if joke["numOfRatings"] > 0:
                average_rating = joke["sumOfRatings"] / joke["numOfRatings"]
                if average_rating >= 4:
                    top_jokes.append((i, joke))
        if len(top_jokes) == 0:
            print("No top rated jokes found")
        else:
            for i, joke in top_jokes:
                print(f"{i+1}: {joke['setup']}")

        

    elif choice == 'q':
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
