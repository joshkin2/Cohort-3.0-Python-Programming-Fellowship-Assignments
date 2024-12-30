# 1. Simple Variable Assignment
x=10
print(x)

# 2. Assigning Different Data Types
age=25
height=5.9
name= 'John'
is_active= True
print([age,height,name,is_active])

# 3. Simple Addition
a= 9
b= 3
print(a+b)

# 4. String Concatenation
first_name= 'Alice'
last_name=' Wonderland'
print(first_name+last_name)

# 5. Variable Type Check
x= 'Hello'
print(type(x))

# 6. Swap Two Variables
a=10
b=5
a=a+b
b=a-b
a=a-b
print([a,b])

# 7. Arithmetic Operations
x=15
y=4
print([x+y,x-y,x*y,x/y,x%y])

# 8. Multiple Variable Assignment
x,y,z=1,2,3
print([x,y,z])

# 9. Updating Variable Values
counter=10
counter+=5
counter-=3
print(counter)

# 10. Variable Re-assignment
x=100
x=50
print(x)

# 11. User input and Variable Assignment
users_name= input('Enter name: ')
print('Hello,' +users_name)

# 12. String to int conversion
num_str= '42'
print(int(num_str))

# 13. Int to Str conversion
num=100
print(str(num))

# 14. Lists
fruits=['apple','banana','cherry']
favorite_fruit=fruits[0]
print(favorite_fruit)

# 15. String length
message= 'Hello, Python!'
length= len(message)
print(length)


# 16. Floating-point arithmetic
a=3.14
b=2.71
print([a+b,a-b,a*b])

# 17. combining strings with variables
first_name= 'John'
last_name= 'Doe'
print('Hello, '+ first_name + ' '+last_name + '!')

# 18. F-strings
age=25
name='Alice'
print(f'My name is {name} and I am {age} years old.')

# 19. Constants convention
PI= 3.14159 #it is written in all caps so that the value remians the same throughout the program
print(PI)

# 20. Dictionaries
person= {'name':'Alice',"Age":25}
age_value=25
print(age_value)

# 21. Global and Local Variables
x=5
def my_function():
    x=10
    print(x)
my_function()
print(x)

# 22. Swap with Pythonic method
x,y=5,10
x,y=y,x
print([x,y])

# 23. Boolean expressions
is_sunny= True
is_raining= False
if is_sunny and not is_raining:
    print('Good day to be out!')
else:
    print('Bad weather for outing')

# 24. Typecasting multiple variables
x='100'
y='50'
z='30'
x_int= int(x)
y_int=int(y)
z_int=int(z)
addition= x_int+y_int+z_int
print(addition)

# 25. Modifying string values
sentence='Python is awesome'
updated_sentence= sentence.replace('awesome','cool')
print(updated_sentence)

# 26. Complex Variable Assignment
person= {'name':'Bob','age':30}
person_name= 'Bob'
person_age= 30
print([person_name,person_age])

# 27. Using Variables in Functions
def greet(name):
    print('Hello, ' + name +'!')
greet('theo')

# 28. Counting Occurences
text= 'apple apple banana apple'
apple_count= text.count('apple')
print(apple_count)

# 29. Multiple variables in a Function
def add_numbers(a,b):
    return a+b
result= add_numbers(5,7)
print(result)

# 30. Variables in Lists and Loops
numbers=[1,2,3,4,5]
doubled_numbers= []
for number in numbers:
    doubled_number= number * 2
    doubled_numbers.append(doubled_number)
print(doubled_numbers)