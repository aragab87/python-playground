#1. reads name.txt into a variable my_name
with open("name.txt") as f:
	my_name=f.read()

#2. writes a new file named hello.txt
with open("hello.txt", "w") as f:
	f.write("Hello, my name is " + my_name)