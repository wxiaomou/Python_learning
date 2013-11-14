# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    """spawn a new ball"""
    global ball_pos, ball_vel # these are vectors stored as lists
    #ball origin in the middle of the canvas
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    #initial velosity
    hor = random.randrange(150, 240) / 80
    vet = random.randrange(60, 180) / 80
    #decide direction of the ball
    if (direction):
        ball_vel = [hor, -vet]
    else:
        ball_vel = [-hor, -vet]


# define event handlers
def new_game():
    """start a new game"""
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = HEIGHT / 2 
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    spawn_ball(LEFT)

def draw(c):
    "draw, ball paddle and score"
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle2_vel
    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    #horizontal
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if (ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT and
            ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT):
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
        else:
            spawn_ball(RIGHT)
            score2 += 1
        
    if ball_pos[0] >= WIDTH - 1 - PAD_WIDTH - BALL_RADIUS:
        if (ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT and
            ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT):
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
        else:
            spawn_ball(LEFT)
            score1 += 1
    #vertical 
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    if ball_pos[1] >= HEIGHT - 1 - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_vel > 0):
        if (paddle1_pos + HALF_PAD_HEIGHT <= HEIGHT - 1):
            paddle1_pos += paddle1_vel
    else:
        if (paddle1_pos - HALF_PAD_HEIGHT >= 0):
            paddle1_pos += paddle1_vel
          
            
    if (paddle2_vel > 0):
        if (paddle2_pos + HALF_PAD_HEIGHT <= HEIGHT - 1):
            paddle2_pos += paddle2_vel
    else:
        if (paddle2_pos - HALF_PAD_HEIGHT >= 0):
            paddle2_pos += paddle2_vel
            
    # draw paddles
    c.draw_polygon([[0, paddle1_pos + HALF_PAD_HEIGHT],
                    [PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT],
                    [PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT],
                    [0, paddle1_pos - HALF_PAD_HEIGHT]],
                    1, "white", "white")
    c.draw_polygon([[WIDTH - PAD_WIDTH - 1, paddle2_pos + HALF_PAD_HEIGHT],
                    [WIDTH - 1, paddle2_pos + HALF_PAD_HEIGHT],
                    [WIDTH - 1, paddle2_pos - HALF_PAD_HEIGHT],
                    [WIDTH - PAD_WIDTH - 1, paddle2_pos - HALF_PAD_HEIGHT]],
                    1, "white", "white")
    # draw scores
    c.draw_text(str(score1), [150, 70], 30, "yellow")
    c.draw_text(str(score2), [450, 70], 30, "yellow")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 2
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -2
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 2
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -2
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if (key == simplegui.KEY_MAP["w"] or
       key == simplegui.KEY_MAP["s"]):
        paddle1_vel = 0
    elif (key == simplegui.KEY_MAP["down"] or
         key == simplegui.KEY_MAP["up"]):
        paddle2_vel = 0
   


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("restart", new_game)


# start frame
new_game()
frame.start()
