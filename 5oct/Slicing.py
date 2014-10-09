#/usr/bin/python

def splitAndJoin():
	a= '/usr/bin/python'
	x= a.split('/')             # split on /
	print(x)
	y= ''.join(x)               # join element in list
	print(y)
	z= '/'.join(x)
	print(z)

def slicing():
	s= 'www.google.com'
	print(s[:3])
	print(s[1:3])
	print(s[1:-3])
	print(s[-10:-3])
	print(s[1:10:2])
	print(s[::-1])                # reverse the string with every byte of string from end
	print(s[::-2])                # reverse the string with every secong byte of string from end


def createList():
	a= [1,2,'Yogi']
	print(type(a))
	
	b= list((1,2,'yogi'))
	print(b)

def appending():
	L1 = [1,5,3,4,2,5]
	L2 = [56,6,17,8]
	L1.extend(L2)                # extend L1 by adding element from L2
	print(L1)
	L1.append(20)                # add elemnt at the end of list
	print(L1)
	L1.sort()
	print(L1)
	L1.append(26)
	print(sorted(L1))
	print(L1.count(5))
	
	L1 = [1,2,2,3,3,4,4,2,3,4,1]
	print(L1.count(4))
	print(L1.index(2,L1.index(2)+1))

	del L1[5:7]
	print(L1)


appending()	

if __name__=='__main':
	createList()	
