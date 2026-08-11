def show_dashboard(employees):

    if len(employees) == 0:
        print("\n❌ No employee data available!")
        return

    total_employees = len(employees)

    total_salary = sum(emp.salary for emp in employees)
    average_salary = total_salary / total_employees

    departments = set(emp.department for emp in employees)

    highest_paid = max(employees, key=lambda emp: emp.salary)
    lowest_paid = min(employees, key=lambda emp: emp.salary)

    print("\n" + "=" * 70)
    print("                 EMPLOYEE DASHBOARD")
    print("=" * 70)

    print(f"\n👥 Total Employees       : {total_employees}")
    print(f"🏢 Total Departments     : {len(departments)}")
    print(f"💰 Average Salary        : ₹{average_salary:.2f}")

    print("\n🏆 Highest Paid Employee")
    print(f"   Name                 : {highest_paid.name}")
    print(f"   Employee ID          : {highest_paid.emp_id}")
    print(f"   Salary               : ₹{highest_paid.salary}")

    print("\n📉 Lowest Paid Employee")
    print(f"   Name                 : {lowest_paid.name}")
    print(f"   Employee ID          : {lowest_paid.emp_id}")
    print(f"   Salary               : ₹{lowest_paid.salary}")

    print("\n🏢 Departments")
    print("-" * 70)

    for department in sorted(departments):
        count = sum(
            1 for emp in employees
            if emp.department.lower() == department.lower()
        )

        print(f"   {department:<25} : {count} employee(s)")

    print("=" * 70)