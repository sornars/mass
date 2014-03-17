from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(name='mass',
      version='0.1.0',
      description='Action multiple files in a folder.',
      author='Shivan Sornarajah',
      author_email='ssornarajah@mediaplex.com',
      py_modules=['mass'],
      long_description=readme,
      license=license
      )
