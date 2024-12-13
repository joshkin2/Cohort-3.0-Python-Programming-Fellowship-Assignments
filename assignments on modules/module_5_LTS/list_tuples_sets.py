# Exercises: Level 1
emp= []
tem= [1,2,3,4,5,6]
print(len(tem))
print(tem[0])
print(tem[2:-2])
print(tem[-1])
mixed_data_types= ['jamal',24,195,'single','2 bony lagos']
it_companies= ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[3])
print(it_companies[-1])
it_companies[1]= 'Tesla'
print(it_companies)
it_companies.append('Silicon')
it_companies.insert(4,'Hugo')
print(it_companies)
it_companies[1]='TESLA'
STR_S= '#; '
SKK= list(STR_S)
add_both= it_companies + SKK
print(add_both)
does_exist= 'Hugo' in it_companies
print(does_exist)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[0:3])
print(it_companies[-4:-1])
print(it_companies[4])
it_companies.remove('TESLA')
print(it_companies)
del it_companies[3:5]
print(it_companies)
del it_companies[-1]
print(it_companies)
del it_companies[0:]
print(it_companies)
del it_companies
front_end=['HTML', 'CSS', 'JS','React','Redux']
back_end=['Node','Express','MongoDB']
full_stack= front_end + back_end
print(full_stack)
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

#Exercises: Level 2
ages= [19,22,19,24,20,25,26,24,25,24]
ages.sort()
print (ages)
min_age= ages[0]
max_age= ages[-1]
ages.append(min_age)
ages.append(max_age)
print(ages)
medi=ages[5:7]
print(medi)
avg_age= sum(ages)/ len(ages)
ran_age= max_age-min_age
comp_min_age= abs(min_age-avg_age)
comp_max_age= abs(max_age - avg_age)
print(comp_min_age)
print(comp_max_age)
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
n= len(countries)
mid_index= n//2
if n%2!=0:
    mid_country= countries[mid_index]
    print(mid_country)
else:
    mid_countries= [countries[mid_index -1], countries[mid_index]]
    print(mid_countries)
half_len= len(countries)//2
one_half= countries[:half_len]
two_half= countries[half_len:]
print(one_half)
print(two_half)
country= ['China','Russia','USA','Finland','Sweden','Norway','Denmark']
one_count, two_count, three_count= country[:3]
scandic_countries= country[3:]
print(one_count,two_count,three_count, scandic_countries)
# Tuple Exercises: Level 1
tpl= ()
f_siblings= ('jane','star')
m_siblings= ('andrew','jim')
siblings= f_siblings + m_siblings
print(len(siblings))
full= list(siblings)
full.append('joe')
full.append('jessica')
family_members= tuple(full)
print(family_members)
# Tuple Exercises: Level 2
sibling1, sibling2, sibling3, sibling4, *parents= family_members
print(sibling1)
print(sibling2)
print(sibling3)
print(sibling4)
print(parents)
fruits= ('mango','watermelon','pineapple')
vegetables= ('spinach', 'kale','beets')
animal_products= ('egg','ponmo','honey')
food_stuff_tp= fruits + vegetables+animal_products
food_stuff_it= list(food_stuff_tp)
print(food_stuff_it)
print(food_stuff_it[-5])
print(food_stuff_it[:3])
print(food_stuff_it[6:])
del(food_stuff_tp)
nordic_countries= ('Denmark','Finland','Iceland','Norway','Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
# Sets Exercises: Level 1
it_companies= {'Facebook', 'Google','Microsoft','Apple','IBM','Oracle','Amazon'}
A={19,22,24,20,25,26}
B= {19,22,20,25,26,24,28,27}
age={22,19,24,25,26,24,25,24}
len(it_companies)
it_companies.add('Twitter')
print(it_companies)
it_companies.update(['Hugo','Selar','OpenAI'])
print(it_companies)
it_companies.remove('Selar')
#when item to be deleted is not found when using remove() it will raise error, whereas when discard() is used it doesn't
#Sets Exercises:Level 2
st3= A.union(B)
print(st3)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
st3= A.union(B)
st4= B.union(A)
st5= st3.union(st4)
print(st5)
print(A.symmetric_difference(B))
del(it_companies)
del(A)
del(B)
# Sets Exercises: Level 3
st_age= set(age)
# string- immutable but ordered sequence of characters enclosed in single, double or triple quotes
# list - ordered and mutable collection of items that allows duplicates
# tuple - ordered but immutable collection of items
# set - unordered but mutable collection of unique items
sentence= 'I am a teacher and I love to inspire and teach people.'
uni_words= set(sentence.split())
print(uni_words)
count_uni_words= len(uni_words)
print(count_uni_words)