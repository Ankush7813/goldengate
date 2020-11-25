# print functions keyword(named arguments)
# sep=', '> this will separated the output with , and space for each value. this only works for multiple object print
# end=' ' > this will give the output in one line if used with iteration loop like FOR.it add space . if without 
# space then it will give no space between output
# join method
# its string fucntion but can use to modify the output of list because list  will give output in form of Square 
# brackets and inverted commas and comma like ['value','value1']
# to overcome this output it as value, value1 we can use join
# join can iterate on list and give results which we can do by writing for loop
A=['value','value1','value2']
for t in A:
    print(t , end =' ') # if we dont use print() then end = ' ' will take the output of below 
    # join print and make it into one line 
print()
# instead of this we can use join method
print(' | '.join(A)) # Value | Value1 | Value2
# NOTE: to use JOIN , LIST must have all the item as string datatype




# split method
# it creates lists from string  # .split() .. ()> can contain the arguments
#()>by default to whitespace > whitespace includes things like tabs ,newline,space 
print('9,233,344,455,666'.split())# it will print whole as list only one item as no space in item
print('9,233,344,455,666'.split())# it will print two items one '9,' and other whoe string as after 9 space found
# 1st method
A='9,233,344,455,666'.split(',')
B=[]
for item in A:
    B.append(int(item))
print(A)
print(B)

# 2nd method
A='9,233,344,455,666'.split(',')
for index,item in enumerate(A):
    A[index]=int(item)
print(A)
# 3rd method
A='9,233,344,455,666'.split(',')
for index in range(len(A)):
    A[index]=int(A[index])
print(A)
print(tuple(A))
