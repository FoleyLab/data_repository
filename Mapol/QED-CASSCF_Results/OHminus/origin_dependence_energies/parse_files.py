import json

def analyze_single_data(filename, level_of_theory, photon_state_type, n_active_electrons=None, n_active_orbitals=None):
    """Analyzes a single data file with the specified parameters."""
    data = {
        'level_of_theory': level_of_theory,
        'basis_set': '6-31G',
        'molecular_z_matrix': "O\nH 1  0.9",
        'molecular_charge': -1,
        'spin_multiplicity' : 1,
        'cavity_frequency' : 0.219,
        'coupling_vector' : [0, 0, 0.05],
        'photon_state_type': photon_state_type,
        'n_photon_states': [],
        'energies': {}
    }

    if level_of_theory in ['casscf', 'casci']:
        data['n_active_electrons'] = n_active_electrons
        data['n_active_orbitals'] = n_active_orbitals

    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                values = line.split()
                if len(values) == 3:
                    try:
                        n_photon = int(values[0])
                        energy_center = float(values[1])
                        energy_displaced = float(values[2])
                        error = energy_displaced - energy_center
                        data['n_photon_states'].append(n_photon)
                        data['energies'][n_photon] = {
                            'energy_center': energy_center,
                            'energy_displaced': energy_displaced,
                            'error': error
                        }
                    except ValueError:
                        print(f"Warning: Could not parse numerical data in line: '{line}' in file '{filename}'. Skipping line.")
                elif values:
                    print(f"Warning: Unexpected number of columns in line: '{line}' in file '{filename}'. Skipping line.")

        data['n_photon_states'] = sorted(data['n_photon_states'])
        return data

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while processing '{filename}': {e}")
        return None

if __name__ == "__main__":
    # Specify the details for your data file
    file_to_analyze = 'cs_casscf_2e2o.txt'  # Replace with your actual filename
    theory_level = 'qed-casscf'
    photon_type = 'coherent state'
    n_electrons = 2
    n_orbitals = 2

    analysis_result = analyze_single_data(file_to_analyze, theory_level, photon_type, n_electrons, n_orbitals)

    if analysis_result:
        output_filename = f"{file_to_analyze}_analysis.json"
        with open(output_filename, 'w') as outfile:
            json.dump(analysis_result, outfile, indent=4)
        print(f"Analysis complete. Results saved to '{output_filename}'")
    else:
        print("Analysis failed.")
