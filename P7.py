# Albin Sanchez
def mtk():
    m = float(input('Number of miles: '))
    k = m * 1.609344
    print('kilometers:', k)
    print('- '*15)
    return 

def ftc():
    f = float(input('Temperature in Farenheit: '))
    c =(f - 32)* 5/9
    print('Celsius:', c)
    print('- '*15)
    return 

def ptkg():
    lb = float(input('Weight: '))
    kg = lb * 0.45359237
    print('Kilograms:',kg)
    return 

def main():
    mtk()
    ftc()
    ptkg()   
main()    
