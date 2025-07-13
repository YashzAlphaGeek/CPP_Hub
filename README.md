# 🚗 Adaptive Cruise Control (ACC) Simulation – C++ Modern Project

A lightweight simulation of an **Adaptive Cruise Control (ACC)** system written in **Modern C++ (C++17)**, demonstrating core automotive logic in a modular structure using `CMake`.

---

## 🧭 Overview

This project simulates a vehicle using basic physics and applies a simple **proportional controller** to maintain a target speed.

It is structured for clarity, testability, and easy extension into more realistic automotive simulation environments like ROS2 or embedded RTOS-based platforms.

---

## ⚙️ Requirements

- C++17-compatible compiler (GCC 9+, Clang, or MSVC)
- [CMake ≥ 3.15](https://cmake.org/)
- `make` or another CMake-supported build tool (Ninja, NMake, etc.)
- Git Bash / WSL / Terminal (recommended for Windows)

---

## 🚀 Building & Running

### 🛠 Prepare and build the project

```bash
make prepare
cd build
cmake .. -DCOMPILE_EXECUTABLE=ON
cmake --build .
```

## 🚀 Run the simulation

```bash
./app/acc_sim
```

You’ll see console output like this:

```bash
Time:   0.0s | Speed: 0.00 m/s
Time:   0.1s | Speed: 0.30 m/s
...
Time:  10.0s | Speed: 29.90 m/s
```

