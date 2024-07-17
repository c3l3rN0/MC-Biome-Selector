import json
import os



with open('overworld.json', 'r') as file:
    python_obj = json.load(file)

print(python_obj)
