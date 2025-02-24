
def darage(a,b,c):
  d= (b ** 2 - 4 * a * c)
  r1= (- b + (d**0.5)) / (2 * a)
  r2= (- b - (d**0.5)) / (2 * a)
  return r1,r2

r1,r2=darage(1,-4,4)
print("first root:" , r1 , "second root:" , r2)
