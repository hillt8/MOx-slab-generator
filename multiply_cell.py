#!/usr/bin/env python3
"""
====================================================
 multiply_cell.py - Create a supercell from a POSCAR
====================================================

Usage:
    python multiply_cell.py -s NX NY NZ [-i INPUT] [-o OUTPUT]

Description:
    - Reads a POSCAR file (default: POSCAR)
    - Multiplies the cell in x, y, and z directions
    - Outputs a supercell in VASP format (default: POSCAR_super)

Arguments:
    -s, --size     Supercell size as three integers (e.g. -s 2 2 2)
    -i, --input    Input POSCAR file (default: POSCAR)
    -o, --output   Output file name (default: POSCAR_super)

Example:
    python multiply_cell.py -s 2 2 1 -i slab.vasp -o slab_2x2.vasp

Author: [Thomas Hill, Cardiff University, 08/04/2025, Supervisor: C.R.A. Catlow]
"""

import argparse
from ase.io import read, write
from ase.build import make_supercell

# === Argument parser ===
parser = argparse.ArgumentParser(
    description="Create a supercell by multiplying the unit cell.",
    epilog="Example: python multiply_cell.py -s 2 2 1 -i POSCAR -o supercell.vasp",
    formatter_class=argparse.RawDescriptionHelpFormatter
)
parser.add_argument('-s', '--size', nargs=3, type=int, required=True, help='Multipliers for a, b, c directions (e.g. -s 2 2 2)')
parser.add_argument('-i', '--input', type=str, default='POSCAR', help='Input POSCAR file (default: POSCAR)')
parser.add_argument('-o', '--output', type=str, default='POSCAR_super', help='Output file name (default: POSCAR_super)')

args = parser.parse_args()

# === Load structure ===
atoms = read(args.input, format='vasp')
print(f"? Loaded structure from {args.input}")

# === Create supercell ===
supercell = atoms.repeat(args.size)
print(f"?? Multiplied cell by {args.size}")

# === Write output ===
write(args.output, supercell, format='vasp')
print(f"? Supercell written to {args.output}")
