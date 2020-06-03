import os
from os import listdir
from os.path import isfile, join
import subprocess


path = os.path.abspath(os.getcwd())
files = [f for f in listdir(path + '/tests/') if isfile(join(path + '/tests/', f))]

for f in files:
    print(f)
    p = subprocess.Popen(['python', 'yaccPatito.py', f])
    p.wait()
    p.terminate()