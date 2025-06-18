class Employee:
    def __init__(self):
        self.__dict__["name"] = "Julian Alvarez"
        self.__dict__["age"] = 22
        self.__dict__["position"] = "soccer player"
        self.__dict__["salary"] = 250000
        self.__dict__["club"] = "Athletico Madrid"
        self.__dict__["country"] = "Argentina"


emp1 = Employee()
print(
    f"{emp1.name} is a {emp1.age}-year old {emp1.position} from {emp1.country} . He earns {emp1.salary} and currently plays for {emp1.club}."
)
