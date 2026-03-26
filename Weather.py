print("Select one of the condition given below as per your area and write YES in front of it, if it is not write NO and proceed- ")

Rainy = input("Rainy: ")
Cloudy = input("Cloudy: ")
Sunny = input("Sunny: ")
Stormy = input("Stormy: ")
Windy = input("Windy: ")
Partly_cloudy = input("Partly Cloudy: ")

Rainy = Rainy.lower()
Cloudy = Cloudy.lower()
Sunny = Sunny.lower()
Stormy = Stormy.lower()
Windy = Windy.lower()
Partly_cloudy = Partly_cloudy.lower()

if Rainy == "yes":
    print("Wear a raincoat and carry an umbrella ")

elif Sunny == "yes":
    print("Wear light cotton clothes, sunglasses and a cap ")

elif Cloudy == "yes":
    print("Wear comfortable clothes, maybe carry a light jacket")

elif Stormy == "yes":
    print("Stay indoors, If going out, wear strong protective clothes")

elif Windy == "yes":
    print("Wear a jacket to protect from wind")

elif Partly_cloudy == "yes":
    print("Wear normal clothes, light layers are good")

else:
    print("No weather selected")