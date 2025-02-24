def pass_validation(a):
    if len(a) < 8:
        return "pass should be atleast 8 char"
    allow_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$#!@"

    for char in a:
        if char not in allow_char:
            return f"your char '{char}' is invalid.please use valid char such as numbers,letters and $#@!"
    return "your pass is valid."


while True:
    a = input(
        "please enter your pass (you can only use numbers,letters and !@#$ and your pass should be atleast 8 char): ")
    validation = pass_validation(a)
    print(validation)
    if validation == "your pass is valid.":
        break