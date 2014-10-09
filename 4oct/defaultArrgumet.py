# /usr/bin/python
'''
Default Arrgument:
	def functionName(var1, var2, var3=10)

	var3=10 : is called as default arrgument and we can call function with 2 or 3 parameters 
	if we call the function with 3 parameter then it will override the value of var3 with given value
	every default parameter should be trailing param not at middle of function param
'''


def defaultArrgument(strVar, x, y=10):
	print("String is  : "+strVar)
	print("X value is : "+str(x))
	print("Y value is : "+str(y))


defaultArrgument('Hello',10)

defaultArrgument('Yogesh', 20,30)
