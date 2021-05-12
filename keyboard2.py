from gpiozero import Robot
from time import sleep
import os
import curses
 
robby = Robot(left=(20, 21), right=(12, 16))
print('robby initialized')
print('Press q to leave robby')
print('Press p to shutdown robby')
 
robby.forward(.1)
sleep(1)
robby.stop()
 
screen = curses.initscr()
 
curses.noecho()
curses.cbreak()
curses.halfdelay(3)
 
screen.keypad(True)
 
try:
    while True:
 
        char = screen.getch()
        #primt char
        if char == ord('q'):
            break
        if char == ord('p'):
            curses.nocbreak()
            screen.keypad(0)
            curses.echo()
            curses.endwin()
            os.system('sudo halt')
        elif char == curses.KEY_DOWN:
            robby.forward(.6)
        elif char == curses.KEY_UP:
            robby.backward(0.9)
        elif char == curses.KEY_LEFT:
            robby.left(.6)
        elif char == curses.KEY_RIGHT:
            robby.right(0.6)
        else:
            robby.stop()
 
finally:
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
