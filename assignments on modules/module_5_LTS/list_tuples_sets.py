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