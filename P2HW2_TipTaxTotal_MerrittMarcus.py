#CTI - 110
#P2HW1-Tip Tax Total
#Marcus Merritt
#4/24/2018

foodcost = float(input("Please enter the food cost:"))

tipamount = 0.18 * foodcost

salestax = 0.07 * foodcost

totalcost = foodcost + tipamount + salestax

print("Food Charge: $" + format(FoodCost, ",.2f"))"Tip: $+ \

print("Tip Amount: $" + format(TipAmount, ",.2f"))

print("Sales Tax: $" + format(SalesTax, ",.2f"))

print("Total Cost: $" + format(TotalCost, ",.2f"))
