# Temperature Unit Conversion Exercise

# Celcius to other Unit Temperature
print("\nSIMPLE PROGRAM TEMPERATURE CONVERSION\n")

# Celcius
celcius = float(input("Enter temparature in celcius unit : "))
print("The temperature is ", celcius,"° in Celcius")

# Reamur
reamur  = (4/5) * celcius
print("The temperature is ", reamur,"° in Reamur")

# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("The temperature is ", fahrenheit,"° in Fahrenheit")

# Kelvin
kelvin  = celcius + 273
print("The temperature is ", kelvin,"° in Kelvin")

# Fahrenheit to Kelvin
fahrenheit = float(input("\nEnter temparature in fahrenheit unit : "))
fh      = 5/9 * (fahrenheit - 32)
klv     = fh + 273
print("The temperature is ", klv,"° in Kelvin")

# Kelvin to Fahrenheit
kelvin  = float(input("\nEnter temparature in kelvin unit : "))
klv     = kelvin - 273
fh      = ((9/5) * klv) + 32
print("The temperature is ", klv,"° in Fahrenheit")