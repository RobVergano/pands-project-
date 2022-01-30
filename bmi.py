#bmi.py
#program to calculate bmi
#Author: Roberto Vergano

print ("Welcome to BMI Calculator!")
weight = int(input("Enter your weight(Kg): "))
height = int(input("Enter your height (cm): "))
heightm = height/100
BMI = weight/(heightm)**2
print (BMI)