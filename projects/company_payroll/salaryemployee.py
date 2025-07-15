from employee import Employee

class SalaryEmployee(Employee):

    def __init__(self, first, last, base_salary: float = 0.0):
        super().__init__(first, last)
        self.base_salary = base_salary
        self.gross_pay = 0

    def __str__(self):
        return (
            f"\nEmployee Personal Info:"
            f"\nfirst: {self.first_name}"
            f"\nlast: {self.last_name}"
            f"\nPay Info:"
            f"\nregular-pay: ${self.gross_pay:.2f}"
            f"\nbonus-pay: ${self.current_bonus_pay:.2f}"
            f"\nYear-to-Date Info:"
            f"\nytd-earnings: ${self.ytd_gross_pay:.2f}"
            f"\nytd-bonus-pay: ${self.ytd_bonus_pay:.2f}\n"
        )

    def __repr__(self):
        return (
            f"SalaryEmployee(first={repr(self.first_name)}, "
            f"last={repr(self.last_name)}, "
            f"base_salary={repr(self.base_salary)})"
        )

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
    sal_emp1 = SalaryEmployee(first="Lara", last="Croft", base_salary=210000)
    print(eval(repr(sal_emp1)))
    for i in range(1, 53):
        # weekly salary based on 45 hours
        sal_emp1.calculate_gross_pay()
        if i == 51:
            sal_emp1.calculate_bonus_pay(20)
    print(f"Check # {"200"+str(i) if i < 10 else "20"+str(i)}")
    print(sal_emp1)
