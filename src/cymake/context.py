from typing import List, Optional

from cymake.cache import Cache
from cymake.project import Project
from cymake.targets import Executable
from cymake.version import Version


class Context:
    def __init__(self):
        self.project_name: Optional[str] = None
        self.executables: List[Executable] = []
        self.version: Optional[Version] = None
        self.cache = Cache()

    def add_executable(self, executable):
        self.executables.append(executable)

    def compile_project(self) -> Project:
        assert self.project_name is not None, "project name must be specified"
        assert self.version is not None, "cmake minimum version must be specified"

        project = Project(name=self.project_name, cmake_version=self.version)
        project.cache.update(self.cache)
        for exe in self.executables:
            project.add_executable(exe)

        return project


global_context = Context()
