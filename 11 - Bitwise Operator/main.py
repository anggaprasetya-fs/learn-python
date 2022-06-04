# Bitwise Operator or Binary Operator 
# OR, AND, XOR, NOT
# !!! Calculate the Binary, not the real number !!!


a = 7
b = 5


# Bitwise OR
c = a | b
print('-- OR --')
print('Data a is :', a, 'in binary is:', format(a, '08b'))
print('Data b is :', b, 'in binary is:', format(b, '08b'))
print('Data c is :', c, 'in binary is:', format(c, '08b'))

# The result is:
# Data a is : 7 in binary is: 00000111
# Data b is : 5 in binary is: 00000101
# ------------------------------------ ( | )
# Data c is : 7 in binary is: 00000111


# Separator
print('\n',30*'=','\n')


# Bitwise AND
c = a & b
print('-- AND --')
print('Data a is :', a, 'in binary is:', format(a, '08b'))
print('Data b is :', b, 'in binary is:', format(b, '08b'))
print('Data c is :', c, 'in binary is:', format(c, '08b'))

# The result is:
# Data a is : 7 in binary is: 00000111
# Data b is : 5 in binary is: 00000101 
# ------------------------------------ ( & )
# Data c is : 5 in binary is: 00000101


# Separator
print('\n',30*'=','\n')


# Bitwise XOR
c = a ^ b
print('-- XOR --')
print('Data a is :', a, 'in binary is:', format(a, '08b'))
print('Data b is :', b, 'in binary is:', format(b, '08b'))
print('Data c is :', c, 'in binary is:', format(c, '08b'))

# The result is:
# Data a is : 7 in binary is: 00000111
# Data b is : 5 in binary is: 00000101
# ------------------------------------ ( ^ )
# Data c is : 2 in binary is: 00000010


# Separator
print('\n',30*'=','\n')


# Bitwise NOT
c = ~a
print('-- NOT --')
print('Data a is :', a, 'in binary is:', format(a, '08b'))
print('Data c is :', c, 'in binary is:', format(c, '08b'))

# The result is:
# Data a is : 7 in binary is: 00000111
# ------------------------------------ ( ~ )
# Data c is : -8 in binary is: -0001000


print('\n',30*'=','\n')


# (Trick) Flip from minus number to positive number
d = 0b0000000111 # from ~a
e = 0b1111111111 # from 1023
f = d ^ e
print('-- Flip From Negative Value to Positive with XOR --')
print('Data f is :', f, 'in binary is:', format(f, '08b'))

# The result is:
# Data f is : 248 in binary is: 11111000