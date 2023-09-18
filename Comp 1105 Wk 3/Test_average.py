#Average test scores

x = float(input("what is the score for the first test? "))
y = float(input("What is the second score? "))
z = float(input("What is the third score? "))


avg = format(((x+y+z)/3), ".2f")

print("The average score is ", str(avg))

if float(avg) >= 95:
	print("The average score is ", float(avg), " congratulations")
else:
	print("You might need to study more")

