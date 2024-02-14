# HubbleHarmony
The project's aim to harmonize differing Hubble constant measurements and methodologies. 
Project is co-authored and assisted by [ChatGPT chat.openai.com](https://chat.openai.com/) specificaly the ["Principia" chat bot](https://chat.openai.com/g/g-tNMzI4smJ-principia)

Our overall approach is pulling the latest data on the Hubble expansion (often referred to in terms of the Hubble constant), and then formatting the various sources into a structured HDF5 format. To be later used for rendering and analysis. Here's our roadmap to accomplish this, that dictates this projects directory structure:

### Step 1: Data Acquisition
Identify Data Sources: Data on the Hubble constant can be found in recent publications or data releases from projects like the Hubble Space Telescope (HST), Planck mission data, or the SH0ES (Supernova H0 for the Equation of State) project. Academic databases like arXiv or NASA's ADS can be valuable resources.

Download Data: Look for datasets provided in accessible formats like CSV, TXT, or FITS. For the Hubble constant, this might include tables of measurements, error estimates, and associated metadata like observation dates and methodologies.

### Step 2: Data Preparation
Initial Review: Examine the datasets for understanding the data structure, content, and any preprocessing needs like unit conversions or handling missing values.

Preprocessing Tools: Utilize tools like Python with libraries such as Pandas (for data manipulation) and Astropy (for handling astronomical data, especially FITS files) to prepare your data. This might involve normalizing data formats, aligning timestamps, and compiling data from multiple sources into a unified dataset.

### Step 3: Conversion to HDF5
Install HDF5 Libraries: Ensure you have the necessary libraries installed for working with HDF5 in Python, such as h5py or PyTables.

Create HDF5 File: Use the h5py library to create an HDF5 file. This involves defining a structure for your data within the file, including groups and datasets that reflect the organization of your data (e.g., measurements, metadata).

Store Data: Populate the HDF5 file with the preprocessed data. Including metadata within the file attributes to provide context for the datasets, such as measurement units, data source references, and any relevant calculation parameters.

### Step 4: Visualization in a Rendering Engine
Select a Rendering Engine: Choose a 3D rendering engine that supports the data you wish to visualize. Prefer Web-based options for online visualization.

Prepare Data for Rendering: Convert the HDF5 data into a format suitable for the chosen rendering engine. This might involve extracting relevant data points and converting them into meshes or other geometric primitives.
