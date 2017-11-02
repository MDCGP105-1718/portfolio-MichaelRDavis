def openFile():
    fileObj = open("lyrics1.txt")
    return fileObj

def readFile(fileObj):
    line = fileObj.readline()
    return line

stringLine = readFile(openFile())
print(stringLine)

freq = {}

def findWord(stringLine):
    stringLine.split()
    if word in stringLine:
        print(word)

findWord(stringLine)

#def findMultipleWords(x):


x = int(input("Enter a number to search duplicate words in song lyrics"))
