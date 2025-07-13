#include <iostream>
#include <iomanip>
#include <chrono>
#include <thread>
#include "../src/my_lib/my_lib.hpp"

int main() {
    acc::Vehicle car(3.0, 5.0); 
    acc::CruiseController controller(30.0); 

    const double dt = 0.1; 

    for (int t = 0; t <= 100; ++t) {
        double current_speed = car.get_speed();
        double throttle = controller.compute_throttle(current_speed);
        car.update(throttle, dt);

        std::cout << "Time: " << std::setw(3) << t * dt
                  << "s | Speed: " << std::fixed << std::setprecision(2)
                  << car.get_speed() << " m/s\n";

        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }

    return 0;
}
