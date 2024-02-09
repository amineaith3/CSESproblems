def missingNumber(array):
    length = len(array)+1
    sumArray = sum(array)
    missing = (((length+1) * length )// 2) - sumArray
    return missing

def main():
    N = int(input())
    data = map(int, input().split())
    print(missingNumber(list(data)))
    
if __name__ == "__main__":
    main()
