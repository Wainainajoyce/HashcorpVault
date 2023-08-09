import mysql.connector
from mysql.connector import Error

# def establish_connection():
try:
        conn = mysql.connector.connect(
            host='localhost',
            database='Student',
            user='falcon',
            password='Githunguri1%'
        )
        if conn.is_connected():
            print('connected to mysql database')
except mysql.connector.Error as e:  
        print(f"Error:{e}")
# return None 

def create_student_table(conn):
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS student_details (
        student_id INT PRIMARY KEY,
        student_name VARCHAR(100),
        student_email VARCHAR(100),
        major VARCHAR(100),
        results INT
        )""")

    conn.commit()
    print("Students details successfully created")

def add_student_details(conn, student_id,student_name,student_email,major,results):
    cursor = conn.cursor()
    sql = "INSERT INTO student_details(student_id,student_name,student_email,major,results) VALUES (%s,%s,%s,%s,%s)"
    val = (student_id,student_name,student_email,major,results)
    cursor.execute(sql,val)
    conn.commit()
    print(f"Student {student_name} added successfully!")


def show_all_students(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student_details")
    student_details = cursor.fetchall()
    print("\nList of all students:")
    for student in student_details:
        print(f"student_id: {student[0]}, student_name: {student[1]}, student_email: {student[2]}, major: {student[3]}, results:{student[4]}")
    

def main():
    # conn = establish_connection()
    if not conn:
        return

    create_student_table(conn)

    while True:
        print("\nPlease enter student details:")
        student_id = input("Student Id: ")
        student_name= input("Student Name: ")
        student_email = input("Student email: ")
        major = input("Major: ")
        results = input("Results: ")

        add_student_details(conn, student_id,student_name, student_email,major,results)

        more_students = input("\nDo you want to add more students? (yes/no): ").lower()
        if more_students != "yes":
            break

    show_all_students(conn)

    conn.close()
    print('Connection closed.')

if __name__ == "__main__":
    main()







    
    
    


