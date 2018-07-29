# Vigenère

This repository provides a Python module that implements a simple [Vigenère cipher](https://en.wikipedia.org/wiki/Vigenère_cipher) based on [this comment](https://gist.github.com/dssstr/aedbb5e9f2185f366c6d6b50fad3e4a4#gistcomment-2310478).

## Usage

The `encrypt` and `decrypt` functions defined in `vigenere.py` are wrappers for `transform`.
For example, running

```python
from vigenere import *

t = "Hello world!"
k = "Key"
e = encrypt(t, k)
d = decrypt(e, k)

print(e)
print(d)
```

prints

```
sKf8UyCUl8Jz
Hello world!
```

to the Python console.
Executing the bash script `launcher` opens a Terminal window with Python and the `vigenere` module preloaded.

## License

All repository content is licensed under the [MIT license](https://github.com/bldavies/vigenere/blob/master/LICENSE).
