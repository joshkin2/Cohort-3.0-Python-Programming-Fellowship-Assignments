# Exercise: Level 1
# 1. map applies function to all elements, filter selects data based on conditions, reduce aggregates data into 1 result.
# 2. H-OF shows how funcs can operate on or return other funcs, Closure helps retain state without using global var, Decorator mods or extends functionality.
def mul(num):
    return num + num
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mul_numbers= list(map(mul,numbers))
print(mul_numbers)
def is_odd(num):
    return num % 2 !=0
odd_num=list(filter(is_odd,numbers))
print(odd_num)
from functools import reduce
def minus(s,p):
    return s-p
deduc_num=reduce(minus,numbers)
print(deduc_num)
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for country in countries:
    print(country)
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for name in names:
    print(name)
for num in numbers:
    print(num)
# Exercises: Level 2
upper_count = map(lambda country: country.upper(), countries)
print(list(upper_count))
squared_num1= map(lambda number: number **2,numbers)
print(list(squared_num1))
upper_namess= map(lambda name:name.upper(),names)
print(list(upper_namess))
def contains(country):
    if country.__contains__('land'):
        return True
    return False
land_count=filter(contains,countries)
print(list(land_count))
def count_six(country):
    if len(country)==6:
        return True
    return False
count_with_six=filter(count_six,countries)
print(list(count_with_six))
def than_six(country):
    if len(country)>6:
        return True
    return False
print(list(filter(than_six,countries)))
def start_e(country):
    if country.startswith("E"):
        return True
    return False
print(list(filter(start_e,countries)))
def double(num):
    return num*2
def is_even(num):
    return num%2==0
result= filter(is_even,map(double,numbers))
print(list(result))
lst= [1,2,3,4,5,6,7,8,9,10]
def get_string_lists(lst):
    return list(map(lambda x: str(x),lst))
print(get_string_lists(lst))
def sum_num(num):
    return reduce(lambda x,y:x+y,num)
print(sum_num(numbers))
sentence= reduce(lambda x, y: f"{x}, {y}" if y != countries[-1] else f"{x}, and {y}", countries) + " are north European countries."
print(sentence)
