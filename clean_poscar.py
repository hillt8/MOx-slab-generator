#!/usr/bin/env python3
"""
===================================================
 clean_poscar.py - Clean and reorder a POSCAR file
===================================================

Usage:
    python clean_poscar.py [-i INPUT] [-a MODE] [-o OUTPUT]

Description:
    - Cleans a messy POSCAR file from ASE surface generator
    - Reorders atom types to group all atoms of the same element
    - Outputs a clean POSCAR with either Cartesian or Direct coordinates

Arguments:
    -i, --input     Input POSCAR file (default: POSCAR_slab)
    -a, --axis      Coordinate mode: 'direct' or 'cartesian' (default: direct)
    -o, --output    Output file name (default: POSCAR_final)

Example:
    python clean_poscar.py -i dirty_POSCAR -a cartesian -o clean_POSCAR

Author: [Thomas Hill, Cardiff University, 08/04/2025, Supervisor: C.R.A. Catlow]
"""

import argparse
from ase.io import read, write
from ase import Atoms

# === Argument parser ===
parser = argparse.ArgumentParser(
    description="Clean and reorder a POSCAR file.",
    epilog="Example: python clean_poscar.py -i dirty_POSCAR -a cartesian -o clean_POSCAR",
    formatter_class=argparse.RawDescriptionHelpFormatter
)
parser.add_argument('-i', '--input', type=str, default='POSCAR_slab', help='Input POSCAR file (default: POSCAR_slab)')
parser.add_argument('-a', '--axis', choices=['direct', 'cartesian'], default='direct', help='Coordinate type (default: direct)')
parser.add_argument('-o', '--output', type=str, default='POSCAR_final', help='Output POSCAR file (default: POSCAR_final)')
args = parser.parse_args()

# === Load structure ===
atoms = read(args.input, format='vasp')
print(f"? Loaded structure from {args.input}")

# === Reorder atoms by element ===
symbols = atoms.get_chemical_symbols()
unique = sorted(set(symbols), key=symbols.index)
grouped_indices = [i for u in unique for i, s in enumerate(symbols) if s == u]
reordered = atoms[grouped_indices]

# === Set coordinate type ===
if args.axis == 'direct':
    reordered.set_scaled_positions(reordered.get_scaled_positions())
    coord_type = 'Direct'
else:
    reordered.set_positions(reordered.get_positions())
    coord_type = 'Cartesian'

print(f"?? Reordered atoms by type: {' '.join(unique)}")
print(f"?? Using {coord_type} coordinates")

# === Write cleaned POSCAR ===
write(args.output, reordered, format='vasp')
print(f"? Clean POSCAR written to {args.output}")
