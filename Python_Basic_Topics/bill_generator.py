units = int(input("Enter units: "))


if units < 0:
    print("invalid input")
else:
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = units * 7
    elif units <= 500:
        bill = units * 10
    else:
        bill = units * 15

    if bill > 5000:
        bill *= 0.10
        # additional = bill * 0.10
        # total_bill = bill + additional
        print(f'Your total bill: {int(bill)}')
    else:
        print(f'Your total bill: {int(bill)}')