# Multiple Choice
Question1 = "What is the oldest anime? \n a) One Piece  \n b) Naruto  \n c) Doraemon  \n d) Dragon Ball Z  \n e) Sazae-san\n"
# The answer is e)

Question2 = """When did One piece first air
\n a) 1998  \n b) 1997 \n c) 1996 \n d) 1999  \n e) 1995\n"""
# The answer is d)

# Numerical Response
Question3 = "How many pokemon are there as currently?"
# The answer is 802

Question4 = "How many members are there in the Akatsuki in Naruto"
# The answer is 10


# True/False
Question5 = """Avatar is considered an anime?"""
# True

questions_wrong = list()
questions_right = list()
score = 0


def multiple_choice_question(question, answer):
    print(question)
    user_answer = input("Input a choice (a-e): \n").lower()
    if user_answer == answer:
        print("You are correct!")
        global score
        score +=1
        questions_right.append("question 1 was right")
        return 1
    else:
        print("Incorrect, The answer is: ", answer)
        score -=1
        questions_wrong.append("question 1 was wrong")
        return 0


def multiple_choice_questions(question, answer):
    print(question)
    user_answer = input("Input a choice (a-e): \n").lower()
    if user_answer == answer:
        print("You are correct!")
        global score
        score +=1
        questions_right.append("question 2 was right")
        return 1
    else:
        print("Incorrect, The answer is: ", answer)
        score -=1
        questions_wrong.append("question 2 was wrong")


def numerical_question(question, answer):
    print(question)
    user_answer = input("Input a number: \n")
    if user_answer == answer and user_answer.isdigit():
        print("You are correct!")
        global score
        score +=1
        questions_right.append("question 3 was right")
        return 1
    # elif user_answer == answer and user_answer.isdigit == False:
    #     print("Inproper format")
    else:
        print("Incorrect, The answer is: ", answer)
        score -=1
        questions_wrong.append("question 3 was wrong")
        return 0



def numerical_questions(question, answer):
    print(question)
    user_answer = input("Input a number: \n")
    if user_answer == answer and user_answer.isdigit():
        print("You are correct!")
        global score
        score +=1
        questions_right.append("question 4 was right")
        return 1
    # elif user_answer == answer and user_answer.isdigit == False:
    #     print("Inproper format")
    else:
        print("Incorrect, The answer is: ", answer)
        score -=1
        questions_wrong.append("question 4 was wrong")
        return 0



def true_false_question(question, answer, fact):
    print(question)
    user_answer = input("Enter True(t) or False(f): \n").lower()
    if user_answer == answer:
        print("You are correct!")
        global score
        score +=1
        questions_right.append("question 5 was right")
        return 1
    else:
        print("Incorrect, The answer is: ", answer, '\n', fact)
        score -=1
        questions_right.append("question 5 was wrong")
        return 0



def summary():
    print("Your final score is " + str(score) + " out of 5")
    if score == 4:
        print("You are a rising weeb")

    elif score == 5:
        print("You are a full fledge weeb")
    else:
        print("You're not a weeb at all \n")



    if questions_wrong == 0:
        print("                 ")
        print(questions_right)



def anime_quiz():
    print("Quiz time! Let's test your knowledge of anime\n")
    multiple_choice_question(Question1, 'e')
    multiple_choice_questions(Question2, 'd')
    numerical_question(Question3, '802')
    numerical_questions(Question4, '10')
    true_false_question(Question5, 't', 'Its only considered an cartoon')
    summary()




if __name__ == "__main__":
    playing = True
    while playing:
        anime_quiz()
        play_again = input("Would you like to retake this quiz? Enter y or n\n".lower())
        if play_again == "y":
            questions_wrong = list()
            questions_right = list()
            score = 0
            anime_quiz()
        else:
            playing = False
