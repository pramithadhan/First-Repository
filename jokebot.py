# Name:  Pramitha Dhanraj


import tkinter
import tkinter.messagebox
import json


class ProgramGUI:

    def __init__(self):

        self.main = tkinter.Tk()
        self.main.title('Joke Bot')
        self.main.resizable(False,False)
        self.main.geometry('700x200')
        self.setupLabel = tkinter.Label(self.main, text=' ')
        self.punchlineLabel = tkinter.Label(self.main, text=' ')
        self.ratingFrame = tkinter.Frame(self.main)
        self.ratingLabel = tkinter.Label(self.ratingFrame, text="Your Rating:")
        self.ratingEntry = tkinter.Entry(self.ratingFrame)
        self.submitButton = tkinter.Button(self.ratingFrame, text='Submit', command=self.rateJoke)
        self.numRatingsLabel = tkinter.Label(self.main, text='')
        self.avgRatingLabel = tkinter.Label(self.main, text=' ')

        self.setupLabel.pack()
        self.punchlineLabel.pack()
        self.ratingFrame.pack()
        self.ratingLabel.pack()
        self.ratingEntry.pack()
        self.submitButton.pack()
        self.numRatingsLabel.pack()
        self.avgRatingLabel.pack()

        try:
            f = open("data.txt", "r")
            print("File successfully opened.")
            self.data = json.load(f)
            print("Data successfully loaded")
            f.close()
        except (FileNotFoundError,json.JSONDecodeError):
            tkinter.messagebox.showerror("Missing/Invalid file", "The data file is missing or contains invalid JSON.")
            self.main.destroy()

        self.currentJoke = 0
        self.allJokesRated = False
        self.showJoke()
        self.main.mainloop()

    def showJoke(self):
        if self.currentJoke >= len(self.data):
            self.allJokesRated = True
            tkinter.messagebox.showinfo("Rating recorded", "Thank you for rating. \n That was the last joke. \n The program will end now.")
            self.main.destroy()
        else:
            joke = self.data[self.currentJoke]
            self.setupLabel.configure(text=joke['setup'])
            self.punchlineLabel.configure(text=joke['punchline'])
            self.numRatingsLabel.configure(text="")
            self.avgRatingLabel.configure(text="")
            self.ratingEntry.delete(0, 'end')
            self.currentJoke += 1
            

    def rateJoke(self):
        
        try:
            rating = int(self.ratingEntry.get())
        except ValueError:
            tkinter.messagebox.showerror("Rating error", "Invalid input, enter an integer between (1-5).")
            return

        if rating < 1 or rating > 5:
            tkinter.messagebox.showerror("Rating error", "Invalid input, enter a rating between 1 and 5.")
            return

        joke = self.data[self.currentJoke - 1]
        joke["numOfRatings"] += 1
        joke["sumOfRatings"] += rating
        average_rating = round(joke["sumOfRatings"] / joke["numOfRatings"], 1)
        self.numRatingsLabel.configure(text=f"Rated {joke['numOfRatings']} time(s)")
        self.avgRatingLabel.configure(text=f"Average rating: {average_rating}/5")

        tkinter.messagebox.showinfo("Rating recorded" , " Thank you for rating, \n The next joke will now appear.")

        
        self.showJoke()

gui = ProgramGUI()



                                      


