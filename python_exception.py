import exceptions

def main():
 #print out exceptions in dir
    for i in dir(exceptions):
        print i
 #exception example       
    #keyerror in dic
    dictEx={'name':'bowang'}
    print dictEx['age']
    #file not exist
    f = open('notExistFile')
    #custom exception
    raise Exception("ExceptionTest")
    # Raise a NameError exception
    print monkey
    # Raise a SyntaxError exception
    #print "Hello'
    #Raise a TypeError exception
    print "Tomato" % 5
    # Raise a ZeroDivisionError exception
    zeroDivisionErr = 1/0
 # handle exception
    try:
      zeroDivision = 1/0
    except ZeroDivisionError:
      print "You can’t divide by zero"
    # Stop multiple exceptions
    try:
     zeroDivision = R/0
    except (ZeroDivisionError,NameError), e:
     print e # Prints out the error message for the first exception caught
     # Catch every exception
    try:
       zeroDivision = R/0
    except:
       print "You messed up"
      # Use finally to always perform an action error or not
    try:
          halfDivision = 1.0/2.0
    except (ZeroDivisionError,NameError):
          print 'You messed something up'
    else:
         print halfDivision
    finally:
         print "I always get to say something"

    
if __name__ == '__main__':main()
