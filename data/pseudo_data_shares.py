import csv

data_shares = [
    ["Actions-Name", "Costs per share (in EUR)", "Profit (after 2 years)"],
    ["Action-1", 20, 0.25],
    ["Action-2", 30, 3],
    ["Action-3", 50, 7.5],
    ["Action-4", 70, 14]
]

filename = "pseudo_data_shares.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    for row in data_shares:
        writer.writerow(row)

print("CSV file created successfully!")
