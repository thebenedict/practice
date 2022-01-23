#!/usr/bin/env python3

from datetime import datetime
from pathlib import Path
import argparse
import os
import random
import shutil


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--count",
        default=3,
        type=int,
        help="number of problems in the problem set",
    )
    args = parser.parse_args()

    exercise_paths = [path for path in Path("exercises").rglob("*.py")]
    outputdir = f'work/{datetime.now().strftime("%Y-%m-%d")}'

    os.mkdir(outputdir)
    for f in random.sample(exercise_paths, args.count):
        shutil.copy(f, outputdir)


if __name__ == "__main__":
    main()
