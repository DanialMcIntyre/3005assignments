import psycopg2

#Change this to connect to your database
connection = psycopg2.connect(database="assignment3", user="test", password="test", host="localhost", port=5432)
cursor = connection.cursor()

#Prints and returns all students from the table
def getAllStudent():
    cursor.execute("SELECT * from students;")
    records = cursor.fetchall()
    for record in records:
        print(record)
    return record

#Adds a student to the database
def addStudent(first_name, last_name, email, enrollment_date):
    cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",  (first_name, last_name, email, enrollment_date))
    connection.commit()

#Updates the student with the given id's email
def updateStudentEmail(student_id, new_email):
    cursor.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
    connection.commit()

#Delete the student with the given id
def deleteStudent(student_id):
    cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id, ))
    connection.commit()

def main():

    #getAllStudent()

    #Add student
    addStudent("Danial", "McIntyre", "danialmcintyre@cmail.carleton.ca", '2025-10-05')
    getAllStudent()

    #Update email
    # updateStudentEmail(10, "new_email@gmail.com")
    # getAllStudent()

    #Delete student
    # deleteStudent(10)
    # getAllStudent()

    #Close connection
    connection.close()
    

main()
