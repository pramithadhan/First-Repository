# Name:  Pramitha Dhanraj
# Student Number:  10634467


import random

candidateWords = ['AETHER', 'BADGED', 'BALDER', 'BANDED', 'BANTER', 'BARBER', 'BASHER', 'BATHED', 'BATHER', 'BEAMED', 'BEANED', 'BEAVER', 'BECKET', 'BEDDER', 'BEDELL', 'BEDRID', 'BEEPER', 'BEGGAR', 'BEGGED', 'BELIES', 'BELLES', 'BENDED', 'BENDEE', 'BETTER', 'BLAMER', 'BLOWER', 'BOBBER', 'BOLDER', 'BOLTER', 'BOMBER', 'BOOKER', 'BOPPER', 'BORDER', 'BOSKER', 'BOTHER', 'BOWYER', 'BRACER', 'BUDGER', 'BUMPER', 'BUSHER', 'BUSIER', 'CEILER', 'DEADEN', 'DEAFER', 'DEARER', 'DELVER', 'DENSER', 'DEXTER', 'EVADER', 'GELDED', 'GELDER', 'HEARER', 'HEIFER', 'HERDER', 'HIDDEN', 'JESTER', 'JUDDER', 'KIDDED', 'KIDDER', 'LEANER', 'LEAPER', 'LEASER', 'LEVIED', 'LEVIER', 'LEVIES', 'LIDDED', 'MADDER', 'MEANER', 'MENDER', 'MINDER', 'NEATER', 'NEEDED', 'NESTER', 'PENNER', 'PERTER', 'PEWTER', 'PODDED', 'PONDER', 'RADDED', 'REALER', 'REAVER', 'REEDED', 'REIVER', 'RELIER', 'RENDER', 'SEARER', 'SEDGES', 'SEEDED', 'SEISER', 'SETTER', 'SIDDUR', 'TEENER', 'TEMPER', 'TENDER', 'TERMER', 'VENDER', 'WEDDER', 'WEEDED', 'WELDED', 'YONDER']


def compareWords(word1, word2):
    numMatching = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            numMatching += 1
    return numMatching


wordList = random.sample(candidateWords, 8)
password = random.choice(wordList)
won = False
guessesRemaining = 4


print("Welcome to the Guess The Word Game.")
while guessesRemaining > 0 and not won:

    print("Password is one of these words:")
    for i, word in enumerate(wordList):
        print(i, ".", word)
    print("\nGuesses remaining:", guessesRemaining)

    
    guessNum = int(input("Guess (0-7): "))
    guess = wordList[guessNum]
    print("\nYour guess was:", guess)


    if guess == password:
        print("PASSWORD CORRECT!")
        won = True
    else:
        print("PASSWORD INCORRECT.")
        numMatching = compareWords(guess, password)
        print(numMatching, "letters match the password.\n")
        guessesRemaining -= 1

if won:
    print("\nYOU WIN!")
else:
    print("\nYOU LOST! The password was:", password)



