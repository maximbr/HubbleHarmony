# this is the main acquisition process that processes all the raw data and updates the "step2_preparation" directory with their HDF5 output

import os
target_dir = os.path.join(os.path.dirname(__file__), '../step2_preparation')

import DRAO_10MHz_hpx_r7
DRAO_10MHz_hpx_r7.to_hdf5(target_dir)

