import os

import yaml

CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config.yaml')

with open(CONFIG_PATH) as f:
    data = yaml.safe_load(f)


def get_config(config_key):
    return data[config_key]
