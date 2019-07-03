#                                               FUNCTIONS
#definition 
def my_fn():
        print 'hello'
        
#arguments/return
def add(n1,n2):
        print n1+n2
        return n1+n2
#multiple return
def square(n1,n2):
        return n1**2,n2**2

#calling
my_fn()
add(1,2)
result =add(n2=1,n1=2) #also valid ..just reverses which goes to which 
print result
print square(2,5)  #result stored in tuples
result1 , result2 = square(1,2) #unpacking tuples
print result1,result2
