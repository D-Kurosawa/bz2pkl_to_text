"""Pickle object compress and decompress"""
import bz2
import pickle


def loads(compress_obj):
    return pickle.loads(bz2.decompress(compress_obj))


def dumps(obj, compress_level=1):
    return bz2.compress(pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL),
                        compresslevel=compress_level)


def load(file_name):
    with bz2.BZ2File(file_name, 'rb') as f:
        pkl = f.read()
    return pickle.loads(pkl)


def dump(obj, file_name, compress_level=1):
    with bz2.BZ2File(file_name, 'wb', compresslevel=compress_level) as f:
        f.write(pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL))


if __name__ == '__main__':
    pass
