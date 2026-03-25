actual_cost = float(input("Enter actual amount of Product: "))
Sales_cost = float(input("Enter Sales amount: "))

if (Sales_cost>actual_cost):
    amount = Sales_cost - actual_cost
    print("Total Profit = {0}".format(amount))
else:
    print("No PROFIT!!")



