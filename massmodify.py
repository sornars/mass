import glob
import fileinput
import sys


def modify(input_dir, file_reg, func):
    """Run func for every line in the files matching file_reg in input_dir."""
    with fileinput.input(glob.glob(input_dir + file_reg), inplace=True) as f:
        for line in f:
            sys.stdout.write(func(line))
