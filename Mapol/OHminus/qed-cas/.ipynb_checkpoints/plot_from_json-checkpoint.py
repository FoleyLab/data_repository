import json
import matplotlib.pyplot as plt
import sys
import os

def extract_error_data(json_file):
    with open(json_file, "r") as f:
        data = json.load(f)

    photon_states = data["n_photon_states"]
    errors = [data["energies"][str(n)]["error"] for n in photon_states]
    label = f"{data['level_of_theory']} ({data['photon_state_type']})"
    return photon_states, errors, label

def plot_error_curves(json_files, output_file="errors_vs_photon_states.png"):
    plt.figure(figsize=(8, 6))

    for file in json_files:
        photon_states, errors, label = extract_error_data(file)
        plt.plot(photon_states, errors, marker='o', label=label)

    plt.xlabel("Number of Photon States", fontsize=12)
    plt.ylabel("Energy Error (Hartree)", fontsize=12)
    plt.title("Energy Error vs. Photon States", fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True)
    #plt.yscale('log')  # Set y-axis to logarithmic scale
    plt.tight_layout()
    plt.savefig(output_file, dpi=300)
    plt.show()

if __name__ == "__main__":
    # Example usage:
    # python plot_errors_from_jsons.py file1.json file2.json ...
    if len(sys.argv) < 2:
        print("Usage: python plot_errors_from_jsons.py <file1.json> <file2.json> ...")
        sys.exit(1)

    json_files = sys.argv[1:]
    plot_error_curves(json_files)

