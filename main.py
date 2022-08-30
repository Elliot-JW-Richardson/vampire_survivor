import controls
import environment
import numpy as np
import cv2
import time

start_pos = [940,680]

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
open_click = [965, 875]

quit_pos = [960, 740]

t0, t1 = 0, 0

game_over = cv2.imread('images/Gameover.png')
level_up = cv2.imread('images/Level_Up.png')
open_box = cv2.imread('images/open_box.png')
open_done = cv2.imread('images/open_done.png')

env = environment.env(start_pos=start_pos, character_pos=character_pos, confirm_pos=confirm_pos,
                      map_pos=map_pos, upgrade_pos=upgrade_pos, open_pos=open_pos, open_click=open_click,
                      done_pos=done_pos, quit_pos=quit_pos)
epochs = 3

for i in range(epochs):
    while True:
        frame = env.screengrabber(trim=120, resize=50, grey=True)
        env.render(frame)
        quit_area = frame[360:390, 355:485]
        level_area = frame[80:120, 340:500]
        box_area = frame[415:460, 350:485]
        t1 = time.time()
        fps = str(int(1 / (t1 - t0)))
        t0 = time.time()
        print(fps)
        if env.status_check(level_area, level_up):
            controls.random_picker(upgrade_pos)
        if env.status_check(box_area, open_box) or env.status_check(box_area, open_done):
            controls.clicker(env.open_click)
        if env.status_check(quit_area, game_over):
            time.sleep(0.5)
            if i == epochs-1:
                break
            else:
                env.reset()
                break
        t1 = time.time()
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            break