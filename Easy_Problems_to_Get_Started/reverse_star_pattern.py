# Problem Statement : https://www.codechef.com/CCSTART2/problems/REVSTRPT
# cook your dish here
def reverse_star_pattern(N):
    for i in range(1, N + 1):
        print(i * "*")


if __name__ == "__main__":
    N = int(input())
    reverse_star_pattern(N)
