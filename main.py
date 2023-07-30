# BMI calculator code starts
print("Welcome to BMI calculator..")
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = int(weight)/float(height)**2
bmi_as_int=int(bmi)
print(f"BMI is:{bmi_as_int}")

# BMI calculator code ends


# age calculator code starts
print("Welcome to age calculator..")
age = input("What is your current age? ")
new_age = 90 - int(age)
days = new_age * 365
weeks = new_age * 52
months = new_age * 12
print(f"You have {days} days, {weeks} weeks, and {months} months left.")

# tipcalculator code starts
print("Welcome to tip calculator..")
print("welcome to the tip calculator..")

bill=input("what was the total bill(BDT)?")

tip=input("What persentage of tip you want to give? 10,12 or 15?")

people=input("How many peple to split the bill?")

calculate = (int(bill)+(int(bill)*(int(tip)/100)))/int(people)

final_amount= round(calculate,2)

print(f"Each person should pay: {final_amount}")

#tipcalculator code ends 


