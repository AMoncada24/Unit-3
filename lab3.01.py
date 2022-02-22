'''
##############
Lab 3.01
##############
1.  Practice importing random** — Use randint with different arguments. Simulate a dice roll, printing out to the user what number they rolled.

2.  Look at the documentation of the random library — Experiment with another function (not randint) that returns a value.

3.  Create a program that simulates a magic 8-ball​
    1.  Store all of the 8-ball's possible responses (shown below) in a list

    2.  Have the program prompt the user to ask the magic 8-ball a question

        then return and print a random response.

Magic 8-Ball Response Examples
Outlook is good

Ask again later

Yes

No

Most likely no

Most likely yes

Maybe

Outlook is not good
'''
import random
answer1 = "Ask again later."
answer2 = "Yes."
answer3 = "No."
answer4 = "Most likely no."
answer5 = "Most likely yes."
answer6 = "Maybe."
answer7 = "Outlook is not good."
answers = [answer1, answer2, answer3, answer4, answer5, answer6, answer7]
question = input("What is your question for the Magic 8-Ball? ")
print(random.choice(answers))
