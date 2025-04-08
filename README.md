Slab Creation with ASE from an optimised VASP bulk structure

Description: These files were created to work with metal oxides. The files take the opitmised strucutre from VASP, read the space groups, then proceed to make a primitive unit cell which will then be used to create a slab of your choice. These scripts will allow you to chose you Miller indices, number of atomic layers, and the size of the vacuum.

Requirements: Python 3.9 or above (has not been tested on older versions), ase, and pymatgen (you can pip -install both ase and pymatgen) 

	pip -install ase
	pip -install pymatgen 

Tutorial: 

All the scripts have a help sections, to use this

	python [name of script].py -h

Default inputs and ouputs are set (denoted by the square brackets [] in the instructions below) so the scripts work in conjunction with one another, these can be changed with the -i and -o option for the input file and output file names respectively. This would be as follows 

	python [name of script].py -i [input file name] -o [output filename]

1. Reading the optimised structure and creating the primitive cell [CONTCAR > POSCAR_prim]: In the same directory as the python scripts, place the CONTCAR file from you VASP calculations in the folder with the python scripts, run the following

		python analyze_symmetry.py

2. Creating the slabs [POSCAR_prim > POSCAR_slab]: The next script reads the output and will generate a slab with the desired parameters. The parameters can be chosen with the following arguments, -m for the miller indices, -l for the number of atomic layers, and -v for the size of the vacuum. Note that the slab will be placed in the middle of the cell so the vacuum will be half the stated amount above and below the slab. Here is an example of how to submit the script:

		python make_slab.py -m [h k l] -l [layers] -v [vacuum] -o [output_name]

	Example: a 111 surface, with 8 atomic layers and a 15 angstrom vacuum 

		python make_slab.py -m 1 1 1 -l 8 -v 15 

3. Cleaning the output [POSCAR_slab > POSCAR_final]: The output from the previous step creates an unsual POSCAR file so this step aims to clean it up. Here you can choose the have it in fractional or cartesian coordinates with the -a argument.

		 python clean_poscar.py -a [cartesian or direct (default is set to direct)]
	
	Example: printing the atompositions in cartesian coordinates

		python clean_poscar.py -a cartesian		

5. Cell mutiplier [POSCAR_final > POSCAR_super]: This is a script that multiplies the slab in the x y z directions using the argument -s.

		python multiply_cell.py -s 'x y z'

	Example: create a 2 x 2 x 2 supercell 

  		python multiply_cell.py -s 2 2 2 
