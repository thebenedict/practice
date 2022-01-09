#!/usr/bin/env python3

from datetime import datetime
from pathlib import Path
import shutil, os

def main():
    exercise_paths = [path for path in Path("exercises").rglob("*.py")]
    outputdir = f'work/{datetime.now().strftime("%Y-%m-%d")}'
    
    os.mkdir(outputdir)
    for f in exercise_paths:
        shutil.copy(f, outputdir) 

if __name__ == "__main__":
    main()