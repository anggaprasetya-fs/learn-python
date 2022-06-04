# Logical Operation or Boolean
# NOT, OR, AND, XOR


# NOT
a = True
b = False
c = not a 
d = not b 
print('\n- NOT -')
print('Data a is : ', a, 'to NOT is : ', c)
print('Data b is : ', b, 'to NOT is : ', d)


# OR 
# If there is True, the result will always True.
# Like 0 + 1 = 1
a = True
b = False
c = a or a 
d = a or b
e = b or a 
f = b or b
print('\n- OR -')
print(a, 'OR', a, 'is', c)
print(a, 'OR', b, 'is', d)
print(b, 'OR', a, 'is', e)
print(b, 'OR', b, 'is', f)


# AND 
# If there is False, the result will always False. 
# Like 0 * 0 = 0
a = True
b = False
c = a and a 
d = a and b
e = b and a 
f = b and b
print('\n- AND -')
print(a, 'AND', a, 'is', c)
print(a, 'AND', b, 'is', d)
print(b, 'AND', a, 'is', e)
print(b, 'AND', b, 'is', f)


# XOR 
# If there is one True, the result will always True. 
# But if there is two True or two False, the result will always False.
a = True
b = False
c = a ^ a 
d = a ^ b
e = b ^ a 
f = b ^ b
print('\n- XOR -')
print(a, 'XOR', a, 'is', c)
print(a, 'XOR', b, 'is', d)
print(b, 'XOR', a, 'is', e)
print(b, 'XOR', b, 'is', f)