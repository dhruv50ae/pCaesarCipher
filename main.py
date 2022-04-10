
import math


def printCalc(height, width, cover):
    area = height * width
    numOfCans = math.ceil(area/cover)
    print(f"You will need {numOfCans} cans of paint")


testH = int(input("Height of wall: "))
testW = int(input("Width of wall: "))
coverage = 5
printCalc(height=testH, width=testW, cover=coverage)
