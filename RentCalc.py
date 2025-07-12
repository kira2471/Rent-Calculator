# inputs we need from user
#Total rent
#Total Food ordered for snacking
#Electricity units spend
#Charge per unit
#Number of person living in the room

#Output
#Total Amount you have to pay is 

rent = int(input("Enter yout Rent :"))
Food = int(input("Enter your Food total :"))
Electricity= int(input("Enter your electricity spend :"))
charge_per_unit = int(input("Enter yout charge per unit :"))
person = int (input("Enter the number of person in room/flat :"))

Total_bill = Electricity * charge_per_unit

output = Total_bill + rent + Food/person
print("Each person will pay :", output)

