#open in http://www.codeskulptor.org/
# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
player = None
dealer = None
deck = None
cnt = 0
player_burst = False
dealer_burst = False
player_win = False
dealer_win = False

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        ret = "Hand contains "
        for i in self.cards:
            ret += i.get_suit() + i.get_rank() + " "
        return ret
    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        ret = 0
        have_ace = False
        for i in self.cards:
            if i.get_rank() == "A":
                have_ace = True
            ret += VALUES[i.get_rank()]
        if ret <= 11 and have_ace:
            ret += 10
        return ret
   
    def draw(self, canvas, pos):
        for i in range(0, len(self.cards)):
            if i >= 5:
                break;
            self.cards[i].draw(canvas, [pos[0] + i * 80, pos[1]])

 
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        self.i = 0
        for i in SUITS:
            for j in RANKS:
                self.cards.append(Card(i, j))

    def shuffle(self):
        random.shuffle(self.cards)
        self.i = 0

    def deal_card(self):
        ret = self.cards[self.i]
        self.i += 1
        return ret
    
    def __str__(self):
        ret = "Deck contains " 
        for i in self.cards:
            ret += str(i) + " "
        return ret



#define event handlers for buttons
def deal():
    global cnt, outcome, in_play, player, dealer, deck, dealer_win
    if in_play:
        print "player lose"
        dealer_win = True
        cnt -= 1
        return
    player = Hand()
    dealer = Hand()
    deck = Deck()
    deck.shuffle() 
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())  
    in_play = True
    player_burst = False
    dealer_burst = False
    player_win = False
    dealer_win = False

def hit():
    global in_play, cnt, player_burst
    if in_play:
        player.add_card(deck.deal_card())
        if player.get_value() > 21:
            player_burst = True
            print "player burst"
            cnt -= 1
            in_play = False
       
def stand():
     global cnt, in_play, player_burst, dealer_burst, player_win, dealer_win
     player_burst = False
     dealer_burst = False
     player_win = False
     dealer_win = False
     if player.get_value() > 21:
        print "player burst"
        player_burst = True
        cnt -= 1
     
     if dealer.get_value() < 17:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())

     
     if dealer.get_value() > 21:
        print "dealer burst"
        dealer_burst = True
        cnt += 1
       
     if player.get_value() > dealer.get_value():
            player_win = True
            print "player"
            cnt += 1
     else:
            dealer_win = True
            print "dealer"
            cnt -= 1
     in_play = False

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global player_burst, dealer_burst, player_win, dealer_win
    canvas.draw_text('Blackjack', (30, 80), 60, 'Blue')
    canvas.draw_text("Score " + str(cnt), (500, 80), 25, 'Red')
    canvas.draw_text('Dealer', (30, 150), 25, 'Black')
    if player_burst:
        canvas.draw_text('you burst', (300, 150), 25, 'Black')
    elif dealer_burst:
        canvas.draw_text('dealer burst', (300, 150), 25, 'Black')
    elif player_win:
        canvas.draw_text('you win', (300, 150), 25, 'Black')
    elif dealer_win:
        canvas.draw_text('dealer win', (300, 150), 25, 'Black')
    else:
        canvas.draw_text('', (300, 150), 25, 'Black')
    dealer.draw(canvas, [50, 200])
    canvas.draw_text('Player', (30, 350), 25, 'Black')
    
    if in_play:
        canvas.draw_text('Hit or stand?', (300, 350), 25, 'Black')
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                          [50 + CARD_BACK_CENTER[0], 200 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)

    else:
        canvas.draw_text('New deal?', (300, 350), 25, 'Black')
    player.draw(canvas, [50, 400])
    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric