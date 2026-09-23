months = [
    "January", "February", "March",
    "April", "May", "June", "July",
    "August", "September", "October",
    "November", "December"
    ]

month = (int(input("")))

if 1 <= month <= 12:
    print(months[month - 1])
else:
    print("Invalid month")