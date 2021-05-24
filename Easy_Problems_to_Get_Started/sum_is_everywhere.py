# Problem Statement : https://www.codechef.com/CCSTART2/problems/SUMEVOD
# cook your dish here
def sum_is_everywhere(N) -> int:
    odd_sum = 0
    even_sum = 0
    for number in range(1, 2*N+1):
        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number
    print(odd_sum, even_sum)

    # -------------Mathematical way to solve this(Preferable) --------------- #
    # # Using direct mathematical formula :
    # sum_of_even_no = N*(N+1)
    # sum_of_odd_no = N*N
    # print(sum_of_odd_no, sum_of_even_no)


if __name__ == "__main__":
    N = int(input())
    sum_is_everywhere(N)
