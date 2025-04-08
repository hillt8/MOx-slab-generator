#!/usr/bin/env python3
"""
=====================================================
 analyze_symmetry.py - Symmetry and primitive cell tool
=====================================================

Usage:
    python analyze_symmetry.py [-i INPUT] [-o OUTPUT]

Description:
    - Loads a structure from a VASP CONTCAR or POSCAR file
    - Analyzes symmetry using pymatgen
    - Converts the structure to a symmetry-refined primitive cell
    - Outputs the primitive cell in VASP format

Arguments:
    -i, --input     Input file (default: CONTCAR)
    -o, --output    Output file name (default: POSCAR_prim)

Example:
    python analyze_symmetry.py -i POSCAR -o POSCAR_prim

Author: [Thomas Hill, Cardiff University, 08/04/2025, Supervisor: C.R.A. Catlow]
"""

import argparse
from pymatgen.core import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from ase.io import write
from pymatgen.io.ase import AseAtomsAdaptor

# === Argument parser ===
parser = argparse.ArgumentParser(
    description="Analyze symmetry and extract primitive cell using pymatgen.",
    epilog="Example: python analyze_symmetry.py -i POSCAR -o POSCAR_prim",
    formatter_class=argparse.RawDescriptionHelpFormatter
)
parser.add_argument('-i', '--input', type=str, default='CONTCAR', help='Input structure file (default: CONTCAR)')
parser.add_argument('-o', '--output', type=str, default='POSCAR_prim', help='Output file name (default: POSCAR_prim)')
args = parser.parse_args()

# === Step 1: Load structure ===
structure = Structure.from_file(args.input)
print(f"? Loaded structure from {args.input}")

# === Step 2: Analyze symmetry ===
sga = SpacegroupAnalyzer(structure, symprec=1e-3)

spacegroup_symbol = sga.get_space_group_symbol()
spacegroup_number = sga.get_space_group_number()
crystal_system = sga.get_crystal_system()

print(f"?? Detected space group: {spacegroup_symbol} ({spacegroup_number})")
print(f"?? Crystal system: {crystal_system}")

# === Step 3: Get primitive cell ===
prim = sga.get_primitive_standard_structure()
print(f"?? Generated primitive cell with {len(prim)} atoms")

# === Step 4: Convert to ASE and export ===
ase_prim = AseAtomsAdaptor.get_atoms(prim)
ase_prim.center()
write(args.output, ase_prim, format='vasp')
print(f"? Written primitive structure to {args.output}")
