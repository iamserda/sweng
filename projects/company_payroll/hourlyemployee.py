from employee import Employee

class HourlyEmployee(Employee):
    """Class to create new Hourly Employee. It inherits from the base Employee class. HourlyEmployee(first:str, last:str, hours:float(default=40.0), rate:float(default=15))"""

    def __init__(self, first, last, hours=0, rate=Employee.MINIMUM_WAGE):
        """
        Creates a new Hourly Employee instance.
        HourlyEmployee(first:str(required), last:str(required), hours:float(default=40.0), rate:float(default=15))
        """
        super().__init__(first, last)
        self.hours_worked = hours
        self.hourly_rate = rate
        self.ot_pay = 0
        self.ot_hours_worked = 0

    def __str__(self):
        return f"""\nfirst: {self.first_name}\nlast: {self.last_name}\nhourly-rate: {self.hourly_rate:.2f}\nhours-worked: {self.hours_worked:.2f}\nregular-pay: ${self.current_gross_pay:.2f}
ot-pay: ${self.ot_pay:.2f}\nbonus-pay: ${self.current_bonus_pay:.2f}\nytd-earnings: ${self.ytd_gross_pay:.2f}\nytd-bonus-pay: ${self.ytd_bonus_pay:.2f}"""

    def __repr__(self):
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
        if self.hours_worked == 0:
            print(
                "Hours worked cannot be 0. Update work hours for this employee and try again."
            )
            return
        if self.hourly_rate < Employee.MINIMUM_WAGE:
            print(
                f"The 'Hourly Rate' cannot be less than the legal minimum-wage: {Employee.MINIMUM_WAGE}."
            )
            print("Update hourly rate for thihs employee, and try again.")
            return
        self.ot_pay = 0
        self.ot_hours_worked = self.hours_worked - Employee.DEFAULT_WORK_HOURS
        if self.ot_hours_worked > 0:
            self.ot_pay = self.ot_hours_worked * self.hourly_rate * 0.5
        self.current_gross_pay = self.hourly_rate * self.hours_worked + self.ot_pay
        self.ytd_gross_pay += self.current_gross_pay
        Employee.SALARY_EXPENSE += self.current_gross_pay

    def calculate_bonus_pay(self, bonus_rate):
        multiplyer = bonus_rate / 100
        self.current_bonus_pay = self.ytd_gross_pay * multiplyer
        self.ytd_bonus_pay += self.current_bonus_pay
        self.ytd_gross_pay += self.current_bonus_pay
        Employee.SALARY_EXPENSE += self.current_bonus_pay




hr_emp1 = HourlyEmployee("James", "Bond")
hr_emp1.hours_worked = 50.00
hr_emp1.hourly_rate = 93.87
for i in range(52):
    # weekly salary based on 45 hours
    hr_emp1.calculate_gross_pay()
    if i == 51:
        hr_emp1.calculate_bonus_pay(15)

print(hr_emp1)
