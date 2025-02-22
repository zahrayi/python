#mesal baraye while:
#------1-----
#adade zooj ra peyda konid? (beine 0 ta 100)
#x=0
#while x<100:
    #if x%2==0:
        #print(x)
    #x+=1
import end as end

#------2------
#chape mosalas?
# row = 1
# while  row <= 5:
#     print ("*" * row)
#     row+=1


#--------3------
#mosalase baraks?
# row=5
# while row>=1:
#     print("*" * row)
#     row-=1

#---------4------
#maqhsom alayh haye adad?
# x=int(input("enter your num:"))
# n=1
# while n<=x:
#     if x%n==0:
#         print(n)
#     n+=1


#-------5------
#adad aval hast ya na?
# x=int(input("enter your number:"))
# c=0
# n=2
# while n<=x-1:
#     if x%n==0:
#         c+=1
#         n+=1
#     else:
#         n+=1
#
# if c>=1:
#     print("nist")
# else:
#     print("hast")


#-------6------
#adad kamel?
# x=int(input("enter your num:"))
# n=1
# l=[]
# while i<=n:
#     if n % i==0:
#         l.append(i)
#     i+=1
# if sum(l)-n==n:
#     print("hast")
# else :
     # print("nist")

#--------7-------
#fibonachi?
#0 1 1 2 3 5 8 13 21 34 ,....
# a=0
# b=1
# i=1
# while i<=20:
#     print(a)
#     a , b = b , a+b
#     i+=1

#___________mesale range va halghe__________
# x=int(input("enter your num: "))
# a=1
# i=1
# while i<= x:
#     a=a*i
#     i+=1
#
# print(a)

#____ba range va for_____

# n=int(input("n: "))
# m=1
# for i in range (1, n+1):
#     m*=i
#
# print(m)

#_____makos kardan_____

x=input("enter a number: ")
for i in range(len(x)-1, -1, -1):
    print(x[i], end=" ")





