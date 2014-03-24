import glob
import fileinput
import sys
import os

def modify(input_dir, file_reg, func, args=None):
    """Run func and replace output for every line in the files matching
    file_reg in input_dir."""
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


def func(input_dir, file_reg, func, args=None, *, encoding='utf-8'):
    """Run func for every line in the files matching file_reg in input_dir."""
    with fileinput.input(glob.glob(input_dir + file_reg),
                         openhook=fileinput.hook_encoded(encoding)) as f:
        for line in f:
            try:
                if args:
                    func(line, *args)
                else:
                    func(line)
            except Exception:
                print(line)
                raise


def rename(input_dir, file_reg, prefix='', suffix='', *, ext=None,
           ext_suffix=None):
    """Add the prefix and suffix to every file matching file_reg in
    input_dir."""
    for f in glob.glob(input_dir + file_reg):
        path = os.path.split(f)
        fname = os.path.splitext(path[1])
        if ext is None:
            cext = fname[1]
        else:
            cext = ext

        if ext_suffix is None:
            cext_suffix = ''
        else:
            cext_suffix = ext_suffix
        os.rename(f, path[0] + '/' + prefix + fname[0] + suffix + cext +
                  cext_suffix)
