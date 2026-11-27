import csv


class InvalidSalaryError(Exception):
    pass


def bonus(salary, rate=0.1, *extras, **options):
    result = salary * rate + sum(extras)

    if "cap" in options:
        result = min(result, options["cap"])

    return result


class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")

        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return (
            f"Manager: {self.name}, "
            f"Salary: {self.salary}, "
            f"Team Size: {self.team_size}"
        )


# Read data from CSV
employees = []

try:
    with open("employees.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                # Skip rows with empty salary
                if not row["salary"].strip():
                    print("Skipped row with empty salary:", row)
                    continue

                row["id"] = int(row["id"])
                row["salary"] = int(row["salary"])

                employees.append(row)

            except ValueError:
                print("Invalid data found. Row skipped:", row)

except FileNotFoundError:
    print("employees.csv not found!")
    exit()


# Employees earning above 50000
above_50000 = [
    emp["name"]
    for emp in employees
    if emp["salary"] > 50000
]

print("\nAbove 50000:")
print(above_50000)


# Salary hike of 10%
raised_salaries = list(
    map(lambda emp: emp["salary"] * 1.10, employees)
)

print("\nRaised Salaries:")
print(raised_salaries)


# Chennai employees
chennai_employees = list(
    filter(lambda emp: emp["city"].strip().lower() == "chennai", employees)
)

chennai_names = [emp["name"] for emp in chennai_employees]

print("\nChennai Employees:")
print(chennai_names)


# Loop example
print("\nLoop Output:")

salary_list = [30000, 0, 45000, 60000, 75000, 90000, 52000]

for sal in salary_list:

    if sal == 0:
        continue

    print("Salary:", sal)

    if sal > 85000:
        print("Salary above 85000 found. Stopping...")
        break


# Bonus examples
print("\nBonus Examples:")
print(bonus(50000))
print(bonus(50000, 0.15, 1000, 2000))
print(bonus(50000, 0.15, 1000, 2000, cap=7000))


# Employee and Manager Objects
emp1 = Employee("Rahul", 60000)
mgr1 = Manager("Divya", 75000, 5)

print("\nEmployee Details:")
print(emp1.get_details())
print("Annual Salary:", emp1.annual_salary())

print("\nManager Details:")
print(mgr1.get_details())
print("Annual Salary:", mgr1.annual_salary())


# Exception Handling
try:
    invalid_emp = Employee("Test", -500)

except InvalidSalaryError as e:
    print("\nError:", e)

finally:
    print("Transaction finished")