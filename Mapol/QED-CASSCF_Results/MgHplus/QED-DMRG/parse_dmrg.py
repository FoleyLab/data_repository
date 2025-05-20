import json
import numpy as np

def read_dmrg_data(filename):
    """
    Reads DMRG data from a file with headers:
    #Bond_Length    E0          E1          E2
    and subsequent columns of data.

    Args:
        filename (str): Path to the DMRG output file.

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

                if line.startswith("#Bond_Length"):
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


def format_data_for_qcarchive(dmrg_data):
    """
    Formats the raw DMRG data into a dictionary structure
    resembling QCArchive standards (where applicable).

    Args:
        dmrg_data (dict): Dictionary containing the raw DMRG data.

    Returns:
        dict: A formatted dictionary suitable for JSON serialization.
    """

    formatted_data = {
        "provenance": {
            "creator": "QED-DMRG",  # Replace with your code's name
            "version": "1.0",       # Replace with your code's version
            "routine": "qed_dmrg_energy_scan" # Changed routine name
        },
        "input_data": {
            "bond_lengths": dmrg_data.get("bond_lengths"),
            "units": "angstrom",
        },
        "properties": {
            "energies": dmrg_data.get("energies"),
            "units": "hartree"
            #  ... (Add other calculated properties)
        },
        "extras": {
            "cavity_frequency" : 0.,
            "cavity_coupling_vector" : [0, 0, 0.0],
            "number_of_photonic_fock_states" : 1,
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
            "method": "QED-DMRG",
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
    dmrg_output_file = "energies.dat"
    json_output_file = "mghplus_dmrg_ccpVDZ.json"

    raw_data = read_dmrg_data(dmrg_output_file)

    if raw_data:
        formatted_data = format_data_for_qcarchive(raw_data)
        write_json(formatted_data, json_output_file)
