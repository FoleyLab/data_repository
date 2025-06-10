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
file_string = "LiH_r_scan_6311g_fci"

# create template for molecular geometry
mol_tmpl = """
Li
H 1 1.0
symmetry c1
"""

# specify basic input parameters for the electronic structure calculation
options_dict = {
        "basis": "6-311G**",
        "scf_type": "pk",
        "e_convergence": 1e-10,
        "d_convergence": 1e-10,
}

# specify input parameters that are unique to the cavity quantum electrodynamics calculation
cavity_options = {
    'molecule_id' : "LiH",
    'omega_value' : 0.0,
    'lambda_vector' : [0, 0, 0.0],
    'ci_level' : 'fci',
    'ignore_coupling' : False,
    'number_of_photons' : 0,
    'natural_orbitals' : False,
    'photon_number_basis' : True,
    'canonical_mos' : True,
    'coherent_state_basis' : False,
    'davidson_roots' : 4,
    'davidson_threshold' : 1e-9,
    'davidson_indim':20,
    'davidson_maxdim':100,
    "casscf_optimization" : False,
    'davidson_maxiter':100,
    'test_mode': False,
}
# create a new instance of the PFHamiltonianGenerator class
test_pf = PFHamiltonianGenerator(mol_tmpl,options_dict,cavity_options)
# create random energy values for 3 different states
casci_energy_values = test_pf.CIeigs.tolist()

