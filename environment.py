import cv2
import numpy as np
import pyautogui
import time
import controls

class env():
    def __init__(self, start_pos, character_pos, confirm_pos, map_pos, upgrade_pos, open_pos, open_click, done_pos, quit_pos):
        self.start_pos = start_pos
        self.character_pos = character_pos
        self.confirm_pos = confirm_pos
        self.map_pos = map_pos
        self.upgrade_pos = upgrade_pos
        self.open_pos = open_pos
        self.open_click = open_click
        self.done_pos = done_pos
        self.quit_pos = quit_pos

    #read the screen, aka observation
    def screengrabber(self, trim=0, resize=100, grey=False):
        screenshot = pyautogui.screenshot()
        cv_img = np.array(screenshot)
        if grey:
            cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
        else:
            cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        if trim > 0:
            cv_img = cv_img[0:int(cv_img.shape[0]), trim:int(cv_img.shape[1] - trim)]
        if resize != 100:
            width = int(cv_img.shape[1] * resize / 100)
            height = int(cv_img.shape[0] * resize / 100)
            dsize = (width, height)
            cv_img = cv2.resize(cv_img, dsize)
        return np.atleast_3d(cv_img)

    #checking if game over or level up
    def status_check(self, img_1, img_2):
        comparison = img_1 == img_2
        return comparison.all()

    #reset the game environment, returning the first image
    def reset(self):
        #click quit
        controls.clicker(self.quit_pos)
        time.sleep(0.5)
        #click done
        controls.clicker((self.done_pos))
        time.sleep(1)
        #click anywhere, click start
        for i in range(2):
            controls.clicker(self.start_pos)
            time.sleep(0.5)
        #select character
        controls.random_picker(self.character_pos)
        time.sleep(0.5)
        #click confirm x2
        for i in range(2):
            controls.clicker(self.confirm_pos)
            time.sleep(0.5)
        #select map
        controls.random_picker(self.map_pos)
        time.sleep(0.5)
        #click confirm x2
        for i in range(2):
            controls.clicker(self.confirm_pos)
            time.sleep(0.5)
        #must return initial observation:
        return self.screengrabber(trim=120, resize=50, grey=True)

    def render(self, img):
        cv2.imshow('Screen', img)