from os import getcwd
from os.path import exists, join
from json import load
from requests import get
from utls import write, getPdfNames, writePdfNames

source = "https://ia601606.us.archive.org/13/items/al-arabi-magazine/" 

def getFileNames(cdir: str) -> list[str]:
    if exists(path := join(cdir, "al-arabi-magazine.json")):
        with open(path, "r") as f: return load(f)
    
    writePdfNames(fileNames := getPdfNames())
    return fileNames

def main():
    cdir = getcwd()
    for fileName in getFileNames(cdir):
        if exists(join(cdir, fileName)): continue
        
        print("started downloading: " + fileName, end='')

        response = get(source + fileName)
        write(join("arch", fileName), response.content)

        print("\tfinished")

    print("done")


if __name__ == "__main__": main()
