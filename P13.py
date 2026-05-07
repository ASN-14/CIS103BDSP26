# Albin Sancehz
def main():
    dt01= {1:'I',
           2:'II',
           3:'III',
           4:'IV',
           5:'V',
           6:'VI',
           7:'VII',
           8:'VIII',
           9:'IX',
           10:'X',
           11:'XI',
           12:'XII',
           13:'XIII',
           14:'XIV',
           15:'XV',
           16:'XVI',
           17:'XVII',
           18:'XVIII',
           19:'XIX',
           20:'XX',
           21:'XXI',
           22:'XXII',
           23:'XXIII',
           24:'XXIV'}
    ans ='y'
    while ((ans == 'y') or (ans == 'Y')):
        afn = input('Enter a number: ')
        if (afn == "") or afn.isspace():
            print('Number cannot be blank')
        else:
            try:
                iafn = int(afn)
                if (iafn <=0):
                    print('Input cannot be negative or zero')
                    break
                else:
                    if iafn in dt01:
                        print('Roman numeral:', dt01[iafn])
                    else:
                        atd = input('Add to dictionary? y/n: ')
                        if (atd == 'y') or (atd =='Y'):
                            ern = input('Enter Roman numeral: ')
                            if ern.isalpha():
                                dt01[iafn]= ern.upper()
                            else:
                                print('Roman numeral must be alphabetic')
                        else:
                            print('Not added to dictionary')
            except ValueError:
                print('Input must be a number (integer)')
            except:
                print('Error')
        ans = input('Run again y/n: ')
    print('Dictionary:',dt01)
main()
