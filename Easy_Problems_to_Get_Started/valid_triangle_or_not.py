# Problem Statement : https://www.codechef.com/CCSTART2/problems/TRIVALCH
# cook your dish here
def valid_triangle_or_not(a, b, c):
    # Sum of two sides shall be greater than third side.
    if (a + b > c) and (b + c > a) and (a + c > b):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    valid_triangle_or_not(a, b, c)
