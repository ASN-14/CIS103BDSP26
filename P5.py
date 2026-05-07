# Albin Sanchez
print('---Program Start')
print('Table codes: a=add. s=substract, m=multiple, d=divide')
seltab=input('Select table code: ')
x=float(input('Enter number: '))
if (seltab=='a') or (seltab=='A'):
    print('add')
    for b in range(1,11,1):
        y = x + b
        print(x,'+',b,'=',y)
elif (seltab=='s') or (seltab=='S'):
    print('substract')
    for c in range(1,11,1):
        y = x - c
        print(x,'-',c,'=',y)
elif (seltab=='m') or (seltab=='M'):
    print('multiple')
    for e in range(1,11,1):
        y = x * e
        print(x,'*',e,'=',y)
elif (seltab=='d') or (seltab=='D'):
        print('divide')
        for f in range(1,11,1):
            y = x / f
            print(x,'/',f,'=',y)
else:
    print('select a table code')
print('--done')
