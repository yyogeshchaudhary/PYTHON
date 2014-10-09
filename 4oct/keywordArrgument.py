# /usr/bin/python
'''

Keyword Arrgument:
	def functionName(var1, var2, var3)

	we can call it as follows:
		functionName(var2=10, var1='String', var3= 40)

	we have to use the same keyword as defined in functionName while defining
'''

def keywordArrgument(var1, var2, var3):
	print("Var1 : "+str(var1))
	print("Var2 : "+str(var2))
	print("Var3 : "+str(var3))


keywordArrgument(var2=10, var3=56, var1=5)
