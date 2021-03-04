import binascii
import pdb

s1 = '1c0111001f010100061a024b53535009181c'
s2 = '3a'
#pdb.set_trace()
bin_s1 = binascii.unhexlify(s1) #s1.decode("hex") 
bin_s2 = binascii.unhexlify(s2) #s2.decode("hex") 

def xor_strings(xs, ys):
    return binascii.hexlify("".join(chr(ord(x) ^ ord(ys)) for x in xs))

xored = xor_strings(bin_s1, bin_s2)
print xored
