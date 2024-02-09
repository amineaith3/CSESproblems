def repetitions(s):
    array = list(s)
    length = len(s)
    currentMax = 1
    currentChar = array[0]
    Max = 1
    for i in range(1,length):
        if(array[i] == currentChar):
            Max += 1
            if(Max > currentMax):
                 currentMax = Max
        else :
            currentChar = array[i]
            Max = 1
    return currentMax

def main():
    string = input()
    print(repetitions(string))

if __name__ == "__main__":
    main()
