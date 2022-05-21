"""BMI Calculator

A person from USA wants to know his Body Mass Index (BMI). He knows his weight in pounds and height in inches. The
evaluator knows the formula for calculating BMI using the formula,

BMI = (weight in kilograms) / (height in m * height in m)

Help the person in finding his BMI by writing a program for him.    (Use the conversion formulae: 1 pound =0.4536
kilograms, 1 inch = 2.54 cms """

weigh_in_pounds = float(input("Enter Weight of person in pounds: "))
height_in_inches = float(input("Enter Height of the person in inches: "))
weight_in_kg = weigh_in_pounds/2.205
height_in_m = height_in_inches/39.37
BMI = weight_in_kg/height_in_m**2
print(f"BMI of the person calculated using the formula,(weight in kilograms)/(height in m * height in m): {'%.2f'%BMI}")
