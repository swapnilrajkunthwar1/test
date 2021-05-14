row=int(input("Enter row size: "))
k=row
for i in range(0,row):
	for sp in range(1,k-i):
		print(end=" ")
	for j in range(i+1):
		print("* ",end="")
	print()
k=row-1
for i in range(row-1,0,-1):
	for sp in range(k,row):
		print(end=" ")
	k-=1
	for j in range(0,i):
		print("* ",end="")
	print()