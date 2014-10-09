# /usr/bin/python


''' 
Variable Number of Arrgument :
	def foo(var1, var2, *args)

	*args is variable number of arrgument in which you can feed any number of values as python in type free with variable type
	**args is Dictionary so we have to pass values along with there keys

variable arrgument dictionary

'''


def variableNumOfArgs(var1, var2, *args):
	print(type(args))
	print("Address of Args : "+str(id(args)))
	print(var1)
	print(var2)
	for x in args :
		if type(x) is int:
			print("Integer : "+str(x))
		if type(x) is str:
			print("String  : "+x)

def varNumOfArgs(var1, var2, *args, **argsw):
	for x in args:
		print("args : "+str(x))

	for data in argsw:
		print(data, argsw[data])



variableNumOfArgs(10,20,30,40,50,'name','yogi')
varNumOfArgs(10,20,30,40,50, name='yogi', surname='chaudhary')

