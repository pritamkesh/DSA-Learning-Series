# cook your dish here
def buy_please(a, b, x, y) -> int:
    if a != 0 or x != 0:
        pens_cost = a * x
    else:
        pens_cost = 0

    if b != 0 or y != 0:
        pencils_cost = b * y
    else:
        pencils_cost = 0

    total_cost = pens_cost + pencils_cost
    print(total_cost)


if __name__ == '__main__':
    a, b, x, y = input().split()
    a = int(a)
    b = int(b)
    x = int(x)
    y = int(y)
    buy_please(a, b, x, y)
    #buy_please(1,1,4,8)
