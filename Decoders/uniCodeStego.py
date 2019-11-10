"""
Unicode Name: Zero width non-joiner
Encoding/Decoding method: UTF-8 (hex)
U+200B, U+200C
"""
import re
import binascii

def decode(EncodedHidden):
    #PlainText = ('%x' %int(''.join(re.sub('[\x00-\x7F]', '', EncodedHidden)).encode('hex').replace('e2808b', '0').replace('e2808c', '1'), 2)).decode('hex')
    PlainText = ('%x' % int(''.join((binascii.hexlify((re.sub('[\x00-\x7F]', '', bytearray.fromhex(str(EncodedHidden,'utf-8')).decode())).encode('utf-8')).decode('utf-8'))).replace('e2808b', '0').replace('e2808c', '1'),2))
    return binascii.unhexlify(PlainText)

def removeNonAscii(hiddenFile):
    with open(hiddenFile, 'rb') as file:
        text = binascii.hexlify(file.read())
        #text = file.read().replace('\n', '')
    decodedText = decode(text)
    return decodedText
