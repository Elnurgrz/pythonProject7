import sqlite3

class Employee:
    def __init__(self,name,surname,Father_name,Date_of_birth):
        self.name = name
        self.surname = surname
        self.Father_name = Father_name
        self.Date_of_birth = Date_of_birth

    def __str__(self):
        return f"employee name:({self.name},Surname:{self.Surname},Father name:{self.Father_name},Date of birth:{self.Date_of_birth}"

class Company:
    def __init__(self):
        self.connection_make()
    def connection_make(self):

        self.connection = sqlite3.connect("company.db")        # what is db??? (data base)
        self.cursor = self.connection.cursor()
        sql_command = "Create table if not exists company (Name TEXT, Surname TEXT, Father_name TEXT, Date_of_birth INT)"
        self.cursor.execute(sql_command)
        self.connection.commit()           # baxmalisan

    def connection_cut(self):             # yoxlama
        self.connection.close()

    def show_employee(self):
        sql_command = "SELECT * FROM company"
        self.cursor.execute(sql_command)
        employees = self.cursor.fetchall()
        if len(employees) ==0:
            print("There are no employees in company.")
        else:
            for i in employees:
                print(i)

    def employee_add(self,employee):
        sql_command="INSERT INTO company VALUES (?,?,?,?)"
        self.cursor.execute(sql_command,(employee.name,employee.surname,employee.Father_name,employee.Date_of_birth))
        self.connection.commit()

    def employee_delete(self,name):
        sql_command = "DELETE FROM company where NAME = ?"
        self.cursor.execute(sql_command,name)
        self.connection.commit()