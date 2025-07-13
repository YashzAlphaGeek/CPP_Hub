#  Adaptive Cruise Control (ACC) Simulation – C++ Modern Project

A lightweight simulation of an **Adaptive Cruise Control (ACC)** system written in **Modern C++ (C++17)**, demonstrating core automotive logic in a modular structure using `CMake`.

---

##  Overview

This project simulates a vehicle using basic physics and applies a simple **proportional controller** to maintain a target speed.

It is structured for clarity, testability, and easy extension into more realistic automotive simulation environments like ROS2 or embedded RTOS-based platforms.

---

##  Requirements

- C++17-compatible compiler (GCC 9+, Clang, or MSVC)
- [CMake ≥ 3.15](https://cmake.org/)
- `make` or another CMake-supported build tool (Ninja, NMake, etc.)
- Git Bash / WSL / Terminal (recommended for Windows)

---

##  Building & Running

### 🛠 Prepare and build the project

```bash
make prepare
cd build
cmake .. -DCOMPILE_EXECUTABLE=ON
cmake --build .
```

##  Build and Run Tests

To build and execute the unit tests, follow these steps:

```bash
make prepare
cd build
cmake .. -DBUILD_TESTS=ON
cmake --build .
ctest --output-on-failure
```

##  Run the simulation

```bash
./app/acc_sim
```

You’ll see console output like this:

When you run the executable, you’ll see a build metadata banner printed at the top, indicating version and build time:

Build Info:
Built: AdaptiveCruiseControl version 1.0.0 on 2025-07-13 at 23:30:47
Author: Yashwanth | License: MIT
Repo: https://github.com/YashzAlphaGeek/CPP_Hub


```bash
Time:   0.0s | Speed: 0.00 m/s
Time:   0.1s | Speed: 0.30 m/s
...
Time:  10.0s | Speed: 29.90 m/s
```

##  Code & Library Explanation

1. **app/main.cpp**  
   - Entry point of the simulation.  
   - Creates vehicle and controller instances.  
   - Runs a time-stepped loop where the controller calculates throttle to maintain target speed.  
   - Updates vehicle speed based on throttle input.  
   - Prints simulation status on the console.  

2. **src/my_lib/my_lib.hpp and my_lib.cpp**  
   These files implement the core ACC library:  

   - **Vehicle class:** Models the vehicle’s speed dynamics responding to throttle input.  
   - **CruiseController class:** Implements a proportional controller adjusting throttle based on speed error (target vs. current speed).  

   This separation:  
   - Keeps the simulation logic modular and reusable.  
   - Enables easy testing and extension.  
   - Allows the app code to focus on simulation flow without physics or control details.  

##  Core Logic of ACC

The heart of this simulation is a **Proportional Controller (P-controller)** used to regulate vehicle speed.

```cpp
throttle = Kp * (targetSpeed - currentSpeed)
```

targetSpeed: Desired speed (e.g., 30 m/s).

currentSpeed: Real-time speed from the Vehicle object.

Kp: Proportional gain (e.g., 0.5) — determines how aggressively the controller reacts.

## Vehicle Dynamics

```cpp
acceleration = throttle * maxAccelerationFactor
speed += acceleration * dt
```

A basic linear model assumes throttle directly impacts acceleration.

The vehicle updates its speed based on the acceleration and time delta (dt)