import os
import json



#make folders
def create_folders(main_name):
    os.makedirs(main_name, exist_ok=True)
    sub_folder(main_name, 'data')
    sub_folder(main_name + "/data", 'minecraft')
    sub_folder(main_name + "/data/minecraft", 'worldgen')
    sub_folder( main_name +"/data/minecraft/worldgen", "noise_settings")
    sub_folder( main_name +"/data/minecraft/worldgen", "world_preset")


def sub_folder(folder, name):
    sub_folder = os.path.join(folder, name)
    os.makedirs(sub_folder, exist_ok=True)


#json file, str, str
def create_data(data, folder, name):
    name_json = name+".json"
    mcmeta_json = json.dumps(data, indent=4)
    path = os.path.join(folder, name_json)
    os.makedirs(name_json, exist_ok=True)
    with open(path, "w", encoding="utf-8") as file:
        file.write(mcmeta_json)

def mcmeta(version, description, main_name):
    mcmeta_content = {
        "pack": {
            "pack_format": 6,
            "description": "Beispiel Pack"
        }
    }
    mcmeta_json = json.dumps(mcmeta_content, indent=4)
    path = os.path.join("main_name", "pack.mcmeta")
    os.makedirs("main_name", exist_ok=True)
    with open(path, "w", encoding="utf-8") as file:
        file.write(mcmeta_json)

    
create_folders("datapack_1")