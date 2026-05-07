# Albin Sanchez
def calc(n):
    if n==1:
        return n
    else:
        return n + calc(n-1)

def main():
    print('-- Sum of given number--')
    ans = 'y'
    while (ans.lower() == 'y'):
        num = input('Enter a number: ')
        if (num == "") or num.isspace():
            print('Input cannot be blank')
        else:
            try:
                inum = int(num)
                if (inum <=0):
                    print('Input cannot be negative')
                else:
                    total = calc(inum)
                    print('The sum:',total)
            except ValueError:
                print('Input must be a number and integer')
            except:
                print('Error')
        ans = input('Run again y/n: ')
    print('--done--')

main()
    
