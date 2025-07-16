import random
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
        self.__hours_worked: float = hours
        self.hourly_rate: float = rate
        self.ot_hourly_rate: float = self.hourly_rate * 1.5
        self.ot_hours_worked: float = 0
        self.regular_pay: float = 0
        self.ytd_regular_pay: float = 0
        self.ot_pay: float = 0
        self.ytd_ot_pay: float = 0

    def __str__(self) -> str:
        return (
            f"\nEmployee: Personal Info:"
            f"\n- First: {self.first_name}"
            f"\n- Last: {self.last_name}"
            f"\n\nRegular Pay Info:"
            f"\n- Hourly-Rate: {self.hourly_rate:.2f}"
            f"\n- Hours Worked: {self.hours_worked:.2f}"
            f"\n- Regular Pay: ${self.regular_pay:.2f}"
            f"\n\nOvertime and Bonus Pay Info(if applicable):"
            f"\n- OT Pay: ${self.ot_pay:.2f}"
            f"\n- Bonus Pay: ${self.current_bonus_pay:.2f}"
            f"\n\nYear-To-Date:"
            f"\n- YTD-Regular-Pay: ${self.ytd_regular_pay:.2f}"
            f"\n- YTD-Bonus-Pay: ${self.ytd_bonus_pay:.2f}"
            f"\n- YTD-OT-Pay: ${self.ytd_ot_pay:.2f}"
            f"\n- YTD-Earnings: ${self.ytd_gross_pay:.2f}\n"
        )

    def __repr__(self) -> str:
        return (
            f"HourlyEmployee(first={repr(self.first_name)}, "
            f"last={repr(self.last_name)}, "
            f"hours={repr(self.hours_worked)}, "
            f"rate={repr(self.hourly_rate)})"
        )

    @property
    def hours_worked(self):
        return self.__hours_worked

    @hours_worked.setter
    def hours_worked(self, hours=0):
        if hours < 0:
            print(
                "WARNING: Hours cannot be less than 0. Hours worked will be set to 0."
            )
            return
        if hours > 80:
            print("WARNING: Hours worked cannot be more than 80 in a single week.")
            return
        self.__hours_worked = hours
        log_message = f"Updated this week's hours worked to {hours} for employee: {self.first_name}, {self.last_name}"
        print(log_message)  # fake-log

    def update_hourly_rate(self, new_hourly_rate: float) -> None:
        if new_hourly_rate >= Employee.MINIMUM_WAGE:
            self.hourly_rate = new_hourly_rate
        else:
            print(
                f"The 'Hourly Rate' must be equal or more than the minimum wage({Employee.MINIMUM_WAGE})."
            )
        return

    def calculate_gross_pay(self) -> None:
        if self.hours_worked <= 0:
            warning_message = f"WARNING: Hours worked CANNOT be less or equal to 0. Hours worked is {self.hours_worked}."
            raise ValueError(f"{warning_message}")
        if self.hourly_rate < Employee.MINIMUM_WAGE:
            print(
                "WARNING: The 'Hourly Rate' is LESS THAN be less than the legal minimum-wage"
                f"CURRENTLY, THE LEGAL MINIMUM WAGE IS {Employee.MINIMUM_WAGE}."
            )
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

    for i in range(1, 53, 1):
        # weekly salary based on 45 hours
        hr_emp1.hourly_rate = 46.83
        hr_emp1.hours_worked = random.randrange(40, 80, 1)
        hr_emp1.calculate_gross_pay()
        if i % 13 == 0:
            hr_emp1.calculate_bonus_pay(15 / 4)
        print(f"""\nCHECK #{"100"+str(i) if i < 10 else "10"+str(i)}\n{hr_emp1}""")
