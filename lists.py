#lists - Array of heterogeneous data types  basically

#initialise
my_list = [1,2,3,":)",True,4.5]

#add items
my_list.append(88)
print  my_list

#access item
print my_list[3] #index starts from 0

#change item
my_list[3]=':D'
print my_list

#remove item
del my_list[3]
print my_list

#iterate
for i in my_list:
        print i
