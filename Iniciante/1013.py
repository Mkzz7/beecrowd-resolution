a, b, c = map(int, input("").split())

maiorab = (a + b + abs(a-b))/2

maior = (maiorab + c + abs(maiorab - c)) // 2

print(f"{maior:.0f} eh o maior")
