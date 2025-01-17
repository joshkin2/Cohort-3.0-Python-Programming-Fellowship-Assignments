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
countries = [ 'Afghanistan','Albania',

  'Algeria',

  'Andorra',

  'Angola',

  'Antigua and Barbuda',

  'Argentina',

  'Armenia',

  'Australia',

  'Austria',

  'Azerbaijan',

  'Bahamas',

  'Bahrain',

  'Bangladesh',

  'Barbados',

  'Belarus',

  'Belgium',

  'Belize',

  'Benin',

  'Bhutan',

  'Bolivia',

  'Bosnia and Herzegovina',

  'Botswana',

  'Brazil',

  'Brunei',

  'Bulgaria',

  'Burkina Faso',

  'Burundi',

  'Cambodia',

  'Cameroon',

  'Canada',

  'Cape Verde',

  'Central African Republic',

  'Chad',

  'Chile',

  'China',

  'Colombi',

  'Comoros',

  'Congo (Brazzaville)',

  'Congo',

  'Costa Rica',

  "Cote d'Ivoire",

  'Croatia',

  'Cuba',

  'Cyprus',

  'Czech Republic',

  'Denmark',

  'Djibouti',

  'Dominica',

  'Dominican Republic',

  'East Timor (Timor Timur)',

  'Ecuador',

  'Egypt',

  'El Salvador',

  'Equatorial Guinea',

  'Eritrea',

  'Estonia',

  'Ethiopia',

  'Fiji',

  'Finland',

  'France',

  'Gabon',

  'Gambia, The',

  'Georgia',

  'Germany',

  'Ghana',

  'Greece',

  'Grenada',

  'Guatemala',

  'Guinea',

  'Guinea-Bissau',

  'Guyana',

  'Haiti',

  'Honduras',

  'Hungary',

  'Iceland',

  'India',

  'Indonesia',

  'Iran',

  'Iraq',

  'Ireland',

  'Israel',

  'Italy',

  'Jamaica',

  'Japan',

  'Jordan',

  'Kazakhstan',

  'Kenya',

  'Kiribati',

  'Korea, North',

  'Korea, South',

  'Kuwait',

  'Kyrgyzstan',

  'Laos',

  'Latvia',

  'Lebanon',

  'Lesotho',

  'Liberia',

  'Libya',

  'Liechtenstein',

  'Lithuania',

  'Luxembourg',

  'Macedonia',

  'Madagascar',

  'Malawi',

  'Malaysia',

  'Maldives',

  'Mali',

  'Malta',

  'Marshall Islands',

  'Mauritania',

  'Mauritius',

  'Mexico',

  'Micronesia',

  'Moldova',

  'Monaco',

  'Mongolia',

  'Morocco',

  'Mozambique',

  'Myanmar',

  'Namibia',

  'Nauru',

  'Nepal',

  'Netherlands',

  'New Zealand',

  'Nicaragua',

  'Niger',

  'Nigeria',

  'Norway',

  'Oman',

  'Pakistan',

  'Palau',

  'Panama',

  'Papua New Guinea',

  'Paraguay',

  'Peru',

  'Philippines',

  'Poland',

  'Portugal',

  'Qatar',

  'Romania',

  'Russia',

  'Rwanda',

  'Saint Kitts and Nevis',

  'Saint Lucia',

  'Saint Vincent',

  'Samoa',

  'San Marino',

  'Sao Tome and Principe',

  'Saudi Arabia',

  'Senegal',

  'Serbia and Montenegro',

  'Seychelles',

  'Sierra Leone',

  'Singapore',

  'Slovakia',

  'Slovenia',

  'Solomon Islands',

  'Somalia',

  'South Africa',

  'Spain',

  'Sri Lanka',

  'Sudan',

  'Suriname',

  'Swaziland',

  'Sweden',

  'Switzerland',

  'Syria',

  'Taiwan',

  'Tajikistan',

  'Tanzania',

  'Thailand',

  'Togo',

  'Tonga',

  'Trinidad and Tobago',

  'Tunisia',

  'Turkey',

  'Turkmenistan',

  'Tuvalu',

  'Uganda',

  'Ukraine',

  'United Arab Emirates',

  'United Kingdom',

  'United States',

  'Uruguay',

  'Uzbekistan',

  'Vanuatu',

  'Vatican City',

  'Venezuela',

  'Vietnam',

  'Yemen',

  'Zambia',

  'Zimbabwe',

]
from collections import Counter
def count_countries_initial(countries):
    return dict(Counter(country[0].upper() for country in countries))
result=count_countries_initial(countries)
print(result)
def get_first_ten_countries(countries):
    return countries[:10]
print(get_first_ten_countries(countries))
def get_last_ten_countries(countries):
    return countries[-10:]
print(get_last_ten_countries(countries))