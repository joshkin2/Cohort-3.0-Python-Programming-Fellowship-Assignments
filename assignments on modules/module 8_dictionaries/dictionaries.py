dog={} #Create an empty dictionary called dog
dog= {'name':'trey', 'color':'beige','breed':'maltese','legs':4,'age':5}
student_dict={
  'first_name':'leo',
  'last_name':'dan',
  'gender':'female',
  'age':14,
  'marital status':'single',
  'skills':'coding',
  'country':'iran',
  'city':'izbeh',
  'address':'2 oslo dr'}
print(len(student_dict))
print(student_dict['skills'])
type(student_dict['skills'])
student_dict['skills']=['writing','drawing'] #Modify the skills values by adding one or two skills
keys= student_dict.keys() # Get the dictionary keys as a list
print(keys)
values= student_dict.values() # Get the dictionary values as a list
print(values)
print(student_dict.items()) #Change the dictionary to a list of tuples using items() method
del student_dict['address'] #Delete one of the items in the dictionary
del dog # Delete one of the dictionaries





