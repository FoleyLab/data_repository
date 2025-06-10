import json
import numpy as np

# read from json file Uncoupled_molecules_data_with_casscf.json
def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

file_1 = '/Users/jfoley19/Code/data_repository/Vibronic_Coupling_results/Uncoupled_molecules_data_with_casscf.json'
file_2 = '/Users/jfoley19/Code/data_repository/Vibronic_Coupling_results/Uncoupled_molecules_data.json'
# read data from the json file
data_w_casscf = read_json(file_1)
data_wo_casscf = read_json(file_2)


