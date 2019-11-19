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


score = 0



def multiple_choice_question(question, answer):
    print(question)
    user_answer = input("Input a choice (a-e): \n").lower()
    if user_answer == answer:
        print("You are correct!")
        global score
        score +=1
        print (score)
        return 1
    else:
        print("Incorrect, The answer is: ", answer)
        return 0


def numerical_question(question, answer):
    print(question)
    user_answer = input("Input a number: \n")
    if user_answer == answer and user_answer.isdigit():
        print("You are correct!")
        global score
        score +=1
        print (score)
        return 1
    # elif user_answer == answer and user_answer.isdigit == False:
    #     print("Inproper format")
    else:
        print("Incorrect, The answer is: ", answer)
        return 0

def true_false_question(question, answer, fact):
    print(question)
    user_answer = input("Enter True(t) or False(f): \n").lower()
    if user_answer == answer:
        print("You are correct!")
        global score
        score +=1
        print (score)
        return 1
    else:
        print("Incorrect, The answer is: ", answer, '\n', fact)
        return 0


multiple_choice_question(Question1, 'e')
multiple_choice_question(Question2, 'd')

numerical_question(Question3, '802')
numerical_question(Question4, '10')

true_false_question(Question5, 't', 'Its only considered an cartoon')

print("Your total score is " + str(score) + " out of 5")
