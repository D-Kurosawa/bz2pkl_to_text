"""Document"""
import bz2
import pickle
import sys
from pathlib import Path

from src import elaptime as et


@et.app_time
def main():
    file = CmdLineArgFile()
    file.get_info()

    print(file.path)
    print(file.name)

    decompressed = load_compress_file(file.path)
    print(decompressed)


def load_compress_file(file_name):
    with bz2.BZ2File(file_name, 'rb') as f:
        pkl = f.read()
    return pickle.loads(pkl)


class CmdLineArgFile:
    """
    :type path: str
    :type name: str
    """

    def __init__(self):
        self.path = None
        self.name = None

    def get_info(self):
        self._get_command_line_argument()
        self._is_exist()
        self._is_file()
        self._get_file_name()

    def _get_command_line_argument(self):
        try:
            self.path = sys.argv[1]
        except IndexError:
            raise IndexError('Not found command line argument')
        except Exception:
            raise Exception

    def _is_exist(self):
        if not Path(self.path).exists():
            raise FileNotFoundError(self.path)

    def _is_file(self):
        if not Path(self.path).is_file():
            raise FileExistsError(self.path)

    def _get_file_name(self):
        self.name = self.path

        exts = Path(self.name).suffixes
        for ext in exts:
            self.name = self.name.replace(ext, '')


if __name__ == '__main__':
    main()
