import json

existing_json = {
  "dimensions": {
    "minecraft:overworld": {
      "type": "minecraft:overworld",
      "generator": {
        "type": "minecraft:noise",
        "settings": "minecraft:sealevel_overworld",
        "biome_source": {
          "type": "minecraft:multi_noise",
          "biomes": [
            {
              "biome": "minecraft:filler",
              "parameters": {
                "temperature": [
                  -1,
                  -0.45
                ],
                "humidity": [
                  -1,
                  1
                ],
                "continentalness": [
                  -1.05,
                  -0.455
                ],
                "erosion": [
                  -1,
                  1
                ],
                "weirdness": [
                  -1,
                  1
                ],
                "depth": 0,
                "offset": 0
              }
            }
          ]}}}}}

new_biome = [
    {
        "biome": "minecraft:example_biome_1",
        "parameters": {
            "temperature": [
                0.5,
                1.0
            ],
            "humidity": [
                0.2,
                0.8
            ],
            "continentalness": [
                0.3,
                0.7
            ],
            "erosion": [
                0.1,
                0.5
            ],
            "weirdness": [
                0.4,
                0.6
            ],
            "depth": 0.1,
            "offset": 0.2
        }
    },
    {
        "biome": "minecraft:example_biome_2",
        "parameters": {
            "temperature": [
                -0.3,
                0.3
            ],
            "humidity": [
                0.4,
                0.6
            ],
            "continentalness": [
                -0.2,
                0.2
            ],
            "erosion": [
                -0.1,
                0.1
            ],
            "weirdness": [
                0.3,
                0.5
            ],
            "depth": 0.2,
            "offset": 0.3
        }
    },
    {
        "biome": "minecraft:example_biome_2",
        "parameters": {
            "temperature": [
                -0.3,
                0.3
            ],
            "humidity": [
                0.4,
                0.6
            ],
            "continentalness": [
                -0.2,
                0.2
            ],
            "erosion": [
                -0.1,
                0.1
            ],
            "weirdness": [
                0.3,
                0.5
            ],
            "depth": 0.2,
            "offset": 0.3
        }
    }
]


def add(existing, biomes):
    existing["dimensions"]["minecraft:overworld"]["generator"]["biome_source"]["biomes"].extend(biomes)

    existing["dimensions"]["minecraft:overworld"]["generator"]["biome_source"]["biomes"] = [
        biome for biome in existing["dimensions"]["minecraft:overworld"]["generator"]["biome_source"]["biomes"]
        if biome["biome"] != "minecraft:filler"]

    # Speichern der aktualisierten JSON-Datei
    with open('updated_json.json', 'w') as f:
        json.dump(existing, f, indent=2)

add(existing_json, new_biome)