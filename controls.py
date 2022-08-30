import numpy as np
import pyautogui


def clicker(location):
    pyautogui.click(location[0],location[1])


def random_picker(positions):
    entries = positions.shape[0]
    selection = np.random.randint(entries, size=1)
    clicker(positions[selection][0])
