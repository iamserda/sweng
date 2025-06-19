class Vehicle:
    def __init__(self):
        pass
    
    def start_engine(self):
        return "engine has started!"
    
    def stop_engine(self):
        return "engine stopped!"

class Car(Vehicle):
    def start_engine(self):
        print(f"Car {Vehicle.start_engine(self)}!")
    def stop_engine(self):
        print(f"Car {Vehicle.stop_engine(self)}")

car1 = Car()
car1.start_engine()
car1.stop_engine()