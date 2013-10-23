# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def number_to_name(number):
    """convert nuber to name"""
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "invalud number, number range is 0-4"


def name_to_number(name):
    """convert name to number"""
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "invalide name should be one of Rock, paper, scissors, lizard, Spock"


def rpsls(name):
    """main process, compute the winner"""
    player_number = name_to_number(name)
    if (player_number == None):
        print "wrong palyer_number"
        return
    comp_number = random.randrange(0,4)
    diff = player_number - comp_number
    
    # compute difference of player_number and comp_number modulo five
    
    # use if/elif/else to determine winner
    
    # convert comp_number to name using number_to_name
    
    # print results
    print ""
    print "Player chooses " + name
    print "Computer chooses " + number_to_name(comp_number)
    diff %= 5
    if diff == 0:
        print "Player and computer tie!"
    elif diff > 0 and diff < 3:
        print "Player wins!"
    else:
        print "Computer wins!"

# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

