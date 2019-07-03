"""
                                                                                        Problem 1 
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

"""
ctr=0
i=1
                                                                                                                """
while (i<1000):
        if(i%3==0) or (i%5==0):
                print i,
                ctr+=i
        i+=1
print "\nTotal", ctr

                                                                                                                """
#ALTERNATE SOLUTION 

for i in range(0,1000,3):
                ctr+=i
i=0
for i in range(0,1000,5):
                ctr+=i
for i in range(0,1000,15):
                ctr-=i                
print ctr
