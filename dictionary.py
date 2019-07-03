"""
        dictionaries - key value pair storage system
         We store a value but access it via a key
"""

#initialise
my_dict = {}

#add item
my_dict['name']='Mainak'
my_dict['state']='West Bengal'
my_dict['age']='18'

print my_dict

#acess item
print my_dict['name']

#change item
my_dict['name']='Moinak'
print my_dict

#remove item
del my_dict['state']
print my_dict

#iterate
for k, v in my_dict.iteritems():  # my_dict.items() fn works as fine
        print k, '=>',v

