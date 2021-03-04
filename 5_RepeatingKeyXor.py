import binascii
def cycle_key(key):
    while True:
        for i in key:
            yield i
def xor_strings(xs, ys):
    xored = "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))
    print binascii.hexlify(xored)
'''
Main
'''
s = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
i1 = cycle_key("ICE")
xor_strings(s, i1)
