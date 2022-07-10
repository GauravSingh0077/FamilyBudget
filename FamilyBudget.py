n=int(input("Select 1 for Creating User, 2 for Selecting User, 3 for exiting program:"))
usercount=4
budgetcount=5
budgettobeshared=[]
c=0
listofuser=[[1,"Karan",[[1,4000,2300]],[]],[2,"Kiran",[[2,4800,2500]],[]],[3,"Ajay",[[3,4000,2300],[4,1000,200]],[]],[4,"Arjun",[[5,4000,2300]],[]]]
while(n!=3):
	if c==1:
		n=int(input("Select 1 for Creating User, 2 for Selecting User, 3 for exiting program:"))
		if n==1:
			n1=int(input("Number of Users to be created:"))
			while n1>0:	
				print("Name the user")
				user=input()
				usercount=usercount+1
				listofuser.append([usercount,user,[],[]])
				numberofbudgets=int(input("Enter the number of budgets to be added by the user"))
				for i in range(0,numberofbudgets):
					income=input("Enter the income:")
					expense=input("Enter the expense:")
					budgetcount=budgetcount+1
					listofuser[-1][2].append([budgetcount,income,expense])
				n1=n1-1				
		elif n==2:
			for k in listofuser:
				print(k[0],k[1])
			print("Select User by its index")
			n2=int(input())
			userinfo=listofuser[n2-1]
			print(userinfo)
			print("Select 1 for all budgets of user")
			print("Select 2 for all budgets shared to user")
			print("Select 3 for adding a budget to user")
			print("Select 4 for sharing a budget of user")
			n3=int(input())
			if n3==1:
				for k in userinfo[2]:
					print(k)
			elif n3==2:
				if userinfo[3]==[]:
					print("No budgets are shared to the User")
				for k in userinfo[3]:
					print(k)
			elif n3==3:
				numberofbudgets=int(input("Enter the number of budgets to be added by the user"))
				for i in range(0,numberofbudgets):
					income=input("Enter the income:")
					expense=input("Enter the expense:")
					budgetcount=budgetcount+1
					userinfo[2].append([budgetcount,income,expense])	
			elif n3==4:
				for k in userinfo[2]:
					print(k)
				n4=int(input("Select index of budget to be shared. It is first number in budget list."))
				for k in userinfo[2]:
					if k[0]==n4:
						budgettobeshared=k
				for k in listofuser:
					print(k[0],k[1])
				n4=int(input("Select index of User it is to be shared with"))
				print(budgettobeshared)
				listofuser[n4-1][3].append(budgettobeshared)
		c=1
	else:
		if n==1:
			n1=int(input("Number of Users to be created:"))
			while n1>0:	
				print("Name the user")
				user=input()
				usercount=usercount+1
				listofuser.append([usercount,user,[],[]])
				numberofbudgets=int(input("Enter the number of budgets to be added by the user"))
				for i in range(0,numberofbudgets):
					income=input("Enter the income:")
					expense=input("Enter the expense:")
					budgetcount=budgetcount+1
					listofuser[-1][2].append([budgetcount,income,expense])
				n1=n1-1				
		elif n==2:
			for k in listofuser:
				print(k[0],k[1])
			print("Select User by its index")
			n2=int(input())
			userinfo=listofuser[n2-1]
			print(userinfo)
			print("Select 1 for all budgets of user")
			print("Select 2 for all budgets shared to user")
			print("Select 3 for adding a budget to user")
			print("Select 4 for sharing a budget of user")
			n3=int(input())
			if n3==1:
				for k in userinfo[2]:
					print(k)
			elif n3==2:
				if userinfo[3]==[]:
					print("No budgets are shared to the User")
				for k in userinfo[3]:
					print(k)
			elif n3==3:
				numberofbudgets=int(input("Enter the number of budgets to be added by the user"))
				for i in range(0,numberofbudgets):
					income=input("Enter the income:")
					expense=input("Enter the expense:")
					budgetcount=budgetcount+1
					userinfo[2].append([budgetcount,income,expense])	

			elif n3==4:
				for k in userinfo[2]:
					print(k)
				n4=int(input("Select index of budget to be shared. It is first number in budget list."))
				for k in userinfo[2]:
					if k[0]==n4:
						budgettobeshared=k
				for k in listofuser:
					print(k[0],k[1])
				n4=int(input("Select index of user it is to be shared with"))
				print(budgettobeshared)
				listofuser[n4-1][3].append(budgettobeshared)
		c=1
