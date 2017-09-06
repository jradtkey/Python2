def odd_even(arg):
    for value in range(1,arg+1):
        if (value % 2 == 0):
            print'Number is', value, '. This is an even number'
        else:
            print'Number is',value, '. This is an odd number'
odd_even(2000)


def multiply(arg, num):
    b = []
    for value in range(0, len(arg)):
        b.append(num * arg[value])
    return b
arg = [2,4,5]
num = 3
multiply(arg, num)
arr = multiply(arg, num)

def layered_mults(arr):
    new_arr = []
    for value in range(0, len(arr)):
        new_arr.append("1"*arr[value])
    print new_arr
layered_mults(arr)
