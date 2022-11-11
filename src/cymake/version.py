from dataclasses import dataclass
from typing import Optional

@dataclass
class Version:
    major: int
    minor: int
    build: Optional[int]

    def __str__(self) -> str:
        ver_str = f"{self.major}.{self.minor}"

        if self.build is not None:
            ver_str += f".{self.build}"

        return ver_str
