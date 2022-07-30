cmake_minimum_required(VERSION 3.15)
project(opencv)

set(CMAKE_CXX_STANDARD 14)

add_executable(opencv
        code/c++/main.cpp
        code/c++/part1.h
        code/c++/part1.cpp
        )

set(OpenCV_DIR D:/github/makeopencv/build/install) # 编译好的
find_package(OpenCV REQUIRED)

message(STATUS "OpenCV library status:")
message(STATUS "version: ${OpenCV_VERSION}")
message(STATUS "libraries: ${OpenCV_LIBS}")
message(STATUS "include path: ${OpenCV_INCLUDE_DIRS}")

include_directories(${OpenCV_INCLUDE_DIRS})

target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS})
