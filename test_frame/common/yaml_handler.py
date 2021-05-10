import yaml
import os
from test_frame.config.path import config_path
ypath=os.path.join(config_path,'config.yaml')
ypath_secret=os.path.join(config_path,'secret.yaml')
def yaml_handler(ypath):
    with open(ypath,encoding='utf-8') as y:
        yaml_data=yaml.load(y,Loader=yaml.SafeLoader)
    return yaml_data


yaml_config=yaml_handler(ypath)
print(type(yaml_config['log']['logger_level']))
yaml_secert_config=yaml_handler(ypath_secret)


# ypath=os.path.join(config_path,'config.yaml')
# print(ypath)
# with open(ypath,encoding='utf-8') as y:
#     yaml_data = yaml.load(y, Loader=yaml.SafeLoader)
#     print(yaml_data)