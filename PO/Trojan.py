from math import sqrt

def is_square(n):
    return sqrt(n).is_integer()


def value_factor(n):
    factor_list = []
    for i in range(1, n+1):
        if n % i == 0:
            factor_list.append(i)

    return factor_list

def list_squared(m,n):
    return_list = []
    for value in range(m,n+1):
        sum = 0
        for i in value_factor(value):
            sum += i**2
        if is_square(sum):
            return_list.append([value,sum])
    return return_list

def main():
    m,n = map(int, input().split())
    print(list_squared(m,n))

if __name__ == '__main__':
    main()


#Для покупки ПО свяжитесь с автором по почте.