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
import re

def extract_emails(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text= f.read()
        email_patt= r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails=re.findall(email_patt,text)
        return emails
filename= 'data\email_exchanges_big.txt'
print(extract_emails(filename))

def find_most_common_words(fn,num):
    with open(fn,'r',encoding='utf-8') as f:
        text= f.read()
        words= re.findall(r'\w+',text)
        word_counts= Counter(words)
        top_words=[(count,word) for word, count in word_counts.most_common(num)]
        return top_words
fn1= 'data\obama_speech.txt'
print(find_most_common_words(fn1,10))
fn2= 'data\michelle_obama_speech.txt'
print(find_most_common_words(fn2,10))
fn3= 'data\donald_speech.txt'
print(find_most_common_words(fn3,10))
fn4= 'data\melina_trump_speech.txt'
print(find_most_common_words(fn4,10))

import re
import string
stop_words = set([
    'i','me','my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 
    'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', 
    "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 
    'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 
    'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 
    'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 
    'after', 'above', 'below', 'to', 'from', 'up','down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 
    'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 
    'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 
    's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 
    'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', 
    "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 
    'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"
])
def load_text_from_file(filename):
    """Reads text from a file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

def clean_text(text):
    """Removes punctuation, converts to lowercase."""
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)  # Remove punctuation
    text = text.strip()
    return text

def remove_support_words(text):
    """Removes stop words from the text."""
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words

def check_text_similarity(file1, file2):
    """Checks similarity between two text files."""
    text1 = load_text_from_file(file1)
    text2 = load_text_from_file(file2)

    if text1 is None or text2 is None:
        return None 
    text1 = clean_text(text1)
    text2 = clean_text(text2)
    words1 = set(remove_support_words(text1))
    words2 = set(remove_support_words(text2))

    if not words1 or not words2:
        return 0.0  

    similarity = len(words1 & words2) / len(words1 | words2)   
    return round(similarity * 100, 2) 

file1 = "data\michelle_obama_speech.txt"
file2 = "data\melina_trump_speech.txt"

similarity = check_text_similarity(file1, file2)
if similarity is not None:
    print(f"Similarity between {file1} and {file2}: {similarity}%")

fn1= 'data\romeo_and_juliet.txt'
print(find_most_common_words(fn1,10))