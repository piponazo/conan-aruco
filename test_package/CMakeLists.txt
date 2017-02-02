project(ArUcoTest)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_set_find_paths()

find_package(ArUco REQUIRED)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

message("ARUCO_LIBRARIES: ${ARUCO_LIBRARIES}")
message("ARUCO_INCLUDE_DIRS: ${ARUCO_INCLUDE_DIRS}")

add_executable(test main.cpp)
target_link_libraries(test aruco)

set_property(TARGET test PROPERTY CXX_STANDARD 11)
