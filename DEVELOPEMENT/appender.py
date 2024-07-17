data = [
    "minecraft:mushroom_field",
    "minecraft:frozen_plains",
    "minecraft:deep_frozen_ocean",
    "minecraft:frozen_ocean",
    "minecraft:deep_cold_ocean",
    "minecraft:cold_ocean",
    "minecraft:deep_ocean",
    "minecraft:ocean",
    "minecraft:deep_lukewarm_ocean",
    "minecraft:warm_ocean",
    "minecraft:stony_shore",
    "minecraft:swamp",
    "minecraft:mangrove_swamp",
    "minecraft:snowy_slopes",
    "minecraft:snowy_plains",
    "minecraft:snowy_beach",
    "minecraft:windswept_gravelly_hills",
    "minecraft:grove",
    "minecraft:windswept_hills",
    "minecraft:snowy_taiga",
    "minecraft:windswept_forest",
    "minecraft:taiga",
    "minecraft:plains",
    "minecraft:meadow",
    "minecraft:beach",
    "minecraft:forest",
    "minecraft:old_growth_spruce_taiga",
    "minecraft:flower_forest",
    "minecraft:birch_forest",
    "minecraft:dark_forest",
    "minecraft:savanna_plateau",
    "minecraft:savanna",
    "minecraft:jungle",
    "minecraft:badlands",
    "minecraft:desert",
    "minecraft:wooded_badlands",
    "minecraft:jagged_peaks",
    "minecraft:stony_peaks",
    "minecraft:frozen_river",
    "minecraft:river",
    "minecraft:ice_spikes",
    "minecraft:old_growth_pine_taiga",
    "minecraft:sunflower_plains",
    "minecraft:old_growth_birch_forest",
    "minecraft:sparse_jungle",
    "minecraft:bamboo_jungle",
    "minecraft:eroded_badlands",
    "minecraft:windswept_savanna",
    "minecraft:frozen_peaks",
    "minecraft:dripstone_caves",
    "minecraft:lush_caves",
    "minecraft:deep_dark"
]
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [0]
res = [""]
def sort(biome):
    letter = biome[10]
    print(letter)
    i = 0
    while get_idx(letter)>numbers[i]:
        i += 1
        if i>=len(numbers):
            break
    numbers.insert(i,get_idx(letter))
    res.insert(i, biome)

def get_idx(letter):
    for i in range(26):
        if abc[i] == letter:
            return i
        
for i in range(len(data)):
    sort(data[i])
    print(numbers)
res.pop(0)
print(res)
        
while False: #True:
    a = "minecraft:" + input(str("Biome hinzufügen "))
    p_a = "abc"
    if not a in data and a != p_a:
        data.append(a)
        print("added")
        p_a = a
        a = ""
    else: 
        print("included")
        p_a = a
        a = ""
