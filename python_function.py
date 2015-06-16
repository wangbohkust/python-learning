# global value could only be changed using global
globalValue = 10
def foo3():
   # declare first then change value
   global globalValue
   globalValue = 15
   # second way
   globals()['globalValue'] = 20
    
# default value 1,2
def foo(numOne=1,numTwo=2):
    return numOne+numTwo

# arbitray arguments, *means list
def foo2(*args):
    finalValue = 0;
    if args:
        for i in args:
            finalValue += i
        return finalValue
    else:
        return "no number"

# create dictionary, **means two dimension
def foo4(**kv):
    print type(kv)
    for i in kv:
        print i, kv[i]
    return

# pass will do nothing
def main():
    foo3()
    print globalValue
    print foo(50,60)
    print foo2(50,60,70)
    print foo2()
    foo4(name="wang",age=24,gender="male")

if __name__ == '__main__':main()
