import numpy as np
import os
import glob
from matplotlib import pyplot as plt

# Load all .npy files in the LiH directory that have pes and 100_points in the name
data_dir = '/Users/jfoley19/Code/data_repository/NPY_Files/LiH/'
data_files = glob.glob(data_dir + '*100_points.npy_pes.npy')

# loop through all data_files, grab their data, store in a combind_data array
for files in data_files:
    data = np.load(files)
    print(files, data.shape)
    # Determine the shape of the combined array
    total_shape = list(data.shape)
    total_shape[0] = len(data_files) * total_shape[0]

    # Create an empty array to hold all the data
    combined_data = np.empty(total_shape)

    # Fill the combined array with data from each file
    start_idx = 0
    for files in data_files:
        data = np.load(files)
        end_idx = start_idx + data.shape[0]
        combined_data[start_idx:end_idx] = data
        start_idx = end_idx

    print("Combined data shape:", combined_data.shape)

# split the file names and identify the lz value for each file
lz_values = []
for files in data_files:
    lz = files.split('_')[10]
    lz_values.append(lz)
print(lz_values)

# reshape the combined data array to be 6x11x100 
# inner most index is the lz values 
# middle index is the indexes either the r-value or the energy of the nth electronic state
# i.e. middle index = 0 -> bond length, middle index = 1 -> energy of first electronic state, etc.
# outer most index is value for each bond length

# example: data_to_plot[0, 0, :] -> bond lengths for first lz value
# example: data_to_plot[5, 1, :] -> energies vs bond lengths for the 2nd electronic state for the last lz value
data_to_plot = combined_data.reshape((6, 11, 100))

# plot data for ground state pes for first lz value
plt.plot(data_to_plot[0, 0, :], data_to_plot[0, 1, :], label=lz_values[0])
# plot data for first excited state pes for first lz value
plt.plot(data_to_plot[0, 0, :], data_to_plot[0, 2, :], label=lz_values[0])
plt.xlabel('Bond Length')
plt.ylabel('Energy')
plt.legend()
plt.show()