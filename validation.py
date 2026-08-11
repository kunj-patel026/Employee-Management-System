def validate_employee_id(employees):
    while True:
        emp_id = input("Enter Employee ID: ").strip()

        if emp_id == "":
            print("Employee ID cannot be empty.")
            continue

        duplicate = False

        for emp in employees:
            if str(emp.emp_id).strip().lower() == emp_id.lower():
                duplicate = True
                break

        if duplicate:
            print("Employee ID already exists! Please enter another ID.")
        else:
            return emp_id


def validate_name():
    while True:
        name = input("Enter Name: ").strip()

        if name == "":
            print("Name cannot be empty.")

        elif not name.replace(" ", "").isalpha():
            print("Name should contain letters only.")

        else:
            return name


def validate_age():
    while True:
        try:
            age = int(input("Enter Age: "))

            if 18 <= age <= 60:
                return age

            print("Age must be between 18 and 60.")

        except ValueError:
            print("Please enter a valid number.")


def validate_gender():
    while True:
        gender = input("Enter Gender (Male/Female/Other): ").strip().capitalize()

        if gender in ["Male", "Female", "Other"]:
            return gender

        print("Please enter Male, Female, or Other.")


def validate_department():
    while True:
        department = input("Enter Department: ").strip()

        if department == "":
            print("Department cannot be empty.")
        else:
            return department


def validate_salary():
    while True:
        try:
            salary = float(input("Enter Salary: "))

            if salary > 0:
                return salary

            print("Salary must be greater than 0.")

        except ValueError:
            print("Please enter a valid salary.")


def validate_email():
    while True:
        email = input("Enter Email: ").strip()

        if email == "":
            print("Email cannot be empty.")
            continue

        if "@" not in email or "." not in email:
            print("Please enter a valid email address.")
            continue

        return email


def validate_phone():
    while True:
        phone = input("Enter Phone Number: ").strip()

        if len(phone) != 10:
            print("Phone number must contain exactly 10 digits.")
            continue

        if not phone.isdigit():
            print("Phone number must contain digits only.")
            continue

        return phone


def validate_joining_date():
    while True:
        joining_date = input("Enter Joining Date (DD-MM-YYYY): ").strip()

        parts = joining_date.split("-")

        if len(parts) != 3:
            print("Invalid date format. Use DD-MM-YYYY.")
            continue

        day, month, year = parts

        if not (day.isdigit() and month.isdigit() and year.isdigit()):
            print("Date must contain numbers only.")
            continue

        day = int(day)
        month = int(month)
        year = int(year)

        if 1 <= day <= 31 and 1 <= month <= 12 and 2000 <= year <= 2100:
            return joining_date

        print("Invalid date. Please enter a valid DD-MM-YYYY date.")