age = int(input("enter your age: "))
if age<0:
    print("invalid number")
elif 0<= age <12 :
    print("childe")
elif 12<= age <20 :
    print("teen")
elif 20<= age <35 :
    print("young")
elif 35<= age <50 :
    print("adult")
elif age>=50:
    print("old")