import csv

data_share = [
    ["Actions-Name", "Costs per share (in EUR)", "Profit (after 2 years)"],
    ["Action-1", 20, 0.25],
    ["Action-2", 30, 3],
    ["Action-3", 50, 7.5],
    ["Action-4", 70, 14],
    ["Action-5", 60, 10.2],
    ["Action-6", 80, 20],
    ["Action-7", 22, 1.54],
    ["Action-8", 26, 2.86],
    ["Action-9", 48, 6.24],
    ["Action-10", 34, 9.18],
    ["Action-11", 42, 7.14],
    ["Action-12", 110, 9.90],
    ["Action-13", 38, 8.74],
    ["Action-14", 14, 0.14],
    ["Action-15", 18, 0.54],
    ["Action-16", 8, 0.64],
    ["Action-17", 4, 0.48],
    ["Action-18", 10, 1.4],
    ["Action-19", 24, 5.04],
    ["Action-20", 114, 20.52]
]

filename = "data_shares.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    for row in data_share:
        writer.writerow(row)

print("CSV file created successfully!")
