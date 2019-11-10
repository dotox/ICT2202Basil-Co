import numpy as np
import scipy as sp
import scipy.io.wavfile

def phraseDecode(fname,textLength):
    rate, data = sp.io.wavfile.read(fname)
    data = data.copy()
    unitLength = 2 * int(2 ** np.ceil(np.log2(2 * textLength)))
    unitMiddle = unitLength // 2
    if len(data.shape) == 1:
        Chars = data[:unitLength]
    else:
        Chars = data[:unitLength, 0]
    Chars = (np.angle(np.fft.fft(Chars))[unitMiddle - textLength:unitMiddle] < 0).astype(np.int8) #reshape(-1,{value}) depends on Length of Text
    #print Chars
    Chars = Chars.reshape((-1, 8)).dot(1 << np.arange(8 -1, -1, -1))
    #print Chars
    return ''.join(np.char.mod('%c', Chars))


