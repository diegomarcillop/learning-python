x = 2 
print(x == 2)

name = "Diego"
age = 23
if  name == 'Diego' and age == 23:
  print('My name is %s and age is %d' % (name, age))

if  name == 'Diego' or name == 'Fernando':
  print("My name is Diego or Fernando")

# IN
number = [1, 2, 3, 4, 5]
if 6 in number :
  print('Yes')

#  IS 
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)
print(x is x)
print ('Diego' is 'Diego')

# NOT 
print (not False)
print ((not False) == False)