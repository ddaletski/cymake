from typing import Any, Optional
from typing_extensions import Self


class Cache:
    def __init__(self):
        self._dict = {}

    def set(self, key: str, value: Any):
        self._dict[key] = value

    def get(self, key: str) -> Optional[Any]:
        return self._dict.get(key)

    def update(self, other: Self):
        self._dict.update(other._dict)
