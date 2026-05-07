# Albin Sannchez
from datetime import*
x = datetime.now()
print('Program started at:', x)
def main():
    inputfile='c:/temp/points.txt'
    rcdcnt = 0
    gradecnt = 0
    errorcnt = 0
    cntA = 0
    cntB = 0
    cntC = 0
    cntD = 0
    cntF = 0
    infile = open(inputfile, 'r')
    line = infile.readline()
    fileout = 'c:/temp/grades.txt'
    outfile = open(fileout, 'w')
    fileout2 = 'c:/temp/error.txt'
    outfile2 = open(fileout2,'w')
    while (line != ""):
        rcdcnt = rcdcnt + 1
        (idnum,name,points) = line.split(',')
        points = points.strip()
        try:
            fpoints = float(points)
            grade = (fpoints/1000)*100
            if fpoints <0:
                error = 'Points cannot be negative'
                errorRec = idnum + ',' + name + ',' + points + ',' + error + '\n'
                outfile2.write(errorRec)
                errorcnt = errorcnt + 1
            elif fpoints >1000:
                error = 'Points must be between 0 & 1000'
                errorRec = idnum + ',' + name + ',' + points + ',' + error + '\n'
                outfile2.write(errorRec)
                errorcnt = errorcnt + 1
            else:
                if (grade >= 90):
                    letterg = 'A'
                    cntA = cntA + 1
                elif (grade >= 80):
                    letterg = 'B'
                    cntB = cntB + 1
                elif (grade >= 70):
                    letterg = 'C'
                    cntC = cntC + 1
                elif (grade >= 60):
                    letterg = 'D'
                    cntD = cntD + 1
                else:
                    letterg = 'F'
                    cntF = cntF + 1
                graderec = idnum + ',' + name + ',' + points + ',' + letterg + '\n'
                outfile.write(graderec)
                gradecnt = gradecnt + 1
        except ValueError:
            error = 'Points must be numeric'
            errorRec = idnum + ',' + name + ',' + points + ',' + error + '\n'
            outfile2.write(errorRec)
            errorcnt = errorcnt + 1
        except:
            print('Error')
        line = infile.readline()
    infile.close()
    outfile.close()
    outfile2.close()
    print('Number or records read:',rcdcnt)
    print("Number of A's:", cntA)
    print("Number of B's:", cntB)
    print("Number of C's:", cntC)
    print("Number of D's:", cntD)
    print("Number of F's:", cntF)
    print('Number of graded records:', gradecnt)
    print('Number of error records:', errorcnt)
    y = datetime.now()
    print('Program ended at:', y)
main() 
