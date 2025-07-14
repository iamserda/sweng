class Employee:
    DEFAULT_WORK_HOURS = 40
    MINIMUM_WAGE = 15
    SALARY_EXPENSE = 0

    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        self.current_gross_pay = 0
        self.current_bonus_pay = 0
        self.ytd_gross_pay = 0
        self.ytd_bonus_pay = 0

    def reset_year(self):
        self.current_gross_pay = 0
        self.current_bonus_pay = 0
        self.ytd_gross_pay = 0
        self.ytd_bonus_pay = 0

    def calculate_gross_pay(self):
        pass

    def calculate_bonus_pay(self):
        pass
