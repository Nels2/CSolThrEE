# import matplotlib.pyplot as plt - look at later. Un(#) later.
# TheFarSide
# Solves accounting equations for you!

AccountingTwo = True
while AccountingTwo:
  print("====================Welcome!=====================")
  print("|-This program has three functions              |")
  print("|-It was made to simplify Accounting.           |")
  print("|-It solves three equations.                    |")
  print("|-All you have to do is input the numbers!      |")
  print("|                                               |")
  print("|                                               |")
  print("|_______________Choose One Below________________|")
  print("|                                               |")
  print("|1. Variable Costs and Revenue  (1)(1a)         |")
  print("|2. Mixed Costs and Revenue                     |")
  print("|3. High/Low Method                             |")
  print("|                                               |")
  print("|===============================================|")
  option = input("> please pick a function: ")
  if option == '1':
    print("=== Variable Costs Solver (1) =================")
    x = float(input("Enter Activity (Sales) : "))
    y = float(input("Enter Total Fixed Cost (Salaries) : "))
    print("Fixed Cost Per Activiy: " + str(float(y / x) * 100) + "%")#just divides y(Salaries) by x(Sales)
    #plt.plot(x, y) --look at later
    #plt.show()
  if option == '1a':
    print("=== Variable Revenue Solver (1a) ==============")
    z = float(input("Enter Activity Levels (Training Hours) : "))
    v = float(input("Enter Total Variable Revenue (Service Fees) : $"))
    print("Variable Revenue per Activity : $" + str(float(v / z)))#divides Training Hours by Service Fees
  if option == '2':
    ##################### continue here downwards. need to add option 2-3 then its done/ clean up code##################
    print()
  contin = input("> New Function? ")
  if contin != 'yes':
    break
print("OK. Exiting...")