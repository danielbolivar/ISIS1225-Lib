# impoting the path to the DISCLib folder
import os
import sys

# import all the modules in the DataStructures namespaces
# M1
from .arraylist import ArrayList
from .singlelinkedlist import SingleLinked
from .doublelinkedlist import DoubleLinked
assert ArrayList
assert SingleLinked
assert DoubleLinked

# config the path to the DISCLib folder
# TODO this used to be in config.py
file_path = os.path.join(os.path.dirname(__file__), '..', '..')
file_dir = os.path.dirname(os.path.realpath('__file__'))
# sys.path.insert(0, os.path.abspath(file_path))
sys.path.append(os.path.abspath(file_path))

