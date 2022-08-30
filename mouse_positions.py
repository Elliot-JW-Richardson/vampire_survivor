from pynput.mouse import Listener

def on_move(x, y):
    print(f"Mouse moved, x:{x}, y: {y}")

def on_click(x, y, button, pressed):
    print("Mouse clicked")

with Listener(on_move=on_move, on_click=on_click) as listener:
    listener.join()