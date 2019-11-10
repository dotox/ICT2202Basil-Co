from PIL import Image
import binascii
import codecs


# ============= PILLOW ===================================================================================
def importPicture():
    # Specifies the directory to import the PACKAGE from. (The file that will be used to contain the secret file)
    directory = "C:\\Users\\ojthe\\Desktop\\img-100x100-0-0-0 - Copy.png"
    importedImage = Image.open(directory)
    return importedImage

def showImageOnScreen(importedImage):
    importedImage.show()


def getAllRGBChannelPerPixel(importedImage):
    pixel_values_list = list(importedImage.getdata())
    print()
    for i in range(0, pixel_values_list.__len__()):
        print(str(i + 1) + ": " + str(pixel_values_list[i]))


def getColoursUsedInPicture(importedImage):
    return importedImage.getcolors()


def getImageDetails(importedImage):
    width, height = importedImage.size
    print()
    print("Height: " + str(height))
    print("Width: " + str(width))
    imageMode = importedImage.mode
    print("Image Mode: " + str(imageMode))
    return width, height


def getPixelChannel(importedImage, yx):
    imageIndividualPixel = importedImage.getpixel(yx)
    return imageIndividualPixel


def setPixelChannel(importedImage, yx, data):
    importedImage.putpixel(yx, data)
    saveImage(importedImage)


def saveImage(importedImage):
    # Specifies the directory to export the NEW-PACKAGE to. (The new file that contains the secret file)
    saveDirectory = str(r"C:\\Users\\ojthe\\Desktop\\output.png")
    importedImage.save(saveDirectory, format=None)


# ============= OTHER FUNCTIONS ==========================================================================
def importPayload():
    # Specifies the directory to import the PAYLOAD from. (The secret file)
    importFromDirectory = str(r"C:\\Users\\ojthe\\Desktop\\img-1x1-0-0-0.png")
    with open(importFromDirectory, 'rb') as f:
        content = f.read()
    hexValues = binascii.hexlify(content)
    return hexValues


def convertToBin(hexValues):
    hexToBinString = ""
    for i in range (0, hexValues.__len__()):
        hexToBinString += hexToBin(hexValues[i])
    return hexToBinString


def hexToBin(query):
    query = str(query)

    if query == "8":
        return "1000"

    elif query < "8":
        if query == "4":
            return "0100"
        elif query < "4":
            if query == "2":
                return "0010"
            elif query < "2":
                if query == "0":
                    return "0000"
                if query == "1":
                    return "0001"
            elif query > "2":
                if query == "3":
                    return "0011"
        elif query > "4":
            if query == "6":
                return "0110"
            elif query < "6":
                if query == "5":
                    return "0101"
            elif query > "6":
                if query == "7":
                    return "0111"

    elif query > "8":
        if query == "b":
            return "1011"
        elif query < "b":
            if query == "9":
                return "1001"
            if query == "a":
                return "1010"
        elif query > "b":
            if query == "d":
                return "1101"
            elif query < "d":
                if query == "c":
                    return "1100"
            elif query > "d":
                if query == "e":
                    return "1110"
                if query == "f":
                    return "1111"


def decToBin(query):
    query = int(query)

    if query == 6:
        return "0110"

    elif query < 6:
        if query == 3:
            return "0011"
        elif query < 3:
            if query == 0:
                return "0000"
            elif query == 1:
                return "0001"
            elif query == 2:
                return "0010"
        elif query > 3:
            if query == 4:
                    return "0100"
            if query == 5:
                    return "0101"
    elif query > 6:
        if query == 8:
            return "1000"
        elif query < 8:
            if query == 7:
                return "0111"
        elif query > 8:
            if query == 9:
                return "1001"


def embed(importedImage, hexToBinString):
    width, height = getImageDetails(importedImage)
    totalPixels = (width * height)
    print()
    print("PACKAGE")
    print("Total Pixels: " + str(totalPixels))
    print("Total Size In Bits (Package): " + str(totalPixels * 3) + " Bits")
    print("Data To Embed: " + str(hexToBinString))
    numberOfCalls = int(hexToBinString.__len__() / 3)
    print("Number Of Calls: " + str(numberOfCalls))

    counterIn3 = 0
    counter = 0
    y = 0
    x = 0

    for i in range (0, width):
        if i + 1 == width:
            print("Reached Last Column of the Image Grid. File too big.")
            return 0
        for j in range (0, height):
            if counter == numberOfCalls:
                y = i
                x = j
                break
            yx = (i,j)

            imageIndividualPixel = getPixelChannel(importedImage, yx)
            red = str(bin(imageIndividualPixel[0]))
            green = str(bin(imageIndividualPixel[1]))
            blue = str(bin(imageIndividualPixel[2]))
            newRed = red[:(red.__len__()-1)] + str(int(hexToBinString[counterIn3]))
            newGreen = green[:(green.__len__()-1)] + str(int(hexToBinString[counterIn3+1]))
            newBlue = blue[:(blue.__len__()-1)] + str(int(hexToBinString[counterIn3+2]))
            dataTurple = (int(newRed, 2), int(newGreen, 2), int(newBlue, 2))
            setPixelChannel(importedImage, yx, dataTurple)

            counterIn3 += 3
            counter = counter + 1

        if counter == numberOfCalls:
            break
    hexToBinStringLength = hexToBinString.__len__()
    remainder = (hexToBinStringLength) - counterIn3

    if remainder == 1:
        yx = (y, x)
        dataTurple = (int(hexToBinString[counterIn3]), int(0), int(0))
        setPixelChannel(importedImage, yx, dataTurple)

    elif remainder == 2:
        yx = (y, x)
        dataTurple = (int(hexToBinString[counterIn3]), int(hexToBinString[counterIn3+1]), int(0))
        setPixelChannel(importedImage, yx, dataTurple)

    if x+1 == height:
        if y+1 == width:
            return 0
        y = y+1
        x = 0
    else:
        x = x+1

    reload = x
    for w in range (y, width):
        for k in range(reload, height):
            yx = (w, k)

            imageIndividualPixel = getPixelChannel(importedImage, yx)

            red = str(bin(imageIndividualPixel[0]))
            green = str(bin(imageIndividualPixel[1]))
            blue = str(bin(imageIndividualPixel[2]))
            newRed = red[:(red.__len__()-1)] + str(int(0))
            newGreen = green[:(green.__len__()-1)] + str(int(0))
            newBlue = blue[:(blue.__len__()-1)] + str(int(0))

            dataTurple = (int(newRed, 2), int(newGreen, 2), int(newBlue, 2))
            setPixelChannel(importedImage, yx, dataTurple)
        reload = 0

    saveImage(importedImage)


def LSBExtractor(openFile):
    # Specifies the directory to import the NEW-PACKAGE from. (The file containing the secret file)
    stegoImageImport = str(openFile)

    importedImage = Image.open(stegoImageImport)
    width, height = getImageDetails(importedImage)
    if width < 5 or height < 5:
        return 0, 0
    counter = 0
    extractAllBin = ""

    for a in range (0, width):
        for b in range(0, height):
            yx = (a, b)
            imageIndividualPixel = getPixelChannel(importedImage, yx)

            red = str(bin(imageIndividualPixel[0]))
            green = str(bin(imageIndividualPixel[1]))
            blue = str(bin(imageIndividualPixel[2]))

            extractAllBin += str(str(bin(imageIndividualPixel[0]))[str(bin(imageIndividualPixel[0])).__len__()-1]) + \
                             str(str(bin(imageIndividualPixel[1]))[str(bin(imageIndividualPixel[1])).__len__()-1]) + \
                             str(str(bin(imageIndividualPixel[2]))[str(bin(imageIndividualPixel[2])).__len__()-1])

            counter += 1
    return str(extractAllBin), str(hex(int(extractAllBin,2)))


def validateSize(importedImage, hexToBinString, hexValues):
    width, height = getImageDetails(importedImage)
    totalPixels = (width * height)

    if int(hexToBinString.__len__()) < int(totalPixels * 3):
        pause = raw_input("Press any key to continue: ")
        return True
    else:
        pause = input("Press any key to continue: ")
        return False


def createOriginalHiddenFile(originalHex):
    # Specifies the directory to export the extracted secret file to. (The extracted secret file)
    with open("../originalHidden.png", 'wb') as f:
        for i in range(2, originalHex.__len__(), 2):
            iteration = bytes.fromhex(str(originalHex[i]) + str(originalHex[i+1])).decode('ansi')
            f.write(bytes(iteration, "ansi"))


def decodeLSB(openFile):
    originalBin, originalHex = LSBExtractor(openFile)
    if originalBin == 0 and originalHex == 0:
        return "Failed To Find Any File"
    createOriginalHiddenFile(originalHex)
    return "File Found and Created"
