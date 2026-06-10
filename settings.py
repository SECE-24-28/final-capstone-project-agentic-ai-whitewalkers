import os
import json

# Absolute path to the project directory
working_dir = os.path.dirname(os.path.realpath(__file__))

# Load configuration from config.json
config_path = os.path.join(working_dir, "config.json")

print("Config path:", config_path)

with open(config_path, "r", encoding="utf-8") as f:
    content = f.read()

print("Content repr:", repr(content))

config_data = json.loads(content)
