from employee import Employee
from hourlyemployee import HourlyEmployee
from salaryemployee import SalaryEmployee

class Company:
    COMPANY_NAME = "The Boring Société Anonym et Compagnie"
    def __init__(self):
        self.salaried_employes:SalaryEmployee[list] = []
        self.hourly_employees: HourlyEmployee[list] = []
        self.salary_expense = 0

    def add_new_employee(self):

        print("\nIs this a salaried employee?")
        is_salaried = True if input("Enter 'yes' or 'no': ").lower() == "yes" else False
        first = input("Employee First Name: ")
        last = input("Employee Last Name: ")

        if is_salaried:
            salary = float(input("Enter employee salary(ex. 42500 or 43,487.79)"))
            new_employee = SalaryEmployee(first, last, salary)
            print(f"New Salaried Employee Created:{new_employee}")
            self.salaried_employes.append(new_employee)
            print(
                f"Logging: Added new salaried-employee: {new_employee.first_name}, {new_employee.last_name} to the company's salaried employee list."
            )
        else:
            hourly_rate = float(input("Enter Hourly rate(ex. 15 for $15/hr)"))
            work_hours = float(input("Enter expected weekly hours(ex. 40 or 50)"))
            new_employee = HourlyEmployee(first, last, hours=work_hours, rate=hourly_rate)
            print(f"New Hourly Employee Created:\n{new_employee}")
            self.hourly_employees.append(new_employee)
            print(
                f"Logging: Added new hourly-employee: {new_employee.first_name}, {new_employee.last_name} to the company's hourly employee list."
            )

    def pay_employees(self):
        for employee in self.salaried_employes + self.hourly_employees:
            employee.calculate_gross_pay()
        self.salary_expense = Employee.SALARY_EXPENSE

    def pay_bonuses(self):
        for employee in self.salaried_employes + self.hourly_employees:
            employee.calculate_bonus_pay(15)
        self.salary_expense = Employee.SALARY_EXPENSE

if __name__ == "__main__":
    co = Company()
    print(co.COMPANY_NAME)

    for i in range(1, 5):
        co.add_new_employee()

    for i in range(1, 53):
        co.pay_employees()
        if i == 2:
            co.pay_bonuses()
    for emp in co.salaried_employes + co.hourly_employees:
        print(emp)
    print(f"{co.salary_expense:.2f}")
