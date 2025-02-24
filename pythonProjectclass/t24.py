user_l=["zahra","elina","atena","melina","saina"]
user=input("enter your name ")
if user in user_l:
    print("welcom")
else:
    print("your not registered")
Q=input("do you want to sign in?")
if Q.lower()=="yes":
    user_l.append(user)
elif Q.lower()=="no":
    print("ok")
else:
    print("invalid input pleas enter yes or no")