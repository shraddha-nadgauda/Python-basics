def check_is_prime(lower_range,upper_range):
    for i in range(lower_range, upper_range):
        for j in range(2, i):
            if i % 2 == 0:
                result = i / j
                print('%d equals %d * %d' % (i, j, result))
                break
            else:
                print('number is prime', i)
                break

if __name__ == '__main__':
    try:
        lower_bound = int(input('please enter lower range'))
        upper_bound = int(input('please enter upper range'))
        check_is_prime(lower_bound,upper_bound)
    except Exception:
        print('you have entered invalid number')
