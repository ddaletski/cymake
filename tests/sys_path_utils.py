import sys
from pathlib import Path

from contextlib import contextmanager

@contextmanager
def cymake_in_syspath():
    src_path = str(Path(__file__).absolute().parent.parent / "src")
    sys.path.append(src_path)
    yield
    sys.path.remove(src_path)