# Problem Statement : https://www.codechef.com/CCSTART2/problems/SQALPAT
# cook your dish here (Yet to solve!)
def alternative_square_pattern(no_of_lines, number_pattern) -> int:

    number_pattern_list = number_pattern.splitlines()
    for i in range(0, no_of_lines):
        print(number_pattern_list[i])


if __name__ == "__main__":
    N = int(input())
    pattern = '1 2 3 4 5\n' \
              '10 9 8 7 6\n' \
              '11 12 13 14 15\n' \
              '20 19 18 17 16\n' \
              '21 22 23 24 25\n' \
              '30 29 28 27 26\n'
    alternative_square_pattern(N, pattern)
