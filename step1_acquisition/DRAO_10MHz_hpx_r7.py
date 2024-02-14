# DRAO_10MHz_hpx_r7 was pulled Feb 14 2024 from https://lambda.gsfc.nasa.gov/product/foreground/fg_drao_10_get.html
SRC_FILE = 'DRAO_10MHz_hpx_r7.fits'

def to_hdf5(target_directory:str):
    import os
    import h5py
    from astropy.io import fits
    import numpy as np
    
    fits_path = os.path.join(os.path.dirname(__file__), SRC_FILE)
    hdf5_path = os.path.join(target_directory, os.path.splitext(SRC_FILE)[0] + ".h5")

    # Open the FITS file and read the binary table data
    with fits.open(fits_path) as hdul:
        table_data = hdul[1].data
        temperature_data = table_data['TEMPERATURE']  # Extract the temperature data

    # Create an HDF5 file and store the temperature data
    with h5py.File(hdf5_path, 'w') as hdf:
        # Create a dataset for the temperature data
        hdf.create_dataset('Temperature', data=np.array(temperature_data))
        # Add relevant metadata as attributes
        hdf['Temperature'].attrs['FREQ'] = '10.03 MHz'
        hdf['Temperature'].attrs['BMAJ'] = 2.6
        hdf['Temperature'].attrs['BMIN'] = 1.9
        hdf['Temperature'].attrs['NSIDE'] = 128
        # Add any additional metadata as needed
