import os
from pathlib import Path


#print("Enter the path where you want to sort the file",end='')
#ch = input()

#os.system("cp sorting_data.py ch");

SUBDIR = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO":['.mp3','.wav'],
    "VIDEO":['.mp4','.webm','.mov','.avi'],
    "IMAGES":['.jpg','.gif','.png','.jpeg'],
    "COMPRESSED": ['.zip','.rar']
}

def pickDirectory(value):
    for category ,suffixes in SUBDIR.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'
def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)
        if directoryPath.is_dir()!=True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organizeDirectory()