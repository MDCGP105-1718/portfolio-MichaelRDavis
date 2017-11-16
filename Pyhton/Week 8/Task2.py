enum class color:
    Red,
    Blue,
    Black,
    White,

class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def printInfo(self):
        print(f"The car name is: {self.name}.\n")
        print(f"The color is: {self.color}.\n")

carName = str(input("What is your car name.\n"))
carColor = str(input("What is the color of your car.\n"))
carInstance = Car(carName, carColor)
carInstance.printInfo()
