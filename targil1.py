
#question 1
def getPentaNum(n):
    if n is not int or n<1: 
        return "ERROR"
    return (n*(3*n-1))/2

def pentaNumRange(n1,n2):
    return [getPentaNum(n) for n in range(n1,n2)]

#question 2
def sumDigit(n):
    if n is not int: 
        return "ERROR"
    l=list()
    while(n!=0):
        l.append(n%10)
        n/=10
    return sum(l)

#question 3
gematria = {
    'א':1,
    'ב':2,
    'ג':3,
    'ד':4,
    'ה':5,
    'ו':6,
    'ז':7,
    'ח':8,
    'ט':9,
    'י':10,
    'כ':20,
    'ל':30,
    'מ':40,
    'נ':50,
    'ס':60,
    'ע':70,
    'פ':80,
    'צ':90,
    'ק':100,
    'ר':200,
    'ש':300,
    'ת':400,
}
def getGematria(str):
    num=0
    for s in str:
        num+=gematria[s]
    return num

#question 4
def checkPrime(n1):
    if n1%2==0 :
        return False
    for i in range(3,n1/2,2):
        if n1%i==0:
            return False
    return True

def returnTwin(n):
    if checkPrime(n+2):
        return n+2
    elif checkPrime(n-2):
        return n-2
    
def returnDict(n):
    d=dict()
    for num in range(n):
        if(checkPrime(num) and returnTwin(num)is not None):
            d[num]=returnTwin(num)
    return d

#question 5

def add3dicts(d1,d2,d3):
    d=dict()
    for k1 in d1.keys:
        d[k1]=d1[k1]
    for k2 in d2.keys:
        if k2 in d.keys:
            d[k2]=tuple(d1[k2],d2[k2])
        else:
            d[k2]=d2[k2]
    for k3 in d3.keys:
        if k3 in d.keys:
            d[k3]=tuple(d1[k3],d2[k3],d3[k3])
        else:
            d[k3]=d3[k3]
    return d

#question 6