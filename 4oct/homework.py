# /usr/bin/python

'''
WAP which will find all such number which are divisible by seven and are not multiple of 5 between 1000 to 2500
WAP to find the factorial of given number
'''
import math

def findNumDivisibleBy7NotMultipleOf5BetweenRange(start,end):
	number =''
	for i in range(start,end):
		if(i%7== 0 and i%5 != 0):
			print(i)


def factorialOfNumber(number):
	if number < 0:
		return 'cant find factorial of negative number'
	if number == 0 or number == 1:
		return 1
	res = 1
	for i in range(2,number+1):
		res = res * i
	print(res)


def Factorial(number):
	if number < 0:
		return 'cant find factorial of negative number'
	if number == 0 or number == 1:
		return 1
	return number * Factorial(number-1)

def FactorialUsingMath(number):
	if number < 0:
		return 'cant find factorial of negative number'
	if number == 0 or number == 1:
		return 1
	return math.factorial(number)

if __name__=='__main__':
	a,b = eval(raw_input("Enter two Number : "))
	findNumDivisibleBy7NotMultipleOf5BetweenRange(a,b)
	c = eval(raw_input("Enter Number to Find Factorial Using range :"))
	factorialOfNumber(c)
	d = eval(raw_input("Enter Number to Find Factorial Using Recursive :"))
	print(Factorial(d))
	d = eval(raw_input("Enter Number to Find Factorial Using Math:"))
	print(FactorialUsingMath(d))
	
	


