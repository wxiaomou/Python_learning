# template for "Stopwatch: The Game"

import simplegui
# define global variables
count = 0
interval = 100
position = [110, 150]
attempts = 0
success = 0
running = False
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = 0
    b = 0
    d = t % 10
    t /= 10
    c = t % 10
    t /= 10
    if t > 0:
        a = t / 6
        b = t % 6
    return str(a) + ":" + str(b) + str(c) + "." + str(d)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global running
    timer.start()
    running = True

def stop():
    global attempts, success, running
    timer.stop()
    if running:
        attempts += 1
        if count % 10 == 0:
            success += 1;
    running = False


def reset():
    global count, attempts, success, running
    attempts = 0
    success = 0
    running = False
    timer.stop()
    count = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global count
    count += 1
    print count

# define draw handler
def draw(canvas):
    global running
    canvas.draw_text(format(count), position, 36, "white")
    canvas.draw_text(str(success) + '/' + str(attempts), [260,30], 20, "red")
    if count >= 6000:
        running = False
        stop();
        canvas.draw_text("maximun is 10 mins", [5, 190], 36, "red")
    pass

# create frame
f = simplegui.create_frame("Stop and Watch", 300, 300)

# register event handlers
f.set_draw_handler(draw)
f.add_button("Start", start, 100)
f.add_button("Stop", stop, 100)
f.add_button("Reset", reset, 100)
timer = simplegui.create_timer(interval, timer_handler)


# start frame
f.start()



# Please remember to review the grading rubric
