import math

#What is the price of a child's meal? 
#What is the price of an adult's meal?
#How many children are there? 
#How many adults are there? 
#What is the sales tax rate? 
#assume % sales tax


child_meal = float (input("What is the price of a child's meal ?"))
child_drink = float (input("What is the price of a child's drink ?"))
child_number = int(input("How many children are there ? "))
adult_meal = float (input("What is the price of an adult's meal ?"))
adult_drink = float (input("What is the price of a adult drink ?"))
adult_number = int (input("How many adults are there ? "))
tax = float (input("What is the sales tax rate ?"))

print('-' * 40)

Subtotal =(child_drink + child_meal)*(child_number) + (adult_drink + adult_meal) * (adult_number)        #Subtotal I managed to reduce the number of variables comparable to the last week
print("Subtotal is: $",Subtotal)
Sales_Tax = (Subtotal * tax / 100)
print("Sales Tax is: $",Sales_Tax)
total = (Subtotal + Sales_Tax)
print("Total is: $",total) 


print('-' * 40)
payment  = float (input("What is the payment amount?"))
change = (payment - total )
print('-' * 40)
 
if change > 0:      
   print (f"Your change is: $ {change:.2f}")   # I managed to learn how to round to two decimals.
if change > 0: 
   print ("Thank you we hope you enjoyed!")
if change < 0 :   
    print (f"You owe us: $ {(change * -1):.2f}")    ## Now I managed to convert to positive by multiplying by -1
if change < 0 :
     (print ("Do you have another form of payment?")) 
print('-' * 40)

#I learned how to make multiple options

print("""We also accept:  
[1] Credit card
[2] Debit card""")
user = int(input("Which of these ways would you like to use?"))

print('-' * 40)
#
if user == 1:
   print (f"You owe us: $ {(change * -1):.2f}")
   sec_payment  = float (input("What is the Credit card payment amount?"))
   sec_change = (sec_payment + change )
   print (f"Your change is: $ {(sec_change * -1):.2f}")
   print("Thamks")
        ### I know there would be no change in card payment, but I wanted to prove myself even more and I got the result.
if user == 2:
   print (f"You owe us: $ {(change * -1):.2f}")
   sec_payment  = float (input("What is the Debit card payment amount?"))
   sec_change = (sec_payment + change )
   print (f"Your change is: $ {(sec_change * -1):.2f}")
   print("Thanks")

#
print('-' * 40)







##Ask the user for the price of a child and an adult meal and store these values properly into variables as floating point numbers.
##Ask the user for the number of adults and children and store these values properly into variables as integers.
##Ask the user for the sales tax rate and store the value properly as a floating point number.
##Compute and display the subtotal (don't worry about rounding to two decimals at this point).
##Compute and display the sales tax.
##Compute and display the total.
##Ask the user for the payment amount and store the value properly as a floating point number.
##Compute and display the change.
##Include a dollar sign ($) before each displayed value.
##Display each value to two decimals.
##Double check that the calculations are correct.
##Show creativity and exceed the core requirements by adding additional features.
##Use good style in your program, including variable names and whitespace.