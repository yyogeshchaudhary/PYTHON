# /usr/bin/python

'''
WAP to Add, Substract, Multiply and Divide two number 
'''

def add(number1, number2):
	return number1+number2

def sub(number1, number2):
	return number1-number2

def mul(number1, number2):
	return number1*number2

def div(number1, number2):
	return number1/number2


number1, number2 = eval(raw_input("Please Enter Two number : "))

print("Addition of "+str(number1)+" and "+str(number2)+" is : "+str(add(number1,number2)))
print("Substraction of "+str(number1)+" and "+str(number2)+" is : "+str(sub(number1,number2)))
print("Multiplication of "+str(number1)+" and "+str(number2)+" is : "+str(mul(number1,number2)))
print("Division of "+str(number1)+" and "+str(number2)+" is : "+str(div(number1,number2)))
