class BMI():
    def __init__(self):
        self.height = 0.0
        self.weight = 0.0
        self.BMI = 0.0


myBMI = [BMI() for x in range(40)]

for x in range(len(myBMI)):
    myBMI[x].height = float(input("Enter Height: "))
    myBMI[x].weight = float(input("Enter Weight: "))
    myBMI[x].BMI = myBMI[x].weight / myBMI[x]. height ** 2
    print("BMI = ", myBMI[x].BMI)
