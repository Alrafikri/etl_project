import pandas as pd
import psycopg2

# Load data from CSV
data = pd.read_csv('../data/raw/employees.csv')

# Connect to PostgreSQL, I create the database name data_engineering with data_user have all privileges
conn = psycopg2.connect(
    dbname="data_engineering",
    user="data_user",
    password="password",
    host="localhost"
)
cursor = conn.cursor()


# Iterate through rows and insert data into the table
for _, row in data.iterrows():
    cursor.execute(
        """
        INSERT INTO employees (id, name, department, salary)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT DO NOTHING
        """,
        (row['id'], row['name'], row['department'], row['salary'])
    )

# Commit and close connection
conn.commit()

# Test inserting sample data into the employees table.
sample_data = {
    "id": 5, 
    "name": "John Doe",
    "department": "Engineering",
    "salary": 75000
}

cursor.execute(
    """
    INSERT INTO employees (id, name, department, salary)
    VALUES (%s,%s, %s, %s)
    """,
    (sample_data["id"], sample_data["name"], sample_data["department"], sample_data["salary"])
)

# Retrieve and print data
cursor.execute("SELECT * FROM employees")
results = cursor.fetchall()

for row in results:
    print(row)

# Commit (optional) and close connection
# conn.commit()
cursor.close()
conn.close()