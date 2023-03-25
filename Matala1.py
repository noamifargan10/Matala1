#Q1

def my_func(x1,x2,x3):
    denominator = x1 + x2 + x3
    numerator = denominator * (x2+x3) * x3
    if denominator == 0:
        print("Not a number – denominator equals zero")
    elif type(x1) == int or type(x2) == int or type(x3) == int:
        print("Error: parameters should be float")
    elif type(x1) != float or type(x2) != float or type(x3) != float:
        print("None")
    else:
        result = float(numerator/denominator)
        return result
print(my_func())

#Q2
def revword(stringw):
    stringt = stringw.lower()[::-1]
    return stringt

def countword():
    counter = 1
    file = open("text.txt")
    for line in file:
        listofwords = line.split()
        if len(listofwords) == 1:
            theword = listofwords[0].rstrip().lower()
        else:
            for i in listofwords:
                word = revword(i).rstrip()
                if word == theword:
                    counter = counter + 1
    print(counter)
countword()





