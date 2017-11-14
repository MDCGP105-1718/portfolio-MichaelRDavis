#Name
Name = "/0"
while True:
    Name = input("Enter your name: \n")
    if not Name.isalpha():
        print("You must insert alphabetical characters.\n")
        continue
    else:
        print("Hello", Name)
        break

#Age
Age = 0
while True:
    try:
        Age = int(input("Enter your age: \n"))
        print("You are", Age, "year's old.\n")
        if(Age <= 0):
            print("You can't be that old.\n")
        break
    except ValueError:
        print("You must insert numerical characters.\n")
        continue

#Height
Height = 0
while True:
    try:
        Height = float(input("Enter your height in centimeters: \n"))
        print("You are", Height, "centimeters tall.\n")
        if(Height > 215):
            print("WOW! You're tall!")
        break
    except ValueError:
        print("You must insert numerical characters.\n")
        continue

#Weight
Weight = 0
while True:
    try:
        Weight = float(input("Enter your weight in kilograms: \n"))
        print("Your weight is", Weight, "kilograms")
        if(Weight > 150):
            print("I think you need to go on a diet!")
        break
    except ValueError:
        print("You must insert numerical characters.\n")

#Eye color
EyeColor = "/0"
while True:
    EyeColor = input("Enter your eye color: \n")
    if not EyeColor.isalpha():
        print("You must insert alphabetical characters.\n")
        continue
    else:
        print("Your eyes are", EyeColor)
        break

#Hair color
HairColor = "/0"
while True:
    HairColor = input("Enter your hair color: \n")
    if not HairColor.isalpha():
        print("You must insert alphabetical characters.\n")
        continue
    else:
        print("Your hair is", HairColor)
        break
