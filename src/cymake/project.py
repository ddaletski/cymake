from typing import List
from cymake.cache import Cache
from cymake.targets import Executable

from cymake.version import Version


class Project:
    def __init__(self, name: str, cmake_version: Version):
        self._name = name
        self._cmake_version = cmake_version
        self._cache = Cache()
        self._executables: List[Executable] = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def cmake_version(self) -> Version:
        return self._cmake_version

    @property
    def cache(self) -> Cache:
        return self._cache

    def add_executable(self, exe: Executable):
        self._executables.append(exe)

    def code(self) -> str:
        executables_code = "\n\n".join([exe.code() for exe in self._executables])

        return "\n".join([
            f"cmake_minimum_required(VERSION {self.cmake_version})",
            f"project({self.name})",
            "",
            executables_code,
            ""
        ])