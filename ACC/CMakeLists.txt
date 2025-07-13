cmake_minimum_required(VERSION 3.15)

project(AdaptiveCruiseControl VERSION 1.0.0 LANGUAGES CXX)

# C++ settings
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(PROJECT_INFO_HEADER_DIR ${CMAKE_BINARY_DIR}/configured)

# Configurable build options
option(COMPILE_EXECUTABLE "Build the main ACC simulation executable" ON)
option(BUILD_TESTS "Build unit tests" OFF)

# Configure file for build settings
add_subdirectory(configured)

# Core library
add_subdirectory(src)

# Main app (simulation)
if (COMPILE_EXECUTABLE)
    add_subdirectory(app)
endif()

# Optional: Add test directory
if (BUILD_TESTS)
    enable_testing()
    add_subdirectory(tests)
endif()
