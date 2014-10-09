# /usr/bin/python

'''
Bitwise Operation performance
'''

def CountNumberOf1Bit(number):
	''' Count number of one bit in input number'''
	count = 0
	while(number):
		count+=1
		number = number & (number-1)
	return count

def CheckNumberIsEvenOrOdd(number):
	''' Check Number is Even or Odd'''
	if(number & 0x01):
		print(str(number)+" is odd number")
	else:
		print(str(number)+" is Even number")

def toggleRightMost1Bit(number):
	''' Toggle Right Most one bit to 0 '''
	if(number == 0):
		print("Number dont have any one bit")
		return 0
	number1 = number
	count = 0
	while(number):
		if(number&0x01):
			number = 0
		else:
			count+=1
			number=number>>1
	number1=number1^(1<<(count))
	print("Number after toggle is :"+str(number1))

def toggleRightBitByPosition(number, position):
	''' Toggle Right 1 bit of position given'''
	number = number^(1<<(position-1))
	print("Number after toggle by position "+str(position)+" is : "+str(number))


'''
# start of program without main
number = eval(raw_input("Enter any number : "))

print("Number of 1 bit in "+str(number)+" is: "+str(CountNumberOf1Bit(number)))

CheckNumberIsEvenOrOdd(number)

toggleRightMost1Bit(number)

number, position = input("Enter any number and position : ")
toggleRightBitByPosition(number,position)
'''
