
# Shapeshifter

Convert 3D model formats. Supports `.obj` and `.mesh` outputs.

## Requirements

- Install Python 3 and pip:
```bash
sudo apt install python3 python3-pip
```
- Install necessary libraries:
```bash
python3 -m pip install -r ./requirements.txt
```

## Usage

Use the `converter.py` script to convert 3D models:

```bash
python ./converter.py <input-file> <output-file>
```

- `<input-file>`: A 3D mesh file compatible with [pyvista](https://docs.pyvista.org/version/stable/api/utilities/_autosummary/pyvista.read.html#pyvista.read), which leverages formats defined by [vtk](https://docs.vtk.org/en/latest/design_documents/VTKFileFormats.html) and [meshio](https://github.com/nschloe/meshio).
- `<output-file>`: Specify the output format as `.obj` (surface) or `.mesh` (volumetric).

### Examples

Convert an STL to OBJ format:
```bash
python ./converter.py ./model.stl ./model.obj
```

Convert an STL to MESH format:
```bash
python ./converter.py ./model.stl ./model.mesh
```
