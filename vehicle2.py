class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

    def show_details(self):
        print("Brand:", self.brand)
        print("Max Speed:", self.max_speed)


class Car(Vehicle):
    def __init__(self, brand, max_speed, model, seats):
        self.model = model
        self.seats = seats
        super().__init__(brand, max_speed)

    def show_details(self):
        print("Model:", self.model)
        print("Seats:", self.seats)
        return super().show_details()

    def fuel_type(self, fuel_type):
        print(self.model, "has", fuel_type)


Gadi = Car("Tech7", 300, "Audi", 7)

Gadi.show_details()
Gadi.fuel_type("Petrol")

print("Is Car a subclass of Vehicle?", issubclass(Car, Vehicle))