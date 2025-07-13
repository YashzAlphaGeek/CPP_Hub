# C++ Hub

## Project Kick Start

![](https://github.com/YashzAlphaGeek/CPP_Hub/blob/master/ProjectKickStart/project_structure_with_cmake_deps.png)

# Visualization Of Project Structure

This project includes tools and instructions to generate a visual graph of your project's folder structure **and** the dependencies between `CMakeLists.txt` files using Graphviz.

---

## Prerequisites

- **Python 3.x**  
- **Graphviz** installed and accessible via the `dot` command
- **CMake**
- **make** (or a compatible alternative like `nmake` or Ninja on Windows)

---

## Generating the Project Structure Graph

1. **Run the Python script** that generates a DOT file representing your project’s directory structure and CMake dependencies:

    ```bash
    python generate_project_structure.py
    ```

    This script scans your project recursively, ignoring `build/`, `docs/`, and `.vscode/` folders.

2. **Generate a PNG image** from the generated DOT file:

    ```bash
    dot -Tpng project_structure_with_cmake_deps.dot -o project_structure_with_cmake_deps.png
    ```

3. **View the generated image** (`project_structure_with_cmake_deps.png`) to inspect your project layout.

---

## Building the Project

Follow these steps to build the project from source using `make` and `cmake`:

```bash
make prepare          # Cleans and creates the build directory
cd build              # Navigate into the build directory
cmake ..              # Generate CMake build files
cmake .. -DCOMPILE_EXECUTABLE=ON   # (Optional) Enable additional compilation flags
cmake --build .       # Build the project

---

## How It Works

- The script traverses the project directory and creates nodes for folders and files.
- Special nodes are created for each `CMakeLists.txt`.
- It parses `CMakeLists.txt` files to detect `add_subdirectory()` commands.
- Blue arrows indicate dependencies between `CMakeLists.txt` files, reflecting the build hierarchy.

---

## Customization

- To skip other directories, modify the `IGNORE_DIRS` list inside `generate_project_structure.py`.
- The script can be extended to recognize more CMake commands and deeper dependency relations.

---

## Troubleshooting

- If Graphviz shows errors like “graph is too large for cairo-renderer bitmaps,” consider:
  - Using `-Gsize` options to limit graph size.
  - Generating SVG instead of PNG by changing `-Tpng` to `-Tsvg`.

---

