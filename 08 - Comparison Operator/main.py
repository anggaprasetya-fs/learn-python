# Compatison Operation
# All the result from comparison operation is boolean
# <, >, >=, <=, ==. !=. is, is not

a = 4
b = 2

# >
result = a > b
print(a, ">", b, '=', result)

# <
result = b < a
print(b, "<", a, '=', result)

# >=
result = a >= 4
print(a, ">= 4", '=', result)

# <=
result = b <= 2
print(b, "<= 2", '=', result)

# ==
result = a == 4
print(a, "== 4", '=', result)

# !=
result = a != b
print(a, "!=", b,'=', result)

# 'is' as comparison object identity
x = 5
y = 5
result = x is y
print("\n",x, "is", y, '=', result)
print('id x is : ', hex(id(x)))
print('id y is : ', hex(id(y)))

# is not' as comparison object identity
c = 5
d = 3
result = c is not d
print("\n",c, "is not", d, '=', result)
print('id c is not : ', hex(id(c)))
print('id d is not : ', hex(id(d)))
