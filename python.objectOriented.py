__metaclass__ = type

# class
class Animal:
    # __ means private attribute, method
    __hungry="yes"
    __name="no"
    # constructor here, all the function use self as first argument
    def __init__(self,**kv):
        self._attributes = kv
    # add property here    
    def set_attributes(self,key,value):
        self.attributes[key]=value
        return
    def get_attributes(self,key):
        return self._attributes.get(key,None)
    # encapsulation
    def set_name(self,newname):
        self.__name=newname
        return
    def get_name(self):
        self.__bark()
        return self.__name
    def __bark(self):
        pass
    def noise(self):
        print("err")
        return
    
#inheritance
class Dog(Animal):
    def __init__(self,**kv):
        # super contructor here
        super(Dog,self).__init__()
        self._attributes = kv
    # override function
    def noise(self):
        print("wang")
        return
#multi-inheritance Dog first
class Dat(Dog,Animal):
   def __init__(self,**kv):
        # super contructor here
        super(Dat,self).__init__()
        self._attributes = kv

# polyphorism
def play(Animal):
    Animal.noise()
    print(Animal.get_attributes("__name"))
    
def main():
    animal = Animal()
    animal.set_name("fred")
    print animal.get_name()
    animal.noise()

    jake = Dog(__name="jake",__hungry="yes")
    play(jake)
    # class type judgement
    print issubclass(Dog,Animal)
    print Dog.__bases__
    print jake.__class__
    print jake.__dict__
    
if __name__ == '__main__':main()
