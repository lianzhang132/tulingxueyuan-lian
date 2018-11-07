import math
print(1)

print(math)
print(math.ceil(5.01))

print (math.ceil(5.9))



print(math.floor(5.01))
print(math.floor(5.9))


import  keyword
print(keyword.kwlist)

print(round(5.5))
print(round(5.9))
print(round(5.01))


print(math.sqrt(4))
print(math.sin(0.5))


print(math.pow(4,3))
print(4**3)

print(math.fabs(-5))
print(math.fabs(2))
print(math.fabs(8))

print(abs(-1))
print(abs(5))
print(abs(-2.5))


print(math.modf(4.5))
print(math.copysign(2,-6))

print(math.e)
print(math.pi)

import random

for i in range(10):
    print(random.random())
    print(random.randint(1,9))

    print('*'*30)
    print(random.randrange(1,9,3))


print(random.choice([1,5,258,6,69]))

print('*' * 30)
list1 = [1,5,7,9,85,9]
random.shuffle(list1)
print(list1)

print(random.uniform(1,9))

