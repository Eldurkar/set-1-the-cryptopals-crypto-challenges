import binascii
"""
Function to convert hex to base64
"""
def hex_to_base64(hexstr):
    binary = binascii.unhexlify(hexstr)
    b64 = binascii.b2a_base64(binary)
    print b64

string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
hex_to_base64(string)
