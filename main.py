print("Welcome to the tip calculator")
bill = float(input("What was the total bill? £"))
tip = int(input("What percentage of a tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people are splitting the bill? "))

bill_with_tip = tip / 100 * bill + bill
final_bill = "{:.2f}".format(bill_with_tip)
bill_per_person = bill_with_tip / people
final_amount = "{:.2f}".format(bill_per_person)
print(f"The toal amount to pay is {final_bill}")
print(f"Each person should pay {final_amount}")
print("Thank you for using Tip Calculator, see you again soon!")
