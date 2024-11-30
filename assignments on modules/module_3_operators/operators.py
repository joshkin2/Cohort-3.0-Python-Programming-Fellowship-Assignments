age= 24
height=196.1
yo= 1j + 1
def cal_triangle_area():
    b= float(input('Enter base: '))
    h= float(input('Enter height: '))
    area = (0.5 * b * h)
    print("The area of the triangle is: ", area)
cal_triangle_area()
def per_of_triangle():
    a=int(input("Enter side a: "))
    b=int(input("Enter side b: "))
    c= int(input("Enter side c: "))
    perimeter= a+b+c
    print("The perimeter of the triangle is", perimeter)
per_of_triangle()
length= float(input('Lenght of rectangle: '))
width= float(input('Width of rectangle: '))
area= length * width
perimeter= 2 * (lenght+width)
print( "Area of rectangle is ", area)
print("Perimeter of rectangle is ", perimeter)
pi=3.14
radius = float(input("Enter radius of circle: "))
area= 3.14*radius**2
circumference= 2*pi*radius
print("Area of circle is ", area)
print("Circumference of circle is ", circumference)
length_python=len("python")
lenght_dragon= len("dragon")
print("Lenghth of python is ", length_python)
print("Length of dragon is ", lenght_dragon)
eg1="python"
eg2="dragon"
if "on" in eg1 and "on" in eg2:
    print("both eg contain 'on'")
else:
    print("one or none contain 'on")
sentence= "I hope this course is not full of jargon."
if "jargon" in sentence:
    print("Word is present")
else:
    print("Word is absent")
eg3 = "python"
eg4 = "dragon"
if "on" in word1 and "on" in word2:
  print("Both contain 'on'")
else:
  print("One or both do not contain 'on'")
length_python=len("python")
python_float=float(length_python)
python_str=str(python_float)
number= int("Enter any number: ")
if number %2==0:
    print(number, "is even number")
else:
    print(number, "is odd number")
div1= 7//3
int_no= int(2.7)
if div1 == int_no:
    print("It is equal")
else:
    print("It is not equal")
str_no= "10"
int_no = 10
if type(str_no) == type(int_no):
    print("They are of same type")
else:
    print("They are different types")
int_no1= int("9.8")
int_no2= 10
if int_no1==int_no2:
    print("It is equal")
else:
    print("It is not equal")
hours= float(input("Enter hours: "))
rate_per_hour=float(input("Enter rate per hour: "))
pay= hours * rate_per_hour
print("Your weekly earning is ", pay)
years= int(input("Enter number of years you lived: "))
seconds_per_year= 365*24*60*60
total_seconds= years* seconds_per_year
print("You have lived for", total_seconds "seconds.")