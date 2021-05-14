no=int(input("enter rows"))
for i in range(no):
	for j in range(i+1):
		print(chr(65+j),end=" ")
	print()
