n=int(input("Enter Pattern size: "))

for i in range(n):
	for k in range(1,n-i):
		print(end=" ")
	for j in range(i+1):
		print("* ",end="")
	print()

