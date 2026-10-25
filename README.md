# Student Management System

A simple command-line application built using Python and MySQL to manage student records.

## Features
- Add student records
- View all students
- Update student grades
- Delete student records

## Technologies Used
- Python
- MySQL
- MySQL Connector/Python

## Database Configuration
- **Host:** `localhost`
- **Database:** `college`
- **Username:** `proj`
- **Password:** `proj`

## MySQL Login
```bash
mysql -u proj -p
```

Enter the password when prompted:
```text
proj
```

## How to Run
1. Log in to MySQL using the command above.
2. Create the `college` database and `students` table.
3. Install the required Python package:
   ```bash
   pip install mysql-connector-python
   ```
4. Configure the MySQL connection in the Python code.
5. Run the application:
   ```bash
   python3 database.py
   ```

## How It Works
Python connects to the MySQL database using `mysql.connector`. The application performs CRUD (Create, Read, Update, Delete) operations to manage student records.

## Learning Outcomes
- Python–MySQL database connectivity
- SQL CRUD operations
- Parameterized SQL queries
- Database transaction commits
