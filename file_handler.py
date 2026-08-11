from employee import Employee


FILE_NAME = "employees.txt"


def save_employee(emp):
    with open(FILE_NAME, "a") as file:
        file.write(
            f"{emp.emp_id}|"
            f"{emp.name}|"
            f"{emp.age}|"
            f"{emp.department}|"
            f"{emp.salary}|"
            f"{emp.gender}|"
            f"{emp.email}|"
            f"{emp.phone}|"
            f"{emp.joining_date}\n"
        )


def load_employees():
    employees = []

    try:
        with open(FILE_NAME, "r") as file:

            for line in file:
                line = line.strip()

                if line == "":
                    continue

                # New format uses |
                if "|" in line:
                    data = line.split("|")

                # Old format may use ,
                else:
                    data = line.split(",")

                # Old employee format - 5 fields
                if len(data) == 5:

                    try:
                        emp = Employee(
                            data[0].strip(),
                            data[1].strip(),
                            int(data[2].strip()),
                            data[3].strip(),
                            float(data[4].strip())
                        )

                        employees.append(emp)

                    except ValueError:
                        print("Invalid old employee record. Skipping record.")

                # New employee format - 9 fields
                elif len(data) == 9:

                    try:
                        emp = Employee(
                            data[0].strip(),
                            data[1].strip(),
                            int(data[2].strip()),
                            data[3].strip(),
                            float(data[4].strip()),
                            data[5].strip(),
                            data[6].strip(),
                            data[7].strip(),
                            data[8].strip()
                        )

                        employees.append(emp)

                    except ValueError:
                        print("Invalid employee record. Skipping record.")

                else:
                    print("Invalid employee data found. Skipping record.")

    except FileNotFoundError:
        pass

    return employees


def save_all_employees(employees):

    with open(FILE_NAME, "w") as file:

        for emp in employees:
            file.write(
                f"{emp.emp_id}|"
                f"{emp.name}|"
                f"{emp.age}|"
                f"{emp.department}|"
                f"{emp.salary}|"
                f"{emp.gender}|"
                f"{emp.email}|"
                f"{emp.phone}|"
                f"{emp.joining_date}\n"
            )

import shutil


BACKUP_FILE = "employees_backup.txt"


def backup_data():
    try:
        shutil.copyfile(FILE_NAME, BACKUP_FILE)
        print("\n✅ Employee data backup created successfully!")

    except FileNotFoundError:
        print("\n❌ No employee data found to backup.")


def restore_data():
    try:
        shutil.copyfile(BACKUP_FILE, FILE_NAME)
        print("\n✅ Employee data restored successfully!")

    except FileNotFoundError:
        print("\n❌ Backup file not found!")            