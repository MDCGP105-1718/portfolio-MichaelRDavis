def openFile():
    fileObj = open("lyrics.txt")
    return fileObj

def readFile(fileObj):
    line = fileObj.readline()
    return line

stringLine = readFile(openFile())
print(stringLine)

x = input("Insert a number to find a word that is most used in song lyrics\n")
