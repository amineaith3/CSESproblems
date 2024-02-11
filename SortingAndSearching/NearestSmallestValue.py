def nearestSmall(n, arr, val):
    for a in arr:
        if a < val:
            return len(arr)-arr.index(a)
    return 0
 
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print("0", end=" ")
    if n > 1:    
        for i in range(1, n):
            print(nearestSmall(n, arr[0:i][::-1], arr[i]), end=" ")
    else : 
        pass
if __name__=="__main__":
    main()