import csv

import environment
import controls
from pynput import keyboard
import pandas as pd
import time
import cv2
import numpy as np

def on_press(key):
    global df
    global t0
    global t1
    global button
    try:
        button = key.char
    except Exception as e:
        print(e)

def save_state(state, button_pressed):
    _state = state.ravel()
    _state = _state.tolist()
    _state.insert(0, button_pressed)
    return _state

def screen_setup():
    start_pos = [940, 680]

    character_pos = np.array(([680, 300],
                              [885, 300],
                              [1060, 300],
                              [1250, 300],
                              [680, 520],
                              [885, 5200],
                              [1060, 520]))

    confirm_pos = [1250, 1000]

    map_pos = np.array(([720, 290],
                        [720, 450],
                        [720, 600]))

    upgrade_pos = np.array(([940, 250],
                            [940, 500],
                            [940, 700]))

    done_pos = [960, 1010]

    open_pos = [960, 875]

    quit_pos = [960, 740]

    game_over = cv2.imread('C:\\Users\\EjwRi\PycharmProjects\\vampire_survivor\\Gameover.png')
    level_up = cv2.imread('C:\\Users\\EjwRi\PycharmProjects\\vampire_survivor\\Level_Up.png')
    open_box = cv2.imread('C:\\Users\\EjwRi\PycharmProjects\\vampire_survivor\\open_box.png')
    box_done = cv2.imread('C:\\Users\\EjwRi\PycharmProjects\\vampire_survivor\\box_done.png')
    env = environment.env(start_pos=start_pos, character_pos=character_pos, confirm_pos=confirm_pos,
                          map_pos=map_pos, upgrade_pos=upgrade_pos, open_pos = open_pos, done_pos=done_pos, quit_pos=quit_pos)
    return env, level_up, game_over, open_box, box_done, upgrade_pos, open_pos

if __name__ =='__main__':

    #initialise starting dataframes for target value and capturing the frame
    t_cols = ['time', 'frame', 'target']
    df = pd.DataFrame(columns=t_cols)

    button = ''
    t0 = time.time()
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    env, level_up, game_over, open_box, box_done, upgrade_pos, open_pos = screen_setup()


    while True:
        with open('training_data.csv', 'a') as f:
            writer = csv.writer(f)
            t1 = time.time()
            frame = env.screengrabber(trim=120, resize=50, grey=True)

            env.render(frame)
            quit_area = frame[360:390, 355:485]
            level_area = frame[80:120, 340:500]
            open_area = frame[415:460, 345:490]
            #cv2.imshow('Screen', open_area)
            # check if leveling up
            if env.status_check(level_area, level_up):
                controls.random_picker(upgrade_pos)
            # check if box to open
            if env.status_check(open_area, open_box):
                controls.clicker(open_pos)
            # close box
            if env.status_check(open_area, box_done):
                controls.clicker(open_pos)
            # check if game over
            if env.status_check(quit_area, game_over):
                #SAVE THE TWO DATAFRAMES
                writer.writerow(save_state(frame, button))
                break

            writer.writerow(save_state(frame, button))

            button = ''
            if cv2.waitKey(1) == ord('q'):
                cv2.destroyAllWindows()
                break