import os
import gnupg
import time
from colorama import *
from art import *
import sys
import py2exe
from distutils.core import setup
setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    console = [{'script': "cppm.py"}],
    zipfile = None,
)
