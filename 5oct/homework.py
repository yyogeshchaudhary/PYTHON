# /usr/bin/python

def findNumberIsAmstrongOrNot(number):
    result = 0;
    num1 = number
    while(number != 0):
        result += (number%10)**3
	number = number/10		
    return result == num1
    

def findNumberIsPrimOrNot(number):
    for i in range(2,((number/2)+1)):
        if (number%i) == 0 :
            return False
    return True

def writeFabonacciSeries(number,number1 = 0, number2=1):
    fabonacci = list()
    fabonacci.append(number2)
    while((number1+number2) < number):
        temp = number1 + number2
        fabonacci.append(temp)
        number1 = number2
        number2 = temp
    return fabonacci

def checkNumberIsPalindromeOrNot(number):
    array = list()
    
    while(number != 0):
        array.append(number%10)
        number = number/10
    
    for i in range(array.__len__()/2):
        if(array[i] != array[array.__len__()-1-i]):
            return False
    return True


def printPatter1(number):
    result = ''
    for i in range(number):
        for j in range(i+1):
            result += '*'
        if(i != number-1):
            result += '\n'
    print(result)


def printPattern2(number):
    result = ''
    for i in range(number):
        for j in range(number):
            if(j < (number - i-1)):
                result += ' '
            else:
                result += '*'
        if(i != number-1):
            result += '\n'
    print(result)

def printPattern3(number):
    result = ''
    for i in range(number):
        for j in range(number):
            if(j >= i):
                result += '*'
            else:
                result += ' '
        if( i != number-1):
            result += '\n'
    print(result)

def printPattern4(number):
    result = ''
    for i in range(number*2):
        for j in range(number*2):
            if( i < number):
                if((j < (number-i)) or (j> (number+i))):
                    result +=' '
                else:
                    result += '*'
                    '''
            else:
                if((j  (number*2-i)) or (j > (number*2-i))):
                    result += ' '
                else:
                    result +='*'
                    '''
        if( i != number*2 -1):
            result += '\n'
    print(result)


if __name__=='__main__':
    number = eval(raw_input("Enter any number to check weather it is Amstrong or Not : "))
    if(findNumberIsAmstrongOrNot(number)):
        print("Number is Amstrong Number")
    else:
        print("number is not a Amstrong Number")
    
    number = eval(raw_input("Enter any number to check weather it is Prim or Not : "))
    if(findNumberIsPrimOrNot(number)):
        print("Number is Prim")
    else:
        print("Number is not Prim Number")
   
    number = eval(raw_input("Enter number to check number is Palindrome or Not : "))
    if(checkNumberIsPalindromeOrNot(number)):
        print("Number is Palindrom")
    else:
        print("Number is Not Palindrom")
    
    number = eval(raw_input("Enter number till which we want fabonacci series : "))
    print(writeFabonacciSeries(number))

    number = eval(raw_input("Enter number to print pattern1 : "))
    printPatter1(number)
    
    number = eval(raw_input("Enter number to print pattern2 : "))
    printPattern2(number)

    number = eval(raw_input("Enter number to print pattern3 : "))
    printPattern3(number)

    number = eval(raw_input("Enter number to print pattern4 : "))
    printPattern4(number)
