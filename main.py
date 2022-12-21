from company import Company, Employee

company = Company()
company.connection_make()

while True:
    order = input("Write order:")
    if order =="create":
        name = input("Write name of the employee:")
        surname = input("Write surname of employee:")
        Father_name = input("Enter father's name: ")
        Date_of_birth = int(input("Enter date of birth:"))
        employee = Employee(name,surname,Father_name,Date_of_birth)
        company.employee_add(employee)
        print("Succesfully added")
    elif order=="search":
        employee_name = input("Write name of the employee:")
        company.employee_search(employee_name)
    elif order == "show_all":
        company.show_employee()