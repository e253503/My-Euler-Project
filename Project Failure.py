#%%
import functools
from functools import reduce

from numpy.lib.function_base import insert, kaiser
from numpy.lib.twodim_base import tri
import numpy as np
from numpy.core.fromnumeric import transpose
from numpy.lib.shape_base import split
from pandas.core.frame import DataFrame
from pandas.core.series import Series
import scipy.stats as stats
import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns
import time

#%%


#%% Eu3 Fail
def ext():
    a = [1,2,3,4,5,6]
    for i in a:
        print('1')
    a[-2:]
def exteu4():
    p=[]
    for i in range(8462696833,600851475143):
        if 600851475143 % i == 0:
            p.append(i)
            print(i)
    print("ended")
    p[-1]
exteu4()
#%% Problem 4 Extension
abc =  1000
type(str(abc))
abcS = str(abc)
abcS.split()[-1][-1] == abcS.split()[-1][-2]
#
a = [1,2,5,4]
a.sort()
a[-1]

#%% Eu 5 Extension
# Unfinished other try/ cannot handle
x = range(1,21)
y = list(reversed(range(1,21)))
a = list()
for i in y:
    for j in x:
        if i > j:
            if i % j != 0:
                if j not in a:
                    print(i,j)
                    a.append(j)
print(a) 
x = range(1,21)
y = list(reversed(range(1,21)))

#%% Eu 5 Extension 2
a= range(1,3)
a1 = list(a)
a2 = list()
b= [1,2]
a1==b 

print(type(a2),type(b))
a2.append(4)
a2.append(5)
print(a2)
#%% Eu 7 Fail
def opf():
    optimus = []
    count= 0
    temp = [4]
    while len(temp) < 4:
        for i in temp:
            print('i',i)
            for j in range(1,i):
                print('j',j)
                if j != 1:
                    if i % j ==0:
                        if (i+1) not in temp:
                            temp.append(i+1)
                        count += 1
                        print('count',count)
                        if (i+1) not in temp:
                            temp.append(i+1)                    
                        break
            if (count == 0) and (i not in optimus):
                optimus.append(i)
                temp.append(i+1)
                break                        
            count=0
#%% Eu 7 Fail
opf()
print('temp',temp,'optimus',optimus)
#%% Eu 7 Fail
while count <= 10:
    temp = [3]
    for i in temp:
        print("i:",i)
        for j in range(2,i):
            print("i:",i,'j',j, count)
            if i % j ==0:
                count += 1
                print('i%j',i,j)
                break
            elif i not in optimus:
                count += 1
                optimus.append(i)
                print("append",i)
                break
            temp.append(i+1)
    break
    # create a list
    # measure each element of this list and control whether it is prime or not and add new element
    # when you fnish the list while will control the length
    # if lenght is not enough cycle will repeat

#%% Eu 7 failed
pr = list(range(2,100000))
prime = []
count = 0
while len(prime) < 10002:
    for i in pr:
        for j in pr:
            if i > j:
                if i % j ==0:
                    count +=1
                    break
            if count == 0:
                if i not in prime:
                    prime.append(i)
            count = 0
    print(i,j,prime)
    if len(prime) < 10002:
        break                               

print('length of prime',len(prime), "\nended", prime[-1])
# 7.1 Useless
def useless():
    pr = list(range(2,10))
    prime = []
    count = 0
    falsePrime = []
    for i in pr:
        for j in pr:
            if i > j:
                if i % j ==0:
                    print("bolunuyor",i,j)
                    count +=1
                    falsePrime.append(i)
                    break
                elif i % j != 0:
                    if i not in prime:
                        if i not in falsePrime:
                            prime.append(i)
                            print('i ekleniyor prime bolumune',i)
                print(i,j,count) 
                count = 0
    prime 
#%%
x = range(1,21)
l= list()
for i in x:
    for j in x:
        if i > j:
            if x[-i] % j == 0:
                if j not in l:
                    l.append(j)
                    print('x[-i]:',x[-i],'\n   j:',j,'\n     l:',l,)
#%%
x = range(1,21)
y = list(reversed(range(1,21)))
a = list()
for i in y:
    for j in x:
        if i > j:
            if i % j != 0:
                if j not in a:
                    print(i,j)
                    a.append(j)
print(a) 



#%%
# Eu 8
# convert string, split them, convert them int again
x = (7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)
def fail():
    y= str(x)
    l = list(y)
    q1 = l
    q2 = l[1:]
    q3 = l[2:]
    q4 = l[3:]
    q5 = l[4:]
    q6 = l[5:]
    q7 = l[6:]
    q8 = l[7:]
    q9 = l[8:]
    q10 = l[9:]
    q11 = l[10:]
    q12 = l[11:]
    q13 = l[12:]
    def list2list(k):
        # list for strings
        l2 = k
        # list for converted strings in the l2 list, to ints
        l3 = list() 
        for i in l2:
            j = int(i)
            l3.append(j)
        return l3
    qT = (q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13)
    for i in qT:
        list2list(i)
    # no2list(x)
    # type(no2list(x)[1]
    q11 = list2list(q1)
    q22 = list2list(q2)
    q33 = list2list(q3)
    q44 = list2list(q4)
    q55 = list2list(q5)
    q66 = list2list(q6)
    q77 = list2list(q7)
    q88 = list2list(q8)
    q99 = list2list(q9)
    q1010 = list2list(q10)
    q1111 = list2list(q11)
    q1212 = list2list(q12)
    q1313 = list2list(q13)

    qr =[q11,q22,q33,q44,q55,q66,q77,q88,q99,q1010,q1111,q1212,q1313]
    # print(q1,"\n",w1,"\n",e1,"\n",r1) 
    # to fix matrix problem, 0s need to be added.
    def fill(k,l):
        while len(k) > len(l):
            l.append(0)
    for i in qr[1:]:
        fill(q11,i)
    def notneed():
        fill(q11,q22)
        fill(q11,q33)
        fill(q11,q44)
        fill(q11,q55)
        fill(q11,q66)
        fill(q11,q77)
        fill(q11,q88)
        fill(q11,q99)
        fill(q11,q1010)
        fill(q11,q1111)
        fill(q11,q1212)
        fill(q11,q1313)

    # print(q1,"\n",w1,"\n",e1,"\n",r1) 
    type(q22[0])
    # result = q1 + w1
    def faile():
        q0p = (q1p , q2p , q3p , q4p , q5p , q6p , q7p , q8p , q9p , q10p , q11p , q12p , q13p )
        def list2series():
            for i,j in qr,q0p:
                p = pd.Series(i)
        list2series()
    
    def notneededSeries():
        global q0p, q1p , q2p , q3p , q4p , q5p , q6p , q7p , q8p , q9p , q10p , q11p , q12p , q13p
        q1p  = pd.Series(q11)
        q2p  = pd.Series(q22)
        q3p  = pd.Series(q33)
        q4p  = pd.Series(q44)
        q5p  = pd.Series(q55)
        q6p  = pd.Series(q66)
        q7p  = pd.Series(q77)
        q8p  = pd.Series(q88)
        q9p  = pd.Series(q99)
        q10p = pd.Series(q1010)
        q11p = pd.Series(q1111)
        q12p = pd.Series(q1212)
        q13p = pd.Series(q1313)
        q0p = (q1p , q2p , q3p , q4p , q5p , q6p , q7p , q8p , q9p , q10p , q11p , q12p , q13p )
        return (q0p, q1p,q2p)
    notneededSeries()

    pds = (q1p , q2p , q3p , q4p , q5p , q6p , q7p , q8p , q9p , q10p , q11p , q12p , q13p)
    pdsT= pd.DataFrame()
    for i in pds:
        pdsT = pdsT.append(i, ignore_index=True)
    type(q1p)
    type(pdsT.sum)

    # print('q1', type(q1[0]),q1, '\nq11:', type(q11[0]),q11,  '\nq1p:',q1p)
    print('\nq1p:',q1p)
    print(pdsT)
    print("colmun:\n", pdsT[0])


    def data(dataF):
        mulp = list()
        for i in range(0,1000):
            mul = 1
            for j in dataF[i]:
                mul *= j
                print(j)
            mulp.append(j)
        mulp = pd.Series(mulp)
        dataF = dataF.append(mulp,ignore_index=True)
        return 
        # data(pdsT)
    xlist = list()

    for j in range(0,1000):
        mul = 1
        c=0
        for i in pdsT[j]:
            mul *= i
            c += 1
            if c ==13:
                c=0
                break
        xlist.append(mul)
        # print("here it is",len(xlist))
    xlist = pd.Series(xlist)
    pdsT = pdsT.append(xlist,ignore_index=True)
    return pdsT
fail()
#fail()


#%%
offset = 10
for i in range(offset, 15 + offset):
    print(i)


#%%
# to insert & get mulp values of data
print("here:")
pL = pdsT.loc[13]
pL.sort_values(ascending=True, inplace=True)

pL2 = list()
for i in pL:
    i = int(i)
    pL2.append(i)
pL2[-1]
pdsT
#%%
a = list()
b = pd.Series()
### Tools I used:
# sorting list

#%%
lT = (q1p * q2p * q3p * q4p * q5p * q6p * q7p * q8p * q9p * q10p * q11p * q12p * q13p)
print(lT.sort_values(ascending=False), lT.sort_values(ascending=False)[0])

lTlist = (lT.sort_values(ascending=False).values.tolist())
print('itlist:\n',lTlist,'\nsum:\n',sum(lTlist[0:13]),'\n13.th:\n',lTlist[0])

# lTlist2 = list()
# for i in lTlist:
#    if i not in lTlist2:
#        lTlist2.append(i)

# print('itlist:\n',lTlist2,'\nsum:\n',sum(lTlist2[0:13]),'\n13.th:\n',lTlist2[14])

# sum(lT.sort_values(ascending = False)[0:5])

#%% Number to list function in int
def no2list(k):
    # k is int()
    # l is store for converted ints
    l = str(k)
    # list for strings
    l2 = list(l)
    # list for converted strings in the l2 list, to ints
    l3 = list() 
    for i in l2:
        j = int(i)
        l3.append(j)
    return l3

#%%
# Eu 8 Back-up to find 4 adjacent digits
# convert string, split them, convert them int again
x = (7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)
a = 123456789
y= str(x)
l = list(y)
q = l
w = l[1:]
e = l[2:]
r = l[3:]
def list2list(k):
    # list for strings
    l2 = k
    # list for converted strings in the l2 list, to ints
    l3 = list() 
    for i in l2:
        j = int(i)
        l3.append(j)
    return l3
# no2list(x)
# type(no2list(x)[1]
q1 = list2list(q)
w1 = list2list(w)
e1 = list2list(e)
r1 = list2list(r)
qr =[q1,w1,e1,r1]
# print(q1,"\n",w1,"\n",e1,"\n",r1) 
# to fix matrix problem, 0s need to be added.
def fill(k,l):
    while len(k) > len(l):
        l.append(0)
fill(q1,w1)
fill(q1,e1)
fill(q1,r1)
# print(q1,"\n",w1,"\n",e1,"\n",r1) 
type(w1[0])
# result = q1 + w1
q1p = pd.Series(q1)
w1p = pd.Series(w1)
e1p = pd.Series(e1)
r1p = pd.Series(r1)
lT = (q1p * w1p * e1p * r1p)
print(lT.sort_values(ascending=False), lT.sort_values(ascending=False)[0])

lTlist = (lT.sort_values(ascending=False).values.tolist())
print('itlist:\n',lTlist,'\nsum:\n',sum(lTlist[0:13]),'\n13.th:\n',lTlist[14])

# lTlist2 = list()
# for i in lTlist:
#    if i not in lTlist2:
#        lTlist2.append(i)

# print('itlist:\n',lTlist2,'\nsum:\n',sum(lTlist2[0:13]),'\n13.th:\n',lTlist2[14])

# sum(lT.sort_values(ascending = False)[0:5])

#%% useless
for (q,w,e,r) in (y,y[1:],y[2:],y[3:]):
    r = int(r)
    e = int(e)
    w = int(w)
    q = int(q)
    print("Last Section:\n","q",q,'r',r,'e',e,'r',r)
    l.append(q*w*e*r)
l
#%%
    x=0
    y=100
    z=str(654)[x:y]
    z
#%%
a = pd.Series()
b= [1,2,3,7,5.0,435.0,456,567]

# b = pd.Series(b)
b
#a.append(b)
c = list()
c.append(0)
c.append(1)
c
b.sort()
b[-1]
list(map(int,b)
#%%





#%% Eu 8 
# 13 adjacent numbers
import functools 

num = '73167176531330624919225119674426574742355349194934'
num += '96983520312774506326239578318016984801869478851843'
num += '85861560789112949495459501737958331952853208805511'
num += '12540698747158523863050715693290963295227443043557'
num += '66896648950445244523161731856403098711121722383113'
num += '62229893423380308135336276614282806444486645238749'
num += '30358907296290491560440772390713810515859307960866'
num += '70172427121883998797908792274921901699720888093776'
num += '65727333001053367881220235421809751254540594752243'
num += '52584907711670556013604839586446706324415722155397'
num += '53697817977846174064955149290862569321978468622482'
num += '83972241375657056057490261407972968652414535100474'
num += '82166370484403199890008895243450658541227588666881'
num += '16427171479924442928230863465674813919123162824586'
num += '17866458359124566529476545682848912883142607690042'
num += '24219022671055626321111109370544217506941658960408'
num += '07198403850962455444362981230987879927244284909188'
num += '84580156166097919133875499200524063689912560717606'
num += '05886116467109405077541002256983155200055935729725'
num += '71636269561882670428252483600823257530420752963450'
num = map(int, num)

a= list(num)
x = list()
for i in range(0,len(a)):
    t = functools.reduce(lambda x,y:x*y,a[i:i+13])
    x.append(t)
x.sort()
# print(x[-1]) 
# print(' sdf',len(a),type(a[4]))
x[-1]
#%%



#%%  Converting
# if you want strings to int list
# map it, list it
def str2int(x):
    x = map(int,x)
    x = list(x)
    return x
# if you want ints to strings
def int2str(x):
    x = str(x)
    x = map(str,x)
    x = list(x)
    return x

x = '1234'
# str2int(x)
# print(x, type(x))

x = 1234
# int2str(x)
# print(x, type(x))

def t2t(a,b):
    if b == 0:
        a = str2int(a)
        return a
    if b == 1:
        a = int2str(a)
        return a
# print(t2t(x,1))
t2t(x,1)
print(type(x),x)
print(type(list(map(str,str(x)))[-1]))

xy = int()
def add(xy):
    xy= int()
    xy += 5
    return xy
# add(xy)

#%%
x = 1234
x = str(x)
x.split()
x = list(map(str,x))
y = [1,2,3,4]
print(type(x[0]),type(y[0]))

#%%
limit = 10001
i = 3
count = 1
prime = 2
while count < limit:
    for x in range(3, int(i ** 0.5) + 1, 2):
        if i % x == 0:
            break
    else:  # no break
        prime = i
        count += 1
    i += 2
print(prime)
#%%
def thlPrime(k):
    t = [2]
    x = 0
    p = 3
    if k == 0:
        return t.remove(2)
    while x < k-1:
        b = range(2,int(p**1/2))
        c = 0
        for i in b:
            if p % i == 0:
                c += 1
        if c == 0:
            if p not in t:
                t.append(p)
        p += 1
        c = 0
        x += 1
    return t
# t gives result of numbers of prime numbers to +1 of given number
# print(len(thlPrime(5)))
x = 100002
c= 2
while len(thlPrime(c)) != (x-1):
    c += 2
print(len(thlPrime(c)), thlPrime(c)) 
# 

#%%
x3 = list()
c= 0
cm = str()
for i in x2:
    cm += str(i)
    c += 1
    # print(cm)
    if c == 2:
        x3.append(int(cm))
        c=0
        cm=str()
#        break
print(x3)
#%%
xT = pd.DataFrame()
c = 0
for i in x4:
    xT = xT.insert(c,pd.Series(i), i)
    c += 1
    # print(pd.Series(i))
print(xT) 

#%%
a= [1,2,3,4,5,6,7]
a[0:1]
for i in range(2,9),a:
    print(i) 
a[11]

#%% EU 12 Fail 2
k = int()

# xLDs = list()
def findTriangleLists():
    for i in xL:
        for j in range(1,int(i)+1):
            if i % j ==0:
                xLDs.append(j)
            
        xLDS.append(xLDs)
        xLDs = list()
    print(xL,'\n',xLDS)

def ftl2():
    for i in xL:
        for j in range(1,int(i)+1):
            if i % j ==0:
                xLDs.append(j)
        if (len(xLDs)-1) ==500 :
            print(xLDs[-1])
            break
        #xLDS.append(xLDs)
        xLDs = list()
    # print(xL,'\n',xLDS)
def desperate():   
    for i in xL:
        i = int(i)
        print(divCount(i))
        if divCount(i) == 501:
            print('this:',i)
            break 

def divCount(n):   
    # sieve method for 
    # prime calculation 
    hh = [1] * (n + 1); 
      
    p = 2; 
    while((p * p) < n): 
        if (hh[p] == 1): 
            for i in range((p * 2), n, p): 
                hh[i] = 0; 
        p += 1; 
  
    # Traversing through  
    # all prime numbers 
    total = 1; 
    for p in range(2, n + 1): 
        if (hh[p] == 1): 
  
            # calculate number of divisor 
            # with formula total div =  
            # (p1+1) * (p2+1) *.....* (pn+1) 
            # where n = (a1^p1)*(a2^p2)....  
            # *(an^pn) ai being prime divisor 
            # for n and pi are their respective  
            # power in factorization 
            count = 0; 
            if (n % p == 0): 
                while (n % p == 0): 
                    n = int(n / p); 
                    count += 1; 
                total *= (count + 1); 
                  
    return total; 

def divcCc(x):
    y=list()
    for i in range(1,int(x/2)+1):
        if x % i == 0:
            y.append(i)
    return (len(y)+1)

def tri(x,y):
    xL=list()
    for i in range(x,y):
        k = (i * (i+1))/2
        xL.append(k)
    return xL
x = 1
y = 5 # number of ..th triplet +1; if you want 4th triplet, give me 5
tri(x,y)
def findDiv(k):
    start_time = time.time()
    x = 1
    y = 2
    a = int()
    while (a != k):
        abc = tri(x,y)
        for i in abc:
            l = divcCc(int(i))
            if  l == k:
                a = l
                print(i,a)
                print("--- %s seconds ---" % (time.time() - start_time))
                break
        print(abc[-1],l)
        x = y
        y *= 2
        if a == k:
            break
findDiv(6)
# divcCc(28)
# take number from triangles
# check whether it`s dicount
# if divcount is not correct, increase range
#%% Eu 12 Fail
def divcCc(x):
    y=list()
    for i in range(1,int(x/2)+1):
        if x % i == 0:
            y.append(i)
    return (len(y)+1)

def tri(x,y):
    xL=list()
    for i in range(x,y):
        k = (i * (i+1))/2
        xL.append(k)
    return xL
def durcan(x):
    start_time = time.time()
    a = 1
    b = 30
    while True:
        for i in range(a,b):
            if divcCc(i) == x:
                if i in tri(1,i):
                    print(i)
                    print("--- %s seconds ---" % (time.time() - start_time))
                    return (i,i)
        a = int(b/2)
        b += 1
durcan(501)

#%% Eu 12 Fail 3
# Highly divisible triangular number
from tqdm import tqdm
#%%

def divisor(n):
    nL=[n]
    for i in tqdm(range(1,int((n/2))+1)):
        if n % i == 0:
            nL.append(i)
    return len(nL)

def tridiv(i):
    a = 1
    b = 0
    while True:
        if b < a:
            b = a
        a += 1
        b = a + b
        if divisor(b) == i:
            print('\n', f'Number of Divisor: {i}','\n','Number:', b)
            break
tridiv(20)

# Fail 4

# They  give sum of points up to x
m = {}
def seq(x):
    start_time = time.time()

    if x not in m:
        if x == 1:  
            m[x] = 1
        else:
            m[x] = seq(x-1)[0] + 1
    return sum(m),("--- %s seconds ---" % (time.time() - start_time))
#seq(1)

def triangleNumber(n):
    start_time = time.time()
    return sum ( [ i for i in range(1, n + 1) ] ),("--- %s seconds ---" % (time.time() - start_time))
seq(500),triangleNumber(500)
# Fail 5

# It gives, Up to a point-last- highest divison one. 
def first(Last):
    x = 1
    y = Last
    for i in tqdm(range(1,Last)):
        a = divN(seq(i))
        if a > x:
            x = a
            y = seq(i)
    return x,y
first(4)
# Fail
def fd(l):
    a= 2
    while True:
        if divN(seq(a)) == l:
            return a+1
        else:
            a += 1
fd(5)

# Fail 6
# In progress. There was some code I made but it worked so slow, I will remake it. 

# They  give sum of points up to x
m = {}
def seq(x):
    start_time = time.time()

    if x not in m:
        if x == 1:  
            m[x] = 1
        else:
            m[x] = seq(x-1)[0] + 1
    return sum(m),("--- %s seconds ---" % (time.time() - start_time))
#seq(1)

def triangleNumber(n):
    start_time = time.time()
    return sum ( [ i for i in range(1, n + 1) ] ),("--- %s seconds ---" % (time.time() - start_time))
seq(500),triangleNumber(500)
# Fail 7

def sd(l): 
    global m 
    a = 1
    while True:
        a1 = seq(a)
        a2 = divN(a1)[0]
        if l == a2:
            return a1,a 
        a +=1
        m = {}
        if a2 > l:
            l += 1
            a = 1
            m = {}
sd(5)

#%%
