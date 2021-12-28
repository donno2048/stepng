# stepng

Encode data into photos

## install

tkinter required - installed by default on Windows, on linux (Debian) use this:

```sh
sudo apt-get install python3-tk -y
```

On Linux you may have to run this to use open cv:

```sh
sudo apt-get install ffmpeg libsm6 libxext6 -y
```

### From PyPI

`python -m pip install stepng`

### From GitHub

`python -m pip install git+https://github.com/donno2048/stepng`

## Usage

From the CLI:

```bash
usage: stepng [-h] (-e | -d)

Encrypt your data in photos

optional arguments:
  -h, --help     show this help message and exit
  -e, --encrypt  Create a new image
  -d, --decrypt  Decrypt an existing image
```

Or in Python:

```py
from stepng import encrypt, decrypt
encrypt()
decrypt()
```
