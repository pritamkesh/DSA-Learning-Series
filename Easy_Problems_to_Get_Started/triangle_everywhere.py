# Problem Statement : https://www.codechef.com/CCSTART2/problems/EXTRICHK
# cook your dish here
def triangle_everywhere(a, b, c) -> int:
    if a != 0 and b != 0 and c != 0:
        if (a + b > c) and (b + c > a) and (c + a > b):
            # Equilateral
            if a == b == c:
                print(1)
            # Isosceles
            elif a == b or a == c or b == c:
                print(2)
            # Scalene
            elif a != b != c:
                print(3)
        else:
            print(-1)
    else:
        print(-1)


if __name__ == "__main__":
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    triangle_everywhere(a, b, c)
