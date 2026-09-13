a, b, c = map(float, input().split())
if (a >= b + c) or (b >= a + c) or (c >= a + b):
    area = (a + b) * c / 2
    print(f"Area = {area:.1f}")
else:
    perimeter = a + b + c
    print(f"Perimetro = {perimeter:.1f}")