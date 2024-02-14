
def play_hd5(hd5_file_path:str):
    import h5py
    import matplotlib.pyplot as plt

    # Open the HDF5 file
    with h5py.File(hd5_file_path, 'r') as file:
        # Assume there's a dataset named 'Temperature' you want to inspect
        data = file['Temperature'][:]
        
        # Plot the data (assuming it's 2D for simplicity)
        plt.imshow(data, cmap='viridis')
        plt.colorbar()
        plt.title('Temperature Data Visualization')
        plt.show()


if __name__ == '__main__':
    import argparse
    import os

    parser = argparse.ArgumentParser("play_hd5.py")
    parser.add_argument("hd5file", help="Path to the HD5 file you would like to play", type=str)
    args = parser.parse_args()

    hd5_file_path = os.path.abspath(args.hd5file)
    if (not os.path.exists(hd5_file_path)):
        print("No file {hd5_file_path} located")
        exit(1)

    play_hd5(args.hd5file)
