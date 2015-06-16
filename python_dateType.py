from math import sqrt

#data type
num = 8
longNum = 20000000000L
floatNum = 2.2
stringValue = "hello"
boolValue = True

print type(num)
print type(longNum)
print type(floatNum)
print type(stringValue)
print type(boolValue)

#boolean manipulate
boolValue2 = False;

print boolValue and boolValue2
print boolValue or boolValue2
print not boolValue

#number calculation
intOne = 7
intTwo = 99
floatOne = 7.9
floatTwo = 9.8

print intTwo / intOne # This should be 14.14
print float(intTwo) / float(intOne)
print int(floatOne)
print int(boolValue)

print intOne > intTwo
print intOne >= intTwo
print intOne < intTwo
print intOne <= intTwo
print intOne != intTwo
print intOne == intTwo

print intOne + intTwo
print intOne - intTwo
print intOne * intTwo
print intTwo / intOne
print intTwo % intOne
print intOne ** intTwo
print sqrt(intOne)

# Input from users
answer = raw_input("What is your name? ")
print "Hello" + answer

# String Basics 
strOne = "Hello"
strTwo = "World"
  #multiple line string should be quoted as '''...''', changeline by \
longStr = '''This is a very long string that \ 
goes on forever and ever'''
print strOne, strTwo
print strOne + strTwo
print longStr
print strOne[1::2]
print strOne.find("ll")
print strOne.count("l",2,5)
print strOne.lower()
print strOne.upper()
print strOne.replace("e","a")
print strOne.split("l")
  # trim edges' blank space but not inside
longStr2="    asdf asdf   asdf  adf asdf "
print longStr2.strip()
