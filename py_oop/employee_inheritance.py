class Employee:
    def __init__(self, fname: str, lname: str, weekly_pay: float = 300.0):
        self.fname = fname
        self.lname = lname
        self.__weekly_pay = 0
        self.__annual_pay = None
        self.weekly_pay = weekly_pay

    def __str__(self):
        return (
            f"\nEmployee:\n"
            f"Firstname: {self.fname}\n"
            f"Lastname: {self.lname}\n"
            f"Weekly Pay: ${self.weekly_pay:.2f}\n"
            f"Annual Pay: ${self.annual_pay:.2f}\n"
        )

    @property
    def weekly_pay(self):
        return self.__weekly_pay

    @weekly_pay.setter
    def weekly_pay(self, weekly_pay):
        if weekly_pay < (7.25):
            print(
                "WARNING: You cannot set an employee's earnings to be less than legal minimum wage."
            )
        else:
            self.__weekly_pay = weekly_pay
            self.__annual_pay = None

    @property
    def annual_pay(self):
        if self.__annual_pay is None:
            self.__annual_pay = self.weekly_pay * 52
        return self.__annual_pay

def run_this(fname="james", lname="bond", company="MI6", hourly_pay=7.25):
    print(f"Company: {company}", sep=None, end=" ")
    weekly_pay = hourly_pay * 40
    employee = Employee(fname, lname, weekly_pay)
    print(employee)

for hourly_pay, company in [
    (5.50, "McDowells"),
    (10.5, "GeekBrags"),
    (21.64, "BigRed Teleco"),
    (31.64, "Ball n' Dine"),
    (48, "GeekFads"),
    (51.64, "The Lloyd's Banks"),
    (66.45, "Purple Consulting Group"),
]:
    run_this("michael", "jackson", company, hourly_pay)