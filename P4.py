# Albin Sanchez
firstn=input('Enter first name: ')
if firstn.isspace()or len(firstn)==0:
    print('Name cannot be blank')
elif len(firstn)<3:
    print('Name to short')
elif firstn.isnumeric():
    print('Name must be alphabetic')
else:
    print('Name:',firstn,'valid')
anum=input('Enter account number: ')
anumlen=len(anum)
if anum.isspace()or len(anum)==0:
    print('Account number cannot be blank')
elif anum.isalpha():
    print('Account number must be numeric')
elif(anumlen!=9):
    print('Account number must be 9 digits')
else:
    print('Account Number:',anum,'valid')
pyamt=input('Enter payment acount: ')
pyamtlen=len(pyamt)
if pyamt.isspace()or(pyamtlen==0):
    print('Pyamt cannot be blank')
elif float(pyamt)<0:
    print('Payment cannot be negative')
elif float(pyamt)<=0:
    print('Payment cannot be zero')
else:
    print('Payment:',pyamt,'valid')
