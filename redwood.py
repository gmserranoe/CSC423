# Gabriela Serrano Echenagucia @ University of Miami (CSC 423)

import sqlite3
import pandas as pd

# Connects to an existing database file in the current directory
# If the file does not exist, it creates it in the current directory
db_connect = sqlite3.connect('redwood.db')

# Instantiate cursor object for executing queries
cursor = db_connect.cursor()

# String variable for passing queries to cursor
# query = """ """

# Execute query, the result is stored in cursor
#cursor.execute(query)


############################### TABLE CREATION ###############################

# DEPARTMENT
query = """
    CREATE TABLE Department(
        deptNo VARCHAR(5) NOT NULL CHECK (deptNo LIKE 'D%'), 
        deptName VARCHAR(100) CHECK (deptName LIKE 'Department%'), 
        chairName VARCHAR(100), 
        faculty_count INT,
        PRIMARY KEY(deptNo)
    );
    """
cursor.execute(query)

# STUDENT
query = """
    CREATE TABLE Student(
        studentID VARCHAR(5) NOT NULL CHECK (studentID LIKE 'R%'), 
        studentName VARCHAR(100), 
        student_initials VARCHAR(4) CHECK (student_initials LIKE '__%'),
        PRIMARY KEY(studentID)
    );
    """
cursor.execute(query)

# MAJOR
query = """
    CREATE TABLE Major(
        majorCode CHAR(3) NOT NULL CHECK (majorCode LIKE '___'),
        majorName VARCHAR(100), 
        deptNo VARCHAR(5),
        PRIMARY KEY(majorCode),
        FOREIGN KEY(deptNo) REFERENCES Department(deptNo)
            ON DELETE CASCADE
    );
    """
cursor.execute(query)

# EVENT
query = """
    CREATE TABLE Event(
        eventNo VARCHAR(5) NOT NULL CHECK (eventNo LIKE 'EV%'), 
        eventName VARCHAR(100), 
        start_date date NOT NULL CHECK (start_date >= 2022-12-02), 
        end_date date NOT NULL,
        CONSTRAINT chk_date CHECK (end_date > start_date), 
        PRIMARY KEY(eventNo)
    );
    """
cursor.execute(query)

# DEPARTMENT EVENT
query = """
    CREATE TABLE DeptEvent(
        deptNo VARCHAR(5) NOT NULL CHECK (deptNo LIKE 'D%'), 
        eventNo VARCHAR(5) NOT NULL CHECK (eventNo LIKE 'E%'), 
        PRIMARY KEY(deptNo, eventNo), 
        FOREIGN KEY(deptNo) REFERENCES Department(deptNo)
            ON DELETE CASCADE,
        FOREIGN KEY(eventNo) REFERENCES Event(eventNo)
            ON DELETE CASCADE
    );
    """
cursor.execute(query)

# STUDENT ATTENDANCE
query = """
    CREATE TABLE StudentAttendance(
        studentID VARCHAR(5) NOT NULL CHECK (studentID LIKE 'R%'),
        eventNo VARCHAR(5) NOT NULL CHECK (eventNo LIKE 'E%'), 
        PRIMARY KEY(studentID, eventNo), 
        FOREIGN KEY(studentID) REFERENCES Student(studentID)
            ON DELETE CASCADE,
        FOREIGN KEY(eventNo) REFERENCES Event(eventNo)
            ON DELETE CASCADE
    );
    """
cursor.execute(query)

# STUDENT MAJOR
query = """
    CREATE TABLE StudentMajor(
        studentID VARCHAR(5) NOT NULL CHECK (studentID LIKE 'R%'),
        majorCode CHAR(3) NOT NULL CHECK (majorCode LIKE '___'), 
        PRIMARY KEY(studentID, majorCode), 
        FOREIGN KEY(studentID) REFERENCES Student(studentID)
            ON DELETE CASCADE,
        FOREIGN KEY(majorCode) REFERENCES Major(majorCode)
            ON DELETE CASCADE
    );
    """
cursor.execute(query)


############################### INSERTION ###############################

# ----------------------------- DEPARTMENT

# Insert row into table
query = """
   INSERT INTO Department
    VALUES ('DEP01', 'Department of Business', 'James Morrison', 162);
    """
cursor.execute(query)

query = """
   INSERT INTO Department
    VALUES ('DEP02', 'Department of Science', 'Lily Watson', 134);
    """
cursor.execute(query)

query = """
   INSERT INTO Department
    VALUES ('DEP03', 'Department of Psychology', 'Emma Howell', 127);
    """
cursor.execute(query)

query = """
   INSERT INTO Department
    VALUES ('DEP04', 'Department of Mathematics', 'Drew Brown', 139);
    """
cursor.execute(query)

query = """
   INSERT INTO Department
    VALUES ('DEP05', 'Department of Engineering', 'Theodore Shaw', 125);
    """
cursor.execute(query)

# ----------------------------- Student

query = """
   INSERT INTO Student
    VALUES ('R0001', 'Gabriela Serrano Echenagucia', 'GSE');
    """
cursor.execute(query)

query = """
   INSERT INTO Student
    VALUES ('R0002', 'Andrea Smith', 'AS');
    """
cursor.execute(query)

query = """
   INSERT INTO Student
    VALUES ('R0003', 'Ana Reyes Gil', 'ARG');
    """
cursor.execute(query)

query = """
   INSERT INTO Student
    VALUES ('R0004', 'Luis Herrera', 'LH');
    """
cursor.execute(query)

query = """
   INSERT INTO Student
    VALUES ('R0005', 'John Lee', 'JL');
    """
cursor.execute(query)

# ----------------------------- Major

query = """
   INSERT INTO Major
    VALUES ('BUS', 'Business', 'DEP01');
    """
cursor.execute(query)

query = """
   INSERT INTO Major
    VALUES ('BIO', 'Biology', 'DEP02');
    """
cursor.execute(query)

query = """
   INSERT INTO Major
    VALUES ('PSY', 'Psychology', 'DEP03');
    """
cursor.execute(query)

query = """
   INSERT INTO Major
    VALUES ('MTH', 'Mathematics', 'DEP04');
    """
cursor.execute(query)

query = """
   INSERT INTO Major
    VALUES ('CSC', 'Computer Science', 'DEP02');
    """
cursor.execute(query)

query = """
   INSERT INTO Major
    VALUES ('ECE', 'Electrical Engineering', 'DEP05');
    """
cursor.execute(query)

# ----------------------------- Event

query = """
   INSERT INTO Event
    VALUES ('EV000', 'Public Speaking 101', '2022-01-31', '2022-02-01');
    """
cursor.execute(query)

query = """
   INSERT INTO Event
    VALUES ('EV001', 'Networking in Business', '2022-03-16', '2022-03-18');
    """
cursor.execute(query)

query = """
   INSERT INTO Event
    VALUES ('EV002', 'Green Day', '2022-03-02', '2022-03-03');
    """
cursor.execute(query)

query = """
   INSERT INTO Event
    VALUES ('EV003', 'Logic and Games', '2022-01-14', '2022-01-15');
    """
cursor.execute(query)

query = """
   INSERT INTO Event
    VALUES ('EV004', 'Spring Hackathon', '2022-02-21', '2022-02-26');
    """
cursor.execute(query)

# ----------------------------- DeptEvent

query = """
   INSERT INTO DeptEvent
    VALUES ('DEP01', 'EV000');
    """
cursor.execute(query)

query = """
   INSERT INTO DeptEvent
    VALUES ('DEP01', 'EV001');
    """
cursor.execute(query)

query = """
   INSERT INTO DeptEvent
    VALUES ('DEP02', 'EV002');
    """
cursor.execute(query)

query = """
   INSERT INTO DeptEvent
    VALUES ('DEP04', 'EV003');
    """
cursor.execute(query)

query = """
   INSERT INTO DeptEvent
    VALUES ('DEP05', 'EV004');
    """
cursor.execute(query)

# ----------------------------- StudentAttendance

query = """
   INSERT INTO StudentAttendance
    VALUES ('R0004', 'EV003');
    """
cursor.execute(query)

query = """
   INSERT INTO StudentAttendance
    VALUES ('R0002', 'EV001');
    """
cursor.execute(query)

query = """
   INSERT INTO StudentAttendance
    VALUES ('R0005', 'EV002');
    """
cursor.execute(query)

query = """
   INSERT INTO StudentAttendance
    VALUES ('R0001', 'EV003');
    """
cursor.execute(query)

query = """
   INSERT INTO StudentAttendance
    VALUES ('R0001', 'EV004');
    """
cursor.execute(query)

query = """
   INSERT INTO StudentAttendance
    VALUES ('R0003', 'EV000');
    """
cursor.execute(query)

# ----------------------------- StudentMajor

query = """
   INSERT INTO StudentMajor
    VALUES ('R0001', 'CSC');
    """
cursor.execute(query)

query = """
   INSERT INTO StudentMajor
    VALUES ('R0002', 'BUS');
    """
cursor.execute(query)

query = """
   INSERT INTO StudentMajor
    VALUES ('R0003', 'PSY');
    """
cursor.execute(query)

query = """
   INSERT INTO StudentMajor
    VALUES ('R0004', 'MTH');
    """
cursor.execute(query)

query = """
   INSERT INTO StudentMajor
    VALUES ('R0005', 'BIO');
    """
cursor.execute(query)


############################### QUERIES ###############################

# List all events that take place in February
# Select data
query = """
    SELECT * 
    FROM Event
    WHERE (start_date LIKE '____-02-__') OR (end_date LIKE '____-02-__');
    """
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)
print("\n")

# Example to extract a specific column
# print(df['name'])

# List all students whose name start with an 'A'
query = """
    SELECT *
    FROM Student
    WHERE studentName LIKE 'A%';
    """
cursor.execute(query)
column_names = [row[0] for row in cursor.description]
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)
print(df)
print(df.columns)
print("\n")

# List all students who plan to attend the Spring Hackathon
query = """
    SELECT s.studentID, s.studentName, e.eventNo, e.eventName, e.start_date, e.end_date
    FROM StudentAttendance a, Student s, Event e
    WHERE (a.studentID = s.studentID) AND (a.eventNo = e.eventNo) AND (e.eventName = 'Spring Hackathon');
    """
cursor.execute(query)
column_names = [row[0] for row in cursor.description]
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)
print(df)
print(df.columns)
print("\n")

# List all details of the Department that has the most faculty  

# The following query works (in SQLite but not Oracle), but chose the other one to use GROUP BY with aggregate function MAX():
#query = """
#    SELECT deptNo, deptName, chairName, MAX(faculty_count) AS faculty_count
#    FROM Department;
#   """

# Works in SQLite and Oracle Live SQL Server:
query = """
    SELECT deptNo, deptName, chairName, MAX(faculty_count) AS faculty_count
    FROM Department
    WHERE faculty_count = (SELECT MAX(faculty_count) FROM Department)
    GROUP BY deptNo, deptName, chairName;
   """
 
cursor.execute(query)
column_names = [row[0] for row in cursor.description]
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)
print(df)
print(df.columns)
print("\n")

# List all students whose major belongs to the Department of Science
query = """
    SELECT s.studentID, s.studentName, m.majorCode, d.deptName
    FROM Student s, Department d, Major m, StudentMajor sm
    WHERE (s.studentID = sm.studentID) AND (m.majorCode = sm.majorCode) AND (d.deptNo = m.deptNo) AND (d.deptName = 'Department of Science');
    """
cursor.execute(query)
column_names = [row[0] for row in cursor.description]
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)
print(df)
print(df.columns)

# Commit any changes to the database
db_connect.commit()

# Close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
db_connect.close()