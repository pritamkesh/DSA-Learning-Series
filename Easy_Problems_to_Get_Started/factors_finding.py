# cook your dish here
def finding_factors(number):
    pass
    total_factor = 0
    factors = []
    for each in range(1, number+1):
        # Checking if the remainder is zero
        if number % each == 0:
            factors.insert(1, each)
            total_factor += 1
    # Sorting the factors in the list
    factors.sort()
    # List to String : using list comprehension
    factors = " ".join([str(each) for each in factors])
    print(total_factor)
    print(factors)


if __name__ == '__main__':
    N = int(input())
    finding_factors(N)
