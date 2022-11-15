from cymake.constants import Constants
from cymake.compat import *

cmake_minimum_required(3, 8)
project("simple_example")

cache.set(Constants.CMAKE_CXX_STANDARD, 14)

sources = ["main.cpp"]
add_executable("main", sources=sources)

write_cmake_file("CMakeLists.txt")
