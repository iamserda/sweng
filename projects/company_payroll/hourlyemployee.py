from employee import Employee


class HourlyEmployee(Employee):
    """Class to create new Hourly Employee. It inherits from the base Employee class. HourlyEmployee(first:str, last:str, hours:float(default=40.0), rate:float(default=15))"""

    def __init__(
        self,
        first: str,
        last: str,
        hours: float = 0,
        rate: float = Employee.MINIMUM_WAGE,
    ):
        """
        Creates a new Hourly Employee instance.
        HourlyEmployee(first:str(required), last:str(required), hours:float(default=40.0), rate:float(default=15))
        """
        super().__init__(first, last)
        self.hours_worked: float = hours
        self.hourly_rate: float = rate
        self.ot_hourly_rate: float = self.hourly_rate * 1.5
        self.ot_hours_worked: float = 0
        self.regular_pay: float = 0
        self.ytd_regular_pay: float = 0
        self.ot_pay: float = 0
        self.ytd_ot_pay: float = 0

    def __str__(self) -> str:
        return f"""
Employee(Hourly): Personal Info:
first: {self.first_name}
last: {self.last_name}
\nRegular Pay Info:
hourly-rate: {self.hourly_rate:.2f}
hours-worked: {self.hours_worked:.2f}
regular-pay: ${self.regular_pay:.2f}
\nOvertime and Bonus Pay Info(if applicable):
ot-pay: ${self.ot_pay:.2f}
bonus-pay: ${self.current_bonus_pay:.2f}
\nYear-To-Date:
ytd-regular-pay: ${self.ytd_regular_pay:.2f}
ytd-bonus-pay: ${self.ytd_bonus_pay:.2f}
ytd-ot-pay: ${self.ytd_ot_pay:.2f}
ytd-earnings: ${self.ytd_gross_pay:.2f}"""

    def __repr__(self) -> str:
        return f"""HourlyEmployee(first:str, last:str, hours:float(default=40.0), rate:float(default=15))"""

    def update_hourly_rate(self, new_hourly_rate: float) -> None:
        if new_hourly_rate >= Employee.MINIMUM_WAGE:
            self.hourly_rate = new_hourly_rate
        else:
            print(
                f"The 'Hourly Rate' must be equal or more than the minimum wage.\nMinimum wage is currently {Employee.MINIMUM_WAGE}."
            )

    def update_hours_worked(self, hours_worked: float) -> None:
        if hours_worked < 0:
            print("Work hours cannot be negative.")
            return
        if hours_worked > 60:
            print("Work hours cannot be more than 80. Please reach out to manager.")
            return

        self.hours_worked = hours_worked
        logging_message = f"Updated this week's hours worked to {hours_worked} for employee: {self.first_name}, {self.last_name}"

    def calculate_gross_pay(self) -> None:
        if self.hours_worked <= 0:
            print(
                "Hours worked cannot be less or equal to 0.\n \
                Update work hours for this employee and try again."
            )
            return
        if self.hourly_rate < Employee.MINIMUM_WAGE:
            print(
                f"The 'Hourly Rate' cannot be less than \
                the legal minimum-wage: {Employee.MINIMUM_WAGE}."
            )
            print("Update hourly rate for thihs employee, and try again.")
            return

        self.ot_pay = 0
        self.ot_hours_worked = self.hours_worked - Employee.DEFAULT_WORK_HOURS

        if self.ot_hours_worked > 0:
            self.ot_pay = self.ot_hours_worked * self.ot_hourly_rate
            self.ytd_ot_pay += self.ot_pay

        self.regular_pay = self.hourly_rate * Employee.DEFAULT_WORK_HOURS
        self.ytd_regular_pay += self.regular_pay

        self.current_gross_pay = self.regular_pay + self.ot_pay
        self.ytd_gross_pay += self.current_gross_pay

        Employee.SALARY_EXPENSE += self.current_gross_pay

    def calculate_bonus_pay(self, bonus_rate) -> None:
        multiplyer = bonus_rate / 100
        self.current_bonus_pay = self.ytd_regular_pay * multiplyer
        self.ytd_bonus_pay += self.current_bonus_pay
        self.ytd_gross_pay += self.current_bonus_pay
        Employee.SALARY_EXPENSE += self.current_bonus_pay


if __name__ == "__main__":
    hr_emp1 = HourlyEmployee("James", "Bond")
    hr_emp1.hours_worked = 50.00
    hr_emp1.hourly_rate = 46.45
    for i in range(52):
        # weekly salary based on 45 hours
        hr_emp1.calculate_gross_pay()
        if i == 51:
            hr_emp1.calculate_bonus_pay(15)
        print(f"""\ncheck #\n{"100"+str(i) if i < 10 else "10"+str(i)}\n{hr_emp1}""")
