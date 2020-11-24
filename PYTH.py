

# LIST key points
# when we do the item assignment of the sequence with slicing then make sure you use the correct iterable item to replace the value.
# like  s=[1,2,3,4] if s[0:4:2]=[123] then it will error as we are trying to replace two items from list but only item has been passed to assignement.
# also if slicing then make sure do not use pure int/float/complex as they are not iterable items

# test code
# when you write a code  make sure its conditions follows for all set of data
# 1. for all met conditions 
# 2. for more then condition value like more then defined values
# 3. empty values like below it mostly works for all set of data to remove the values from list
data=[1,2,100,101,150,200,201,299,300,301]
# data=[100,101,150,200,201,299,300,301]
#data=[1,2,100,101,150,200,201,299]
#data=[101,103,1000,1001,1003]
# data=[1,2,100,101,150,200,201,299,300,301]

min_value=100
max_value=300
A=None # for debugging only
for index in range(len(data)-1,-1,-1): 
# if we are removing values from sequence with for loop then make sure you understood how it work. 
# in list when we use for loop it will only move forward , when we remove the ites from sequence 
# then at that time sequence index /length also reduced and adjacent values which needs to remove 
# wont remove as they occupy the index vale of the removed item like [1,2,100,200,300] if we removed 
# 1 then 2 wont shows up in loop as loop only move forward    A=data[index] # for debugging
    if data[index] > max_value or data[index] < min_value:
        print(index, data)
        del data[index]
print(data)
# for ordered list/sequence
data=[1,2,100,101,150,200,201,299,300,301]
# data=[100,101,150,200,201,299,300,301]
#data=[1,2,100,101,150,200,201,299]
#data=[101,103,1000,1001,1003]
# data=[1,2,100,101,150,200,201,299,300,301,302]

min_va=100
max_v=300
for value in data:
  if value >max_v or value < min_v:
    data.remove(value)  #o/p will be [2,100,101,150,200,201,299,300,302] As 2 and 302 occupy the index position of 1 and 301
 
 
stop=0
for index, value in enumerate(data):
  if value > min_v:
    stop=index
    break
del data[:stop]

start=0
for index, value in enumerate(data): # this function will cause the issue as if conditon dont 
                                     # statisfy then start remains 0 and del will run on all the list 
                                     # to overcome this we can use backward indexing 
                                     # for index in range(len(data)-1,-1,-1):
                                     #   if data[index] < max_v:
                                     #     start=index+1
                                     #     break
  if value >max_v:
    start=index+1
    break
del data [start:]
print(data)
