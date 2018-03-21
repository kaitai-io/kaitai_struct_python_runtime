import os
from setuptools import setup
from setuptools.config import read_configuration

this_dir = os.path.dirname(__file__)
cfg = read_configuration(os.path.join(this_dir, 'setup.cfg'))
#print(cfg)
cfg["options"].update(cfg["metadata"])
cfg = cfg["options"]

setup(**cfg)
