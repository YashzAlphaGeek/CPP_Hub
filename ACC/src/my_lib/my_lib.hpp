#pragma once

namespace acc {

class Vehicle {
public:
    Vehicle(double max_acceleration, double max_deceleration);

    void update(double throttle, double dt);
    double get_speed() const;

private:
    double speed_;
    double max_acc_;
    double max_dec_;
};

class CruiseController {
public:
    CruiseController(double target_speed);

    double compute_throttle(double current_speed) const;

private:
    double target_speed_;
};

} // namespace acc
