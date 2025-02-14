#Assignment:
#Number 1:
age=int(input("enter your age: "))
if age<=10:
	print("the ticket is 5$")
elif age>10 and age<=20:
	print("the ticket is 10$")
elif age>20 and age<=30:
	print("the ticket is 15$")
else:
	print("the ticket is 20$")