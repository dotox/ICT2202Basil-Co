
from PIL import Image


def getHiddenString(message):
    with open('../Output Files/Wav_Output.wav', 'wb') as file:
        file.write(message)
        return "Successful file extracted"

def BinaryToString(binary):
    message = ''
    for i in range(0, len(binary), 8):
        message += chr(int(binary[i:i+8],2))
    return message

def decodingWav(filename):
    data = Image.open(filename).convert('RGBA')
    binary = ''
    if data.mode in 'RGBA':
        datas = data.getdata()
    for item in datas:
        pixel = item
        r   = pixel[0]
        g = pixel[1]
        b  = pixel[2]
        sumof = r + g + b
        if sumof % 3 == 0:
            bit = 1
        else:
            bit = 0
        binary += str(bit)
        if (binary[-17:] == '11111110011111111'):
            binary = binary[:-17]
            break
    return getHiddenString(BinaryToString(binary))

