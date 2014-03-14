import glob
import fileinput
import sys


def modify(input_dir, file_reg, func, args=None):
    """Run func for every line in the files matching file_reg in input_dir."""
    with fileinput.input(glob.glob(input_dir + file_reg), inplace=True) as f:
        for line in f:
            try:
                if args:
                    sys.stdout.write(func(line, *args))
                else:
                    sys.stdout.write(func(line))
            except Exception:
                print(line)
                raise


def concat(input_dir, file_reg, output, *, encoding='utf-8'):
    """Concatenate all files matching file_reg in input_dir into output."""
    with fileinput.input(glob.glob(input_dir + file_reg),
                         openhook=fileinput.hook_encoded(encoding)) as f, \
            open(output, 'w', encoding=encoding) as o:
        for line in f:
            try:
                o.write(line)
            except Exception:
                print(line)
                raise


def func(input_dir, file_reg, func, args=None, *, inplace=False):
    with fileinput.input(glob.glob(input_dir + file_reg),
                         inplace=inplace) as f:
        for line in f:
            try:
                if args:
                    func(line, *args)
                else:
                    func(line)
            except Exception:
                print(line)
                raise
