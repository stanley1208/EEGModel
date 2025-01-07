import os
import mne
import pandas as pd

# 1. Set the directory containing EDF files
folder_path = "./"  # Replace with the folder containing your EDF files

# 2. Process each EDF file in the directory
for file_name in os.listdir(folder_path):
    if file_name.endswith(".edf"):  # Check if it's an EDF file
        input_path = os.path.join(folder_path, file_name)
        output_file_name = os.path.splitext(file_name)[0] + ".csv"  # Same name with .csv extension
        output_path = os.path.join(folder_path, output_file_name)

        try:
            # Load the EDF file
            raw = mne.io.read_raw_edf(input_path, preload=True)

            # Convert to DataFrame
            df = raw.to_data_frame()

            # Save DataFrame to CSV in the same directory
            df.to_csv(output_path, index=False)
            print(f"Converted {file_name} to {output_file_name}")
        except Exception as e:
            print(f"Error processing {file_name}: {e}")

print("Batch conversion completed.")
