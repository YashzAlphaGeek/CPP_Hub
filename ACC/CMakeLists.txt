cmake_minimum_required(VERSION 3.15)

project(AdaptiveCruiseControl VERSION 1.0.0 LANGUAGES CXX)

# C++ settings
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(PROJECT_INFO_HEADER_DIR ${CMAKE_BINARY_DIR}/configured)
set(CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake/")


option(ENABLE_TESTING "Enable a Unit Testing Build" ON)

option(ENABLE_WARNINGS "Enable compiler warnings for a target" ON)
option(ENABLE_WARNINGS_AS_ERRORS "Enable compiler warnings as errors" OFF)

option(ENABLE_SANITIZE_ADDR "Enable address sanitizer" ON)
option(ENABLE_SANITIZE_UNDEF "Enable undefined sanitizer" ON)

# Configurable build options
option(COMPILE_EXECUTABLE "Build the main ACC simulation executable" ON)
option(BUILD_TESTS "Build unit tests" OFF)

# Configure file for build settings
add_subdirectory(configured)

# Core library
add_subdirectory(src)

if (BUILD_TESTS)
    include(FetchContent)

    FetchContent_Declare(
      googletest
      GIT_REPOSITORY https://github.com/google/googletest.git
      GIT_TAG v1.13.0 
    )

    set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
    FetchContent_MakeAvailable(googletest)

    enable_testing()
    add_subdirectory(tests)
endif()

# Main app (simulation)
if (COMPILE_EXECUTABLE)
    add_subdirectory(app)
endif()