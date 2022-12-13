# DemoLoop.py

value = 5
while value > 0:
    print(value)
    value -= 1


lst = [1,2,3,4,5,7,8,9,10]
for i in lst:
    print(i)

color = {"apple":100, "kiwi":200, "banana":300}
for item in color.keys():
    print(item)

for item in color.values():
    print(item)

lst = list(range(1,11))
print( [ i**2 for i in lst if i >5] )

tp = ("apple", "kiwi", "banana")
print( [len(i) for i in tp] )

print("--필터링하는 경우---")
#함수 정의
def getBiggerThan20(i):
    return i > 20

lst = [10, 25, 30]
iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)

