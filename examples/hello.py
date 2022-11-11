from cymake import Project, Constants, Executable, Version

project = Project(name="simple_example", cmake_minimum=Version(3, 8))

project.cache.set(Constants.CMAKE_CXX_STANDARD, 14)

sources = ["main.cpp"]
main = Executable("main")
main.set_sources(sources)

project.add_executable(main)

project.write_cmake_file("CMakeLists.txt")
