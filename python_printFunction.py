import math

# print function
stringValue = 'fred'
floatValue = 35.4
intValue = 2;
charValue = 'a'
boolValue = True;
print '%s %.1f %c %d %s' % (stringValue,floatValue,charValue,intValue,boolValue)
 # set precision bit
print '%.15f' % math.pi
print '%20f' % math.pi
print '%.*f' % (intValue,math.pi)
