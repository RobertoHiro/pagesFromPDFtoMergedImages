from pdf2image import convert_from_path
import glob
import os
from tkinter import * 
from tkinter.filedialog import askdirectory
from PIL import Image
  
filenames = []
itensOnTheRow = 4
itensOnTheCollumn = 4
imagesToMerge = itensOnTheRow * itensOnTheCollumn
arrayOfRow = []
arrayOfFiles = []
pathToPlaceConvertedFiles = "./converted"

stringFileNames = ""
stringRowNames = ""
pathname = ""

def cleanExportFolder():
    filesToDelete = glob.glob(pathToPlaceConvertedFiles+"/*")
    for f in filesToDelete:
        os.remove(f)

def getTargetFolder():
    Tk().withdraw()
    global pathname
    pathname = askdirectory()

# def convertPDFtoFiles():
#   pages = convert_from_path("/tcg_cards.pdf", 500)
#   for page in pages:
#       page.save(pathToPlaceConvertedFiles+'/out.png', 'PNG')

def appendFilesToArray():
    global filenames
    for filename in glob.glob(pathname+'/*.png'): 
        im=Image.open(filename)
        filenames.append(filename)

def createFiles():
    global filenames, imagesToMerge, itensOnTheCollumn, itensOnTheRow, stringFileNames, pathToPlaceConvertedFiles, arrayOfRow, stringRowNames, arrayOfFiles
    index = 0
    for z in range(int(len(filenames)/imagesToMerge)+1):
        for x in range(itensOnTheCollumn):
            row = []
            for y in range(itensOnTheRow):
                if index < len(filenames):
                    row.append(filenames[index])
                    stringFileNames += (filenames[index] + " ")
                    index += 1
            arrayOfRow.append(row)
            os.system(f'magick convert +append {stringFileNames}{pathToPlaceConvertedFiles}/row{len(arrayOfRow)}.png')
            stringFileNames = ""
            stringRowNames += f"{pathToPlaceConvertedFiles}/row{len(arrayOfRow)}.png "
        arrayOfFiles.append(arrayOfRow)
        print(stringRowNames)
        os.system(f'magick convert -append {stringRowNames}{pathToPlaceConvertedFiles}/file{len(arrayOfFiles)}.png')
        stringRowNames = ""

cleanExportFolder()

getTargetFolder()

appendFilesToArray()

createFiles()