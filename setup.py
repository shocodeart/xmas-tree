from setuptools import setup


def readfile(filename):
    with open(filename, 'r+') as f:
        return f.read()


setup(
    name="xmas-tree",
    version="2022-10-05:2",
    description="",
    long_description=readfile('README.md'),
    author="Shodmon Ravshanov",
    author_email="shocodeart@gmail.com",
    url="https://github.com/shocodeart/",
    py_modules=['tree/__init__', 'tree/tree_console', 'tree/tree_class'],
    license='',  # readfile('LICENSE'),
    entry_points={
        'console_scripts': [
            'xmas = tree.tree_console:draw'
        ]
    },
)
