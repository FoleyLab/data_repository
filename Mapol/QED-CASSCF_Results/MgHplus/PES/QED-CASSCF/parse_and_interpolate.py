import json
import numpy as np
from scipy.interpolate import CubicSpline
from matplotlib import pyplot as plt

def read_casscf_data(filename):
    """
    Reads CASSCF data from a file with headers:
    #Bond_Length    E0          E1          E2
    and subsequent columns of data.

    Args:
        filename (str): Path to the CASSCF output file.

    Returns:
        dict: A dictionary containing the extracted data:
              {
                  "bond_lengths": [list of bond lengths],
                  "energies": {
                      "E0": [list of ground state energies],
                      "E1": [list of first excited state energies],
                      "E2": [list of second excited state energies]
                  }
              }
              Returns None if there's an error.
    """

    data = {"bond_lengths": [], "energies": {"E0": [], "E1": [], "E2": []}}
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue  # Skip empty lines

                if line.startswith("#Bond_length"):
                    continue  # Skip the header line
                else:
                    try:
                        values = line.split()
                        bond_length = float(values[0])
                        e0 = float(values[1])
                        e1 = float(values[2])
                        e2 = float(values[3])

                        data["bond_lengths"].append(bond_length)
                        data["energies"]["E0"].append(e0)
                        data["energies"]["E1"].append(e1)
                        data["energies"]["E2"].append(e2)
                    except (ValueError, IndexError):
                        print(f"Warning: Skipping malformed data line: {line}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

    return data

def fit_spline_data(data):
    """
    Fits cubic splines to the energy data as a function of bond length.

    Args:
        data (dict): A dictionary containing the extracted data
                     from the read_casscf_data function.

    Returns:
        dict: A dictionary containing the spline functions:
              {
                  "E0": spline function for ground state energy,
                  "E1": spline function for first excited state energy,
                  "E2": spline function for second excited state energy
              }
              Returns None if the input data is invalid.
    """
    if not data or "bond_lengths" not in data or "energies" not in data:
        print("Error: Invalid input data for spline fitting.")
        return None

    bond_lengths = np.array(data["bond_lengths"])
    energies = data["energies"]
    splines = {}

    for key, energy_values in energies.items():
        energy_array = np.array(energy_values)
        if len(bond_lengths) != len(energy_array) or len(bond_lengths) < 2:
            print(f"Warning: Not enough data points for spline fitting for {key}.")
            splines[key] = None
        else:
            splines[key] = CubicSpline(bond_lengths, energy_array)

    return splines

if __name__ == "__main__":
    filename = "energies_0_05.dat"  # Replace with your actual filename
    casscf_data = read_casscf_data(filename)

    if casscf_data:
        spline_functions = fit_spline_data(casscf_data)
        if spline_functions:
            # Example of using the spline functions to interpolate
            new_bond_length = 1.65
            if spline_functions["E0"]:
                interpolated_e0 = spline_functions["E0"](new_bond_length)
                print(f"Interpolated E0 at {new_bond_length} Angstroms: {interpolated_e0}")
            if spline_functions["E1"]:
                interpolated_e1 = spline_functions["E1"](new_bond_length)
                print(f"Interpolated E1 at {new_bond_length} Angstroms: {interpolated_e1}")
            if spline_functions["E2"]:
                interpolated_e2 = spline_functions["E2"](new_bond_length)
                print(f"Interpolated E2 at {new_bond_length} Angstroms: {interpolated_e2}")
        else:
            print("Spline fitting failed.")
    else:
        print("Data reading failed.")

    
    # now createa an array of bond lengths
    new_bond_lengths = np.linspace(1.0, 3.5, 100)  # Example range from 1.0 to 3.5 Angstroms

    # get interpolated energies for each bond length for E0
    new_e0 = spline_functions["E0"](new_bond_lengths)
    new_e1 = spline_functions["E1"](new_bond_lengths)
    new_e2 = spline_functions["E2"](new_bond_lengths)

    # plot the original data and the interpolated data
    plt.figure(figsize=(10, 6))
    plt.plot(casscf_data["bond_lengths"], casscf_data["energies"]["E0"], 'o', label='Original E0 Data')
    plt.plot(new_bond_lengths, new_e0, '-', label='Interpolated E0')
    plt.plot(casscf_data["bond_lengths"], casscf_data["energies"]["E1"], 'o', label='Original E1 Data')
    plt.plot(new_bond_lengths, new_e1, '-', label='Interpolated E1')
    plt.plot(casscf_data["bond_lengths"], casscf_data["energies"]["E2"], 'o', label='Original E2 Data')
    plt.plot(new_bond_lengths, new_e2, '-', label='Interpolated E2')
    plt.legend()
    plt.show()

    # save the data to a npy file
    pes = np.array([new_bond_lengths, new_e0, new_e1, new_e2])
    np.save("mghplus_casscf_8e_12o_10ph_ccpVDZ_lambda_0.05_om_0.136.npy", pes)
    print("Data saved to pes.npy")


