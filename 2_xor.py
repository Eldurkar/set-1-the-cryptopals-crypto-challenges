#import binascii
import pdb

s1 = '1c0111001f010100061a024b53535009181c'
s2 = '686974207468652062756c6c277320657965'

bin_s1 = s1.decode("hex") #binascii.unhexlify(s1)
bin_s2 = s2.decode("hex") #binascii.unhexlify(s1)

def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

pdb.set_trace()
xored = xor_strings(bin_s1, bin_s2)#.encode("hex")
print xored
