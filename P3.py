# Albin Sanchez
npounds=input('Number of pounds: ')
price=0.99
gsales=float(npounds)*float(price)
if float(npounds)>=1 and float(npounds)<=9:
    print('Gross sales:',gsales)
    print('Discount: 0')
    famt=gsales-0
    print('FInal Amount:',famt)
elif float(npounds)>=10 and float(npounds)<=99.99:
    print('Gross sales:',gsales)
    damt1=gsales*0.10
    print('Discount:',damt1)
    famt1=gsales-damt1
    print('Final Amount:',famt1)
elif float(npounds)>=100 and float(npounds)<=999.99:
    print('Gross sales:',gsales)
    damt2=gsales*0.20
    print('Discount:',damt2)
    famt2=gsales-damt2
    print('Final Amount:',famt2)
elif float(npounds)>=1000 and float(npounds)<=9999.99:
    print('Gross sales:',gsales)
    damt3=gsales*0.30
    print('Discount:',damt3)
    famt3=gsales-damt3
    print('Final Amount:',famt3)
elif float(npounds)>=10000:
    print('Gross sales:',gsales)
    damt4=gsales*0.40
    print('Discount:',damt4)
    famt4=gsales-damt4
    print('Final Amount:',famt4)
else:
    ('Error')
