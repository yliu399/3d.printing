import numpy as np
import os

first_position = -19.69
n_slices = 4046
last_position = first_position + 0.01 * (n_slices - 1)

os.chdir("U:\\Research Projects\\Jyoti Laser Manufacturing with Metin\\Nebraska Scan\\1dr")

# probability, diameter, center y, voxel
info_table = np.loadtxt("queried_pores.csv", delimiter = ',', skiprows=1, usecols=(0, 2, 4, 7))

# define table of contents
pores_mat = np.zeros((n_slices, 3))

for i in range(info_table.shape[0]):
    ind_num = info_table[i, 2]
    ind_loc = int((ind_num - first_position) / 0.01)
    
    pores_mat[ind_loc, 0] += 1 # number of holes
    pores_mat[ind_loc, 1] += info_table[i, 1] # averaged diameter
    pores_mat[ind_loc, 2] += info_table[i, 3] # averaged voxel
    
nonzero_ind = pores_mat[:, 0] > 0
pores_mat[nonzero_ind, 1] = pores_mat[nonzero_ind, 1] / pores_mat[nonzero_ind, 0]
pores_mat[nonzero_ind, 2] = pores_mat[nonzero_ind, 2] / pores_mat[nonzero_ind, 0]
