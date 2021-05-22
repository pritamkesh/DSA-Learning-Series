# Yet to solve this problem
def sum_is_everywhere(N) -> int:
    odd_sum = 0
    even_sum = 0
    even_count = 1
    odd_count = 0
    i = 1
    while even_count <= N:
        for number in range(1, N):
            if number % 2 == 0:
                even_sum += number
                even_count += 1

    # print(odd_sum)
    print(even_sum)


if __name__ == "__main__":
    N = int(input())
    sum_is_everywhere(N)
