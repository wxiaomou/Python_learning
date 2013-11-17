# implementation of card game - Memory

import simplegui 
import random 

mem_list = []
expose = []
cur = []
state = 0
turns = 0

# helper function to initialize globals
def new_game():
    global mem_list, expose
    mem_list = []
    expose = []
    turns = 0
    for i in xrange(0, 8):
        mem_list.append(i)
        expose.extend((False, False))      
    mem_list += mem_list
    random.shuffle(mem_list)

def dist(pos):
    return pos[0] / 50 + 1
    
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, expose, cur, turns
    index = dist(pos)
    if expose[index - 1]:
        return
    expose[index - 1] = True
    if state == 0:
        state = 1
        cur.append(index - 1)     
    elif state == 1:
        state = 2
        cur.append(index - 1)
        if (mem_list[cur[0]] == mem_list[cur[1]]):
            turns += 1
            label.set_text("Turns = " + str(turns))
    else:
        if (mem_list[cur[0]] != mem_list[cur[1]]):
            expose[cur[0]] = False
            expose[cur[1]] = False
        cur = []
        cur.append(index - 1)
        state = 1

    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    j = 0
    for i in mem_list:
        canvas.draw_text(str(i), [j * 50 + 20, 55], 30, "White")
        j += 1
    j = 0
    for i in expose:
        if not i:
            canvas.draw_polygon([[j * 50, 0], [(j + 1) * 50, 0], [(j + 1) * 50 , 100], [j * 50, 100]],
                                2, 'Green', 'Black')
        j += 1
    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric