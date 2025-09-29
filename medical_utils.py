def get_bmi_category(weight_kg, height_m):

    try:
        n = weight_kg/height_m**2
        if 18.5 <= n <= 25:
            print("Healthy range")
        elif n < 18.5:
            print("Underweight")
        elif 25 < n < 30:
            print("Overweight")
        elif n > 30:
            print("Obesity")
    except Exception:
        print("Enter valid numbers")


def calculate_bmi(weight_kg, height_m):
        if weight_kg <= 0:
            print("You might wanna put on some weight")
            return
        if height_m <= 0:
            print("You might need to come back next year when you grow up a little")
            return

        return get_bmi_category(weight_kg, height_m);

