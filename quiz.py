no_of_questions = 4

questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in the earth?: ",
             "How many bones are in the human body?: ",
             "Which planet is the hottest in the solar system?: ")

options = (("A. 116","B. 117","C. 118","D. 118"),
           ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
           ("A. Nitrigen","B. Oxygen","C. lauging gas","D. Hydrogen"),
           ("206","207","08","209"),
           ("A. Mercury","B. Venus","C. Earth","D. Mars"))

answers = ("C","D","A","A","B")
guesses = []
score = 0


question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
 
    guess = input("Enter (A ,B ,C ,D): ").upper()
    if guess == answers[question_num]:
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")

    if guess == answers[question_num]:
        score += 1
    else:
        score = score
    question_num += 1

score = int(score/len(questions) * 100)
print("------------------------")
print(f"RESULT: {score}")
print("------------------------")