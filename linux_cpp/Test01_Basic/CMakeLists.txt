cmake_minimum_required(VERSION 3.5)

project(opencv-hello-world)

#set(CMAKE_CXX_STANDARD 11)
#set(CMAKE_CXX_STANDARD_REQUIRED ON)
#set(CMAKE_CXX_EXTENSIONS OFF)
#set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fopenmp")

find_package(OpenCV REQUIRED)
include_directories(${CMAKE_CURRENT_SOURCE_DIR} ${OpenCV_INCLUDE_DIRS})

add_executable(opencv-helloworld helloworld.cpp)
target_link_libraries(opencv-helloworld ${OpenCV_LIBS})
