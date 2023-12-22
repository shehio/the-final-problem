import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)

print(data['ip1'])
print(data['ip2'])
print(data['ip3'])

