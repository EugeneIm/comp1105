#Average test scores

x = float(input("what is the score for the first test? "))
y = float(input("What is the second score? "))
z = float(input("What is the third score? "))


avg = ((x+y+z)/3)

print("The average score is ", avg)

if avg >= 95:
	print("The average score is ", avg, " congratulations")
else:
	print("You might need to study more")