from pathlib import Path
from typing import List, Optional

from .context import global_context as ctx
from .targets import Executable
from .version import Version

cache = ctx.cache


def project(name: str):
    ctx.project_name = name


def add_executable(name: str, sources: List[str]) -> Executable:
    exe = Executable(name)
    exe.set_sources(sources)
    ctx.executables.append(exe)
    return exe


def generate_cmake_file() -> str:
    project = ctx.compile_project()

    return project.code()


def write_cmake_file(path: Path | str):
    content = generate_cmake_file()

    path = Path(path)
    path.parent.mkdir(exist_ok=True)

    with open(path, "w") as f:
        f.write(content)


def cmake_minimum_required(major: int, minor: int = 0, build: Optional[int] = None):
    ctx.version = Version(major, minor, build)
