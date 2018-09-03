# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
if(n%2!=0):
    print("Weird")
if(n%2==0 and n in range(1,6)):
    print ("Not Weird")
if(n%2==0 and n in range(5,21)):
    print("Weird")
if (n%2==0 and n>20):
    print ("Not Weird")