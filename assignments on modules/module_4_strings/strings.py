words= 'Thirty','Days','Of','Python'
concat_words= ' '.join(words)
print(concat_words)
cil= 'Coding','For','All'
concat_cil= ' '.join(cil)
company= 'Coding For All'
print(company)
print(len(company))
upp_company= company.upper()
print(upp_company)
low_company= company.lower()
print('Coding For All'.capitalize())
print('Coding For All'.title())
print('Coding For All'.swapcase())
ca= 'Coding For All'
print(ca[1:])
print(company.index('Coding'))
print(company.replace('Coding','Python'))
xt= 'Python For All'
print(xt.replace('For','for'))
print(xt.replace('All','Everyone'))
print(ca.split(' '))
top= 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(top.split(', '))
print(ca[0])
print(ca[-1])
print(ca[10])
PYE= 'Python For Everyone'
CFA= 'Coding For All'
print(CFA.find('C'))
print(CFA.find('F'))
CFAP= 'Coding For All People'
print(CFAP.rfind('l'))
sent1= 'You cannot end a sentence with because because because is a conjunction'
print(sent1.find('because'))
print(sent1.rfind('because'))
print(sent1[31:54])
print(sent1.find('because'))
print(sent1[31:54])
print(CFA.startswith('Coding'))
print(CFA.endswith('coding'))
s_CFA= ' Coding For All '
print(s_CFA)
print(s_CFA.strip(' '))
DOP= '30DaysOfPython'
DOP_1= 'thirty_days_of_python'
print(DOP.isidentifier())
print(DOP_1.isidentifier())
py_lib= ['Django','Flask','Bottle','Pyramid','Falcon']
res=' '.join(py_lib)
print(res)
print('I am enjoying this challenge.\nI just wonder what is next')
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')
radius=10
area=3.14* radius**2
format_string='The area of a circle with radius %d is %.2f meters square'%(radius,area)
print(format_string)
a=8
b=6
print('{} + {} = {}'.format(a,b,a+b))
print('{} - {} = {}'.format(a,b,a-b))
print('{} * {} = {}'.format(a,b,a*b))
print('{} / {} = {:.2f}'.format(a,b,a/b))
print('{} % {} = {}'.format(a,b,a%b))
print('{} // {} = {}'.format(a,b,a//b))
print('{} ** {} = {}'.format(a,b,a**b))