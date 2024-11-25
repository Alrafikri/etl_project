# ETL PROJECT

## Objective
This project is designed for me to learn basic data engineering concepts, particularly around extracting, transforming, and loading (ETL) data. The goal is to practice working with databases and CSV files in Python.

## Tech Stack
- Python
  - Libraries: psycopg2, pandas
- PostgreSQL (Database)

## Setup Instructions

1. **Install Python dependencies:**
   You can install the necessary libraries by running:
   pip install -r requirements.txt

2. **Set up PostgreSQL:**
   - Install PostgreSQL if it's not already installed.
   - Create a database called `data_engineering` by running the following command in PostgreSQL:
     CREATE DATABASE data_engineering;

3. **Create a Table in PostgreSQL:**
   - You can create a table called `employees` by running the following SQL commands in PostgreSQL:
     CREATE TABLE employees (
         id SERIAL PRIMARY KEY,
         name VARCHAR(50) NOT NULL,
         department VARCHAR(50),
         salary INTEGER
     );

4. **Create CSV File:**
   - You can generate a sample `employees.csv` file by running the `create_employees.py` script. The CSV data will look like this:
     id,name,department,salary
     1,John,Engineering,60000
     2,Jane,HR,50000
     3,Sam,Engineering,75000
     4,Anna,Sales,65000

5. **Run the ETL Script:**
   - Once you have the CSV file, you can run the ETL pipeline to load the data into your PostgreSQL database.

## Database Schema

### `employees` Table
The `employees` table stores information about company employees.

| Column Name  | Data Type   | Constraints     | Description                                  |
|--------------|-------------|-----------------|----------------------------------------------|
| id           | SERIAL      | PRIMARY KEY     | Unique identifier for each employee.        |
| name         | VARCHAR(50) | NOT NULL        | The name of the employee.                   |
| department   | VARCHAR(50) |                 | The department the employee belongs to.     |
| salary       | INTEGER     |                 | The employee's salary.                      |

#### Notes:
- The `id` column auto-increments with each new record.
- This table is a single table for testing purposes.

## Example Queries
You can find example queries in the `~/src/sql_queries.sql` file.
