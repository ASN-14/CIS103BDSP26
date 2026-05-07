# Albin Sanchez
print('Conversion Program')
print('\n'*1)
def ath():
    try:
        A = float(input('Enter Acres: ' ))
        if A < 0:
            print('Input error -> acres cannot be negative')
        else:
            H = A * 0.4047
            print(A, 'converts to', H,'Hectares')
    except:
        print('input error -> acres')
    print('-'*16)
def qt1():
    try:
        Q = float(input('Enter Quarts: '))
        if Q < 0:
            print('input error -> quarts cannot be negative')
        else:
            L = Q * 0.946353
            print(Q, 'converts to', L,'Liters')
    except:
        print('input error -> quarts')
    print('-'*16)
def ftk():
    try:
        F = float(input('Enter Farenheit: '))
        K = (F - 32) * 5/9 + 273.15
        print(F, 'converts to', K,'Kelvin')
    except:
        print('input error -> farenheit')
def main():
    ragain = 'y'
    while ((ragain == 'y') or (ragain == 'Y')):
        ath()
        qt1()
        ftk()
        ragain = input('run again y/n: ')
        print('-'*16)
    print('-done-')
    return
main()
