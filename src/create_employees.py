import csv

# Data to be written to CSV
data = [
    ["id", "name", "department", "salary"],
    [1, "John", "Engineering", 60000],
    [2, "Jane", "HR", 50000],
    [3, "Sam", "Engineering", 75000],
    [4, "Anna", "Sales", 65000]
]

with open('../data/raw/employees.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)