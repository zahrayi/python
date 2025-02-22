#mesale fasle4--------
#-------1-------
#zoj ya fard
# x =int(input("enter your num:" ))
# if x%2==0 :
#     print("zoj")
# else:
#     print("fard")


#---------2-------
#beyne doo adad kochektarin
# x =int(input("enter your num1:" ))
# y=int(input("enter your num2:" ))
# if x==y:
#     print("brabar")
# elif x<y:
#     print(x)
# else:
#     print(y)

#tamrin shart
#---------1--------
# x =int(input("enter your num:" ))
# if x%5==0 and x%2==0:
#     print("bakhsh pazir!")
# else:
#     print("bakhsh pazir nist!")

#----------2--------
# a =int(input("enter your num1:" ))
# b =int(input("enter your num2:" ))
# d =int(input("enter your num3:" ))
# if a+b>d and b+d>a and a+d>b:
#     print("YES!")
#     if a == b and a == d and b == d:
#         print("motasavi azla")
#     if  a == b or d == b or d == a:
#         print("motasavi sagein")
#     if a != b and a != d and b!=d:
#             print("mokhtalef")
#     if (a * a) + (b * b) == d * d or (a * a) + (d * d) == b * b or (d * d) + (b * b) == a * a:
#         print("ghaem")
#else:
    #print("NO!")
#---------3---------
ch = input("enter ur char: ")
if ord(ch)>=48 and ord (ch)<=57:
    print("number")
elif ord(ch)>=65 and ord (ch)<=90  or ord(ch)>=97 and ord (ch)<=122:
    print("letter")
else :
    print("other")



