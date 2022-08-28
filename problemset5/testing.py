import string
shift = 3
dictLower = {}
dictUpper = {}
lc = string.ascii_lowercase
uc = string.ascii_uppercase
lclong = lc + lc
uclong = uc + uc
for i in range(len(lc)):
    dictLower[lc[i]] = lclong[i+shift]
    dictUpper[uc[i]] = uclong[i+shift]

dict = {}
dict.update(dictLower)
dict.update(dictUpper)


