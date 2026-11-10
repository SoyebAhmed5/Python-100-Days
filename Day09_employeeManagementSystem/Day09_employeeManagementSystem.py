# Employee Management System

# Base Class: Employee
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        
    def display_info(self):
        print("\n__Employee Details__")
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.salary}")
        
    def calculate_bonus(self):
        return self.salary * 0.1
    
# Derived Class : Manager
class Manager(Employee):
    def __init__(self, name, emp_id, salary,department):
        super().__init__(name, emp_id, salary)
        self.department = department
        
    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
        
    def calculate_bonus(self):
        return self.salary * 2
        
# Derived Class: Developer
class Developer(Employee):
    def __init__(self, name, emp_id, salary, programming_language):
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language
        
    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")
        
    def calculate_bonus(self):
        return self.salary * 0.5
    
# Main Program
employee = []

def add_employee():
    print("\n--- Choose Employee Type ---")
    print("1. Employee")
    print("2. Manager")
    print("3. Developer")
    choice = int(input("Enter your choice: "))
    
    name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")
    salary = float(input("Enter employee salary: "))
    
    if choice == 1:
       
        emp = Employee(name, emp_id, salary)
        employee.append(emp)
    elif choice == 2:
        department = input("Enter department: ")
        mgr = Manager(name, emp_id, salary, department)
        employee.append(mgr)
    elif choice == 3:
        programming_language = input("Enter programming language: ")
        dev = Developer(name, emp_id, salary, programming_language)
        employee.append(dev)
        
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Calculate Bonus")
        print("4. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            add_employee()
            
        elif choice == '2':
            if not employee:
                print("No employees in the system.")
            else:
                for emp in employee:
                    emp.display_info()
                    
        elif choice == '3':
            if not employee:
                print("No employees in the system.")
            else:
                for emp in employee:
                    bonus = emp.calculate_bonus()
                    print(f"Bonus for {emp.name} (ID: {emp.emp_id}): {bonus}")
                    
        elif choice == '4':
            print("Exiting Employee Management System.")
            break
            
        else:
            print("Invalid choice. Please try again.")