#list
fruits = ['apple', 'orange']
fruits[1]= 'cherry'
numbers=[1,1,2,5,4,5,8,3]
a=["a",1,1.2,True,"s"]
empty_list=[]
print(a[len(a)-1])
print(fruits[1], numbers, numbers[-1], a)
print(numbers[1:4]) #یه بازه ای از لیستو نمابش می ده
print(a[0:3:2])#قدم مشخص میکنیم
print(a[::-1])#برعکس میکنه
numbers[3:6]=[True] #به جای 3 تا 6 true میداره
print(numbers)
numbers[4:6]=[100,"b"]
print(numbers)
a[0:0]=["inserted value"] #یدونه اضاقه میکنه
numbers[3:3]=["z"]
print(a,numbers)
print(1 in a )

