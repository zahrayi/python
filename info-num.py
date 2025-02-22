# Mehdi, who is tired of coding, has recently become interested in the field of industries. For this reason, he
# has decided to research this field. He goes to different people and each of them gives him some information.
# He is surprised at the amount of information he gets from people. For example, if it receives one number of
# information, it will say Wow!, if it receives two information, it will say Woow! And in the same way, the amount
# of drawing the word (the number of o's) increases. Now you have to say that if someone gives nn information to Mahdi,' \
#' what word should we expect from him.



x = int(input())
if 1 <= x <= 10:
    b = "o" * x
    print(f"W{b}w!")
else:
    print("your number should be between 1 to 10")


