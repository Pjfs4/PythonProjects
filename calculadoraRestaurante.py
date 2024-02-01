import string

#num_char = len(input("what is you name?"))
#new_num_char = str(num_char)
#print("Your name has " + new_num_char + " characters.")

print("Welcome to the tip calculator")
bill = input("What was the total bill? €")
bill_float = float(bill)
tip = int(input("What percentage tip would you like to give? 10%, 12%, or 15%?"))
tip_float = float(tip)
people = int(input("How many people to split the bill?"))

total_bill = bill_float + bill_float*(tip_float/100)
each_person_payment = total_bill / people
each_person_payment = "{:.2f}".format(each_person_payment)

print(f"Each person should pay: €{each_person_payment}")