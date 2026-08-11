from validation import (
    validate_employee_id,
    validate_name,
    validate_age,
    validate_gender,
    validate_department,
    validate_salary,
    validate_email,
    validate_phone,
    validate_joining_date
)

from auth import login
from employee import Employee
from dashboard import show_dashboard
from file_handler import (
    save_employee,
    load_employees,
    save_all_employees,
    backup_data,
    restore_data
)
employees = load_employees()

def add_employee():
    print("\n===== Add New Employee =====")

    emp_id = validate_employee_id(employees)
    name = validate_name()
    age = validate_age()
    gender = validate_gender()
    department = validate_department()
    salary = validate_salary()
    email = validate_email()
    phone = validate_phone()
    joining_date = validate_joining_date()

    emp = Employee(
        emp_id,
        name,
        age,
        department,
        salary,
        gender,
        email,
        phone,
        joining_date
    )

    employees.append(emp)
    save_employee(emp)

    print("\n✅ Employee Added Successfully!")


def view_employees():
    if len(employees) == 0:
        print("\n❌ No Employee Found!")
        return

    print("\n" + "=" * 130)
    print(
        f"{'ID':<8}"
        f"{'Name':<20}"
        f"{'Age':<6}"
        f"{'Gender':<10}"
        f"{'Department':<18}"
        f"{'Salary':<14}"
        f"{'Email':<28}"
        f"{'Phone':<13}"
        f"{'Joining Date':<15}"
    )

    print("=" * 130)

    for emp in employees:
        print(
            f"{emp.emp_id:<8}"
            f"{emp.name:<20}"
            f"{emp.age:<6}"
            f"{emp.gender:<10}"
            f"{emp.department:<18}"
            f"{emp.salary:<14}"
            f"{emp.email:<28}"
            f"{emp.phone:<13}"
            f"{emp.joining_date:<15}"
        )

    print("=" * 130)
    print(f"Total Employees: {len(employees)}")


def search_employee():
    emp_id = input("\nEnter Employee ID to Search: ").strip()

    for emp in employees:

        if emp.emp_id.lower() == emp_id.lower():

            print("\n" + "=" * 50)
            print("          EMPLOYEE DETAILS")
            print("=" * 50)

            print(f"Employee ID : {emp.emp_id}")
            print(f"Name        : {emp.name}")
            print(f"Age         : {emp.age}")
            print(f"Gender      : {emp.gender}")
            print(f"Department  : {emp.department}")
            print(f"Salary      : ₹{emp.salary}")
            print(f"Email       : {emp.email}")
            print(f"Phone       : {emp.phone}")
            print(f"Joining Date: {emp.joining_date}")

            print("=" * 50)

            return

    print("\n❌ Employee not found!")     

def search_employee_by_name():
    search_name = input("\nEnter Employee Name to Search: ").strip().lower()

    found = False

    for emp in employees:

        if search_name in emp.name.lower():

            if not found:
                print("\n" + "=" * 50)
                print("          SEARCH RESULTS")
                print("=" * 50)

            found = True

            print(f"\nEmployee ID : {emp.emp_id}")
            print(f"Name        : {emp.name}")
            print(f"Age         : {emp.age}")
            print(f"Gender      : {emp.gender}")
            print(f"Department  : {emp.department}")
            print(f"Salary      : ₹{emp.salary}")
            print(f"Email       : {emp.email}")
            print(f"Phone       : {emp.phone}")
            print(f"Joining Date: {emp.joining_date}")

            print("-" * 50)

    if not found:
        print("\n❌ No employee found with that name.")

def employee_statistics():

    if len(employees) == 0:
        print("\n❌ No Employee Data Available!")
        return

    total_employees = len(employees)

    total_age = sum(emp.age for emp in employees)
    average_age = total_age / total_employees

    total_salary = sum(emp.salary for emp in employees)
    average_salary = total_salary / total_employees

    highest_salary = max(employees, key=lambda emp: emp.salary)
    lowest_salary = min(employees, key=lambda emp: emp.salary)

    print("\n" + "=" * 60)
    print("              EMPLOYEE STATISTICS")
    print("=" * 60)

    print(f"Total Employees       : {total_employees}")
    print(f"Average Age           : {average_age:.2f}")
    print(f"Average Salary        : ₹{average_salary:.2f}")

    print("\nHighest Paid Employee")
    print(f"Name                  : {highest_salary.name}")
    print(f"Employee ID           : {highest_salary.emp_id}")
    print(f"Salary                : ₹{highest_salary.salary}")

    print("\nLowest Paid Employee")
    print(f"Name                  : {lowest_salary.name}")
    print(f"Employee ID           : {lowest_salary.emp_id}")
    print(f"Salary                : ₹{lowest_salary.salary}")

    # Department statistics
    department_count = {}

    for emp in employees:
        department = emp.department

        if department in department_count:
            department_count[department] += 1
        else:
            department_count[department] = 1

    print("\nEmployees by Department")
    print("-" * 60)

    for department, count in department_count.items():
        print(f"{department:<25} : {count}")

    print("=" * 60)
    
def sort_by_name():

    if len(employees) == 0:
        print("\n❌ No Employee Data Available!")
        return

    print("\n===== SORT EMPLOYEES BY NAME =====")
    print("1. Sort A to Z")
    print("2. Sort Z to A")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        sorted_employees = sorted(
            employees,
            key=lambda emp: emp.name.lower()
        )

        print("\n✅ Employees Sorted A to Z")

    elif choice == "2":
        sorted_employees = sorted(
            employees,
            key=lambda emp: emp.name.lower(),
            reverse=True
        )

        print("\n✅ Employees Sorted Z to A")

    else:
        print("\n❌ Invalid choice!")
        return

    print("\n" + "=" * 78)

    print(
        f"{'ID':<10}"
        f"{'Name':<20}"
        f"{'Age':<8}"
        f"{'Department':<20}"
        f"{'Salary':<15}"
    )

    print("=" * 78)

    for emp in sorted_employees:
        print(
            f"{emp.emp_id:<10}"
            f"{emp.name:<20}"
            f"{emp.age:<8}"
            f"{emp.department:<20}"
            f"{emp.salary:<15}"
        )

    print("=" * 78)

def sort_by_salary():

    if len(employees) == 0:
        print("\n❌ No Employee Data Available!")
        return

    print("\n===== SORT EMPLOYEES BY SALARY =====")
    print("1. Low to High")
    print("2. High to Low")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        sorted_employees = sorted(
            employees,
            key=lambda emp: emp.salary
        )

        print("\n✅ Employees Sorted by Salary: Low to High")

    elif choice == "2":
        sorted_employees = sorted(
            employees,
            key=lambda emp: emp.salary,
            reverse=True
        )

        print("\n✅ Employees Sorted by Salary: High to Low")

    else:
        print("\n❌ Invalid choice!")
        return

    print("\n" + "=" * 78)

    print(
        f"{'ID':<10}"
        f"{'Name':<20}"
        f"{'Age':<8}"
        f"{'Department':<20}"
        f"{'Salary':<15}"
    )

    print("=" * 78)

    for emp in sorted_employees:
        print(
            f"{emp.emp_id:<10}"
            f"{emp.name:<20}"
            f"{emp.age:<8}"
            f"{emp.department:<20}"
            f"{emp.salary:<15}"
        )

    print("=" * 78)

def update_employee():
    emp_id = input("\nEnter Employee ID to Update: ").strip()

    for emp in employees:

        if emp.emp_id.lower() == emp_id.lower():

            print("\n" + "=" * 50)
            print("             UPDATE EMPLOYEE")
            print("=" * 50)

            print("\nCurrent Employee Details:")
            print(f"Name        : {emp.name}")
            print(f"Age         : {emp.age}")
            print(f"Gender      : {emp.gender}")
            print(f"Department  : {emp.department}")
            print(f"Salary      : ₹{emp.salary}")
            print(f"Email       : {emp.email}")
            print(f"Phone       : {emp.phone}")
            print(f"Joining Date: {emp.joining_date}")

            print("\nEnter New Details")
            print("(Press Enter to keep the current value)\n")

            # Name
            new_name = input(f"Enter Name [{emp.name}]: ").strip()

            if new_name != "":
                while True:
                    if new_name.replace(" ", "").isalpha():
                        emp.name = new_name
                        break
                    else:
                        print("Name should contain only letters.")
                        new_name = input(f"Enter Name [{emp.name}]: ").strip()

                        if new_name == "":
                            break

            # Age
            new_age = input(f"Enter Age [{emp.age}]: ").strip()

            if new_age != "":
                while True:
                    try:
                        new_age = int(new_age)

                        if 18 <= new_age <= 100:
                            emp.age = new_age
                            break
                        else:
                            print("Age must be between 18 and 100.")

                    except ValueError:
                        print("Please enter a valid age.")

                    new_age = input(f"Enter Age [{emp.age}]: ").strip()

                    if new_age == "":
                        break

            # Gender
            new_gender = input(
                f"Enter Gender (Male/Female/Other) [{emp.gender}]: "
            ).strip()

            if new_gender != "":
                while True:
                    if new_gender.lower() in ["male", "female", "other"]:
                        emp.gender = new_gender.capitalize()
                        break
                    else:
                        print("Please enter Male, Female, or Other.")

                        new_gender = input(
                            f"Enter Gender [{emp.gender}]: "
                        ).strip()

                        if new_gender == "":
                            break

            # Department
            new_department = input(
                f"Enter Department [{emp.department}]: "
            ).strip()

            if new_department != "":
                emp.department = new_department

            # Salary
            new_salary = input(
                f"Enter Salary [{emp.salary}]: "
            ).strip()

            if new_salary != "":
                while True:
                    try:
                        new_salary = float(new_salary)

                        if new_salary >= 0:
                            emp.salary = new_salary
                            break
                        else:
                            print("Salary cannot be negative.")

                    except ValueError:
                        print("Please enter a valid salary.")

                    new_salary = input(
                        f"Enter Salary [{emp.salary}]: "
                    ).strip()

                    if new_salary == "":
                        break

            # Email
            new_email = input(
                f"Enter Email [{emp.email}]: "
            ).strip()

            if new_email != "":
                while True:
                    if "@" in new_email and "." in new_email:
                        emp.email = new_email
                        break
                    else:
                        print("Please enter a valid email.")

                        new_email = input(
                            f"Enter Email [{emp.email}]: "
                        ).strip()

                        if new_email == "":
                            break

            # Phone
            new_phone = input(
                f"Enter Phone Number [{emp.phone}]: "
            ).strip()

            if new_phone != "":
                while True:
                    if new_phone.isdigit() and len(new_phone) == 10:
                        emp.phone = new_phone
                        break
                    else:
                        print("Phone number must contain exactly 10 digits.")

                        new_phone = input(
                            f"Enter Phone Number [{emp.phone}]: "
                        ).strip()

                        if new_phone == "":
                            break

            # Joining Date
            new_joining_date = input(
                f"Enter Joining Date [{emp.joining_date}]: "
            ).strip()

            if new_joining_date != "":
                emp.joining_date = new_joining_date

            # Save updated data
            save_all_employees(employees)

            print("\n" + "=" * 50)
            print("✅ Employee Updated Successfully!")
            print("=" * 50)

            return

    print("\n❌ Employee not found!")

def delete_employee():
    emp_id = input("\nEnter Employee ID to Delete: ").strip()

    for emp in employees:

        if emp.emp_id.lower() == emp_id.lower():

            print("\n" + "=" * 50)
            print("          EMPLOYEE DETAILS")
            print("=" * 50)

            print(f"Employee ID : {emp.emp_id}")
            print(f"Name        : {emp.name}")
            print(f"Age         : {emp.age}")
            print(f"Gender      : {emp.gender}")
            print(f"Department  : {emp.department}")
            print(f"Salary      : ₹{emp.salary}")
            print(f"Email       : {emp.email}")
            print(f"Phone       : {emp.phone}")
            print(f"Joining Date: {emp.joining_date}")

            print("=" * 50)

            confirm = input(
                "\nAre you sure you want to delete this employee? (Y/N): "
            ).strip().lower()

            if confirm == "y":
                employees.remove(emp)

                save_all_employees(employees)

                print("\n✅ Employee Deleted Successfully!")

            elif confirm == "n":
                print("\n❌ Delete operation cancelled.")

            else:
                print("\n⚠️ Invalid choice. Delete operation cancelled.")

            return

    print("\n❌ Employee not found!")

def department_report():

    if len(employees) == 0:
        print("\n❌ No employee data available!")
        return

    departments = sorted(
        set(emp.department for emp in employees)
    )

    print("\n" + "=" * 50)
    print("           DEPARTMENT REPORT")
    print("=" * 50)

    for i, department in enumerate(departments, start=1):
        print(f"{i}. {department}")

    print(f"{len(departments) + 1}. Back")

    choice = input("\nEnter your choice: ").strip()

    if not choice.isdigit():
        print("\n❌ Please enter a valid number!")
        return

    choice = int(choice)

    if choice == len(departments) + 1:
        return

    if choice < 1 or choice > len(departments):
        print("\n❌ Invalid choice!")
        return

    selected_department = departments[choice - 1]

    department_employees = [
        emp for emp in employees
        if emp.department.lower() == selected_department.lower()
    ]

    total_salary = sum(emp.salary for emp in department_employees)
    average_salary = total_salary / len(department_employees)

    print("\n" + "=" * 80)
    print(f"        {selected_department.upper()} DEPARTMENT REPORT")
    print("=" * 80)

    print(
        f"{'ID':<10}"
        f"{'Name':<20}"
        f"{'Age':<8}"
        f"{'Salary':<15}"
    )

    print("-" * 80)

    for emp in department_employees:
        print(
            f"{emp.emp_id:<10}"
            f"{emp.name:<20}"
            f"{emp.age:<8}"
            f"₹{emp.salary:<14.2f}"
        )

    print("-" * 80)

    print(f"Total {selected_department} Employees : {len(department_employees)}")
    print(f"Average {selected_department} Salary  : ₹{average_salary:.2f}")

    print("=" * 80)


print("\nTesting Login System...")

if login():
    print("You can access the Employee Management System.")
else:
    print("Access Denied. Program Closed.")

while True:    
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee By ID")
    print("4. Search Employee by Name")
    print("5. Update Employee")
    print("6. Delete Employee")
    print("7. Employee Statistics")
    print("8. Sort Employees by Name")
    print("9. Sort Employees by Salary")
    print("10.Dashboard")
    print("11.Employee Report")
    print("12.Backup Data")
    print("13.Restore Data")
    print("14. Exit")

    choice = input("\nEnter your choice: ").strip()

    if not choice.isdigit():
        print("\n❌ Please enter a number from 1 to 14.")
        continue
    choice = int(choice)

    if choice == 1:
        add_employee()

    elif choice == 2:
        view_employees()

    elif choice == 3:
        search_employee()

    elif choice == 4:
        search_employee_by_name()

    elif choice == 5:
        update_employee()

    elif choice == 6:
        delete_employee()

    elif choice == 7:
        employee_statistics()  

    elif choice == 8:
        sort_by_name()  

    elif choice == 9:
        sort_by_salary()        

    elif choice == 10:
        show_dashboard(employees)

    elif choice == 11:
        department_report()  

    elif choice == 12:
        backup_data()

    elif choice == 13:
        restore_data()
        employees = load_employees()
        print("\n✅ Employee data reloaded successfully!")          

    elif choice == 14:
        print("\nThank you for using Employee Management System!")    
        break
        
    else:
        print("\n❌ Invalid choice! Please select a valid option.")
        
             


        