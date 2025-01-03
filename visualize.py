import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to your combined CSV file
csv_path = "combined_output.csv"

# Load the CSV into a DataFrame
data = pd.read_csv(csv_path)

# # Display the first few rows
# print("First few rows of the data:")
# print(data.head())
#
# # Display a random sample of 10 rows
# print("\nRandom sample of the data:")
# print(data.sample(10))
#
# # Display basic statistics about the data
# print("\nSummary statistics:")
# print(data.describe())


# Define the fraction of data to visualize (e.g., first 100 rows or a random sample)
fraction_data = data.head(100)  # To use the first 100 rows
# fraction_data = data.sample(100)  # For a random sample of 100 rows


# Plot 1: Line Plot for First Two Columns
plt.figure(figsize=(10,6))
plt.plot(fraction_data.iloc[:,0],fraction_data.iloc[:,1],label="Line Plot")
plt.xlabel("Column 1")
plt.ylabel("Column 2")
plt.title("Line Plot for Fraction of Data")
plt.legend()
plt.show()