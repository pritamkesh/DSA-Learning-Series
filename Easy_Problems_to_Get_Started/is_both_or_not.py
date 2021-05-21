# cook your dish here
def is_both_or_not(N) -> str:
    if N % 5 == 0 and N % 11 == 0:
        print("BOTH")
    elif N % 5 == 0 or N % 11 == 0:
        print("ONE")
    elif N % 5 != 0 or N % 11 != 0:
        print("NONE")


if __name__ == '__main__':
    N = int(input())
    is_both_or_not(N)
