# dictionary
profile = {12:"zahra" , 13:"liam" , 14:"fatemeh"}
print(len(profile))
print(profile[12])
profile[12]="zahra yousefi"
print(profile)
d1= {1:"a", 2:"b", 1:"x"}
print(d1)
# f = {[1,2] : "a", [4,5] : "z"} #به جای کلید میتونیم نوع داده هایی بذاریم که تغییر ناپذیر باشند مثل تاپل و مجموعه
f = {(1,2) : "a" , (3,4) : "b"}
print(f[(1,2)])
print(f.keys())
print(f.values())