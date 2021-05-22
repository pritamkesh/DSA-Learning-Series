# Problem Statement : https://www.codechef.com/CCSTART2/problems/ADDNATRL
# cook your dish here
def add_natural_numbers(N) -> int:
    total = (N*(N+1))//2
    print(total)


if __name__ == "__main__":
    N = int(input())
    add_natural_numbers(N)

# ----------------------------------- Time limit exceed using while/for loop -----------------------------#
# # Time limit exceeded. Time : 5.01 seconds
# def add_natural_numbers(N) -> int:
#     total = 0
#     i = 1
#     while i <= N:
#         total += i
#         i += 1
#     print(total)
#
#
# if __name__ == "__main__":
#     N = int(input())
#     add_natural_numbers(N)


# cook your dish here
# def add_natural_numbers(N) -> int:
#     total = 0
#     for i in range(1, N + 1):
#         total += i
#         i += 1
#     print(total)
#
#
# if __name__ == "__main__":
#     N = int(input())
#     add_natural_numbers(N)