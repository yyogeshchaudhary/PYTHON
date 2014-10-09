# /usr/bin/python

'''
WAP to implement stack

IsEmpty()	check stack is empty or not
IsFull()	check weather the stack is full or not
Push()   	push the item to stack
Pop()		Pop the item from stack
peep()   	check the upper most item

'''

def IsEmpty(l1):
	if l1.__len__() is 0:
		return True
	else:
		return False
	
def Push(l1, element):
	l1.append(element)
	return l1

def Pop(l1):
	if(IsEmpty(l1)):
		print("Stack is Empty")
		return 0
	return l1.pop(l1.__len__()-1)

def Peep(l1):
	return l1[l1.__len__()-1]

def IsFull(l1, lenght):
	if l1.__len__() == lenght:
		return True
	else:
		return False
		

if __name__=='__main__':
	print('Enter number of element to be store into stack : ')
	length = eval(raw_input())
	L1 =[]
	while(True):
		print('1.Push')
		print('2.Pop')
		print('3.Peep')
		print('4.Is Empty')
		print('5.Is Full')
		print('6.Exit')
		option = eval(raw_input("Enter your option : "))
		if option is 1:
			element = eval(raw_input("Enter element to push :"))
			Push(L1,element)
		elif option is 2:
			Pop(L1)
		elif option is 3:
			Peep(L1)
		elif option is 4:
			if(IsEmpty(L1)):
				print("List is Empty")
			else:
				print("List have Element : "+str(L1))
		elif option is 5:
			if(IsFull(L1,length)):
				print("List is Full")
			else:
				print("List can aquire more element")

		elif option is 6:
			break

