import json
import numpy as np

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


def format_data_for_qcarchive(casscf_data):
    """
    Formats the raw CASSCF data into a dictionary structure
    resembling QCArchive standards (where applicable).

    Args:
        casscf_data (dict): Dictionary containing the raw CASSCF data.

    Returns:
        dict: A formatted dictionary suitable for JSON serialization.
    """

    formatted_data = {
        "provenance": {
            "creator": "QED-CASSCF",  # Replace with your code's name
            "version": "1.0",       # Replace with your code's version
            "routine": "qed_casscf_energy_scan" # Changed routine name
        },
        "input_data": {
            "bond_lengths": casscf_data.get("bond_lengths"),
            "units": "angstrom",
        },
        "properties": {
            "energies": casscf_data.get("energies"),
            "units": "hartree"
            #  ... (Add other calculated properties)
        },
        "extras": {
            "cavity_frequency" : 0.136,
            "cavity_coupling_vector" : [0, 0, 0.05],
            "maximum_photonic_occupation" : 10,
            #  ... (Add any other DMRG-specific data)
        },
        "molecule": {  # If you have molecule info, add it
            "symbols": ["Mg", "H"],  # Example: list of atomic symbols
            "geometry": [[0.0, 0.0, 0.0], [0.0, 0.0, None]],  #Example: list of coordinates; None placeholder
            "units": "angstrom",
            "charge" : "1",
            "multiplicity" : "1"
        },
        "keywords": { # Computational settings
            "method": "QED-CASSCF",
            "basis": "cc-pVDZ",
            # ...
        }
    }

    # Clean up any 'None' values for better JSON output
    formatted_data = {k: v for k, v in formatted_data.items() if v is not None}

    return formatted_data


def write_json(data, filename):
    """
    Writes the data to a JSON file.

    Args:
        data (dict): The data to write.
        filename (str): The name of the JSON file.
    """
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)  # indent for pretty formatting
        print(f"Data written to '{filename}' successfully.")
    except Exception as e:
        print(f"Error writing to file '{filename}': {e}")


if __name__ == "__main__":
    casscf_output_file = "energies_0_01.dat"  # Replace with your DMRG output filename
    json_output_file = "mghplus_casscf_ccpVDZ_lz__10p_01_lambda_0p05_om_0.136.json"

    raw_data = read_casscf_data(casscf_output_file)

    if raw_data:
        formatted_data = format_data_for_qcarchive(raw_data)
        write_json(formatted_data, json_output_file) 
