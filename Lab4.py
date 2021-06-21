'''
for i in range(1,64):
    for k in range(64,i):
       if i % k  == 0:
           print ()
           break
    print(i)
   '''
'''

def fibonacciFinder (max):
i = 0
j = 1
k= 0 
while i < 1000:
    print(k)
    k = i + j
    i = j = k
    j = k
return ("Fibonacci yay!") 

def primeFinder (max):
    for i in range (2,max):
        for j in range (2,i):
            if i % j ==0:
                break
        else:
            print(i)
    return(max)
'''
'''
def triangleArea(base, height):
    area = base*height/2
    print(area)
    return area

n = 5
m = 5
areaList = [0]*n*m
for h in range(0,n):
    for b in range(0,m):
    areaList[b] = triangleArea(b,h)
print(areaList)      

#appen,extend, insert
#pop, remove, clear
'''

listNumbers = []
size = 5 
for i in range (size):
   listNumbers.append(10*np.random.random())
   
listCities =["New York","Los Angeles", "Oakland", ""]
print(listNumbers)
listNumbers.sort()
print(listNumbers)

