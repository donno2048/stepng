# stepng

Encode data into photos

## install

From Pypi:

`python -m pip install stepng`

From GitHub:

`python -m pip install git+https://github.com/donno2048/stepng`

## Usage

From the CLI:

```bash
usage: python -m stepng [-h] -k  (-e | -d)

Encrypt your data in photos

optional arguments:
  -h, --help     show this help message and exit
  -k, --key      Key to encrypt with ("password")
  -e, --encrypt  Create a new image
  -d, --decrypt  Decrypt an existing image
```

Or in Python:

```py
from stepng import encrypt, decrypt
encrypt(100)
decrypt(100)
```
