import enum
from enum import Enum
from typing import List

from .common import CodeGenerator, DefaultFormatter


class Target:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    def __repr__(self) -> str:
        type_ = type(self)
        module = type_.__module__
        qualname = type_.__qualname__
        return f"<{module}.{qualname}[name='{self.name}']>"


class SourceListHolder:
    def __init__(self):
        self._sources: List[str] = []

    @property
    def sources(self) -> List[str]:
        return self._sources

    @sources.setter
    def sources(self, value):
        assert(type(value) == list)
        for src in value:
            assert(type(src) == str)

        self._sources = value


class Executable(Target, SourceListHolder, CodeGenerator):
    def __init__(self, name: str):
        Target.__init__(self, name)
        SourceListHolder.__init__(self)

    def code(self) -> str:
        print(DefaultFormatter.indent)
        return DefaultFormatter.lines(
            f'add_executable({self.name} "")',

            f"target_sources({self.name} PRIVATE",
            DefaultFormatter.indent,
            *self.sources,
            DefaultFormatter.unindent,
            ")"
        )


class LibraryType(Enum):
    SHARED = "SHARED"
    STATIC = "STATIC"
    OBJECT = "OBJECT"


class NormalLibrary(Target, SourceListHolder, CodeGenerator):
    def __init__(self, name: str, kind: LibraryType):
        Target.__init__(self, name)
        SourceListHolder.__init__(self)
        self._kind = kind

    @property
    def kind(self) -> LibraryType:
        return self._kind

    def code(self) -> str:
        return DefaultFormatter.lines(
            f"add_library({self.name} ${self.kind.value}",
            DefaultFormatter.indent,
            *self.sources,
            DefaultFormatter.unindent,
            ")"
        )


class InterfaceLibrary(Target):
    def __init__(self, name: str):
        super().__init__(name)


class Library:
    @ staticmethod
    def shared(name: str) -> NormalLibrary:
        return NormalLibrary(name, LibraryType.SHARED)

    @ staticmethod
    def static(name: str) -> NormalLibrary:
        return NormalLibrary(name, LibraryType.STATIC)

    @ staticmethod
    def interface(name: str) -> NormalLibrary:
        return InterfaceLibrary(name)
