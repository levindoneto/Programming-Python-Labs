cont = "y" # continue until the user press <n> or <N>

while (cont!="n" and cont!="N" or cont=="y" or cont=="Y"):
	a = input ("Enter number 1\n")
	b = input ("Enter number 2\n")
	op = input ("Enter the operation\n")
	if (op=="*" or op=="mult" or op=="multiplication"):
		result = int(a)*int(b)
		print ("Result: ", result)
	elif (op=="+" or op=="add" or op=="addition"):
		result = int(a)+int(b)
		print ("Result: ", result)
	else:
		print("Invalid operator!")
		
	cont = input ("Do you want to continue (Y/N):\n")
	if (cont!="y" and cont!="Y" and cont!="n" and cont!="N"):
		print("Invalid answer!")