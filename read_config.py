import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)


def get_config(config_key):
    return data[config_key]