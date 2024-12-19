# Exercises: Level 1
age= int(input('Enter your age:'))
if age >= 18:
    print('You are old enough to learn to drive.')
else:
    years_left= 18-age
    print(f'You need  {years_left} more years to learn to drive.')
your_age=int(input('Enter your age:'))
my_age= 30
if your_age == 30:
    print('We are agemates!')
else:
    if your_age> my_age:
        age_diff= your_age - my_age
        print(f'You are {age_diff} years older than me')
num_one=int(input('Enter number one: '))
num_two= int(input('Enter number two: '))
if num_one> num_two:
    print(f'{num_one} is greater than {num_two}')
elif num_one< num_two:
    print(f'{num_one} is smaller than {num_two}')
else:
    print(f'{num_one} is equal to  {num_two}')
# Exercises: Level 2
score=int(input('What is your score?'))
if score>=80 or score==100:
    print(f'Your grade is A')
elif score>=70 or score==89:
    print(f'Your grade is B')
elif score>=60 or score==69:
    print(f'Your grade is C')
elif score>=50 or score==59:
    print(f'Your grade is D')
else:
    print(f'Your grade is F')
season= input('What month are you in? ')
if season== 'September' or season == 'October' or season== 'November':
    print(f'The season is Autumn')
elif season=='December' or season=='January'or season=='February':
    print(f'The season is Winter')
elif season=='March'or season=='April'or season=='May':
    print(f'The season is Spring')
else:
    print(f'The season is Summer')
fruits = ['banana','orange','mango','lemon']
add_fruit= input('Check for fruit ')
if add_fruit is in fruits:
    print('That fruit already exist in the list')
elif add_fruit is not in fruits:
    print()
