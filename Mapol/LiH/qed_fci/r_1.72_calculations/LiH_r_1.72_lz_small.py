# set path to the directory where helper_PFCI.py is located
import sys
sys.path.append("/Users/jfoley19/Code/qed-ci/src")

# import helper libraries
import numpy as np
import psi4
from helper_PFCI import PFHamiltonianGenerator
import json

# set precision for printing numpy arrays
np.set_printoptions(threshold=sys.maxsize)

# create file prefix for output json file
file_string = "LiH_r_1.72_qedfci_lz_0.01_om__6_311Gss"

# create template for molecular geometry
mol_str = """
Li
H 1 1.72
0 1
symmetry c1
"""

# specify basic input parameters for the electronic structure calculation
options_dict = {
        "basis": "6-311G**",
        "scf_type": "pk",
        "e_convergence": 1e-12,
        "d_convergence": 1e-12,
}

# specify input parameters unique to the cavity quantum electrodynamics calculation
cavity_options = {
    'molecule_id' : "LiH",
    'omega_value' : 0.12086,
    'lambda_vector' : [0, 0, 0.01],
    'ci_level' : 'fci',
    'ignore_coupling' : False,
    'number_of_photons' : 10,
    'natural_orbitals' : False,
    'photon_number_basis' : True,
    'canonical_mos' : True,
    'coherent_state_basis' : False,
    'davidson_roots' : 8,
    'davidson_threshold' : 1e-5,
    'davidson_indim':20,
    'davidson_maxdim':100,
    'davidson_maxiter':100,
    'davidson_indim':8,
    'test_mode': False,
}

# create new dictionary to store calculation data
calculation_data = {
    "molecular_geometry" : {
        "z-matrix" : [],
    },
    "return_results" : {
        "fci_energies" : [],
        "dipole_array": []
    }
}

# store cavity and standard electronic structure data
calculation_data.update(cavity_options)
calculation_data.update(options_dict)

# run calculation
test_pf = PFHamiltonianGenerator(
        mol_str,
        options_dict,
        cavity_options)

energy_values = test_pf.CIeigs.tolist()
dipole_values = test_pf.dipole_array.tolist()

calculation_data["return_results"]["fci_energies"].append(energy_values)
calculation_data["return_results"]["dipole_array"].append(dipole_values)

# write dictionary to JSON file
with open(f"{file_string}.json", "w") as f:
    json.dump(calculation_data, f, indent=4)

