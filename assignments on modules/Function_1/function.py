# Level 1
from statistics import mean, median, mode, variance
from math import sqrt as std
def add_two_numbers(a,b):
    return a+b
def area_of_circle(r):
    PI=3.14
    area=PI*r*r
    return area
def add_all_nums(*nums):
    total=0
    for num in nums:
        total+=num
    return total
print(add_all_nums(2,3,4,5))
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit
print(convert_celsius_to_fahrenheit(37))
def check_season(month):
    if month in ['January','February','March']:
        return 'Winter'
    elif month in ['April','May','June']:
        return 'Spring'
    elif month in ['July','August','September']:
        return 'Summer'
    elif month in ['October','November','December']:
        return 'Autumn'
print(check_season('August'))
def calculate_slope(x1,y1,x2,y2):
    slope=(y2-y1)/(x2-x1)
    return slope
print(calculate_slope(3,3,4,9))
def print_list(lst):
    for l in lst:
        print(l)
print_list([8,13,19,4,2])
def reverse_list(lst):
    return lst[::-1]
print(reverse_list([1,2,3,4,5]))
print(reverse_list(["A","B","C"]))
def capitalize_list_items(lst):
    return [i.upper() for i in lst]
print(capitalize_list_items(['potato','mango','banana']))
def add_item(lst,item):
    lst.append(item)
    return lst
print(add_item([1,2,3,4,5],6))
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff,'Meat'))
def remove_item(food_staff,item):
    food_staff.remove(item)
    return food_staff
print(remove_item(food_staff, 'Potato'))
numbers= [2,3,7,9]
print(remove_item(numbers, 3))
def sum_of_numbers(n):
    total=0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers(5)) 
print(sum_of_numbers(10)) 
print(sum_of_numbers(100))
def sum_of_odds(n):
    total=0
    for i in range(1,n+1,2):
        total+=i
    return total
print(sum_of_odds(5))
def sum_of_even(n):
    total=0
    for i in range(0,n+1,2):
        total+=1
    return total
print(sum_of_even(8))
# Level 2
def evens_and_odds(n):
    even = 0
    odd = 0
    for i in range(0, n + 1):
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)
print(evens_and_odds(100))
def factorial(n):
    facto=1
    for i in range(1,n+1):
        facto*=i
    return facto
print(factorial(5))
def is_empty(info):
    if len(info)==0:
        return True
    else:
        return False
print(is_empty('e'))
from statistics import mean, median, mode, variance, stdev
def calculate_range(lst):
    return max(lst) - min(lst)
def descriptive_stats(lst):
    return (mean(lst), median(lst), mode(lst), calculate_range(lst), variance(lst), stdev(lst))
print(descriptive_stats([1,2,3,4,5,4,6,7,8,8,9,10]))
# Level 3
def is_prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
            else:
                return True
    else:
        return False
print(is_prime(7))
def is_unique(lst):
    if len(lst)==len(set(lst)):
        return True
    else:
        return False
print(is_unique([1,2,3,4,4,5,6]))
def same_type(lst):
    return len(set(map(type,lst)))==1
print(same_type([1,2,3,4,5,"4"]))
def valid_variable(name):
    return name.isidentifier()
print(valid_variable('name'))
# List comprehension Exercises
numbers=[-4,-3,-2,-1,0,2,4,6]
neg_numbers=[i for i in numbers if i<1]
print(neg_numbers)
list_of_lists=[[[1,2,3]], [[4,5,6]],[[7,8,9]]]
flat_list=[number for row in list_of_lists for row1 in row for number in row1]
print(flat_list)
answer1=[tuple([i] + [1]+ [i**r for r in range(1,6)])
for i in range(11)]
for row in answer1:
    print(row)
countries=[[('Finland','Heksinki')],[('Sweden','Stockholm')],[('Norway','Oslo')]]
flat_count=[[country.upper(), country[:3].upper(),capital.upper()]
for sublist in countries
for country, capital in sublist]
print(flat_count)
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
list_dict= [
    {'country':country.upper(),'city':city.upper()}
    for sublist in countries
    for country,city in sublist
]
print(list_dict)
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concat_str= [
    f'{firstname} {lastname}'
    for sublist in names
    for firstname, lastname in sublist]
print(concat_str)