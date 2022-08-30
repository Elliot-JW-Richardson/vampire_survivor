import pandas as pd
import numpy as np
import environment
import cv2
import csv
import time
import sys


def screen_setup():
    start_pos = [940, 680]

    character_pos = np.array(([680, 300],
                              [885, 300],
                              [1060, 300],
                              [1250, 300],
                              [680, 520],
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

    with open('training_data.csv', newline='') as f:
        reader = csv.reader(f)
        i=0
        for row in reader:
            if len(row)>0:
                try:
                    i+=1
                    button = row[0]
                    frame = np.array(row[1:]).reshape((540, 840, 1)).astype(np.uint8)
                    cv2.imshow('screen', frame)
                    print(button)
                    time.sleep(0.5)
                except Exception as e:
                    print(e)

            if cv2.waitKey(1) == ord('q'):
                cv2.destroyAllWindows()
                break