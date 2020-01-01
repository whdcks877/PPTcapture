import keyboard  # using module keyboard
from PIL import ImageGrab
from PIL import Image

def Capture(cnt):
    img = ImageGrab.grab()
    saves = "C:/Users/whdck/Desktop/Automatic/{}{}".format(cnt, '.png')
    img.save(saves)

def SavePDF(cnt):
    images = []
    for num in range(cnt):
        name = "C:/Users/whdck/Desktop/Automatic/{}{}".format(num, '.png')
        im = Image.open(name)
        images.append(im)
    filename = input("Enter File Name: ")
    Fdir = "C:/Users/whdck/Desktop/Automatic/{}{}".format(filename, '.pdf')
    images[0].save(Fdir, save_all=True, append_images=images[1:], quality = 100)
    print("saved")

def main():
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

                if keyboard.is_pressed('e'):
                    SavePDF(cnt)
                    break
            except:
                break

main()