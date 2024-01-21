#!/usr/bin/env python3

import argparse
from pathlib import Path
from os import chmod
import stat

FILE_CONTENTS = """#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

def main():
    MainWindow().mainloop()

if __name__ == '__main__':
    main()
"""

def write_tkinter_app_file(tkinter_source_file: Path):
    if tkinter_source_file.exists():
        overwrite = input(f'The file "{str(tkinter_source_file)}" already '
                           'exists. Do you want to overwrite it? (y/N) ')
        if overwrite.lower().strip() != 'y':
            return 
    tkinter_source_file.write_text(FILE_CONTENTS)
    chmod(tkinter_source_file, 
             stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)

def setup():
    parser = argparse.ArgumentParser()
    parser.add_argument('tkinter_source_file', type=Path)
    return parser.parse_args()

def main():
    args = setup()
    tkinter_source_file = args.tkinter_source_file
    write_tkinter_app_file(tkinter_source_file)


if __name__ == '__main__':
    main()
