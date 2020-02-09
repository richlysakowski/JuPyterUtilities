import os
import subprocess
FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

def launch_explorer(path):
    ''' Get and pass current path to user-defined function open_WinExplorer()
        to open Windows Explorer in Python's current working directory.  
        After 2-3 seconds delay Windows Explorer launches with a top-level GUI focus.'''
    # explorer would normally choke on forward slashes
    path = os.path.normpath(path)

    if os.path.isdir(path):
        subprocess.run([FILEBROWSER_PATH, path])
    elif os.path.isfile(path):
        subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])
        
# Open Windows Explorer in the directory where this notebook resides
launch_explorer(os.getcwd())