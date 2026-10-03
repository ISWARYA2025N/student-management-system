import mysql.connector
from mysql.connector import Error

def create_connection():
    """Establish database connection."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='student_management',
            user='proj',         # Replace with your MySQL username
            password='proj' # Replace with your MySQL password
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def add_student():
    conn = create_connection()
    if not conn: return
    cursor = conn.cursor()
    
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    
    query = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
    values = (name, age, grade)
    
    cursor.execute(query, values)
    conn.commit()
    print(f"Success! Student {name} added with ID {cursor.lastrowid}.")
    
    cursor.close()
    conn.close()

def view_students():
    conn = create_connection()
    if not conn: return
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, name, age, grade FROM students")
    rows = cursor.fetchall()
    
    print("\n--- Student Records ---")
    print(f"{'ID':<5} | {'Name':<20} | {'Age':<5} | {'Grade':<5}")
    print("-" * 45)
    for row in rows:
        print(f"{row[0]:<5} | {row[1]:<20} | {row[2]:<5} | {row[3]:<5}")
        
    cursor.close()
    conn.close()

def update_student():
    conn = create_connection()
    if not conn: return
    cursor = conn.cursor()
    
    student_id = input("Enter the ID of the student to update: ")
    new_grade = input("Enter the new grade: ")
    
    query = "UPDATE students SET grade = %s WHERE id = %s"
    cursor.execute(query, (new_grade, student_id))
    conn.commit()
    
    if cursor.rowcount > 0:
        print("Student record updated successfully!")
    else:
        print("Student ID not found.")
        
    cursor.close()
    conn.close()

def delete_student():
    conn = create_connection()
    if not conn: return
    cursor = conn.cursor()
    
    student_id = input("Enter the ID of the student to delete: ")
    
    query = "DELETE FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))
    conn.commit()
    
    if cursor.rowcount > 0:
        print("Student record deleted successfully!")
    else:
        print("Student ID not found.")
        
    cursor.close()
    conn.close()

def main():
    while True:
        print("\n=== Real-World Student Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student Grade")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 5.")

if __name__ == "__main__":
    main()
