# Albin Sanchez
print('Calorie Table Program')
print('\n'*1)
ans = 'y'
while ((ans == 'y') or (ans == 'Y')):
    mins = input('Enter running minutes: ')
    if mins.isspace() or len(mins)==0:
        print('Minutes cannot be blank')
    elif float(mins)<= 4:
        print('Minutes must be greater than 5')
    else:
        x = 0
        a = int(mins) - 5
        while(x <= a):
            x = x + 5
            bcal = 4.33 * x
            print('Minutes:',x,'Calories:',bcal)
    ans = input('Run again y/n:')
    print('---------------')
print('- done -')
