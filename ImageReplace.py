#from PIL import Image
from os import scandir

###

#Path to the directory that contains all images
path = ''
#Path to the default image
default = ''
#Extension of the images - PNG or JPG
extension = 'png'

###

defaultImg = Image.open(default)

###

def ReplaceImage(imgPath):

        currentImg = Image.open(imgPath)

        currentImg = defaultImg

        currentImg = currentImg.save(imgPath)

def ScanFolder(folderPath):

    entries = scandir(folderPath)

    for entry in entries:

        if entry.is_file():

            if entry.name[len(entry.name)-3] == extension[0] and entry.name[len(entry.name)-2] == extension[1] and entry.name[len(entry.name)-1] == extension[2]:

                ReplaceImage(folderPath + entry.name)

            
        if entry.is_dir():

            print('Scanning folder ' + entry.name)

            ScanFolder(folderPath + entry.name + '/')

###

ScanFolder(path)