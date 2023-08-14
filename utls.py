from requests import get

def getPdfNames() -> set[str]:
    fileNames = set() 
    res = get("https://ia601606.us.archive.org/13/items/al-arabi-magazine/al-arabi-magazine_files.xml")

    cont = res.content.decode()
    index = 0
    while True:
        if index == len(cont): break
        if cont[index: index+10] != "<file name" : 
            index += 1
            continue

        end = getStr(cont, (index := index+12))
        fileName = cont[index:end]
        if fileName.endswith(".pdf"):
            fileNames.add(fileName)

        index = end + 1
    return fileNames

def getStr(text: str, start: int) -> int:
    while True:
        if text[start] == '"': return start # the end of the string 
        start += 1 

def write(file: str, text: bytes):
    with open(file, 'wb') as f: f.write(text)

