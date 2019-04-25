import os
import sys
import time
from tkinter import filedialog
import tkinter

default_path = "C:\Riot Games\\League of Legends"

file_content = ""

basePath = os.getcwd()

def get_path():
    tkinter.Tk().withdraw()
    browse_path = filedialog.askdirectory()
    return (browse_path)

def write_file(content):
    with open(basePath+"\path.txt", 'w') as a:
        a.write(content)


with open("path.txt",'r') as a:
    try:
        file_content = a.read().split("\n")[0]
    except:
        file_content = "null"

try:
    os.chdir(file_content)
    riot_dir = True
except:
    riot_dir = False

if not riot_dir:
    given_path = get_path()
    while not given_path.endswith("League of Legends"):
        given_path = get_path()
    os.chdir(given_path)

sub_path = "\Config\PersistedSettings.json"
print(os.getcwd())
write_file(os.getcwd())

os.chdir(os.getcwd()+"\Config")
