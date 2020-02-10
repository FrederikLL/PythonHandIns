import os
import os.path

#2
#A

def writeTo(pathToFolder):
    onlyfiles = [f for f in os.listdir(pathToFolder) if os.path.isfile(os.path.join(pathToFolder,f))]
    print(onlyfiles)
    return onlyfiles

writeTo('C:\\Users\\Bruger\\Documents\\4semester\\Python')

#B

def writeToRec(pathToFolder):
    for root, dirs, files in os.walk(pathToFolder):
        for name in files:
            print(name)

#virke rmen printer ekstra ting(skjulte filer måske)
#writeToRec('C:\\Users\\Bruger\\Documents\\4semester\\Python\\HandIns')

#C
foldpath = 'C:\\Users\\Bruger\\Documents\\4semester\\Python'
listOfFileNames = writeTo(foldpath)
def printFirstLine(listOfFile):
    for file in listOfFile:
        with open(os.path.join(foldpath, file)) as f:
	        print(f.readline())
            

printFirstLine(listOfFileNames)

#D
foldpath1 = 'C:\\Users\\Bruger\\Documents\\4semester\\Python'
listOfFileNames1 = writeTo(foldpath)
def printEmail(listOfFile):
    for file in listOfFile:
        with open(os.path.join(foldpath1, file)) as f:
            for line in f:
                if '@' in line:
                    print(line)

printEmail(listOfFileNames1)

#E