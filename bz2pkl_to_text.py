"""Document"""
import bz2
import pickle
import sys
from pathlib import Path

import pandas as pd


def main():
    file = CmdLineArgFile()
    file.get_info()

    print(f"\n>> Decompress file : {Path(file.path).name}")
    decompressed = load_compress_file(file.path)

    print(f">> Save file       : {Path(file.name)}.tsv")
    text = ToText(decompressed, file.name)
    text.save()


def load_compress_file(file_name):
    with bz2.BZ2File(file_name, 'rb') as f:
        pkl = f.read()
    return pickle.loads(pkl)


class Params:
    extensions = [
        '.pkl',
        '.bz2'
    ]


class CmdLineArgFile:
    """
    :type path: str | None
    :type name: str | None
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
            if ext in Params.extensions:
                self.name = self.name.replace(ext, '')


class ToText:
    def __init__(self, obj, filename):
        self.obj = obj
        self.file = f"{filename}.tsv"

    def save(self):
        if isinstance(self.obj, (pd.Series, pd.DataFrame)):
            self._save_pandas()
            return

        raise TypeError(f"{type(self.obj)} is not compatible")

    def _save_pandas(self):
        self.obj.to_csv(self.file, sep='\t', encoding='utf-8')


if __name__ == '__main__':
    main()
