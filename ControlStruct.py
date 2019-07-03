#if/else/elif
age = 18

if age>=18 :
        print 'Adult'
elif age>=12:
        print 'Young Adult'
elif age>=3:
        print 'Child'
else:
        print 'Minor'

#ternery
""" 
if age>=21:
        old_enough=True
else:
        old_enough=False 
        """
        
old_enough = True if age>=21 else False 

#while
while age<=20:
        #print 'Pass '+ str(age)
        print 'Pass %d' % age
        age=age+1
        
        #print int('5') OK .....but print int('Pass') WRONG
