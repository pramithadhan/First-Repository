# Name:  Pramitha Dhanraj
# Student Number:  10634467


import tkinter
import tkinter.messagebox
import json


class ProgramGUI:

    def __init__(self):

        self.main = tkinter.Tk()
        self.main.title('JOKE BOT')
        self.main.geometry('1000x200')
        self.main.resizable(False,False)
        self.main.configure(bg='black')
        self.setupLabel = tkinter.Label(self.main, text=' ', font = ('Arial', 16 ),fg='red')
        self.punchlineLabel = tkinter.Label(self.main, text=' ', font= ('Arial', 16),fg='red')
        self.punchlineButton = tkinter.Button(self.main, text='Reveal Punchline', command=self.revealPunchline, font=('Arial', 12))
        self.ratingFrame = tkinter.Frame(self.main, pady=10, bg = 'black')
        self.ratingLabel = tkinter.Label(self.ratingFrame, text="Your Rating:", font= ('Arial',12))
        self.ratingEntry = tkinter.Entry(self.ratingFrame, font= ('Arial',12 ))
        self.submitButton = tkinter.Button(self.ratingFrame, text='Submit', command=self.rateJoke, font = ('Arial',12))
        self.numRatingsLabel = tkinter.Label(self.main, text='', font= ('Arial',12))
        self.avgRatingLabel = tkinter.Label(self.main, text=' ', font = ('Arial',12))
        self.ratingVar = tkinter.IntVar()
        
        self.setupLabel.pack()
        self.punchlineLabel.pack()
        self.punchlineButton.pack()
        self.ratingFrame.pack()
        self.ratingLabel.pack(side='left')
        self.numRatingsLabel.pack()
        self.avgRatingLabel.pack()

        for i in range(1,6):
            rb = tkinter.Radiobutton(self.ratingFrame, text=str(i), variable= self.ratingVar, value=i, font=('Arial', 12))
            rb.pack(side='left', padx=5)

        self.submitButton = tkinter.Button(self.ratingFrame, text ='submit', command=self.rateJoke,font = ('Arial',12))
        self.submitButton.pack(side='left')

       

        try:
            f = open("data.txt", "r")
            print("File successfully opened")
            self.data = json.load(f)
            print("Data successfully loaded")
            f.close()
        except (FileNotFoundError, json.JSONDecodeError):
            tkinter.messagebox.showerror("Missing/Invalid file", "The data file is missing or contains invalid JSON.")
            self.main.destroy()

        self.currentJoke = 0
        self.allJokesRated = False
        self.showJoke()
        self.main.mainloop()

    def showJoke(self):
        if self.currentJoke >= len(self.data):
            self.allJokesRated = True
            tkinter.messagebox.showinfo("End of jokes", "Thank you for rating. \n That was the last joke. \n The program will now end.")
            self.main.destroy()
        else:
            joke = self.data[self.currentJoke]
            self.setupLabel.configure(text=joke['setup'])
            self.punchlineLabel.configure(text='')
            self.punchlineButton.configure(state='normal')
            self.numRatingsLabel.configure(text="")
            self.avgRatingLabel.configure(text="")
            
            self.currentJoke += 1

    def revealPunchline(self):
        joke = self.data[self.currentJoke - 1]
        self.punchlineLabel.configure(text=joke['punchline'])
        self.punchlineButton.configure(state='disabled')

    def rateJoke(self):
        
        try:
            rating = self.ratingVar.get()
        except ValueError:
            tkinter.messagebox.showerror("Invalid rating", "Please enter a valid integer rating (1-5).")
            return

        if rating < 1 or rating > 5:
            tkinter.messagebox.showerror("Invalid rating", "Please enter a rating between 1 and 5.")
            return

        joke = self.data[self.currentJoke - 1]
        joke["numOfRatings"] += 1
        joke["sumOfRatings"] += rating
        average_rating = round(joke["sumOfRatings"] / joke["numOfRatings"], 1)
        self.numRatingsLabel.configure(text=f"Rated {joke['numOfRatings']} time(s)")
        self.avgRatingLabel.configure(text=f"Average rating: {average_rating}/5")

        tkinter.messagebox.showinfo("Thank you " , " Thank you for rating. \n The next joke will appear now.")

        
        self.showJoke()

gui = ProgramGUI()



                                      

