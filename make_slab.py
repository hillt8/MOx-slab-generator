# make_slab.py
# --------------------------------------------
# How to run this script:
# python make_slab.py -m [h k l] -l [layers] -v [vacuum] -o [output_name]
# Example:
# python make_slab.py -m 1 1 1 -l 8 -v 15 -o slab_111.vasp
# --------------------------------------------

import argparse
from ase.io import read, write
from ase.build import surface

# === Argument parser ===
parser = argparse.ArgumentParser(description="Create a slab from a primitive POSCAR file.")
parser.add_argument('-m', '--miller', nargs=3, type=int, required=True, help='Miller indices h k l (e.g. -m 1 1 1)')
parser.add_argument('-l', '--layers', type=int, default=8, help='Number of atomic layers (default: 8)')
parser.add_argument('-v', '--vacuum', type=float, default=15.0, help='Vacuum thickness in angstroms (default: 15.0)')
parser.add_argument('-i', '--input', type=str, default='POSCAR_prim', help='Input POSCAR file (default: POSCAR_prim)')
parser.add_argument('-o', '--output', type=str, default='POSCAR_slab', help='Custom output filename (e.g. slab.vasp)')

args = parser.parse_args()

hkl = tuple(args.miller)
layers = args.layers
vacuum = args.vacuum
input_file = args.input

# Determine output file name
if args.output:
    output_file = args.output
else:
    output_file = f"POSCAR_slab_{hkl[0]}{hkl[1]}{hkl[2]}"

# === Step 1: Load structure ===
atoms = read(input_file, format='vasp')
print(f"✅ Loaded structure from {input_file}")

# === Step 2: Create the slab ===
slab = surface(atoms, hkl, layers, vacuum=vacuum)
slab.center(vacuum=vacuum, axis=2)
print(f"🧱 Built slab with Miller indices {hkl}, {layers} layers, {vacuum} Å vacuum")

# === Step 3: Export to POSCAR ===
write(output_file, slab, format='vasp')
print(f"✅ Slab written to {output_file}")
