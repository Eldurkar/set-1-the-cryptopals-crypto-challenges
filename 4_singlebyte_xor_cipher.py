import collections
import binascii
import string
'''
function to calculate string score using character frequency as a metric. 
chisquare function
'''
def chisq_score(string1):
    # Populate freq_english dict with frequency of english text
    freq_en = {'A': 8.167, 'B':1.492, 'C':2.782, 'D':4.253, 'E':12.702, \
    'F':2.228, 'G':2.015, 'H':6.094, 'I':6.966, 'J':0.153, 'K':0.772, 'L':4.025, \
    'M':2.406, 'N':6.749, 'O':7.507, 'P':1.929, 'Q':0.095, 'R':5.987, 'S':6.327, \
    'T':9.056, 'U':2.758, 'V':0.978, 'W':2.360, 'X':0.150, 'Y':1.974, 'Z':0.074}
    string1 = list(set(freq_en.keys()).intersection(string1.upper()))
    freq_str = collections.Counter(string1)
    chisq_values = []
    for i in freq_en.iterkeys():
        exp = freq_en.get(i)
        if i in freq_str:
            obs = freq_str.get(i)
        else: obs = 0
        chisq_values.append(pow((obs - exp), 2) / exp)
    chisq = 0
    for i in chisq_values:
        chisq += i
    return chisq
'''
XOR function. Input strings in binary
'''
def xor_strings(xs, ys):
    xs = binascii.unhexlify(xs)
    ys = chr(ys)
    return "".join(chr(ord(x) ^ ord(ys)) for x in xs)
'''
Program start
'''
enc_str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
d_decrypt={}
for i in range(256):
    xored_str = xor_strings(enc_str, i)
    score = chisq_score(xored_str)
    d_decrypt[str(i) + ' ' + xored_str] = score
b_score = min(d_decrypt.itervalues())
for key, value in d_decrypt.items():
    if value == b_score:
        if list(set(key).difference(string.printable)) == []: print key