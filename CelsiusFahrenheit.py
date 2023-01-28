print("Celsius to Fahrenheit")
celsius=int(input("Enter number:"))
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
fahrenheit2 = celsius_to_fahrenheit(celsius)
print(fahrenheit2)

print("Fahrenheit to Celsius")
fahrenheit=int(input("Enter number:"))
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
celsius2 = fahrenheit_to_celsius(fahrenheit)
print(celsius2)