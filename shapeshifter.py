#!/usr/bin/python3

import sys, os
import pyvista
import gmsh
import tetgen

if len(sys.argv) < 3:
    print("Usage: python ./converter.py <input-file> <output-file>")
    print("Supported output formats are '.obj' (surface) or '.mesh' (volumetric)")
    sys.exit(1)

input_file, output_file = sys.argv[1], sys.argv[2]
file_type = output_file.split('.')[-1]

print(f"Converting '.{input_file.split('.')[-1]}' to '.{file_type}'")
if file_type == "obj":
    pyvista.save_meshio("temp.stl", pyvista.read(input_file))
    gmsh.initialize()
    gmsh.open("temp.stl")
    gmsh.write("temp.stl")
    pyvista.save_meshio(output_file, pyvista.read("temp.stl"))
    os.remove("temp.stl")
elif file_type == "mesh":
    tet_mesh = tetgen.TetGen(pyvista.read(input_file))
    tet_mesh.tetrahedralize()
    tet_mesh.grid.save("temp.vtu")
    pyvista.save_meshio(output_file, pyvista.read("temp.vtu"))
    os.remove("temp.vtu")
else:
    print(f"!!! Error: '{file_type}' is an unsupported output format. Supported output formats are '.obj' (surface) or '.mesh' (volumetric).")
    sys.exit(1)

print("> Success")
sys.exit(0)
