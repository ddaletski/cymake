from typing import List


class Executable:
    def __init__(self, name: str):
        self._name = name
        self._sources: List[str] = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def sources(self) -> List[str]:
        return self._sources

    @sources.setter
    def sources(self, value):
        self._sources = value

    def set_sources(self, sources: List[str]):
        self._sources = sources

    def __repr__(self) -> str:
        type_ = type(self)
        module = type_.__module__
        qualname = type_.__qualname__
        return f"<{module}.{qualname}[{self.name}]>"

    def code(self) -> str:
        sources_list_definition = "\n".join([
            f"target_sources({self.name} PRIVATE",
            *["  " + src for src in self._sources],
            ")"
        ])

        return "\n".join([
            f'add_executable({self.name} "")',
            sources_list_definition
        ])
