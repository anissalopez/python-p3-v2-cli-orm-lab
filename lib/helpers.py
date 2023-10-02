from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name = input("Please enter employee name: ")
    employees = Employee.get_all()
    search = ""
    for employee in employees:
        if name.lower() == employee.name.lower():
            search = employee.name
    try:
            employee_match = Employee.find_by_name(search)
            print(employee_match)
    except Exception as exc:
            print("error finding employee", exc)


            
    9

def find_employee_by_id():
    id = input("please enter employee id: ")
    employee = Employee.find_by_id(id)
    print(employee) if employee else print("Employee id is invalid")
   


def create_employee():
    name = input("Enter employee name: ")
    department_id = int(input("Please enter department id: "))
    job_title = input("Please enter job title: ")
    try:
        employee = Employee.create(name=name, department_id=department_id, job_title=job_title)
        print(f"{employee.name} succesfully entered into database")
    except Exception as exc:
        print("Error", exc)


def update_employee():
    id = int(input("Please enter employee id: "))
    if employee := Employee.find_by_id(id):
        try:
            name = input("Please enter employee name: ")
            employee.name = name
            department = input("Please enter department: ")
            employee.department_id = int(department)
            job = input("Please enter job title: ")
            employee.job_title  = job
            employee.update()
            print(employee)
        except Exception as exc:
            print("Error", exc)
    else:
        print(f"Department {id} not found")





def delete_employee():
    employee_id = input("please enter employee id: ")
    if employee := Employee.find_by_id(employee_id):
        employee.delete()
    else:
        print(f"Employee {employee_id} is invalid")


def list_department_employees():
    department_id = input("please enter deparment id: ")
    if department := Department.find_by_id(department_id):
        for employees in department.employees():
            print(employees)
    else:
        print(f"{department_id} is invalid")