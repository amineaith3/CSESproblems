def runSim(n):
    answer = list()
    answer.append(n)
    while (n != 1):
        if(n % 2 == 0):
            n //= 2
            answer.append(n)
        else : 
            n = 3 * n +1
            answer.append(n)
            
    return answer

def main():
    n = int(input())
    save = runSim(n)
    for s in save:
        print(f"{s} ", end="")
    
if __name__ == "__main__":
    main()
