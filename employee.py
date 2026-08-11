class Employee:

    def __init__(
        self,
        emp_id,
        name,
        age,
        department,
        salary,
        gender="",
        email="",
        phone="",
        joining_date=""
    ):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary
        self.gender = gender
        self.email = email
        self.phone = phone
        self.joining_date = joining_date

    def display_details(self):
        print("\n" + "=" * 50)
        print("              Employee Details")
        print("=" * 50)

        print(f"Employee ID  : {self.emp_id}")
        print(f"Name         : {self.name}")
        print(f"Age          : {self.age}")
        print(f"Gender       : {self.gender}")
        print(f"Department   : {self.department}")
        print(f"Salary       : ₹{self.salary}")
        print(f"Email        : {self.email}")
        print(f"Phone        : {self.phone}")
        print(f"Joining Date : {self.joining_date}")

        print("=" * 50)