# if statement, indent control
numValue=25
if(1>0)and(2>0):
  if(numValue==25):
      print "matched"
  elif(numValue==35):
       print "35"
  else:
       print "different"
else:
    print "wrong"
print  "large" if(1>0) else"small"  

#no swith statement

#in operator
listEx = [4,5,6]
print 3 in listEx

#while statement
x=1
while x<=10:
  print x,
  x+=1

# for statement
for i in listEx:
    print i
for i in range(1,10):
   print i,
