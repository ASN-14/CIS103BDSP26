# Albin Sanchez
#property tax calculator 1
def part1():
    nheac = 0.004
    mwrdc = 0.406
    pmab = 0.006
    cpd = 0.362
    MiscTx = nheac + mwrdc + pmab + cpd
    return MiscTx
def part2():
    bec = 3.726
    cccd = 0.169
    Schooltax = bec + cccd
    return Schooltax
def part3():
    csbif = 0.128
    clf = 0.122
    city = 1.630
    Citytx = csbif + clf + city
    return Citytx
def part4():
    ccfpd = 0.063
    cook = 0.316
    ccps = 0.130
    cchf = 0.087
    CookCtyTx = ccfpd + cook + ccps + cchf
    return CookCtyTx
def main():
    mt = part1()
    st = part2()
    ct = part3()
    cc = part4()
    TotalTaxRate = mt + st + ct + cc
    print('Property Tax Rate is:', TotalTaxRate)
main()
