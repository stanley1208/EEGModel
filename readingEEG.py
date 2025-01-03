import pandas as pd
import glob
import os
import seaborn as sns
import matplotlib.pyplot as plt


# #
# # Specify the path to the CSV file
# file_path='chb01_01.csv'
#
# # Load the CSV file into a DataFrame
# df=pd.read_csv(file_path)
#
#
# # Display the first few rows of the DataFrame
# print(df)

# Get the current directory
current_directory=os.getcwd()


# Find all CSV files in the current directory
csv_files=glob.glob(os.path.join(current_directory, '*.csv'))


# Check if any CSV files were found
if not csv_files:
    print('No files found in the current directory.')
else:
    # Combine all CSV files
    combined_csv=pd.concat([pd.read_csv(file) for file in csv_files])


    # Save the combined CSV to a new file
    output_file=os.path.join(current_directory, 'combined_output.csv')
    combined_csv.to_csv(output_file, index=False)
    print(f'combined CSV saved as: {output_file}')



# Load the combined CSV file
data=pd.read_csv("combined_output.csv")

# Quick data preview
print(data.head())