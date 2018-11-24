"""Usage: 
    docopt_demo.py -h | --help | -v | --version
    docopt_demo.py --path PATH
    docopt_demo.py (new | rm) [--path PATH] [<files>...]
    docopt_demo.py show [--path PATH]
    docopt_demo.py rename (--path PATH NEW_PATH | -f FILE NEW_FILE)

Commands:
    show            Show the files in the Path, default PATH is current Path
    new             Add a new File(s) or a Path, default PATH is current Path
    rm              Remove the file(s) from a Path, default PATH is current Path
    rename          Rename an existing PATH or FILE
Options:
    -h --help          Show this Screen
    -v --version       Show the version
    -p --path          The path to work
    -f --file          The filename
Examples:
    docopt_demp.py --help
    docopt_demo.py --version

Please refer https://docopt.readthedocs.io/en/latest/#
"""

from docopt import docopt
import os

if __name__ == '__main__':
    version = '0.5'
    path = os.getcwd()

    arguments = docopt(__doc__, version=version)
    print(arguments)
