import os
import pandas as pd

folder_path = "./"
output_file = "combined_output.csv"

csv_files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]
print("CSV Files to Process:", csv_files)

combined_data = pd.DataFrame()

for file_name in csv_files:
    file_path = os.path.join(folder_path, file_name)
    try:
        if os.stat(file_path).st_size == 0:  # Skip empty files
            print(f"Skipping empty file: {file_name}")
            continue

        print(f"Processing {file_name}")
        df = pd.read_csv(file_path)
        combined_data = pd.concat([combined_data, df], ignore_index=True)
        print(f"Successfully added {file_name}")
    except Exception as e:
        print(f"Error processing {file_name}: {e}")

print("All files processed. Saving combined CSV...")
output_path = os.path.join(folder_path, output_file)
combined_data.to_csv(output_path, index=False)

print(f"Combined CSV saved to: {output_path}")

