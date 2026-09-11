import math

a, b, c = map(float, input().split())

delta = b**2 - 4 * a * c

if a == 0:
    print("Impossivel calcular")
if delta < 0:
    print("Impossivel calcular")
    
if a and b and c >= 0 and delta >= 0:
    bhaskara1 = (-b + math.sqrt(delta))/(2*a)
    bhaskara2 = (-b - math.sqrt(delta))/(2*a)

    print(f"R1 = {bhaskara1:.5f}")
    print(f"R2 = {bhaskara2:.5f}")