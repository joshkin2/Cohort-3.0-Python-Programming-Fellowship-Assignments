dog={}
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
  'address':'2 oslo dr'
print(len(student_dict))
print(student_dict['skills'])
type(student_dict['skills'])
student_dict['skills']=['writing','drawing']
keys= student_dict.keys()
print(keys)
values= student_dict.values()
print(values)
print(student_dict.items())
del student_dict['address']
del dog





