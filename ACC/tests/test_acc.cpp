#include <gtest/gtest.h>
#include <gmock/gmock.h>

#include "../src/my_lib/my_lib.hpp"

using acc::Vehicle;
using acc::CruiseController;

using acc::Vehicle;
using acc::CruiseController;

class MockVehicle : public Vehicle {
public:
    MockVehicle() : Vehicle(  10.0, 10.0) {} 

    MOCK_METHOD(double, get_speed, (), (const, override));
    MOCK_METHOD(void, update, (double throttle, double dt), (override));
};

class CruiseControllerTest : public ::testing::Test {
protected:
    CruiseController controller{10.0};
};

TEST_F(CruiseControllerTest, CalculatesThrottleToReachTarget) {
    MockVehicle mockVehicle;

    EXPECT_CALL(mockVehicle, get_speed())
        .WillOnce(::testing::Return(5.0))
        .WillOnce(::testing::Return(9.0));

    double throttle1 = controller.compute_throttle(mockVehicle.get_speed());
    double throttle2 = controller.compute_throttle(mockVehicle.get_speed());

    EXPECT_GT(throttle1, 0);
    EXPECT_GT(throttle2, 0);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
