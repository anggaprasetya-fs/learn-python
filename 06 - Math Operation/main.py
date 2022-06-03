# Operasi Aritmatika
a = 11
b = 3


# Addition Operation +
result  = a + b
print(a, '+', b, '=', result)


# Subtraction Operation -
result  = a - b
print(a, '-', b, '=', result)


# Multiplication *
result  = a * b
print(a, '*', b, '=', result)


# Division / 
result  = a / b
print(a, ':', b, '=', result)


# Exponentiation (pangkat) **
result  = a ** b
print(a, '**', b, '=', result)


# Modulus (sisa pembagian) %
result  = a % b
print(a, '%', b, '=', result)


# Operasi floor division //
result  = a // b
print(a, '//', b, '=', result)


# Precedence Operation

'''
The order of priority 

1. ()
2. Exponen **
3. * , / , % , //
4. + , -
'''

x = 3
y = 2
z = 4
result = x ** y * z + x / y - y % z // x
print(x, '**', y, '*', z, '+', x, '/', y, '-', y, '%', z, '//', x, '=', result)