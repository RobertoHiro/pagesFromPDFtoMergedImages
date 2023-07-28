from PIL import Image
import glob
import os
  
filenames = []
itensOnTheRow = 6
itensOnTheCollumn = 5
imagesToMerge = itensOnTheRow * itensOnTheCollumn
arrayOfRow = []
arrayOfFiles = []

stringFileNames = ""
stringRowNames = ""

for filename in glob.glob('C:/Users/RobertoHiroshi/Documents/Projetos/Jasper/tcg_cards/*.png'): #assuming gif
    im=Image.open(filename)
    filenames.append(filename)

index = 0
for z in range(int(len(filenames)/imagesToMerge)):
    for x in range(itensOnTheCollumn):
        row = []
        for y in range(itensOnTheRow):
            row.append(filenames[index])
            stringFileNames += (filenames[index] + " ")
            index += 1
        arrayOfRow.append(row)
        print(stringFileNames)
        os.system(f'magick convert +append {stringFileNames}row{len(arrayOfRow)}.png')
        stringFileNames = ""
        stringRowNames += f"row{len(arrayOfRow)}.png "
    arrayOfFiles.append(arrayOfRow)
    print(stringRowNames)
    os.system(f'magick convert -append {stringRowNames}file{len(arrayOfFiles)}.png')
    stringRowNames = ""

# rowIndex = 0
# fileIndex = 0
# for z in range(len(arrayOfFiles)):
#     thisFile = arrayOfFiles[fileIndex]
#     os.system(f'magick convert +append 1.png 2.png result{rowIndex}.png')
