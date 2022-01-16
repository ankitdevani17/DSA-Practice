
def rotate( arr, n):
    arr[:] = arr[-1:] + arr[:-1]
    return arr


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1

if __name__ == "__main__":
    main()





    
