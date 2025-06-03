import json
import matplotlib.pyplot as plt
import numpy as np


plt.rcParams.update({
    "font.family": "serif",
    "font.size": 14,
    "axes.titlesize": 16,
    "axes.labelsize": 14,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "legend.fontsize": 12,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "lines.linewidth": 2,
    "lines.markersize": 8,
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "figure.figsize": [8, 6],
    "legend.frameon": False
})

def analyze_energy_data(json_file_path):
    """
    Reads energy data from a JSON file, calculates errors, and plots the results.

    Args:
        json_file_path (str): The path to the JSON file.
    """
    try:
        with open(json_file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found at {json_file_path}")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {json_file_path}")
        return

    if "energies" not in data:
        print("Error: 'energies' key not found in the JSON data.")
        return

    energies_data = data["energies"]
    photon_basis_sizes = sorted([int(k) for k in energies_data.keys() if k.isdigit()])

    error_data = {
        "Eavg_error": [],
        "E0_error": [],
        "E1_error": [],
        "E2_error": [],
        "photon_basis_size": []
    }

    for size in photon_basis_sizes:
        size_str = str(size)
        if size_str in energies_data:
            photon_data = energies_data[size_str]
            try:
                eavg_error = photon_data["Eavg_energy_displaced"] - photon_data["Eavg_energy_center"]
                e0_error = photon_data["E0_energy_displaced"] - photon_data["E0_energy_center"]
                e1_error = photon_data["E1_energy_displaced"] - photon_data["E1_energy_center"]
                e2_error = photon_data["E2_energy_displaced"] - photon_data["E2_energy_center"]

                error_data["Eavg_error"].append(eavg_error)
                error_data["E0_error"].append(e0_error)
                error_data["E1_error"].append(e1_error)
                error_data["E2_error"].append(e2_error)
                error_data["photon_basis_size"].append(size)

            except KeyError as e:
                print(f"Warning: Missing key {e} for photon basis size {size}.")

    # Plotting the error data
    color3 = "rebeccapurple"
    color2 = "salmon"
    color1 = "forestgreen"
    color4 = "dodgerblue"
    color5 = "orangered"
    plt.figure(figsize=(10, 6))
    plt.plot(error_data["photon_basis_size"], np.abs(error_data["Eavg_error"]), marker='o', markersize=10, linestyle='-', color="black", label='Error of Average Energy')
    plt.plot(error_data["photon_basis_size"], np.abs(error_data["E0_error"]), marker='s', markersize=10, linestyle='--', color=color5, label='Error of Ground State Energy')
    plt.plot(error_data["photon_basis_size"], np.abs(error_data["E1_error"]), marker='^', markersize=10, linestyle=':', color=color1, label='Error of LP Energy')
    plt.plot(error_data["photon_basis_size"], np.abs(error_data["E2_error"]), marker='x', markersize=10, linestyle='-.', color=color4, label='Error of UP Energy')

    plt.xlabel("Photon Basis Size")
    plt.ylabel("Energy Error (Displaced - Center)")
    #plt.title("Energy Errors vs. Photon Basis Size")
    plt.yscale("log")
    plt.legend()
    plt.grid(True)
    plt.xticks(error_data["photon_basis_size"])
    plt.tight_layout()
    plt.savefig("mghp_origin_error_vs_photon_states.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    json_file = '/Users/jfoley19/Code/data_repository/Mapol/MgHplus/origin_invariance/mghp_cs_casscf_8e_12o_ccpVDZ_lz_0.05_om_0.136.json'  # Replace with the actual path to your JSON file
    analyze_energy_data(json_file)
