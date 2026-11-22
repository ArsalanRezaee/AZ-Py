num = int(input("Enter a number"))

if num == 0:
    print("The num is zero ")

elif num % 2 == 0:
    if num > 0:
        print("The number is positive and even")
    else:
        print("The number is negative and even")

else:
    if num > 0:
        print("The number is positive and odd")
    else:
        print("The number is negative and odd")

# تمرین دوم 
age = int(input("Enter your age: "))

if age <= 0:
    print("invalid age")
elif age < 5:
    print("your ticket is free")
elif age < 18:
    print("You should pay 50000 Toman")

elif age < 60:
    print("You should pay 100000 Toman")

else:
    print("You should pay 70000 Toman")


# تمرین سوم 
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("It is a leap year")

elif year % 100 == 0:
    print("It is a normal year")

elif year % 4 == 0:
    print("It is a leap year")

else:
    print("It is a normal year")

# تمرین چهارم 
salary = float(input("Enter your salary: "))

child = input("Do you have children? (y/n): ")

if salary <= 10000000:
    tax = 0

elif salary <= 25000000:
    tax = (salary - 10000000) * 0.10

else:
    tax = (15000000 * 0.10) + (salary - 25000000) * 0.20

if child == "y":
    tax = tax - 500000

if tax < 0:
    tax = 0

print("Your tax is:", tax)
print("Your salary after tax is:", salary - tax)


# تمرین پنجم 
score = float(input("Enter your score: "))

if score < 0 or score > 20:
    print("Invalid score")

elif score >= 17:
    print("Grade A")

elif score >= 15:
    print("Grade B")

elif score >= 10:
    print("Grade C")

else:
    print("Failed")


# تمرین ششم 
age = int(input("Enter your age: "))

license = input("Do you have a license? (y/n): ")

drunk = input("drunk? (y/n): ")

if age >= 18 and license == "y" and drunk == "n":
    print("You can drive")

else:
    print("You cant drive")


# تمرین هفتم 
amount = float(input("How much did you buy? "))

tier = input("Enter your tier (gold/silver/bronze): ").lower()

if amount < 10000000:

    if tier == "gold":
        discount = 15

    elif tier == "silver":
        discount = 10

    elif tier == "bronze":
        discount = 5

    else:
        discount = -1

else:

    if tier == "gold":
        discount = 20

    elif tier == "silver":
        discount = 15

    elif tier == "bronze":
        discount = 10

    else:
        discount = -1

if discount == -1:
    print("Invalid tier")

else:
    final_price = amount - (amount * discount / 100)

    print("Your discount is:", discount, "%")
    print("You should pay:", final_price)