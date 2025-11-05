# Temperature conversions from fehrenheit to celsius
# promt user for temperature in fehrenheit
fehrenheit = float(input("Enter temperature in fehrenheit: "))

# conversion formula
celsius = (fehrenheit - 32) * 5/9
print(f"The temperature in celsius is: {celsius:.2f}°C")

