def add(a ,b):
    return a+b

def mul(a, b):
    return a*b

def calculate(f, a, b):
    result = f(a,b)
    return result

f1 = mul
x = f1(2,3)

res1 = calculate( add, 12 ,13)
print( res1 )

# print( range(12) )
# print( list(range (12)))
# print( list(range (-5,12,2)))

# a = [ "Avarham", "Yitzhak", "יעקב" ]
# for i in range( len(a) ):
#     print(i, a[i])

# i = 12
# while i>0:
#     print(i)
#     i -= 1
