print('hello world')
a = [1,2,'aaa',[]]

print(a)
print(a[0])
print(a[3])

print(a[-2][1])


def power(a, b):
  result = a ** b
  print(result)
  return result


power(2,10)
p = power(10,11)

print(p)
p-= 1000
print(p)
