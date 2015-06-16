#tuple is immutable
tupleEx = ('ab',4,True)
tupleOneItem = (4,)
 # start with 0,1,2,3... reverse order with index -1,-2,-3...
print tupleEx[0]
print tupleEx[-1]
print tupleEx
 # start from first parameter to second parameter index
print tupleEx[1:2]
 # tuple will tear apart string
tupleEx2 = tuple('abcd')
print tupleEx2 

#list is mutable
listEx= ['ab',4,True,3,False]
 # blank means end 
print listEx[:3]
print listEx[-3:]
 # list every other numbers from index 1 to end 
print listEx[1::2]
print len(listEx)
print min(listEx)
print max(listEx)
 # list will tear apart string
listEx2 = list('abcd')
print listEx2
 # replace elements
listEx2[2:]='f'
print listEx2
 # join list elements by string
print ''.join(listEx2)
 # delete element
del listEx2[1]
print listEx2
listEx.append('extra');
listEx.remove('extra');
print listEx
 # insert element
listEx.insert(2,'extra');
print listEx
 # sort elements
listEx.sort()
print listEx
 # multi dimension
listEx3 = [ [1,2,3], ['a','b','c'], [True,False,True]]

#dictionary is immutable
dictEx = {"a":1,"b":2,"c":3,"d":4}
print dictEx.get('a')
print dictEx.items()
print dictEx.values()
dictEx.pop("c")
print dictEx.items()
