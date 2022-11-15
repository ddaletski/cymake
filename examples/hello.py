from cymake import Project, Constants, Executable, Library, Version

project = Project(name="simple_example", cmake_minimum=Version(3, 8))

project.cache.set(Constants.CMAKE_CXX_STANDARD, 14)

lib = Library.shared("mylib")
lib.sources = ["lib.hpp"]

main = Executable("main")
main.sources = ["main.cpp"]

project.add_targets(lib, main)

project.write_cmake_file("CMakeLists.txt")
