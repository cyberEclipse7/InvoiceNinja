# "shop_details" function – Returns all required info for menu() function
def shop_details():
    return product_1, price_1, product_2, price_2, product_3, price_3

# "menu" function - Displays the menu
def menu(product_1, price_1, product_2, price_2, product_3, price_3):
    print("==========================================================")
    print("Please select what you want to buy from the following menu:")
    print(f"1. {product_1} (each ${price_1:.2f})")
    print(f"2. {product_2} (each ${price_2:.2f})")
    print(f"3. {product_3} (each ${price_3:.2f})")
    print("4. Done!")
    print("==========================================================")

# "valid_input" function - Validates User Entry for choices [1-4]
def valid_input(product_1, price_1, product_2, price_2, product_3, price_3):

        sum = 0
        numberOfProducts = 0
        x = False
        while x == False:
            try:
                print("Please select what you want to buy from the following menu:")
                print(f"1. {product_1} (each ${price_1})")
                print(f"2. {product_2} (each ${price_2})")
                print(f"3. {product_3} (each ${price_3})")
                print("4. Done!")
                print("==========================================================")

                choice = int(input())
                if choice == 1:
                    numberOfProducts = int(input(f"How many {product_1:s} do you want? "))
                    sum += (numberOfProducts * price_1)
                    print(f"Current Total: ${sum:.2f}")
                    print("==========================================================")
                elif choice == 2:
                    numberOfProducts = int(input(f"How many {product_2:s} do you want? "))
                    sum += (numberOfProducts * price_2)
                    print(f"Current Total: ${sum:.2f}")
                    print("==========================================================")
                elif choice == 3:
                    numberOfProducts = int(input(f"How many {product_3:s} do you want? "))
                    sum += (numberOfProducts * price_3)
                    print(f"Current Total: ${sum:.2f}")
                    print("==========================================================")
                elif choice == 4:
                    continueOrNot = input("Do you want to continue and see the invoice (i) or cancel the transaction (c)? \n")
                    if continueOrNot == 'i':
                        show_invoice(sum)
                        pay_method()
                        x = True
                    elif continueOrNot == 'c':
                        print("Thank you for trying!")
                        x = True
                else:
                    print(f"Sorry, {choice} is not a valid choice! Please select from the menu.")
                    print("==========================================================")
                    continue

            except ValueError:
                print("Oops! That is not a valid value. Try again...")

# "show_invoice" function - Displays the invoice
def show_invoice(sum):
    print("\nYour invoice is here!")

    print("\n=====================")
    print(f"Subtotal:     ${sum:4.2f}")
    tax = (0.13 * sum)
    print(f"Tax:          ${tax:>4.2f}")
    print("----------------------")
    total = sum + tax
    print(f"\nTotal:        ${total:>4.2f}")
    print("=====================")

# "pay_method" function - Displays the sample 4-digit number 2345 as ‘xx45’
def pay_method():
    print("How would you like to pay? Select one from the following menu.")
    print("(a) Cash")
    print("(b) Prepaid Card")

    paymentType = input()
    if(paymentType == 'a'):
        print("Thank you for your payment. Have a nice day!")
    elif paymentType == 'b':
        creditCardNumber = int(input("Enter 4 digit card number: "))

        temp = creditCardNumber
        lastNumber = temp % 10
        temp /= 10
        secondLastNumber = int(temp) % 10

        print(f"\nYou have paid by xx{secondLastNumber:d}{lastNumber:d}. Have a nice day!")


# Main Program
fullName = input("What is your name: ")
companyName = input("What is your company name? ")

print(f"\nHi {fullName:s}! We can set up your '{companyName:s}' sales menu. ")
print("Please enter 3 products and the prices you would like to sell.")

print(f"\nEnter Product 1 and its price:")
product_1 = input()
price_1 = float(input())

print(f"\nEnter Product 2 and its price:")
product_2 = input()
price_2 = float(input())

print(f"\nEnter Product 3 and its price:")
product_3 = input()
price_3 = float(input())

shop_details()
menu(product_1, price_1,product_2, price_2,product_3, price_3)
valid_input(product_1, price_1, product_2, price_2, product_3, price_3)
