def new_game():
    
    guesses = []
    correct_guesses = 0
    question = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question-1]:
            print(i)
        guess = input("Enter your choice: ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question += 1

    display_score(correct_guesses, guesses)

# Check the given answer is right or not?
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
#display the score you got in quiz
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULT:")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    if correct_guesses==1:
        print("Poor")
    if correct_guesses==2:
        print("Bad")
    if correct_guesses==3:
        print("Good")
    if correct_guesses==4:
        print("Strong")
    if correct_guesses==5:
        print("Very Strong")

# Here we can restart the game if we want to
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


questions = {
 "Who created Python?: ": "A",
 "What year was Python created?: ": "B",
 "Who won the FIFA World Cup in 2018?: ": "C",
 "In Which year India won the first World Cup: ": "C",
 "Which of the following is a leap year?: " : "B"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Argentina", "B. Spain", "C. France", "D. Germany"],
          ["A. 1975", "B. 1983", "C. 2000", "D. 2009"],
          ["A. 2011","B. 2020","C. 2003","D. 2005"]]

new_game()

while play_again():
    new_game()

print("Byeeeeee!")