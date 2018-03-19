import  math
import random
#--------------------------------------------------------
print(math.floor(2.356))
print(math.floor(-2.356))


#--------------------------------------------------------
print(int(2.78),math.floor(2.78),round(2.78))
#>> 2 2 3
print(int(-2.78),math.floor(-2.78),round(-2.78))
#>> -2 -3 -3
print(int(2.28),math.floor(2.28),round(2.28))
#>> 2 2 2
print(int(-2.28),math.floor(-2.28),round(-2.28))
#>> -2 -3 -2

#--------------------------------------------------------

print(random.random())
# 0-1 随机实数 如0.729851345648
print(round(random.random(),3))
# 0-1随机实数保留3位小数如 0.123
print(int(random.random()*1000))
# 获得0-1000内的随机整数

#--------------------------------------------------------

print(math.sqrt(2))
#>>  1.4142135623730951



a = 12
b = 10

if (a>=b):
    print(a)
else:
    print(b)

def max_my(a,b):
    if(a>=b):
        print(a)
    else:
        print(b)

max_my(12,10)  #12
max_my(12,12)   #12
max_my(12,10.025)   #12
max_my(-12,-10)   #-10
max_my(-12,10)   #10
