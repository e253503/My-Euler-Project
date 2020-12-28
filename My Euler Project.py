#%%
# Author: Orcun Sami Tandogan
# Personal Euler Trials.
# Codings have been made without looking to other people works and forcing myself into deal by myself. 
# In this reason, I spent a lot of time and there is also Euler Fail Project in where I analyze my mistakes to no repeat myself.
#%%
from os import remove
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns
import math
from tqdm import tqdm
from math import *
import time
#%% Eu 1
# Multiples of 3 and 5
x=[]
xsum = 0
for i in tqdm(range(1,1000)):
    if (i % 3 == 0) or (i % 5 == 0):
        x.append(i)
        xsum += i
x
xsum
#%% Eu 2
# Even Fibonacci numbers
f = [1,2]
for i in f:
    f.append(f[-1]+f[-2])
    if f[-1] > 4000000:
        print(f)
        break
fsum=0
for i in f:
    if i % 2 == 0:
        fsum += i 
fsum


# %% Eu3 
# Finding Prime Numbers of Any Number
p  = [1]
p2 = []
count=0
def findPrimes(x):
    for i in tqdm(range(2,int(x**(1/2)))):
       if x % i == 0:
           p.append(i)
    # print(p)
    for i in p:
        for j in p:
            # print(i,j)
            if i > j:                
                if i % j ==0:
                    if j not in p2:
                        p2.append(j)
findPrime(600851475143)
print(p2[-1])

#1 Firstly, calculate all divisors of the target value and take them into a list
#2 Then, compare them w each other; according to diviility to each other,
#3 take the ones which divide the bigger ones
#4 send these ones to new list by checking they exist in this new list already

#%% Eu 4
# Largest palindrome product
ns= range(800,999)
p = []
for i in ns:
    for j in ns:
        ij = i * j
        ijs = str(ij)
        if ijs.split()[-1][-1] == ijs.split()[-1][0]:
            if ijs.split()[-1][-2] == ijs.split()[-1][1]:
                if ijs.split()[-1][-3] == ijs.split()[-1][2]:
                    p.append(ijs)
p.sort()
p[-1]

#%% Eu 5
x = range(1,21)
x1 = list(x)
y= list()
for i in tqdm(range(2519,1000000000)):
    for j in x:
        if i % j ==0:
            y.append(j)
            # print(i,j,y)
    if x1 != y:
            y = [] 
    elif x1 == y:
        break 
if i != range(2519,100000000)[-1]:
    print(i)
print("ended") 

#%% Eu 6
# Sum square difference
x = range(1,101)
xsum = int()
for i in x:
    xsum += i**2
xssum = int()
for i in x:
    xssum += i 
xSsum = xssum ** 2
abs(xsum - xSsum)


#%% Eu 7 
# 10001st prime
# Finding ...th Prime Number
# It also gives list of prime number up to your point
def thlPrime(k):
    t = [2]
    x = 0
    p = 3
    if k == 0:
        return t.remove(2)
    while x < k-1:
        b = tqdm(range(2,int(p**1/2)))
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
# print(thlPrime(12),'\n',list(range(1,14)))

# we take prime numbers list from thPrime
# then assign temp as 1
# 
def thPrime(y):
    temp= 1
    thP = thlPrime(temp)
    while len(thP) < y+2:
        if len(thP) == y+1:
            return print(thP,thP[-1])
        temp += 1
        thP = thlPrime(temp)
thPrime(6) 
# You can change the number, but higher number results need more time
#%% Eu 8 
# Largest product in a series in condition of 13 adjacent numbers
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

#%% EU 9 
# Pythagorean Triplet
x = 1000
y= range(1,x)
while True:
    for i in y:
        for j in y[1:]:
            if i < j:
                for z in y[2:]:
                    if j < z:
                        if i**2 + j**2 == z**2:
                            if i + j + z == 1000:
                                print(i,j,z)
                                print(i*j*z)
    break

#%% Ee 10
# Summation of primes
k = range(1,2000000)
psum = 2
for x in k:
    c= 0
    if x % 2 !=0 and x !=1: 
        for i in range(3,int(x**1/2),2):
            if x % i == 0:
                # print("it`s not prime\n",x)
                c +=1
                break
        if c == 0:
            # print('it`s prime:\n',x)
            psum += x
            print(psum)
        c= 0
psum 

#%% EU 11
# Largest product in a grid
numbers = '''08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'''
numbers
# create 4x4 matrixs but first combine two of them each
x=list()
a=int()
for i in numbers.strip():
    if i == '\n':
        None
    else: 
        x.append(i)
x2= list()
for i in x:
    if i == ' ':
        None
    else:
        x2.append(i)
# print(x2)

# Now we are having total 20 x 20 numbers
# Now we can create matrixs dfgdfgf
# for i in range(1,17):

x4 = list()
for i in range(0,380,20):
    x4.append(x3[i:i+20])
# print(x4)
x3T = list()
x4T = list()
for i in x4:
    for j in range(0,16):
        x = i[j:j+4]
        y = 1
        c = 0
        x4T.append(x)
        for k in x:
            y *= k 
            c += 1
        x3T.append(y)
        c=0
# x4T.sort()
x4T[-1]
print(x4)

x5 = list()
x6=list()
for i in range(0,400-60):
    x5.append(x3[i])
    x5.append(x3[i+20]) 
    x5.append(x3[i+40])
    x5.append(x3[i+60])
    x6.append(x5)
    x5=list()
print(x5,'abc\n\n\n\n',x6)
x6T = list()
for i in x6:
    y = 1
    for j in i:
        y *= j
    x6T.append(y)
        
# print(len(x3),len(x6T),len(x4T))
# x6T.sort()
x6T[-1]
print(x3)


x7 = list()
x8=list()
for i in range(0,400-63):
    x7.append(x3[i])
    x7.append(x3[i+21]) 
    x7.append(x3[i+42])
    x7.append(x3[i+63])
    x8.append(x7)
    x7=list()


x8T = list()
for i in x8:
    y = 1
    for j in i:
        y *= j
    x8T.append(y)
x8T.sort()
x8T[-1]



x9 = list()
x10=list()
for i in range(0,400-63):
    x9.append(x3[i+3])
    x9.append(x3[i+22]) 
    x9.append(x3[i+41])
    x9.append(x3[i+60])
    x10.append(x9)
    x9=list()


x10T = list()
for i in x10:
    y = 1
    for j in i:
        y *= j
    x10T.append(y)
x10T.sort()
x10T[-1]

print('x4:\n',x4,'\nx4T:\n',x4T,'\nx3T\n',x3T)
# x4T: 4 adjcanet in horizons
# x3T multipication of x4T horizons
print('x7:', x7,'abc\n\n\n\n','x8:\n', x8)
# x8 diagonel of numbers; from left up to right bottom
print('x5:\n', x5,'abc\n\n\n\n','x6:\n', x6)
# x6 vertical of 4 adjcanet numbers
print(len(x3),len(x6T),len(x8T),len(x4T),x4T[-1])   
print('x9:\n',x9,'\nx10:\n',x10)     
x10T.sort()
x10T[-1]



#%% Eu 12
# Highly divisible triangular number
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

# Gives numbers of divisors of x
def divN(x):
    start_time = time.time()
    c = 0
    for i in range(1,(int((x)**(1/2))+1)):
        if x % i == 0:
            c += 1
    return c*2,("--- %s seconds ---" % (time.time() - start_time))
divN(6)

def sd(x):
    a = 1
    while True:
        a1 = seq(a)[0]
        a2 = divN(a1)[0]
        if a2 == x:
            return ('divisor number: ', a2,'Our Tri Number: ',a1)
        elif a2 > x:
            x += 1
            a = 1
        a += 1
sd(500)


#%% Eu 13 
# Large sum
a = '''37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690'''
type(numbers)
# a = '12345\n67890\n12345'
lena = len('86188088225875314529584099251203829009407770775672')
b= list()
c= list()
x=0
for i in a:
    if i != '\n':
        #print(i)
        x += 1
        b.append(i)
        if x == lena:
            c.append(b)
            x=0
            b = list()
print(c)
x= 0
d=list()
for i in c:
    k=str()
    for j in i:
        x += 1
        k += j
        if len(k)==lena:
            d.append(k)
d 
e=list()
for i in d:
    e.append(int(i))
e
sT=int()
for i in e:
    sT += i
sT
str(sT)
k=str()
for i in str(sT)[0:10]:
    k += i
print(d,e,sT,k)

#%% Eu 14
# Longest Collatz sequence
m = {}                               
def cs(n):
    if n not in m:                   
        if n == 1:                     
            m[n] = 1                 
        elif n % 2 == 0:
            m[n] = cs(int(n / 2)) + 1
        else:
            m[n] = cs(3 * n + 1) + 1
    return m[n]                     
cs(13)
x = {}
for i in tqdm(range(13,10**6)):
    x[i] = cs(i)
x.values
xd = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
xdv = list(xd.values())[-1]
def get_key(val):
    for key, value in xd.items():
         if val == value:
             return key
print('\nNumber: ', xdv, 'Length of Chain: ', get_key(xdv))

#%%
import time
start = time.time()

def collatzSeq (n):
    chainNumber = 1
    n1 = n
    while n1 != 1:
        if n1 % 2 == 0:
            n1 = n1/2
            chainNumber += 1
        else:
            n1 = (3*n1) + 1
            chainNumber += 1
    return [chainNumber, n]

fullList = []
for i in range(2, 1000000):
    fullList.append(collatzSeq(i))
sortedList = sorted(fullList, reverse=True)
print(sortedList[:1])

# %% Eu 15
# Lattice paths
def findingWays(a1,b1,c1):
    x = 0
    y = 0
    e=list()
    v = 0
    while x !=2 or y != -2:
        a = [0,1]
        c= 0
        d= list()
        for j in range(0,4):
            i = random.choice(a)
            if i == 0:
                x += 1
                c += 1
                cx = 'right'
                d.append(cx)
            elif i == 1:
                y -= 1
                c += 1
                cy = 'down'
                d.append(cy)
        if x == 2 and y == (-2) and d not in e:
            e.append(d)
            v += 1
        if v == (math.factorial(a1) / (math.factorial(b1) * math.factorial(c1)) ):  # in how many times it is possible
            print(x,y,e) 
            break
        if c == 4:
            x = 0 
            y = 0
# findingWays(4,2,2) 
v = (math.factorial(40) / (math.factorial(20) * math.factorial(20)) )
v
# Pertmutation: math.factorial(a) / math.factorial(b) * math.factorial(c)
# Combination: To pick: math.factorial(a) / math.factorial(a-b) * math.factorial(b)



#%% Eu 16
# Power digit sum
def exp(a,b):
    x = a ** b
    x = str(x)
    xsum = int()
    for i in x:
        i = int(i)
        xsum += i
    return xsum
exp(2,1000)

#%% Eu 17
# Number letter counts
a = {1 : "one"}
a[1]
pool = ['one','two','three','four','five','six','seven','eight','nine']
p10 = ['one','two','three','four','five','six','seven','eight','nine','ten']
pool2 = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
p10two20 = ['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']

c= list()
for i in pool2:
    for j in pool:
        ij = i+j
        c.append(ij)
c
d=list()
for i in pool:
    ijh = i + 'hundred'
    d.append(ijh)
d
p100 = []
p99 = p10 + pool2 + p10two20 +c 
len(p100)
e = list()
for i in d:
    for j in p99:
        ijl = i + 'and' + j 
        e.append(ijl)
thousand = ['thousand','ten']
p1000 = p99 + e + d + thousand
len(p1000)
x = str()
for i in p1000:
    x += i
print(len(x))
# len(p99)
len(e[244])



#%% Eu 18
# Maximum path sum I
a = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23 56'''

list(a)
type(a)
b=list()
c=list()
j = str()
for i in a:
    if i != '\n':
        b.append(i)
    if i == '\n':
        for i in b:
            j += i
        c.append(j)
        b=list()
        j=str()
print(type(c))
d = list()
for i in c:
    j = i.split()
    d.append(j)

e = list()
f = list()
for i in d:
    for j in i:
        print(j)
        k = int(j)
        e.append(k) 
    f.append(e) 
    e = list() 
# print(type(f[0][0]),f) 
# choice always biggest one and take them into list
c = 0
cs = int()
a = int()
for i in f[-1]:
    a = i 
    if i >= a:
        a = i
        cs = c
    c += 1

f
# and final:
for n in reversed(range(1,len(f))):
    for i in range(n):
        k = max(f[n][i], f[n][i+1])
        f[n-1][i] += k
print(f,'\nresult: ',f[0])
#%% Eu 19
# To be updated. 