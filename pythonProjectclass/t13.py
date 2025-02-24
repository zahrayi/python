user_profile = ["neda majd" , "09357482"]
email=input("insert ur email: ")
height = int(input("insert ur height: "))
weight = int(input("insert ur weight: "))
# user_profile.append(email)
# user_profile.append(height)
# user_profile.append(weight)
# به جای اون سه تا خط بالایی میشه خط پایینیو نوشت
user_profile.extend([email, height , weight])
print(user_profile)
user_profile[0]="zahra majd"
print(user_profile)
user_profile.pop(1)
print(user_profile)

