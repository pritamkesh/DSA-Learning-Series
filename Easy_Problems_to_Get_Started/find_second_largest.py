# Problem Statement : https://www.codechef.com/CCSTART2/problems/SECLAR
# cook your code here
def find_second_largest(A, B, C):
    numbers = []
    for each in A, B, C:
        numbers.insert(1, each)
    numbers.sort()
    print(numbers[1])



if __name__ == '__main__':
    A = int(input())
    B = int(input())
    C = int(input())
    find_second_largest(A, B, C)
