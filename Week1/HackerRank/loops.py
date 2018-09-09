import math
if __name__ == '__main__':
    n = int(raw_input())
    for i in range(0,n*n):
        j=int(math.sqrt(i))
        if(j==math.sqrt(i)):
            print(i)
        