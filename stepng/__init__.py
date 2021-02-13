from argparse import ArgumentParser
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.simpledialog import askstring
def encrypt(key: int) -> None:
    t = Tk()
    t.withdraw()
    text, output = askstring("Give me a string to encrypt", t), [bin(i).replace('0b', '') for i in open(askopenfilename(filetypes = [('PNG files', '*.png')]), 'rb').read()]
    bin_message = [bin(i).replace('0b', '').zfill(8) for i in bytearray(text + '\x00', 'utf8')]
    for i in range(len(bin_message)):
        for j in range(8): output[key + 8 * i + j] = output[key + 8 * i + j][:-1] + bin_message[i][j]
    open(asksaveasfilename(filetypes = [('PNG files', '*.png')]) + '.png', 'wb').write(b''.join([int(i, 2).to_bytes(1, 'big') for i in output]))
def decrypt(key: int) -> None:
    Tk().withdraw()
    response = ''.join([i[-1] for i in [bin(i).replace('0b', '') for i in open(askopenfilename(filetypes = [('PNG files', '*.png')]), 'rb').read()][key:]])
    response = response[:response.find('0' * 8)]
    response = [response[i:i + 8] for i in range(0, len(response), 8)]
    response[-1] += '0' * (8 - len(response[-1]))
    print(''.join([chr(int(i, 2)) for i in response]))
def main() -> None:
    parser = ArgumentParser(description = 'Encrypt your data in photos')
    parser.add_argument('-k', '--key', metavar = '', required = True, type = int, help = 'Key to encrypt with ("password")')
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('-e', '--encrypt', action = 'store_true', help = 'Create a new image')
    group.add_argument('-d', '--decrypt', action = 'store_true', help = 'Decrypt an existing image')
    args = parser.parse_args()
    if args.encrypt: encrypt(args.key)
    elif args.decrypt: decrypt(args.key)
