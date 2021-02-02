import mysql.connector
#import datetime
#from dateutil.relativedelta import relativedelta
#from dateutil.parser import *
def get_connection(localhost,user,pswd,dbname):
    connection = mysql.connector.connect(host=localhost,
                                         user=user,
                                         password=pswd,
                                         database=dbname)
    return connection
def close_connection(connection):
    if connection:
        connection.close()
host=input("Enter host name\n")
username= input("Enter user name\n")
pswd= input("Enter password\n")
dbname = input("Enter database name\n")
connection = get_connection(host,username,pswd,dbname)
cursor = connection.cursor()
def read_database_version():
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print("You are connected to MySQL version: ", db_version)
read_database_version()
def create_table():
        q1= "create table if not exists Hospital( Hospital_Id INTEGER NOT NULL PRIMARY KEY, Hospital_Name TEXT(50) NOT NULL, Bed_Count INTEGER NOT NULL)"
        cursor.execute(q1)
        for s in range(0,2):
            hospital_id = input('Hospital Id: ')
            hospital_name = input('Hospital name: ')
            bed_count = input('bed count:')
            insert_data = ("""INSERT INTO Hospital (Hospital_Id,Hospital_Name, Bed_Count)
            VALUES ({},'{}',{});""".format(hospital_id,hospital_name,bed_count))
            cursor.execute(insert_data)
        q2 = "create table if not exists Doctor(Doctor_Id INTEGER NOT NULL PRIMARY KEY,Doctor_Name TEXT NOT NULL, Hospital_Id INTEGER NOT NULL, Joining_Date TEXT(50) NOT NULL, Speciality TEXT NOT NULL, Salary INTEGER NOT NULL,Experience INTEGER)"
        cursor.execute(q2)
        for k in range(0, 2):
            Doctor_Id= input('Doctor Id: ')
            Doctor_Name= input('Doctor name: ')
            Hospital_Id = input('Hospital Id:')
            Joining_Date = input('Joining Date:')
            Speciality= input('Speciality:')
            Salary = input('Salary:')
            Experience = input('Experience:')
            insert_data1 = ("""INSERT INTO Doctor (Doctor_Id,Doctor_Name,Hospital_Id,Joining_Date,Speciality,Salary,Experience)
                    VALUES ({},'{}',{},'{}','{}',{},{});""".format(Doctor_Id,Doctor_Name,Hospital_Id,Joining_Date,Speciality,Salary,Experience))
            cursor.execute(insert_data1)
create_table()
def get_hospital_details(h_id):
        query1 = f"select * from hospital where hospital_id={h_id}"
        cursor.execute(query1)
        records = cursor.fetchall()
        print("Printing hospital record\n")
        for r in records:
            print("hospital id:",r[0])
            print("hospital name:", r[1])
            print("bed count:", r[2],"\n")
get_hospital_details(2)
def get_doctor_details(d_id):
        query2 = f"select * from doctor where Doctor_Id={d_id}"
        cursor.execute(query2)
        data=cursor.fetchall()
        print("Printing doctor record\n")
        for d in data:
            print( "Doctor Id:",d[0])
            print("Doctor Name:",d[1])
            print("Hospital Id:",d[2])
            print("Joining Date:",d[3])
            print("Specialty:",d[4])
            print("Salary:",d[5])
            print("Experience:",d[6])
get_doctor_details(105)
def get_specialist_doctors_list(speciality, salary):
        query3 = f"select * from doctor where Speciality=%s and Salary > %s"
        cursor.execute(query3,(speciality, salary))
        lst = cursor.fetchall()
        print("Printing doctors whose speciality is",speciality,"and salary greater than",salary,"\n")
        for l in lst:
            print("Doctor Id:",l[0])
            print("Doctor Name:", l[1])
            print("Hospital Id:", l[2])
            print("Joining Date:", l[3])
            print("Speciality:", l[4])
            print("Salary:", l[5])
            print("Experience:", l[6],"\n")
        close_connection(connection)
get_specialist_doctors_list("Garnacologist", 30000)
def get_doctors(hospital_id):
        query4=f"select * from doctor where Hospital_Id=%s"
        cursor.execute(query4,(hospital_id,))
        lst1=cursor.fetchall()
        for l in lst1:
            print(l)
get_doctors(2)
close_connection(connection)