import os
from slugify import slugify
import shutil
import json

os.mkdir('dst')


# folder path
dir_path = r'2004Mbit'

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        if ".gba" in path.lower():
            slug = slugify(path[:-3])
            folder =  f'dst/{slug}'
            os.mkdir(f'dst/{slug}')
            shutil.copyfile(f"{dir_path}/{path}", f"{folder}/{slug}.gba")
            game_manifest = {
                    "slug": slug,
                    "screenshots": [],
                    "tags": ["2004Mbit"],
                    "files": [{ 
                                "default": True,
                                "filename": f"{slug}.gba",
                                "playable": True
                               }],
                    "title": path[:-3],
                    "platform": "GBA",
                    "typetag": "game",
                    "developer": ""
            }
            with open(f'{folder}/game.json', 'w') as fp:
                json.dump(game_manifest, fp, indent=3)

            res.append(path)
print(res)
