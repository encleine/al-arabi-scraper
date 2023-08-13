from asyncio import get_event_loop
import requests
from os import getcwd
from os.path import exists, join


url = "https://ia601606.us.archive.org/13/items/al-arabi-magazine/" 
fileName = "العربي%20-%20{}.pdf"
cdir = getcwd()
date = 1958

async def get(url):
    loop = get_event_loop()
    return await loop.run_in_executor(None, requests.get, url)

async def write(file, response):
    with open(file, 'wb') as f: f.write(response.content)

async def main():
    for inc in range(33):
        name = fileName.format(date + inc)
        if exists(join(cdir, name)): continue

        print("started downloading: " + name)

        response = await get(url + name)
        await write(name, response)

        print("finished")
    print("done")


loop = get_event_loop()
loop.run_until_complete(main())
