from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


class CodeGenerator(ABC):
    @abstractmethod
    def code(self) -> str:
        ...


@dataclass
class Indent:
    offset: int = 0


@dataclass
class LineEnd:
    count: int = 1


ControlSequence = Indent | LineEnd


class DefaultFormatter:
    @property
    def indent(self):
        return Indent(4)

    @property
    def unindent(self):
        return Indent(-4)

    @property
    def newline(self):
        return LineEnd()

    def newlines(self, count: int):
        return LineEnd(count)

    def lines(self, line: str, *_lines: List[str | ControlSequence]) -> str:
        result = ""

        current_indent = 0
        for line in [line, *_lines]:
            match line:
                case LineEnd(count):
                    result += "\n" * count
                case Indent(offset):
                    print(offset)
                    current_indent += offset
                case str(str_value):
                    if result != "":
                        result += "\n"
                    result += f"{' '*current_indent}{str_value}"

        return result


DefaultFormatter = DefaultFormatter()