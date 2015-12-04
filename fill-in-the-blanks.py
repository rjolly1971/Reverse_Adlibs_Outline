# I am giving credit where credit is due.  SaltedC's code really helped me with the envisioned
# solution that I really wanted to develop.  In addition to Udacity, I have been
# using "Learn Python The Hardway" to learn Python.  The lesson on lists, dictionaries,
# and tuples were helpful but there were no examples that really tied everything together.
# I have a DB background so I am used to tables, stored procedures and SQL scripts.
# My goal was to develop a solution that uses the power of dictionaries and lists
# in order to have prompts to give the user hints to each question.
# I was going for a program that shows "user empathy".

# For over a month, I have searched for lesson samples and documentation
# to help me achieve this objective.
# I really cannot put into words, how helpful SaltedC's model was to help me understand
# the power of combining different dictionaries together to build arrays.  His solution
# allowed me to embellish and put in what I really wanted to achieve. Most importantly,
# it really helped me to learn Python. I was very close to giving up to just build a bare bones solution.
# I am so glad that that I was patient. Cheers to SaltedC!

# https://github.com/SaltedC/reverse_madlibs/blob/master/reverse_madlibs.py

from sys import exit
import random

#source for questions come from:
# http://www.openbookproject.net/books/bpp4awd/index.html
# https://en.wikibooks.org/wiki/A_Beginner%27s_Python_Tutorial
# http://www.tutorialspoint.com/python/python_loop_control.htm


easyArray = {'questionString':
'__1__ is a widely used general purpose, high level, object oriented programming \n'
'language which is named after __2__. Compared to languages like Java or C++, __1__ \n'
'uses whitespace instead of keywords or curly brackets to delimit blocks.  __1__ was \n'
'originally developed and written by __3__ in 1996 and its __4__ are considered to be \n'
'similar to C and Java.\n',
'questions': {
'q1': {'blank': '__1__', 'value': 'Python',},
'q2': {'blank': '__2__', 'value': 'Monty Python'},
'q3': {'blank': '__3__', 'value': 'Guido van Rossum'},
'q4': {'blank': '__4__', 'value': 'functions'}
  } ,'prompts':{
    'p1': {'hint': '\nQ1. Your choices are: Viper, Python, Mamba, Anaconda'},
    'p2':  {'hint': '\nQ2. Your choices are: Monty Python, Monty Hall, Pythagoras, Cold Play'},
     'p3': {'hint': '\nQ3. Your choices are: Cher, Bono, Guido van Rossum, Lady Gaga'},
     'p4': {'hint': '\nQ4. Your choices are: disciplines, functions, variables, intersections'},
}}

mediumArray = {
'questionString': 'With __1__ loops you can use one or more loops inside another \n'
'while Loop control statements change execution from its normal sequence. \n'
'The __2__ loop repeats a statement or group of statements __2__ a given \n'
'condition is true. It tests the condition before executing the loop body. \n'
'With __3__ loops, one can use additional loops to operate instruction sets based \n'
'on the respective conditions.  The __4__ statement terminates the loop statement \n'
'and transfers execution to the statement immediately following the loop. The \n'
'__5__ statement in Python returns the control to the beginning of the while loop.\n'
'The continue statement rejects all the remaining statements in the current iteration\n'
'of the loop and moves the control back to the top of the loop The __6__ statement \n'
'in Python is used when a statement is required syntactically but you do not want \n'
'any command to execute. The __6__ statement is a __7__ operation; __8__ happens \n'
'when it executes.  __6__ is also useful in places where your code will eventually \n'
'go, but has not been written yet (e.g., in stubs for example).',
  'questions': {
  'q1': {'blank': '__1__', 'value': 'for'},
  'q2': {'blank': '__2__', 'value': 'while'},
  'q3': {'blank': '__3__', 'value': 'nested'},
  'q4': {'blank': '__4__', 'value': 'break'},
  'q5': {'blank': '__5__', 'value': 'continue'},
  'q6': {'blank': '__6__', 'value': 'pass'},
  'q7': {'blank': '__7__', 'value': 'null'},
  'q8': {'blank': '__8__', 'value': 'nothing'}
  }, 'prompts':{
    'p1':{'hint': '\nQ1. Hints: for, nested, fruit, while'},
    'p2':{'hint': '\nQ2. Hints: while, hula, infinate, for'},
    'p3':{'hint': '\nQ3. Hints: while, for, nested, loopty'},
    'p4':{'hint': '\nQ4. Hints: broken, break, nasty, honest'},
    'p5':{'hint': '\nQ5. Hints: continue, pass, master, freaky'},
    'p6':{'hint': '\nQ6. Hints: pass, continue, break, ssss'},
    'p7':{'hint': '\nQ7. Hints: null, empty, souless, serious'},
    'p8':{'hint': '\nQ8. Hints: doody, nothing, everything, something'}
}

    }


difficultArray= {'questionString':
'Sequence Data: Integers and floats are __1__ which means they hold numbers. We can \n'
'use the numeric operators  to form numeric expressions. The Python interpreter can then \n'
'evaluate these expressions to produce numeric values making Python a very powerful __2__. \n'
'Strings, lists, and tuples are all __3__, so called because they behave like a __4__ - an \n'
'ordered collection of objects. Sequence types are qualitatively different from numeric \n'
'types because they are __5__ data types. Meaning they are made up of smaller pieces. \n'
'In the case of strings, they are made up of smaller strings, each containing one __6__. \n'
'There is also the __7__ string, containing no characters at all. In the case of lists or \n'
'tuples, they are made up of __8__, which are values of any Python datatype, including \n'
'other lists and tuples. __9__ are enclosed in square brackets ([ and ]) and __10__ in \n'
'parentheses (( and )).\n',

'questions': {
  'q1': {'blank': '__1__', 'value': 'numeric types'},
  'q2': {'blank': '__2__', 'value': 'calculator'},
  'q3': {'blank': '__3__', 'value': 'sequence types'},
  'q4': {'blank': '__4__', 'value': 'sequence'},
  'q5': {'blank': '__5__', 'value': 'compound'},
  'q6': {'blank': '__6__', 'value': 'character'},
  'q7': {'blank': '__7__', 'value': 'empty'},
  'q8': {'blank': '__8__', 'value': 'elements'},
  'q9': {'blank': '__9__', 'value': 'lists'},
  'q10': {'blank': '__10__', 'value': 'tuples'}
   },'prompts':{
    'p1': {'hint': '\nQ1. Hints: not my type, numeric types, interesting types'},
    'p2': {'hint': '\nQ2. Hints: calculator, snake, brand'},
    'p3': {'hint': '\nQ3. Hints: boring types, iterative types, sequence types'},
    'p4': {'hint': '\nQ4. Hints: sequence, pattern, dirty old man'},
    'p5': {'hint': '\nQ5. Hints: multiplication, compound, derivative'},
    'p6': {'hint': '\nQ6. Hints: letter, number, character'},
    'p7': {'hint': '\nQ7. Hints: nonsense, null, empty'},
    'p8': {'hint': '\nQ8. Hints: elements, stuff, containers'},
    'p9': {'hint': '\nQ9. Hints: dirty laundry, boxes, lists'},
    'p10': {'hint': '\nQ10. Hints: tuples, lists, dictionaries'}}
   }


#lists of the variable to call the game level.
levelsArray= [easyArray, mediumArray, difficultArray]


#list of potential random resonses. South Park Humor.
correct_responses= [
'You know your Python, Friend!',
'Way to go, Guy!',
'Nice Job, Buddy!'
]



#South Park Humor. Random response generator
incorrect_responses = [
'Try again, Guy!',
'Incorrect, Buddy!',
'Give it another go, Friend!']

#Meet and greet.
def start_game():
    name = raw_input("What is your name?")
    print ""
    print "Welcome to the exciting game of REVERSE MADLIBS,", name
    playGame(levelsArray)



#This function asks for the level of difficulty so that it can set up the
#question string, hints, and anwser key for the player.  The arguments are then
#passed on to the function getAnswer().
def getlevel(levelsArray):
    level= raw_input("Please choose level of difficulty \n Easy, Medium, Difficult >>").lower()
    if level == "easy":
        questionString = levelsArray[0]['questionString']
        qArray = levelsArray[0]['questions']
        pArray = levelsArray[0]['prompts']
    elif level == "medium":
        questionString = levelsArray[1]['questionString']
        qArray = levelsArray[1]['questions']
        pArray = levelsArray[1]['prompts']
    elif level == "difficult":
        questionString = levelsArray[2]['questionString']
        qArray = levelsArray[2]['questions']
        pArray = levelsArray[2]['prompts']
    return questionString, qArray, pArray
    print len(qArray)
    #playGame()


# This function loops through the questions with the respective hints depending
# on the game level chosen.  Each question is then given a random correct or
# incorrect response.  The player gets 3 changes to answer correctly
def getAnswer(questionString, question, prompts):
    print questionString
    n=0
    while n<3:
        print prompts['hint']
        user_input = raw_input('What goes in blank ' + question['blank'] + '?')
        if user_input.lower() == question['value'].lower():
            questionString= questionString.replace(question['blank'], question['value'].upper())
            print ""
            print random.choice(correct_responses)
            print ""
            return questionString
        else:
            print ""
            print random.choice(incorrect_responses)
            print ""
        n=n+1
    print "The answer is " + str(question['value']).upper()
    questionString = questionString.replace(question['blank'], question['value'].upper())
    return questionString

def playGame(levelsArray):
# asks for level, cycles through questions for that level
# if the question is not answered in 3 chances the program give the player a
# charity answer and moves on to the next question.
  questionString, qArray, pArray = getlevel(levelsArray)
  x = 0
  while x < len(qArray):
    questionString = getAnswer(questionString, qArray['q' + str(x + 1)], pArray['p' + str(x + 1)])
    x += 1
  print questionString
  print 'Great!  You finished the game!'
  playAgain()

def playAgain():
#asks user if he/she would like to play another round at a new level or exit.
#if yes then the playGame function is called to prompt level choices.
    print "You have finished this level"
    userprompt = raw_input("Would you like to play again?").lower()
    if userprompt.lower()=="yes".lower():
        print playGame(levelsArray)
    elif userprompt.lower() =="no":
        goodbye()
    else:
        userprompt = raw_input("Sorry, did not get that. Would you like to play again?")
        playAgain()

def goodbye():
    print""
    print "Thanks for playing,"
    print "Now, go out and play!!"
    exit() #stops program


#print playGame(levelsArray)
start_game()
