# Problem Statement : https://www.codechef.com/CCSTART2/problems/RNGEODD
# cook your code here

def range_odd(L, R) -> int:
    i = 0
    odd_numbers = []
    for number in range(L, R+1):
        if number % 2 != 0:
            odd_numbers.insert(i, number)
            i += i
    odd_numbers.sort()
    odd_numbers = " ".join([str(number) for number in odd_numbers])
    print(odd_numbers)


if __name__ == '__main__':
    L, R = input().split()
    L = int(L)
    R = int(R)
    range_odd(L, R)
