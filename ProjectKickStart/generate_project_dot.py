import os
import re

IGNORE_DIRS = {'build', 'docs', '.vscode'}
CMAKE_FILE_NAME = "CMakeLists.txt"

def escape_label(label):
    return label.replace('"', '\\"')

def parse_cmake_for_subdirs(cmake_path):
    subdirs = []
    try:
        with open(cmake_path, 'r', encoding='utf-8') as f:
            content = f.read()
            matches = re.findall(r'add_subdirectory\s*\(\s*([^\s\)]+)', content, re.IGNORECASE)
            for m in matches:
                subdir = m.strip('\"\'')
                subdirs.append(subdir)
    except Exception:
        pass
    return subdirs

def generate_dot_for_directory(root_dir, dot_file_path):
    node_id = 0
    nodes = []
    edges = []

    cmake_nodes = {}  # path (relative from root) -> node_id

    def add_node(name, label, shape="folder", color=None, style=None):
        nonlocal node_id
        nid = f"node{node_id}"
        node_id += 1
        attr = f'label="{escape_label(label)}" shape={shape} margin=0.2 fontsize=10'
        if color:
            attr += f' color="{color}"'
            # For orange filled nodes, set font color black for visibility
            if color.lower() == "orange":
                attr += ' fontcolor="black"'
            else:
                attr += f' fontcolor="{color}"'
        if style:
            attr += f' style="{style}"'
        nodes.append(f'{nid} [{attr}];')
        return nid

    def walk_dir(path, parent_id=None, rel_path=""):
        basename = os.path.basename(path) or path
        if basename in IGNORE_DIRS:
            return

        current_id = add_node(basename, basename, "folder")
        if parent_id:
            edges.append(f"{parent_id} -> {current_id};")

        try:
            for entry in sorted(os.listdir(path)):
                if entry in IGNORE_DIRS:
                    continue
                full_path = os.path.join(path, entry)
                entry_rel_path = os.path.join(rel_path, entry) if rel_path else entry
                if os.path.isdir(full_path):
                    walk_dir(full_path, current_id, entry_rel_path)
                else:
                    # Default style for files
                    file_color = None
                    file_style = None

                    if entry == CMAKE_FILE_NAME:
                        # Determine if this is the root/main CMakeLists.txt
                        if entry_rel_path == CMAKE_FILE_NAME:
                            # Root CMakeLists.txt - color it green and bold
                            file_color = "darkgreen"
                            file_style = "bold"
                        else:
                            # Child CMakeLists.txt files - orange and filled
                            file_color = "orange"
                            file_style = "filled"

                        cmake_nodes[entry_rel_path] = None  # placeholder for node id

                    file_id = add_node(entry, entry, "note", file_color, file_style)

                    if entry == CMAKE_FILE_NAME:
                        cmake_nodes[entry_rel_path] = file_id

                    edges.append(f"{current_id} -> {file_id};")

        except PermissionError:
            pass  # skip folders without permission

        return current_id

    walk_dir(root_dir)

    # Now parse cmake dependencies and add edges
    for cmake_rel_path, cmake_node_id in cmake_nodes.items():
        full_cmake_path = os.path.join(root_dir, cmake_rel_path)
        subdirs = parse_cmake_for_subdirs(full_cmake_path)
        for subdir in subdirs:
            base_dir = os.path.dirname(cmake_rel_path)
            sub_cmake_rel_path = os.path.normpath(os.path.join(base_dir, subdir, CMAKE_FILE_NAME))
            if sub_cmake_rel_path in cmake_nodes:
                sub_node_id = cmake_nodes[sub_cmake_rel_path]
                edges.append(f'{cmake_node_id} -> {sub_node_id} [color=blue, label="add_subdirectory", fontcolor=blue];')

    with open(dot_file_path, "w") as f:
        f.write("digraph ProjectStructure {\n")
        f.write("  node [fontname=\"Helvetica\"];\n")
        f.write("  edge [arrowhead=normal];\n")
        f.write("\n".join(nodes) + "\n")
        f.write("\n".join(edges) + "\n")
        f.write("}\n")

if __name__ == "__main__":
    root_project_dir = "/home/yash/StructuringOfProjects"  # Adjust to your path
    output_dot_file = "project_structure_with_cmake_deps.dot"
    generate_dot_for_directory(root_project_dir, output_dot_file)
    print(f"DOT file generated: {output_dot_file}")
