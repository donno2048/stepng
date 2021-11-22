from tkinter import Tk
from cv2 import imwrite, imread
from argparse import ArgumentParser
from tkinter.simpledialog import askstring
from tkinter.filedialog import askopenfilename, asksaveasfilename
def encrypt() -> None:
    global image, mask0, mask1, x, y, channel
    t = Tk()
    t.withdraw()
    text, image, mask0, mask1, x, y, channel = askstring("Give me a string to encrypt", t), imread(askopenfilename(filetypes = [('PNG files', '*.png')])), 254, 1, 0, 0, 0
    def append(bits: str) -> None:
        global image, mask0, mask1, x, y, channel
        for c in bits:
            val = list(image[y, x])
            if int(c) == 1: val[channel] = int(val[channel]) | mask1
            else: val[channel] = int(val[channel]) & mask0
            image[y, x] = tuple(val)
            channel += 1
            if channel == image.shape[2]:
                channel = 0
                x += 1
                if x == image.shape[1]:
                    x = 0
                    y += 1
                    if y == image.shape[0]:
                        y = 0
                        if mask1 == 128: raise ValueError("Image too small")
                        else:
                            mask0 -= mask1
                            mask1 *= 2
    append(bin(len(text))[2:].zfill(16))
    for char in text: append(bin(ord(char))[2:].zfill(8))
    imwrite(asksaveasfilename(filetypes = [('PNG files', '*.png')]) + ".png", image)
def decrypt() -> None:
    global image, mask0, mask1, x, y, channel
    Tk().withdraw()
    image, mask0, mask1, x, y, channel = imread(askopenfilename(filetypes = [('PNG files', '*.png')])), 254, 1, 0, 0, 0
    def read_next() -> None:
        global image, mask0, mask1, x, y, channel
        val = image[y, x][channel]
        val = int(val) & mask1
        channel += 1
        if channel == image.shape[2]:
            channel = 0
            x += 1
            if x == image.shape[1]:
                x = 0
                y += 1
                if y == image.shape[0]:
                    y = 0
                    if mask1 == 128: raise ValueError("Image too small")
                    else:
                        mask0 -= mask1
                        mask1 *= 2
        if val: return "1"
        return "0"
    print(str().join([chr(int(str().join([read_next() for _ in range(8)]), 2)) for _ in range(int(str().join([read_next() for _ in range(16)]), 2))]))
def main() -> None:
    parser = ArgumentParser(description = 'Encrypt your data in photos')
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('-e', '--encrypt', action = 'store_true', help = 'Create a new image')
    group.add_argument('-d', '--decrypt', action = 'store_true', help = 'Decrypt an existing image')
    args = parser.parse_args()
    if args.encrypt: encrypt()
    elif args.decrypt: decrypt()
