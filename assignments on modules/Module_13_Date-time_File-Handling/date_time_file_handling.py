#Datetime Exercises
from datetime import datetime
from datetime import date
now= datetime.now()
print(now)
format_date= now.strftime('%m/%d/%Y,%H:%M:%S')
print(format_date)
date_str='5 December,2019'
date_obj= datetime.strptime(date_str,'%d %B,%Y')
print(date_obj)
today= date(year=2025,month=1,day=31)
new_year= date(year=2026, month=1,day=1)
time_left_newyear= new_year-today
print(time_left_newyear)
date1=date(year=1970,month=1,day=1)
time_diff=today - date1
print(time_diff)
def new_year_message(today):
    today= datetime.today()
    if today.month==1 and today.day==1:
        return 'Happy New Year!!!'
    else:
        return 'Just another day in the trenches'
print(new_year_message(today))
# File Handling
def count_words(file_name):
    with open(file_name,'r',encoding="utf-8") as f:
        words= f.read().split()
        return len(words)
def count_lines(file_name):
    with open(file_name,'r', encoding="utf-8") as f:
        lines= f.readlines()
        return len(lines)
with open(r'C:\Users\theop\OneDrive\Documents\GitHub\Cohort-3.0-Python-Programming-Fellowship-Assignments\data\obama_speech.txt','r',encoding="utf-8") as f:
    print(f.read())
file_path1= r'C:\Users\theop\OneDrive\Documents\GitHub\Cohort-3.0-Python-Programming-Fellowship-Assignments\data\obama_speech.txt'
file_path2= r'C:\Users\theop\OneDrive\Documents\GitHub\Cohort-3.0-Python-Programming-Fellowship-Assignments\data\michelle_obama_speech.txt'
file_path3= r'C:\Users\theop\OneDrive\Documents\GitHub\Cohort-3.0-Python-Programming-Fellowship-Assignments\data\donald_speech.txt'
print("summary of (a) obama_speech.txt:")
print("no. of words: ",count_words(file_path1))
print("no. of lines: ",count_lines(file_path1))
print("summary of (b) michelle_speech.txt:")
print("no. of words: ",count_words(file_path2))
print("no. of lines: ",count_lines(file_path2))
print("summary of (c) melina_trump_speech.txt:")
print("no. of words: ",count_words(file_path3))
print("no. of lines: ",count_lines(file_path3))

import json
from collections import Counter
def ten_most_spoken_languages(json_file,num):
    with open(json_file,'r',encoding="utf-8") as f:
        data= json.load(f)
        print("data type",type(data))
    all_lang=[]
    for country in data:
        all_lang.extend(country.get('languages',[]))
    lang_counts= Counter(all_lang)
    top_lang=[(count,lang) for lang, count in lang_counts.most_common(num)]
    return top_lang
json_file= "data\countries_data.json"
print(ten_most_spoken_languages(json_file,10))

def most_populated_countries(json_file_c,num):
    with open(json_file_c,'r',encoding="utf-8") as f:
        data= json.load(f)
    all_countries=[]
    for country in data:
        all_countries.append((country.get('name'),country.get('population')))
        
    country_counts= Counter(all_countries)
    top_countries=[(count,country) for country, count in country_counts.most_common(num)]
    print(top_countries)
json_file_c= "data\countries_data.json"
print(most_populated_countries(json_file_c,10))

#Exercises: Level 2
