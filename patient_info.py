name = input("Enter patient's name: ")



def isValidNumber(value):
    try:
        float(value);
        return True;
    except ValueError:
        return False

while True:
    age = input("Age: ")
    isValidAge = isValidNumber(age);
    if isValidAge:
        break;
    else:
        print('Enter a valid number for age');


temperature = input("Temperature: ")


isValid = isValidNumber(temperature)
if isValid:
    if float(temperature) > 37.5:
        print(name, "is having a fever:", temperature)
    else:
        print(name, "has normal temperature:", temperature)
else:
    print("Enter a valid number")
