from fractions import Fraction
def toPartial(A):
    l = Fraction(1,A[-1])
    i = len(A)-2
    while (i >= 0):
        temp = Fraction(A[i],1)
        l = Fraction(1,sum((temp,l)))
        i -= 1
    return Fraction(1,l)

def add(a,b):
    return sum((a,b))

def minus(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def convert(a):
    l = []
    while (a.denominator != 1):
        l.append(a.numerator/a.denominator)
        a = Fraction(a.denominator,a.numerator%a.denominator)
        l.append(a.numerator)
    return l

def out(l):
    for ch in l:
        print(ch)

def main():
    ans = []
    while(True):
        n,m = map(int,raw_input().split(' '))
        if (n == 0 and m == 0):
            break
        a = map(int,raw_input().split(' '))
        b = map(int,raw_input().split(' '))
        ans.append((a,b))
        i = 1
        for ch in ans:
            trans_a = toPartial(ch[0])
            trans_b = toPartial(ch[1])
            out(convert(add(trans_a,trans_b)))
            out(convert(minus(trans_a,trans_b)))
            out(convert(mul(trans_a,trans_b)))
            out(convert(div(trans_a,trans_b)))

main()