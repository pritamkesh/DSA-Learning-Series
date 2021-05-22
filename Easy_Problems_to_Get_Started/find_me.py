def find_me(N, K, numbers_in_N):
    # The solution is not working ! I will update the solution later point of time.
    print(N)
    print(K)
    print(numbers_in_N)
    for number in numbers_in_N:
        if K in number:
            print(1)
            break
        else:
            print(-1)


if __name__ == "__main__":
    N, K = input().split()

    N = int(N)
    K = int(K)
    numbers_in_N = []

    find_me(N, K, numbers_in_N)



