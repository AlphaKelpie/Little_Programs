import os
from subprocess import run

files = []
IMAGES = ['jpeg', 'png', 'webp']
VIDEOS = ['mp4', 'mov']
PATH = '../cartella/'

with os.scandir(PATH) as entries:
    for entry in entries:
        INFO = entry.stat()
        NAME = str(entry.name)
        TIME = float(INFO.st_birthtime)
        # print(name, time)
        files.append({'name' : NAME, 'time' : TIME})

files = sorted(files, key=lambda x: x['time'])
# print('\n'.join(f"{x['name']}\t{x['time']}" for x in files))

# i = 1
# for file in files:
#     print(file['name'])
#     print(file['time'])
#     run(['mv', f'{PATH}{file["name"]}', f'{PATH}file_{i:02d}.txt'])
#     i += 1

img = 1
vid = 1
for file in files:
    # name = file['name'][:-4]
    # print(name)
    EXTENSION = file['name'].split('.')[-1]
    # print(EXTENSION)
    if EXTENSION in IMAGES or EXTENSION in VIDEOS:
        run(['mv', f'{PATH}/{file["name"]}', f'{PATH}/IMG_{img:03d}.{EXTENSION}'])
        img += 1
    else:
        vid += 1

print('Images:\t', img-1)
print('Videos:\t', vid-1)