# one.py

def func():
	print("func() in one.py")

def myfunc():
	pass

def func2():
	pass

def func3():
	pass


print("Top level in one.py")

# In larger .py scripts, you'll see below without the else statement, where 
# top level functions are being called
if __name__ == '__main__':
	print("one.py is being run directly")
	func()
	myfunc()
	func2()
	func3()
	# ....

else:
	print("one.py is being imported")