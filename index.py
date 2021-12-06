from termcolor import colored
import os
import random

def start():
    print(colored("""
Hangman for Windows
===================
1. Start
2. Exit
    """, "cyan"))
    mainMenuInput = input("> ")
    if mainMenuInput not in ["1", "2"]: return
    if mainMenuInput == "2": return

    wordObject = random.choice(randomWords)

    wordObject["word"] = wordObject["word"].lower()
    
    resultOfGame = playHangman(wordObject)
    clearConsole()
    if resultOfGame == True:
        print(colored(f"""
Congratulations! You passed!
The word was '{wordObject["word"]}'.

Press ENTER to exit the program. If you want to play again, restart the program.
        """, "green"))
    else:
        print(colored(f"""
You have failed.
The word was '{wordObject["word"]}'.

Press ENTER to exit the program. If you want to play again, restart the program.
        """, "red"))   
    input() 


def generateHangedMan(attempt):
    toReturn = ""
    if attempt == 9:
        toReturn = """










------
        """
    elif attempt == 8:
        toReturn = """
  |
  |
  |
  |
  |
  |
  |
  |
  |
  | 
------
        """    
    elif attempt == 7:
        toReturn = """
  |------
  |
  |
  |
  |
  |
  |
  |
  |
  |   
------
        """ 
    elif attempt == 6:
        toReturn = """
  |------
  |     |
  |
  |
  |
  |
  |
  |
  |
  |
------
        """
    elif attempt == 5:
        toReturn = """
  |------
  |     |
  |   ----
  |  |    |
  |   ----
  |
  |
  | 
  |
  |  
------
        """
    elif attempt == 4:
        toReturn = """
  |------
  |     |
  |   ----
  |  |    |
  |   ----
  |     |
  |     |
  |     |
  |
  |   
------
        """
    elif attempt == 3:
        toReturn = """
  |------
  |     |
  |   ----
  |  |    |
  |   ----
  |     |
  |    \|/
  |     |
  |
  |   
------
        """
    elif attempt == 2:
        toReturn = r"""
  |------
  |     |
  |   ----
  |  |    |
  |   ----
  |     |
  |    \|/
  |     |
  |    / \
  |   
------
        """
    elif attempt == 1:
        toReturn = colored("""
 .----------------. .----------------. .----------------. .----------------. 
| .--------------. | .--------------. | .--------------. | .--------------. |
| |  ________    | | |  _________   | | |      __      | | |  ________    | |
| | |_   ___ `.  | | | |_   ___  |  | | |     /  \     | | | |_   ___ `.  | |
| |   | |   `. \ | | |   | |_  \_|  | | |    / /\ \    | | |   | |   `. \ | |
| |   | |    | | | | |   |  _|  _   | | |   / ____ \   | | |   | |    | | | |
| |  _| |___.' / | | |  _| |___/ |  | | | _/ /    \ \_ | | |  _| |___.' / | |
| | |________.'  | | | |_________|  | | ||____|  |____|| | | |________.'  | |
| |              | | |              | | |              | | |              | |
| '--------------' | '--------------' | '--------------' | '--------------' |
 '----------------' '----------------' '----------------' '----------------' 
""", "red")

    if attempt != 1:
        toReturn = colored(toReturn, "yellow")
    return toReturn    

    

def playHangman(wordObject):
    toReturn = False
    hangedMan = ""
    wordAnswer = []

    for x in wordObject["word"]:
        wordAnswer.append("_")
    
    clearConsole()

    attemptsRemaining = 9
    remainingLetters = []
    for x in wordObject["word"]:
        remainingLetters.append(x)

    word = list(wordObject["word"].lower())

    while attemptsRemaining > 0:
        clearConsole()
        if len(remainingLetters) == 0:
            break

        print(f"""
{hangedMan}
-----
{colored("Hint: " + wordObject["hint"], "yellow")}
{colored("Attempts remaining: " + str(attemptsRemaining), "yellow")}
-----
{wordAnswer}

{colored("Enter ONLY ONE letter.", "cyan")}
            """)
        letterInput = input("> ")
        if letterInput.lower() in remainingLetters:
            firstIndexOfLetterInWord = word.index(letterInput.lower())
            wordAnswer[firstIndexOfLetterInWord] = letterInput.lower()
            word[firstIndexOfLetterInWord] = word[firstIndexOfLetterInWord] + "-"
            remainingLetters.remove(letterInput.lower())
        else:
            hangedMan = generateHangedMan(attemptsRemaining)
            attemptsRemaining = attemptsRemaining - 1


    if len(remainingLetters) == 0 and attemptsRemaining > 0:
        return True
    else:
        return False
   

if __name__ == "__main__":
    os.system("color")
    clearConsole = lambda: os.system("cls")
    randomWords = [
       
        {
            "word": "Banana",
            "hint": "monke eat"
        },
        {
            "word": "Apple",
            "hint": "common red fruit"
        }
    ]
    start()    
    
