-- Example Queries

-- CREATE TABLE employees (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(50),
--     department VARCHAR(50),
--     salary INTEGER
-- );

-- Retrieve employees earning more than $50,000.
SELECT * FROM employees
WHERE salary > 50000;

-- Find the average salary grouped by department.
SELECT 
    department
    , AVG(salary) AS avg_salary 
FROM employees
GROUP BY 1; 

-- Rank employees within each department by salary.
SELECT 
    id
    , name 
    , department
    , salary 
    , rank () OVER (PARTITION BY department ORDER BY salary DESC) AS salary_rank
FROM employees;
