add_executable(acc_gmock_tests
    test_acc.cpp
)

target_link_libraries(acc_gmock_tests
    PRIVATE
    gtest_main
    gmock
    my_lib
)

target_include_directories(acc_gmock_tests PRIVATE
    ${PROJECT_SOURCE_DIR}/src
)

# Automatically register Google Test tests with CTest
include(GoogleTest)
gtest_discover_tests(acc_gmock_tests)
