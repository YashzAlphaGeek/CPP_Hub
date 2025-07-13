#include "my_lib.hpp"
#include <algorithm>

namespace acc {

Vehicle::Vehicle(double max_acc, double max_dec)
    : speed_(0.0), max_acc_(max_acc), max_dec_(max_dec) {}

void Vehicle::update(double throttle, double dt) {
    double acc = std::clamp(throttle, -1.0, 1.0);
    acc *= (acc >= 0 ? max_acc_ : max_dec_);
    speed_ += acc * dt;
    speed_ = std::max(0.0, speed_);
}

double Vehicle::get_speed() const {
    return speed_;
}

CruiseController::CruiseController(double target_speed)
    : target_speed_(target_speed) {}

double CruiseController::compute_throttle(double current_speed) const {
    double error = target_speed_ - current_speed;
    return std::clamp(error * 0.1, -1.0, 1.0);

}
} // namespace acc
