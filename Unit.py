print("=== Unit Converter ===")
print("1. Length")
print("2. Capacity")
print("3. Temperature")

choice = input("Choose 1, 2 or 3: ")

# ---------- LENGTH ----------
if choice == "1":
    print("Units: m, Km, cm, mm")
    from_unit = input("Convert FROM: ")
    to_unit = input("Convert TO: ")

    if from_unit not in ["m", "Km", "cm", "mm"]:
        print("Wrong FROM unit! Please type m, Km, cm or mm")
    elif to_unit not in ["m", "Km", "cm", "mm"]:
        print("Wrong TO unit! Please type m, Km, cm or mm")
    else:
        value = float(input("Enter the number: "))

        if from_unit == "m":
            meter = value
        elif from_unit == "Km":
            meter = value * 1000
        elif from_unit == "mm":
            meter = value / 1000
        elif from_unit == "cm":
            meter = value / 100

        if to_unit == "m":
            answer = meter
        elif to_unit == "Km":
            answer = meter / 1000
        elif to_unit == "mm":
            answer = meter * 1000
        elif to_unit == "cm":
            answer = meter * 100

        print(value, from_unit, "=", answer, to_unit)

# ---------- CAPACITY ----------
elif choice == "2":
    print("Units: l, ml")
    from_unit = input("Convert FROM: ")
    to_unit = input("Convert TO: ")

    if from_unit not in ["l", "ml"]:
        print("Wrong FROM unit! Please type l or ml")
    elif to_unit not in ["l", "ml"]:
        print("Wrong TO unit! Please type l or ml")
    else:
        value = float(input("Enter the number: "))

        if from_unit == "l":
            liters = value
        elif from_unit == "ml":
            liters = value / 1000

        if to_unit == "l":
            answer = liters
        elif to_unit == "ml":
            answer = liters * 1000

        print(value, from_unit, "=", answer, to_unit)

# ---------- TEMPERATURE ----------
elif choice == "3":
    print("Units: C, F, K")
    from_unit = input("Convert FROM: ")
    to_unit = input("Convert TO: ")

    if from_unit not in ["C", "F", "K"]:
        print("Wrong FROM unit! Please type C, F or K")
    elif to_unit not in ["C", "F", "K"]:
        print("Wrong TO unit! Please type C, F or K")
    else:
        value = float(input("Enter the number: "))

        if from_unit == "C":
            celsius = value
        elif from_unit == "F":
            celsius = (value - 32) * 5 / 9
        elif from_unit == "K":
            celsius = value - 273.15

        if to_unit == "C":
            answer = celsius
        elif to_unit == "F":
            answer = celsius * 9 / 5 + 32
        elif to_unit == "K":
            answer = celsius + 273.15

        print(value, from_unit, "=", answer, to_unit)

else:
    print("Please choose 1, 2 or 3")