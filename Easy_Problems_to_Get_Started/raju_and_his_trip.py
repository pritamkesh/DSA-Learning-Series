# Problem Statement : https://www.codechef.com/CCSTART2/problems/VALTRI
# cook your dish here
def raju_and_his_trip(Bus_No) -> str:
    if Bus_No % 5 == 0 or Bus_No % 6 == 0:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    N = int(input())
    raju_and_his_trip(N)
