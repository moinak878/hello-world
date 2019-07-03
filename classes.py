#definition/self/properties/methods
class Person:
        #class body
        name=None
        age=None
        
        #def __init__(self):       ctor overloading DOES NOT SEEM TO WORK
                #self.name="No name supplied"
                #self.age=0
        
        def __init__(self,name,age):
              self.name=name
              self.age=age
        
        def say_name(self):          #SELF is referencing the class
                #body of method
                print 'My name is %s'% self.name
                
        def say_age(self):
                print 'My age is %d' % self.age
                
        def have_birthday(self):
                self.age +=1


