import time
start = time.time()
def my_sqrt(number):
    low_limit = 0
    high_limit = number

    counter = 0
    # init
    while (1):
        mean_value = (low_limit + high_limit) / 2
        counter = counter + 1
        square_value = mean_value ** 2  # mean * mean also works
        if (square_value > number):
            high_limit = mean_value
            # print('when choose: ', mean_value, 'the square number is', square_value, 'bigger than ', number)
        else:
            low_limit = mean_value
            # print('when choose: ', mean_value, 'the square number is', square_value, 'smaller than ', number)
        if ((high_limit - low_limit) < (1 / 1e10)):
            mean_value = (low_limit + high_limit) / 2
            # print(mean_value,counter)
            break
    print(round(mean_value,10), counter)

# run
def my_hand_sqrt(number):
    sqrtnum = 0
    counter = 0
    for num in range(10):
        if(num**2<number):
            sqrtnum = num
        else:
            break
    else:
        print(sqrtnum)

    for bit in range(10):
        for num1 in range(10):
            counter = counter +1
            if((sqrtnum*10 + num1)**2 >number*100):
                sqrtnum = sqrtnum * 10 + num1 - 1
                number = number * 100
                break
            # print(sqrtnum)
    print(sqrtnum/(1e10),counter)
    return sqrtnum/(1e10)


for i in range(2,10):
    # my_sqrt(i)
    my_hand_sqrt(i)
# my_hand_sqrt(2)
# my_sqrt(2)

end = time.time()
print(end-start)