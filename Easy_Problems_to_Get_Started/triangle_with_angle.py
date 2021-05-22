# Problem Statement : https://www.codechef.com/CCSTART2/problems/ANGTRICH
# cook your dish here
def triangle_with_angle(a, b, c) -> str:
    if a != 0 and b != 0 and c != 0:
        if a + b + c == 180:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")


if __name__ == "__main__":
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    triangle_with_angle(a, b, c)
