from employee import Employee

class SalaryEmployee(Employee):
    def __init__(self, first, last, base_salary=0):
        super().__init__(first, last)
        self.base_salary = base_salary
        self.gross_pay = 0

    def __str__(self):
        return f"""\nfirst: {self.first_name}\nlast: {self.last_name}\nregular-pay: ${self.gross_pay:.2f}\nbonus-pay: ${self.current_bonus_pay:.2f}\nytd-earnings: ${self.ytd_gross_pay:.2f}\nytd-bonus-pay: ${self.ytd_bonus_pay:.2f}"""

    def __repr__(self):
        return f"""HourlyEmployee(first:str, last:str, hours:float(default=40.0), rate:float(default=15))"""

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.base_salary = new_salary

    def calculate_bonus_pay(self, bonus_rate):
        if bonus_rate <= 0:
            self.current_bonus_pay = 0
        else:
            self.current_bonus_pay = self.base_salary * (bonus_rate / 100)

        self.ytd_bonus_pay += self.current_bonus_pay
        self.ytd_gross_pay += self.current_bonus_pay
        Employee.SALARY_EXPENSE += self.current_bonus_pay

    def calculate_gross_pay(self):
        self.gross_pay = self.base_salary / 52
        self.ytd_gross_pay += self.gross_pay
        Employee.SALARY_EXPENSE += self.gross_pay


if __name__ == "__main__":
    sal_emp1 = SalaryEmployee("Lara", "Croft", 210000)

    sal_emp1.hours_worked = 50.00
    sal_emp1.hourly_rate = 93.87
    for i in range(52):
        # weekly salary based on 45 hours
        sal_emp1.calculate_gross_pay()
        if i == 51:
            sal_emp1.calculate_bonus_pay(20)

    print(sal_emp1)
    print(f"Total Salary Expense: {Employee.SALARY_EXPENSE}")
