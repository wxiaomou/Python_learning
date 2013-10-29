# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# initialize global variables used in your code
secret_num = -1
attempt_num = 0
range = 100


# helper function to start and restart the game
def new_game():   
    """start a new game with same range"""
    global secret_num
    global attempt_num
    if range == 100:
        range100()
    else:
        range1000()




# define event handlers for control panel
def range100():    
    """button that changes range to range [0,100) and restarts"""
    global secret_num
    global attempt_num
    global range
    range = 100
    secret_num = random.randrange(0, 100)
    attempt_num = 7
    print ""
    print "Range is 100, Start!"
   # print secret_num


def range1000():
    """button that changes range to range [0,1000) and restarts"""
    global secret_num
    global attempt_num
    global range
    range = 1000
    secret_num = random.randrange(0, 1000)
    attempt_num = 10
    print ""
    print "Range is 1000, Start!"
  #  print secret_num

    
def input_guess(guess):
    """get the input and print according message"""
    global attempt_num
    
    try:	
        x = int(guess)
        print "guess is " + guess
    except ValueError:
        print "input is not valid number"
        new_game()
        return
    
    if x == secret_num:
        print "Correct"
        new_game()
        return
    elif x > secret_num:
        print "Higher"
    else:
        print "Lower"
   
    attempt_num = attempt_num - 1
    print attempt_num, " attempts left"
    print ""
    
    if attempt_num <= 0:
       print "No more attempt"
       print "correct number is ", secret_num
       new_game()
       return

    
# create frame
f = simplegui.create_frame("Guess the number", 300, 300)


# register event handlers for control elements
f.add_button("Range [0, 100)", range100, 200)
f.add_button("Range [0, 1000)", range1000, 200)
f.add_input("Your Guess", input_guess, 200)

# call new_game and start frame

new_game()
f.start()

# always remember to check your completed program against the grading rubric
