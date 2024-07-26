#imports
import subprocess
import sys

#pillow is not a standard libary, so we need to install it
subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
import tkinter as tk
from PIL import Image, ImageTk
import ctypes
import os
import json
from assets.file import all_biomes as RAW
from assets.file import spawn as spawn

#main function
def main():
  #confirm start
  label = tk.Label(root, text="Bug")
  label.place(x = 670, y= 10)

  #get inputs
  mode = white.get()
  sea_level = int(sea_lvl.get())
  version = version_to_pack_format(version_e.get())
  description = description_e.get()
  title = title_e.get()
  version_f = int(version) #version_f is in mcmeta format
  noise_mode = int(noise_set.get())

  #get biomes
  selected_biomes = []
  if mode == str(1):
    #Whitelist
    for i in range(len(ram)):
      if ram[i].get() == str(1):
        selected_biomes.append(data[i])
  else:
    #Blacklist
      for i in range(len(ram)):
        if ram[i].get() == str(0):
          selected_biomes.append(data[i])
  
  create_folders(title)
  mcmeta(version_f, description, title)
  main_w(selected_biomes, title)
  add_noise_setting(noise_mode, title)
  set_sea_lvl(title, sea_level)
  #confirm end
  label = tk.Label(root, text="Finished")
  label.place(x=630, y=10, height=20, width=100)

# Get the desired biomes list
def main_w(allow, main_name):
  ''' The main functionality '''
  # Read the full biome list into a Python list
  dirty_biomes = parse_w(RAW)

  # Filter that list
  clean_biomes = narrow_w(dirty_biomes, allow)

  # Assemble the filtered biomes back into a .json object
  out = assemble_w(clean_biomes)
  output_path = os.path.join(main_name +"/data/minecraft/worldgen/world_preset", "normal.json")
  with open(output_path, "w") as f:
      f.write(out)
  # Done!
  return 0

def parse_w(string):
  ''' Take a string and break it up into a list of brackets '''

  # Hold each { .... } while we assemble it
  tmp = ""

  # The list to return
  out = []

  # How many brackets deep are we?
  depth = 0

  # Start at ~20 as we assume the all_biomes starts with
  # { "biomes": [
  # and new lines and junk. We just don't want that first bracket

  # For each character in the string...
  for c in string[20:]:

      # Record it
      tmp += c

      # Each element in the list ends with a closing bracket.
      # Is this the closing bracket that matches with the opening bracket?
      if (c == "}"):
          depth -= 1

      # Each element in the list starts with an opening bracket.
      elif (c == "{"):
          depth += 1

      # Have we fully found a { ... } ?
      if (depth == 0):

          # Store it as a list element
          out.append(tmp)

          # Get ready for a new list element
          tmp = ""

  # Return the list!
  return out

def narrow_w(lst, filt):
  ''' Filter the list by a list of allowed elements '''

  # What to return
  out = []

  # For each element in the list to be filtered...
  for l in lst:

      # For each element in the filter...
      for f in filt:

          # If the list element contains an allowed biome...
          if (f in l):

              # Record it!
              out.append(l)

              # Save time
              break

  # Return the filtered list
  return out

def assemble_w(lst):
  ''' Reassemble the string into something that looks like a .json '''

  # Start the .json off with the given header
  header = '''{
"dimensions": {
  "minecraft:overworld": {
    "type": "minecraft:overworld",
    "generator": {
      "type": "minecraft:noise",
      "settings": "minecraft:overworld",
      "biome_source": {
        "type": "minecraft:multi_noise",
'''
  out = header + "\"biomes\": ["

  # For each { ... } element, except the last one
  for l in lst[:-1]:

      # Record it
      out += l

      # Add a comma
      out += ",\n"

  # Now add the last element, with no comma
  out += lst[-1]

  # Add a newline and close the list
  out += "\n]"

  # Add the closing brackets for the JSON structure
  footer = '''    }}},
    "minecraft:the_end": {
      "type": "minecraft:the_end",
      "generator": {
        "type": "minecraft:noise",
        "biome_source": {
          "type": "minecraft:the_end"
        },
        "settings": "minecraft:end"
      }
    },
    "minecraft:the_nether": {
      "type": "minecraft:the_nether",
      "generator": {
        "type": "minecraft:noise",
        "biome_source": {
          "type": "minecraft:multi_noise",
          "preset": "minecraft:nether"
        },
        "settings": "minecraft:nether"
      }}}}
'''
  out += footer

  # Return it!
  return out

def sub_folder(parent, name):
  path = os.path.join(parent, name)
  os.makedirs(path, exist_ok=True)
  return path

def create_folders(main_name):
  #script_dir = os.path.dirname(os.path.abspath(__file__))
  main_path = main_name
  os.makedirs(main_path, exist_ok=True)
  data_path = sub_folder(main_path, 'data')
  minecraft_path = sub_folder(data_path, 'minecraft')
  worldgen_path = sub_folder(minecraft_path, 'worldgen')
  sub_folder(worldgen_path, 'noise_settings')
  sub_folder(worldgen_path, 'world_preset')

def add_noise_setting(noise_mode, main_name):
  json_names = ["amplified.json", "caves.json", "end.json", "floating_islands.json", "large_biomes.json", "nether.json","overworld.json"]
  file = json_names[noise_mode]
  destination_folder = os.path.join(main_name, "data", "minecraft",  "worldgen", "noise_settings")
  add_json_to_folder(file, destination_folder)
  if file == "caves.json":
     add_better_spawn(os.path.join(main_name, "data"))

def add_json_to_folder(file_path, destination_folder):
  # Read the JSON file
  with open(os.path.join("jsons",file_path), 'r') as file:
    data = json.load(file)
  
  # Create the destination folder if it doesn't exist
  if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
  
  # Save the JSON file to the new location
  base_name = os.path.basename(file_path)
  destination_path = os.path.join(destination_folder, base_name)
  with open(destination_path, 'w') as file:
    json.dump(data, file, indent=4)
  os.rename(os.path.join(destination_folder, base_name), os.path.join(destination_folder,"overworld.json"))

#prevents the player from spawning on top of the bedrock
def add_better_spawn(path):
  path_namespace = sub_folder(path, 'name')
  path_advancement = sub_folder(path_namespace, 'advancements')
  path_functions = sub_folder(path_namespace, "functions")
  add_json_to_folder('start.json', path_advancement)

  #save spawn.mcfunction
  path = os.path.join(path_functions, "spawn.mcfunction")
  with open(path, "w", encoding="utf-8") as file:
    file.write(spawn)

#int, str, str
def mcmeta(version, description, main_name):
  mcmeta_content = {
      "pack": {
          "pack_format": version,
          "description": description
      }
  }
  mcmeta_json = json.dumps(mcmeta_content, indent=4)

  path = os.path.join(main_name, "pack.mcmeta")
  os.makedirs(main_name, exist_ok=True)
  with open(path, "w", encoding="utf-8") as file:
      file.write(mcmeta_json)

#str,int
def set_sea_lvl(main_name,level):
  path = os.path.join(main_name, "data", "minecraft", "worldgen", "noise_settings", "overworld.json")
  with open(path) as file:
    data = json.load(file)

  #change "sea_level" data 
  if isinstance(data, dict):
      data["sea_level"] = level
  elif isinstance(data, list):
      for ram in data:
          if "sea_level" in ram:
              ram["sea_level"] = level


  # Save the updated JSON with formatted output
  with open(path, 'w') as f:
      json.dump(data, f, indent=4)

#str
def version_to_pack_format(user_version):
  versions = [
    ["1.18", "8"],
    ["1.18.1", "8"],
    ["1.18", "8"],
    ["1.18.2", "8"],
    ["1.19", "10"],
    ["1.19.1", "10"],
    ["1.19.2", "10"],
    ["1.19.3", "10"],
    ["1.19.4", "12"],
    ["1.20.1", "15"],
    ["1.20", "15"],
    ["1.20.2", "18"],
    ["1.20.3", "26"],
    ["1.20.4", "26"],
    ["1.20.5", "41"],
    ["1.20.6", "41"],
    ["1.21", "48"],
    ["1.21.1", "48"]
  ]
  for i in range(len(versions)):
    if versions[i][0] == user_version:
      return(int(versions[i][1]))


#gui inits
root = tk.Tk()
root.geometry("820x400")
root.title("Biome Selector")

#icon
icon_path = os.path.join("assets", "icon3.png")
icon_image = Image.open(icon_path)
photo = ImageTk.PhotoImage(icon_image)
myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
root.iconphoto(False, photo)

#variables
data = ['minecraft:bamboo_jungle', 'minecraft:badlands', 'minecraft:birch_forest', 'minecraft:beach', 'minecraft:cold_ocean', 'minecraft:deep_dark', 
        'minecraft:dripstone_caves', 'minecraft:desert', 'minecraft:dark_forest', 'minecraft:deep_lukewarm_ocean', 'minecraft:deep_ocean', 
        'minecraft:deep_cold_ocean', 'minecraft:deep_frozen_ocean', 'minecraft:eroded_badlands', 'minecraft:frozen_peaks', 'minecraft:frozen_river', 
        'minecraft:flower_forest', 'minecraft:forest', 'minecraft:frozen_ocean', 'minecraft:frozen_plains', 'minecraft:grove', 'minecraft:ice_spikes', 
        'minecraft:jagged_peaks', 'minecraft:jungle', 'minecraft:lush_caves', 'minecraft:meadow', 'minecraft:mangrove_swamp', 'minecraft:mushroom_field', 
        'minecraft:old_growth_birch_forest', 'minecraft:old_growth_pine_taiga', 'minecraft:old_growth_spruce_taiga', 'minecraft:ocean', 'minecraft:plains', 
        'minecraft:river', 'minecraft:sparse_jungle', 'minecraft:sunflower_plains', 'minecraft:stony_peaks', 'minecraft:savanna', 'minecraft:savanna_plateau', 
        'minecraft:snowy_taiga', 'minecraft:snowy_beach', 'minecraft:snowy_plains', 'minecraft:snowy_slopes', 'minecraft:swamp', 'minecraft:stony_shore', 
        'minecraft:taiga', 'minecraft:windswept_savanna', 'minecraft:wooded_badlands', 'minecraft:windswept_forest', 'minecraft:windswept_hills', 
        'minecraft:windswept_gravelly_hills', 'minecraft:warm_ocean']
ram = [] #later biome data

#widgets
#whitelist or blacklist?
white = tk.StringVar()
white.set(True)  #standard choice
whitelist = tk.Radiobutton(root, text="Whitelist", variable=white, value=True)
blacklist = tk.Radiobutton(root, text="Blacklist", variable=white, value=False)
whitelist.place(x=0, y=0, width = 80, height = 20)
blacklist.place(x=0, y=20, width = 80, height = 20)

#run button
icon_path = os.path.join("assets", "run.png")
icon_image = Image.open(icon_path)
img = ImageTk.PhotoImage(icon_image)
button = tk.Button(root, image=img, command=main)
button.place(x=770,y=0,width=50,height=50)

#create list of biomes
i = 0
for x in range(3):
  for y in range (round(len(data)/3)):
    ram.append(tk.StringVar(value=""))
    checkbutton = tk.Checkbutton(root, text = "", variable=ram[i], font = ("Arial",10))
    checkbutton.deselect()
    label = tk.Label(root, text = data[i],anchor=tk.W)
    label.place(x=25+x*250, y = 50+y*20, width = 250, height = 20)
    checkbutton.place(x=0+x*250, y = 50+y*20, width = 40, height = 20)
    i+=1

ram.append(tk.StringVar(value=""))
checkbutton = tk.Checkbutton(root, text = "", variable=ram[i], font = ("Arial",10))
checkbutton.deselect()
label = tk.Label(root, text = data[i],anchor=tk.W)
label.place(x=25+x*250, y = 50+y*20, width = 250, height = 20)
checkbutton.place(x=0+x*250, y = 50+y*20, width = 40, height = 20)

#which noise setting?
noise_set = tk.StringVar()
noise_set.set(6)  #standard choice

ampliefied_e = tk.Radiobutton(root, text="", variable=noise_set, value=0)
ampliefied_e.place(x=700, y=50, width = 20, height = 20)

caves_e = tk.Radiobutton(root, text="", variable=noise_set, value=1)
caves_e.place(x=700, y=70, width = 20, height = 20)

end_e = tk.Radiobutton(root, text="", variable=noise_set, value=2)
end_e.place(x=700, y=90, width = 20, height = 20)

floating_islands_e = tk.Radiobutton(root, text="", variable=noise_set, value=3)
floating_islands_e.place(x=700, y=110, width = 20, height = 20)

large_biomes_e = tk.Radiobutton(root, text="", variable=noise_set, value=4)
large_biomes_e.place(x=700, y=130, width = 20, height = 20)

nether_e = tk.Radiobutton(root, text="", variable=noise_set, value=5)
nether_e.place(x=700, y=150, width = 20, height = 20)

overworld_e = tk.Radiobutton(root, text="", variable=noise_set, value=6)
overworld_e.place(x=700, y=170, width = 20, height = 20)

#labels for noise setting
label = tk.Label(root, text = "Amplified", anchor='w')
label.place(x = 720, y = 50, width =75)

label = tk.Label(root, text = "Caves", anchor='w')
label.place(x = 720, y = 70, width =75)

label = tk.Label(root, text = "End", anchor='w')
label.place(x = 720, y = 90, width =75)

label = tk.Label(root, text = "Floating Island", anchor='w')
label.place(x = 720, y = 110, width =90)

label = tk.Label(root, text = "Large Biome", anchor='w')
label.place(x = 720, y = 130, width =75)

label = tk.Label(root, text = "Nether", anchor='w')
label.place(x = 720, y = 150, width =75)

label = tk.Label(root, text = "Overworld", anchor='w')
label.place(x = 720, y = 170, width =75)

#description
label = tk.Label(root, text = "Description")
label.place(x = 100, y = 10, width =75)
description_e = tk.Entry(root) #_e means entry object
description_e.place(x = 175, y = 10) 
description_e.insert(0,"Custom Worldgen")

#version
label = tk.Label(root, text = "Version")
label.place(x = 330, y = 10, width =75)
version_e = tk.Entry(root)
version_e.place(x = 400, y = 10, width = 50) 
version_e.insert(0,"1.19.4")

#title
label = tk.Label(root, text = "Title")
label.place(x = 450, y = 10, width =75)
title_e = tk.Entry(root)
title_e.place(x = 510, y = 10, width = 100) 
title_e.insert(0,"My Datapack")

#sea_level slider
value_label = tk.Label(root, text="Sea Level")
value_label.place(x = 675, y = 195, width = 100) 

sea_lvl = tk.IntVar()
sea_lvl.set(63)

slider = tk.Scale(root, from_=-64, to=256, orient=tk.VERTICAL, variable=sea_lvl)
slider.place(x=695, y=215, width=100, height=180)

root.mainloop()