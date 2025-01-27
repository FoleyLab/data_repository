import os
import glob
import sys
def extract_scf_energy(base_folder):
    results = {}
    for subfolder in os.listdir(base_folder):
        subfolder_path = os.path.join(base_folder, subfolder)
        if os.path.isdir(subfolder_path):
            file_pattern = os.path.join(subfolder_path, "Untitled*")
            files = glob.glob(file_pattern)
            if files:
                tamm_test_path = files[0]
                with open(tamm_test_path, 'r') as file:
                    for line in file:
                        if "** Total SCF energy" in line:
                            energy = float(line.split('=')[-1].strip())
                            results[subfolder] = energy
                            break
    return results
if __name__ == "__main__":
    
    # Ensure that there is at least one argument (folder path)
    if len(sys.argv) < 2:
        print("Usage: python script.py <base_folder>")
        sys.exit(1)
    # Get the base folder path from command-line arguments
    base_folder = os.path.abspath(sys.argv[1])
    # Ensure that the given base folder path is valid
    if not os.path.isdir(base_folder):
        print(f"Error: The path {base_folder} is not a valid directory.")
        sys.exit(1)
    output_file = "scf_energies.txt"
    scf_energies = extract_scf_energy(base_folder)
    with open(output_file, 'w') as f:
        for subfolder, energy in scf_energies.items():
            f.write(f"Subfolder: {subfolder}, SCF Energy: {energy}\n")












