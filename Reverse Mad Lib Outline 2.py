from sys import exit
import random

#All questions are prompted with choices to demonstrate 'user empathy'.

#Introduction section
def start():
    print "-" * 15
    print "What is your name?"
    name = raw_input("> ")
    print "-" * 15
    print "Welcome to this version of Reverse Mad Libs, ", name
    print ""
    print ""
    selection()

#Selection to choose a path.
def selection():
    print "Please choose one of the three options:"
    print "1. Easy, 2. Medium, 3. Difficult"
    choice = raw_input("> ").lower()
    if choice == "1" or choice == "easy":
		easy_1()
    elif choice == "2" or choice == "medium":
		medium_1()
    elif choice == "3" or choice == "difficult":
		difficult()
    else:
        print "Please select a valid response."
        selection()

# questions and answers are set as global variables so that they can be
# called by functions multiple times to reduce code. I was not certain
# if there really was a better way to do this...
easy_question = """
%s is a widely used general purpose, high level,
object oriented programming language which is named after %s.
Compared to languages like Java or C++, %s uses whitespace instead
of keywords or curly brackets to delimit blocks.  %s was originally
developed and written by %s in 1996 and its %s are considered to
be similar to C and Java."""

medium_question = """
To define a function or method in Python, example of proper syntax
would be: %s. Repeated execution of a set of statements is called %s.
Because %s is so common, Python provides language features to make it
easier. One example is with %s and lists which creates a container of
things that are organized in order from first to last.  You can begin
lists by using %s in order to designate the container.  Python then
takes the list and its contents and assigns them to the variable. %s
have the ability to iterate over the items of any sequence. If a
sequence contains an expression it will be evaluated %s.
"""

# answers are set in dictionaries so that attributes can be properly called.
easy_answers= {
        'Q1': 'Python',
        'Q2': 'Monty Python',
        'Q3': 'Guido van Rossum',
        'Q4': 'functions'}

medium_answers = {
        'Q1': 'def example():',
        'Q2': 'iteration',
        'Q3': 'for-loops',
        'Q4': 'square brackets',
        'Q5': 'first'
}

correct_responses = [
"Good going, guy!",
"Way to go, friend!",
"You really know your Python, buddy!"
]

incorrect_responses = [
"Not a good response there, buddy!",
"You need to brush up on your Python, guy!",
"Incorrect guess, Friend!"
]

# The beginning of the code for easy questions.
def easy_1():
    print "-" * 15
    print "You have selected EASY"
    print "-" * 15
    print easy_question % ('__(1)__', '__(2)__',
    '__(1)__','__(1)__','__(3)__','__(4)__')
    print "-" * 15
    choice = False
    while True:
        choice = raw_input(
        "Q1. Your choices are: Viper, Python, Mamba, Anaconda > ").lower()
        if choice == easy_answers['Q1'].lower():
            print random.choice(correct_responses)
            easy_2()
        else:
            print random.choice(incorrect_responses)

def easy_2():
    print easy_question % (easy_answers['Q1'], '__(2)__',easy_answers['Q1'],
    easy_answers['Q1'],'__(3)__','__(4)__' )
    print "-" * 15
    choice = raw_input(
    "Q2. Your choices are: Monty Python, Monty Hall, Pythagoras, Cold Play > ").lower()
    if choice == easy_answers['Q2'].lower():
        print random.choice(correct_responses)
        easy_3()
    else:
        print random.choice(incorrect_responses)
        easy_2()

def easy_3():
    print easy_question % (easy_answers['Q1'], easy_answers['Q2'],easy_answers['Q1'],
    easy_answers['Q1'],'__(3)__','__(4)__' )
    print "-" * 15
    choice = raw_input(
    "Q3. Your choices are: Socrates, Guido Van Rossum, Hedy Lamarr, Augusta Ada King > ").lower()
    if choice == easy_answers['Q3'].lower():
        print random.choice(correct_responses)
        easy_4()
    else:
        print random.choice(incorrect_responses)
        easy_3()

def easy_4():
    print easy_question % (easy_answers['Q1'], easy_answers['Q2'],easy_answers['Q1'],
    easy_answers['Q1'],easy_answers['Q3'],'__(4)__' )
    print "-" * 15
    choice = raw_input(
    "Q4. Your choices are: disciplines, functions, variables, intersections > ").lower()
    if choice == easy_answers['Q4'].lower():
        print random.choice(correct_responses)
        easy_end()
    else:
        print random.choice(incorrect_responses)
        easy_4()
        
def easy_end():
	print "You have completed the easy level"
	print "Do you want to play again? > Yes or No"
	response =raw_input('> ').lower()
	if response =='yes' or response == 'y':
		selection()
	elif response.lower() =='no' or response.lower() =='n':
		exit()
	else:
		print "Sorry, I didn't get that. Please repeat."
		easy_end()
	
        
#--- end of easy questions.

#beginning of the code for the medium level questions.
def medium_1():
    print medium_question % ('__(1)__','__(2)__','__(2)__',
    '__(3)__', '__(4)__', '__(3)__','__(5)__')
    print "-" * 15
    choice = raw_input(
    "Q1. Your choices are: def example!, %def example%, def example():, (def example) > ").lower()
    if choice == medium_answers['Q1'].lower():
        print random.choice(correct_responses)
        medium_2()
    else:
        print random.choice(incorrect_responses)
        medium_1()

def medium_2():
    print medium_question % (medium_answers['Q1'],'__(2)__','__(2)__',
    '__(3)__', '__(4)__', '__(3)__','__(5)__')
    print "-" * 15
    choice = raw_input(
    "Q2. Your choices are: iteration, persperation, laceration, intoxication > ").lower()
    if choice == medium_answers['Q2'].lower():
        print random.choice(correct_responses)
        medium_3()
    else:
        print random.choice(incorrect_responses)
        medium_2()

def medium_3():
    print medium_question % (medium_answers['Q1'],medium_answers['Q2'],
    medium_answers['Q2'],'__(3)__', '__(4)__', '__(3)__','__(5)__')
    #note that in the previous statment, I dont know if the code can be reduced further. 
    #I tried and can't. Please provide feedback if possible.
    print "-" * 15
    choice = raw_input(
    "Q3: Your choices are: loopty-loops, for-loops, fruit loops, hula-hoops > ").lower()
    if choice == medium_answers['Q3'].lower():
        print random.choice(correct_responses)
        medium_4()
    else:
        print random.choice(incorrect_responses)
        medium_3()

def medium_4():
    print medium_question % (medium_answers['Q1'],medium_answers['Q2'],
    medium_answers['Q2'],medium_answers['Q3'],'__(4)__', medium_answers['Q3']
    ,'__(5)__')
    print "-" * 15
    choice = raw_input(
    "Q4: Your choices are: square brackets, curly brackets, parentheses > ").lower()
    if choice == medium_answers['Q4'].lower():
        print random.choice(correct_responses)
        medium_5()
    else:
        print random.choice(incorrect_responses)
        medium_4()

def medium_5():
    print medium_question % (medium_answers['Q1'],medium_answers['Q2'],
    medium_answers['Q2'],medium_answers['Q3'],medium_answers['Q4'],
    medium_answers['Q3'],'__(5)__')
    print "-" * 15
    choice = raw_input(
    "Q5: Your choices are: last, next, today, first > ").lower()
    if choice == medium_answers['Q5'].lower():
        print random.choice(correct_responses)
        print "Do you want to play again? > Yes or No"
        response = raw_input('> ').lower()
        if response == 'yes' or response == 'y':
            selection()
        elif response == 'no' or response == 'n':
            exit()
        else:
            print "Sorry, I didn't get that. Please repeat."
    else:
        print random.choice(incorrect_responses)
        medium_5()
# end of medium level quiz

# start of difficult level


start()

