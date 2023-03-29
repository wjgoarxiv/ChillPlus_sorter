import os
import csv
import argparse

# Argparse
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory", help="directory of the text files", default="CHILL+")
parser.add_argument("-o", "--output", help="output CSV file name", default="CHILL+_results.csv")
args = parser.parse_args()

# Set the directory where your text files are stored
chillplus_dir = args.directory

# Define the output CSV file name
output_csv = args.output

# Initialize an empty list to store the extracted data
data = []

# Get the sorted list of filenames as integers
sorted_filenames = sorted(
    (int(f[:-4]) for f in os.listdir(chillplus_dir) if f.endswith(".txt"))
)

# Loop through the sorted filenames
for frame_number in sorted_filenames:
    filename = f"{frame_number}.txt"
    file_path = os.path.join(chillplus_dir, filename)

    with open(file_path, "r") as file:
        lines = file.readlines()

        # Extract the header line
        header_line = lines[0].strip()

        # Split the header line into attribute names
        attribute_names = header_line.split()

        # Prepare the CSV header by removing double quotes
        header = [attr.replace('"', '') for attr in attribute_names]

        # Find the line with the relevant data (starts with a number)
        for line in lines:
            if line.strip() and line.strip()[0].isdigit():
                # Split the line by spaces and convert the values to integers
                values = list(map(int, line.strip().split()))

                # Add the frame number to the beginning of the values list
                values.insert(0, frame_number)

                # Add the data to the list
                data.append(values)
                break

# Write the data to a CSV file
with open(output_csv, "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(header)
    csv_writer.writerows(data)