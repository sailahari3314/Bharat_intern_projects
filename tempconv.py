def celsius_to_fahrenheit(celsius):
  return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5/9

temperature = float(input("Enter the temperature: "))
unit = input("Is this temperature in C or F? (enter C or F): ")

if unit.upper() == 'C':
  result = celsius_to_fahrenheit(temperature)
  print(f"{temperature} C is equal to {result} F")

elif unit.upper() == 'F':
  result = fahrenheit_to_celsius(temperature)
  print(f"{temperature} F is equal to {result} C")

else:
  print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")
