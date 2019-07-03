"""
                                                        Largest prime factor
                                                                Problem 3 
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

"""

#NOT EXECUTING TILL COMPLETION BUT WE GET AN ANS 
import math

def isprime(n):
        f=1 ;i=2
        while i<n:
                if(n%i==0):
                        f=0
                        break
                i+=1
        return  f

"""
def isdiv(n1,n2):
        if(n1%n2==0):
                return 1
        else:
                return 0
"""
x=int(math.ceil(math.sqrt(600851475143)))

for i in range (2,x,1) :
        if (isprime(i) ) and (600851475143%i==0):
                print i
        i+=1https://medium.com/@kingrayhan/500-data-structures-and-algorithms-practice-problems-and-their-solutions-b45a83d803f0
