# Write a program that takes nn from the input table and prints the multiplication from 1 to n.
# input
# The only input line contains the number n.
# 1≤n≤100
# output
# # The output should contain n lines and in these nn lines you should print the multiplication table up to the number n.

n = int(input())
if 1<=n<=100:
    for i in range (1,n+1):
        for j in range (1,n+1):
            r=i*j
            print(r, end=" ")
        print()
else:
    print("your num should be between 1 to 100")

