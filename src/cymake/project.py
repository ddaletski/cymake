from pathlib import Path
from typing import List

from .cache import Cache
from .common import DefaultFormatter, CodeGenerator
from .targets import Executable, Target
from .version import Version


class Project(CodeGenerator):
    def __init__(self, name: str, cmake_minimum: Version):
        self._name = name
        self._cmake_version = cmake_minimum
        self._cache = Cache()
        self._targets: List[Target] = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def cmake_version(self) -> Version:
        return self._cmake_version

    @property
    def cache(self) -> Cache:
        return self._cache

    def add_targets(self, target: Target, *_targets: List[Target]):
        self._targets.append(target)
        self._targets.extend(_targets)

    def code(self) -> str:
        targets_code = DefaultFormatter.lines(
            *(exe.code() for exe in self._targets)
        )

        return DefaultFormatter.lines(
            f"cmake_minimum_required(VERSION {self.cmake_version})",
            f"project({self.name})",
            DefaultFormatter.newlines(2),
            targets_code,
        )

    def write_cmake_file(self, path: Path | str):
        content = self.code()

        path = Path(path)
        path.parent.mkdir(exist_ok=True)

        with open(path, "w") as f:
            f.write(content)
