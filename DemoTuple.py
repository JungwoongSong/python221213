# DemoTuple.py
tp = (1,2,3)
print( len(tp) )
print( type(tp) )
print( tp[0] )

#함수를 정의
def calc(a,b):
    return a+b, a*b


#호출
result = calc(3,4)
print( result )
print( result[0] )
print( result[1] )

print("id: %s, nmae: %s" % ("kim", "김유신"))

args = (5,6)
print( calc(*args) )

print("---형식변환---")
a = (10,20,30)
b = list(a)
b.append(40)
print(b)