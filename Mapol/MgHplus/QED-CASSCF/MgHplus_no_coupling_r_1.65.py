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
file_string = "MgHp_r_scan_ccpVDZ_qed_casscf_8e_12o_no_coupling"

# create template for molecular geometry
mol_str = """
Mg
H 1 1.65
1 1
symmetry c1
"""

# specify basic input parameters for the electronic structure calculation
options_dict = {
        "basis": "cc-pVDZ",
        "scf_type": "pk",
        "e_convergence": 1e-10,
        "d_convergence": 1e-10,
}

# specify input parameters that are unique to the cavity quantum electrodynamics calculation
cavity_options = {
    'molecule_id' : "LiH",
    'omega_value' : 0.,
    'lambda_vector' : [0, 0, 0.05],
    'ci_level' : 'cas',
    'ignore_coupling' : False,
    'number_of_photons' : 0,
    'natural_orbitals' : False,
    'photon_number_basis' : False,
    'canonical_mos' : False,
    'coherent_state_basis' : True,
    'davidson_roots' : 6,
    'davidson_threshold' : 1e-5,
    'davidson_indim':20,
    'davidson_maxdim':100,
    'spin_adaptation': "singlet",
    'casscf_weight':np.array([1,1,1]),
    'davidson_maxiter':100,
    'davidson_indim':8,
    'test_mode': False,
    'nact_orbs' : 12,
    'nact_els' : 8
}

# create new dictionary to store calculation data
calculation_data = {

    "molecular_geometry" : {
        "z-matrix" : [],
    },
    "return_results" : {

        "casci_energies" : [],
        "casscf_energies" : []
    }

}
# store cavity parameters in dictionary
for keys, values in cavity_options.items():
    calculation_data[keys] = values
# store standard electronic structure data in dictionary
for keys, values in options_dict.items():
    calculation_data[keys] = values

test_pf = PFHamiltonianGenerator(
        mol_str,
        options_dict,
        cavity_options)
# create random energy values for 3 different states
casci_energy_values = test_pf.CIeigs.tolist()
casscf_energy_values = test_pf.CASSCFeigs.tolist()
# create random dipole values for 3 different states
# add mol_str to the molecular geometry dictionary
calculation_data["molecular_geometry"]["z-matrix"].append(mol_str)
# add energy values to the return_results dictionary
calculation_data["return_results"]["casci_energies"].append(casci_energy_values)
calculation_data["return_results"]["casscf_energies"].append(casscf_energy_values)


print(calculation_data)
