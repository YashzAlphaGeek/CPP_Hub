# Project metadata
set(PROJECT_DESCRIPTION "Modern C++ Adaptive Cruise Control Simulation")
set(PROJECT_AUTHOR "Yashwanth")
set(PROJECT_LICENSE "MIT")
set(PROJECT_REPOSITORY "https://github.com/YashzAlphaGeek/CPP_Hub")
string(TIMESTAMP PROJECT_BUILD_DATE "%Y-%m-%d")
string(TIMESTAMP PROJECT_BUILD_TIME "%H:%M:%S")

# Configure the header file
configure_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/project_info.hpp.in
    ${CMAKE_CURRENT_BINARY_DIR}/project_info.hpp
    @ONLY
)

# Make it accessible to other targets
set(PROJECT_INFO_HEADER ${CMAKE_CURRENT_BINARY_DIR}/project_info.hpp PARENT_SCOPE)
