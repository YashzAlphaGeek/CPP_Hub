namespace acc {

class Vehicle {
public:
    Vehicle(double max_acceleration, double max_deceleration);
    virtual ~Vehicle() = default;

    virtual void update(double throttle, double dt);
    virtual double get_speed() const;

private:
    double speed_;
    double max_acc_;
    double max_dec_;
};

class CruiseController {
public:
    explicit CruiseController(double target_speed);
    double compute_throttle(double current_speed) const;

private:
    double target_speed_;
};

}  // namespace acc
