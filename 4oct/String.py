# /usr/bin/python


'''
WAP to cenvert string to Upper case
WAP to cenvert string to Lower case
'''


def convertToUpper(strVar):
	return strVar.upper()

def convertToLower(strVar):
	return strVar.lower()

def countNumberOfCharacter(strVar, toFind):
	return strVar.count(toFind[0:toFind.__len__()])

def countNumberOfDigits(strVal):
        count = 0
        for x in strVal:
		if(x.isdigit()):
			count+=1
	return count        


def findNumberOfSpecialChar(strVar):
	count = 0
	for ch in strVar:
		if(not(ch.isdigit() or ch.isalpha() or ch.isspace())):
			count+=1
	return count

def countSpaceDigitSpecialVowel(strVar):
	vowelCount = 0
	specialCount = 0
	spaceCount = 0
	digitCount = 0
	# for i in range(len(strVar):
	# 	strVar[i]
	for ch in strVar:
		if ch.isdigit():
			digitCount+=1
		elif ch.isspace():
			spaceCount+=1
		elif ch.isalpha() and ch in "aeiouAEIOU":
			vowelCount+=1
		elif not ch.isalpha():
			specialCount+=1
	return vowelCount,specialCount,spaceCount,digitCount

def countSpaceDigitSpecialVowelUsingRange(strVar):
	vowelCount = 0
        specialCount = 0
        spaceCount = 0
        digitCount = 0
        for i in range(len(strVar)):
                if strVar[i].isdigit():
                        digitCount+=1
                elif strVar[i].isspace():
                        spaceCount+=1
                elif strVar[i].isalpha() and strVar[i] in "aeiouAEIOU":
                        vowelCount+=1
                elif not strVar[i].isalpha():
                        specialCount+=1
        return vowelCount,specialCount,spaceCount,digitCount


#if __name__=='__main__'

strVariable = raw_input("Enter any String : ")
print("Number of Digit in String is : "+str(countNumberOfDigits(strVariable)))
print("Number of Space in String is : "+str(countNumberOfCharacter(strVariable," ")))
print("String After upper case      : "+convertToUpper(strVariable))
print("String After Lower case      : "+convertToLower(strVariable))
print("Number of Special Characters : "+str(findNumberOfSpecialChar(strVariable)))
print("Merged Function              : "+str(countSpaceDigitSpecialVowel(strVariable)))
print("Merged Function using range  : "+str(countSpaceDigitSpecialVowelUsingRange(strVariable)))
