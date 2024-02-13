cmake_minimum_required(VERSION 3.16)
project(cmake_example_project
  VERSION 1.0.0
  DESCRIPTION "Minimal CMake Example Project"
)

file(GLOB_RECURSE SOURCES src/*.cpp include/*.h)

add_executable(cmake_example ${SOURCES})

target_include_directories(cmake_example PUBLIC include)

install(TARGETS cmake_example DESTINATION bin)
