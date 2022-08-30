import cv2
import numpy as np
import pyautogui
import time
import controls



def screengrabber(trim=0, display=False, fps=None, resize=100, grey=False):
    screenshot = pyautogui.screenshot()
    cv_img = np.array(screenshot)
    if grey:
        cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
    else:
        cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    if trim >0:
        cv_img = cv_img[0:int(cv_img.shape[0]), trim:int(cv_img.shape[1]-trim)]

    if resize != 100:
        width = int(cv_img.shape[1] * resize / 100)
        height = int(cv_img.shape[0] * resize / 100)
        dsize = (width, height)
        cv_img= cv2.resize(cv_img, dsize)

    if display:
        if fps is not None:
            cv2.putText(cv_img, fps, (7,70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100,255,0), 3, cv2.LINE_AA)
        cv2.imshow('Computer Vision', cv_img)

    return np.atleast_3d(cv_img)


def status_check(live, saved):
    comparison = live==saved
    return comparison.all()

if __name__=='__main__':

    upgrade_pos = np.array(([940, 250],
                            [940, 500],
                            [940, 700]))

    t1=0
    t2=0
    game_over = cv2.imread('C:\\Users\\EjwRi\PycharmProjects\\vampire_survivor\\Gameover.png')
    level_up = cv2.imread('C:\\Users\\EjwRi\PycharmProjects\\vampire_survivor\\Level_Up.png')
    while True:
        t1=time.time()
        fps=str(int(1/(t1-t2)))
        x=screengrabber(trim=120, display=True, fps=fps, resize=50, grey=True)
        t2=time.time()
        #print(x.shape)
        quit_area = x[360:390, 355:485]
        level_area = x[80:120, 340:500]
        box_area = x[415:460, 350:485]
        cv2.imshow('box', box_area)
        #print(status_check(quit_area, game_over))
        if status_check(level_area, level_up):
            controls.random_picker(upgrade_pos)
        if cv2.waitKey(1) == ord('q'):
            cv2.imwrite('images\open_done.png', box_area)
            cv2.destroyAllWindows()
            break
