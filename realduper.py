# Script gifted by Origin/Wolk to Arma3 Community
import csv

input_file = 'duper.txt'
output_file = 'output.txt'

# Read input CSV file
with open(input_file, 'r') as file:
    reader = csv.reader(file, delimiter=";")
    rows = list(reader)

# Remove duplicate rows
unique_rows = []
seen = set()

for row in rows:
    #print(row)  # Print each row, enable this row if you want to see the output to screen
    key = (round(float(row[1]), 3), round(float(row[2]), 3))  # Compare values up to 3 decimal places
    if key not in seen:
        unique_rows.append(row)
        seen.add(key)

# Write output CSV file
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file, delimiter=";",quoting=csv.QUOTE_NONE, quotechar= '')
    for row in unique_rows:
        row[0] = f'"{row[0]}"'  # Add double quotes to the first column
        writer.writerow(row)
