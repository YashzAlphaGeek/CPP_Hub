add_executable(acc_sim main.cpp)
target_link_libraries(acc_sim PRIVATE my_lib)
target_include_directories(acc_sim PRIVATE ../src/my_lib)
include_directories(${PROJECT_INFO_HEADER_DIR})

