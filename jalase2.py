# مجموع اعداد 
total = 0

for i in range(1, 11):
    total += i

print("Sum is:", total)


# تمرین فاکتوریل 
num = int(input("Enter a number: "))

fact = 1

while num > 0:
    fact *= num
    num -= 1

print("Factorial is:", fact)


# حلقه بریک 
for i in range(1, 51):

    if i == 42:
        break

    if i % 5 == 0:
        continue

    if i % 3 == 0:
        print(i)



# تشخیص عدد اول 
num = int(input("Enter a number: "))

if num <= 1:
    print("It is not a prime number")

else:
    for i in range(2, num):

        if num % i == 0:
            print("It is not a prime number")
            break

    else:
        print("It is a prime number")



#تمرین خودپرداز
balance = 1000000

while True:

    print("\n1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
        print("Your balance is:", balance)

    elif choice == 2:

        amount = int(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Deposit successful!")

        else:
            print("Invalid amount!")

    elif choice == 3:

        amount = int(input("Enter withdraw amount: "))

        if amount <= 0:
            print("Invalid amount")

        elif amount > balance:
            print("Not enough balance")

        else:
            balance -= amount
            print("Withdraw successful")

    elif choice == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid option")