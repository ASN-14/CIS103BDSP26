# Albin Sanchez
def main():
    rainflist = []
    inputfile = 'c:/temp/rainfall2017.txt'
    infile = open(inputfile, 'r')
    line = infile.readline()
    while (line != ""):
        data = line.strp()
        line = infile.readline()
        if (data==""):
            print('Amount cannot be blank')
        else:
            try:
                fdata = float(data)
                if (fdata <0):
                    print('Amount cannot be negative')
                else:
                    rainflist.append(fdata)
            except ValueError:
                print('Amount has to be a number')
            except:
                print('Error with amount')
    infile.close()
    if (len(rainflist)> 0):
        avg = sum(rainflist)/len(rainflist)
        print('Data list:', rainflist)
        print('Highest:', max(rainflist))
        print('Lowest:', min(rainflist))
        print('Total:', sum(rainflist))
        print('Average:', avg)
    else:
        print('Error with data')
main()
