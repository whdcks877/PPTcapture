import keyboard  # using module keyboard
from PIL import ImageGrab

def Capture(cnt):
    img = ImageGrab.grab()
    saveas = "C:/Users/whdck/Desktop/Automatic/{}{}".format(cnt, '.png')
    img.save(saveas)

cnt = 0
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            Capture(cnt)
            cnt += 1
            while True:
                if not (keyboard.is_pressed('q')):
                    break
    except:
        break