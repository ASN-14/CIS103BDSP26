# Albin Sanchez
# property tax program calculator 2
def getinput(msg):
    xin = float(input(msg))
    return xin

def main():
    AssessmentLevel = 0.10
    HomeOwnerEx = 500.43
    SeniorCEX = 357.45
    PropertyValue = getinput('Enter value of property: ')
    StateEqualizer = getinput('Enter state equalizer rate: ')
    LocalTaxRate = getinput('Enter loacal tax rate: ')
    print('\n'*1)
    AssessedValue = PropertyValue * AssessmentLevel
    EqualizeValue = AssessedValue * StateEqualizer
    PropertyTaxBefore = EqualizeValue * (LocalTaxRate / 100)
    TotalPropertyTax = PropertyTaxBefore - HomeOwnerEx - SeniorCEX
    print('\n'*1)
    print('Property tax due: ',TotalPropertyTax)
    return
main()
